import base64
import logging
import subprocess
import sys
from os import chdir, environ, path

import click
import docker
import requests
import yaml
from compose.progress_stream import stream_output
from dotenv import dotenv_values

_logger = logging.getLogger(__name__)


def get_ssh_key():
    if environ.get("SSH_PRIVATE_KEY"):
        _logger.info("Using env privkey")
        if environ.get("CI"):
            _logger.info("CI Enviroment detected, decoding ssh-key from base64")
            return base64.b64decode(environ["SSH_PRIVATE_KEY"]).decode()
        else:
            return environ["SSH_PRIVATE_KEY"]
    else:
        ssh_key_loc = path.expanduser("~/.ssh/id_rsa")
        _logger.info("Using " + ssh_key_loc)
        return open(ssh_key_loc).read()


@click.command(name="build")
@click.option(
    "-tn",
    "--test_name",
    "--test-name",
    help="Runs a specific test if -rt is also specified",
)
@click.option(
    "-rt",
    "--run_tests",
    "--run-tests",
    "rt",
    is_flag=True,
    help="If specified will run the tests",
)
@click.option(
    "-dc",
    "--disable_cache",
    "--disable-cache",
    is_flag=True,
    help="Disabled the docker build cache",
)
@click.option(
    "-p",
    "--path",
    "buildp",
    default=".",
    show_default=True,
    help="Docker build context path",
)
@click.option(
    "-t",
    "--tag",
    default="stage",
    show_default=True,
    type=click.Choice(["dev", "stage", "prod"]),
    help="Name of the tag you want to build.",
)
@click.option(
    "-f",
    "--model_file",
    "--model-file",
    "mpath",
    default="./",
    help="Path to the engine model.yaml to build, if this is a folder model.yaml will be assumed to be in there "
    "Examples: nomnom/test/waittask/model.yaml",
)
@click.pass_context
def engine_build(ctx, test_name, rt, disable_cache, buildp, tag, mpath):
    "Build engine docker images and optionally run tests."
    chdir(buildp)
    if path.isdir(mpath):
        mpath = path.join(mpath, "model.yaml")
    engine_model = yaml.load(open(mpath))
    engine_name = engine_model["location"]["image"].split(":")[0]

    if "docker" in engine_model:
        env_file = engine_model["docker"].get("env_file")
        docker_file = engine_model["docker"].get("docker_file", "build.dockerfile`")
        buildargs = engine_model["docker"].get("buildargs", {})
        if env_file:
            env_file_args = dotenv_values(dotenv_path=env_file)
            if not env_file_args:
                raise ValueError(f"Failed to load any values from {env_file}")
            buildargs.update(env_file_args)
    else:
        docker_file = "build.dockerfile"
        buildargs = {}
    client = docker.from_env()
    try:
        client.ping()
    except (requests.ConnectionError, docker.errors.APIError) as e:
        raise Exception(
            "There was a problem connecting to the docker agent, ensure it is running and in a good state"
        ) from e
    if rt:
        compose_filename = "tests_compose.yml"
        dev_compose_filename = "tests_compose.dev.yml"
        if environ.get("CI"):
            compose_files = [compose_filename]
        else:
            compose_files = [compose_filename, dev_compose_filename]
        if path.exists(compose_filename):
            _logger.info(
                "----Running {} tests with docker-compose ----".format(engine_name)
            )
            run_tests_docker_compose(
                loglevel=ctx.obj["LOG_LEVEL"],
                test_name=test_name,
                disable_cache=disable_cache,
                compose_files=[x for x in compose_files if path.exists(x)],
            )
        else:
            img_name = build_engine(
                engine_name=engine_name,
                client=client,
                tag=tag,
                disable_cache=disable_cache,
                buildargs=buildargs,
                docker_file=docker_file,
            )
            _logger.info("----Running {} tests [no compose]----".format(engine_name))
            run_tests(
                img_name=img_name,
                client=client,
                test_name=test_name,
                loglevel=ctx.obj["LOG_LEVEL"],
            )
    else:
        build_engine(
            engine_name=engine_name,
            client=client,
            tag=tag,
            disable_cache=disable_cache,
            buildargs=buildargs,
            docker_file=docker_file,
        )
    _logger.info("Built {}:{}".format(engine_name, tag))


def log_build_log(build_log):
    stream_output(build_log, sys.stdout)


def write_creds():
    _logger.info("Base64 encoded creds detected in env variable, using those")
    creds_json = environ["NOMIGEN_TEST_JSON_BASE64"]
    creds_json = base64.b64decode(creds_json)
    creds_path = path.join(
        environ["NOMIGEN_TEST_CREDENTIALS"], "nomigen_test_credentials.json"
    )
    with open(creds_path, "wb") as outf:
        outf.write(creds_json)


def run_tests(img_name, client, test_name, loglevel):
    image = client.images.get(img_name)
    exposed_ports = image.attrs["Config"].get("ExposedPorts", {})
    for key in exposed_ports:
        port, proto = key.split("/")
        exposed_ports[key] = port
    _logger.info("Running tests")
    creds_fp = environ["NOMIGEN_TEST_CREDENTIALS"]
    if environ.get("NOMIGEN_TEST_JSON_BASE64"):
        write_creds()
    nnd_cmd = "nnd "
    if loglevel:
        nnd_cmd += "-l " + loglevel
    nnd_cmd += " engine run_tests"
    if test_name:
        nnd_cmd += " -t " + test_name
    cmd = ["sh", "-c", nnd_cmd]
    container = client.containers.run(
        image=image,
        command=cmd,
        volumes={
            creds_fp: {"bind": "/nomnom/test_config", "mode": "rw"},
            path.abspath("pkg/tests"): {"bind": "/nomnom/pkg/tests", "mode": "rw"},
        },
        stderr=True,
        ports=exposed_ports,
        detach=True,
    )
    try:
        log_generator = container.logs(stdout=True, stderr=True, stream=True, follow=True)
        for log in log_generator:
            print(log.decode("utf-8").rstrip())
        result = container.wait()
        if result["StatusCode"] == 0:
            fn = path.join(path.dirname(__file__), "testpass.out")
            print(open(fn, "r").read())
        sys.exit(result["StatusCode"])
    finally:
        container.reload()
        _logger.info("Container status {}".format(container.status))
        if container.status != "exited":
            container.kill()
        container.remove()


def run_tests_docker_compose(loglevel, test_name, disable_cache, compose_files):
    _logger.info("Using compose files: {}".format(" ".join(compose_files)))
    base_cmd = "docker-compose --project-directory . "
    compose_file_cmds = " ".join(["-f {} ".format(x) for x in compose_files])
    base_cmd += compose_file_cmds
    build_cmd = (
        base_cmd + " build" + " --build-arg SSH_PRIVATE_KEY='{}'".format(get_ssh_key())
    )
    if disable_cache:
        build_cmd += " --no-cache"
    down_cmd = base_cmd + "down -v"
    run_cmd = base_cmd + "run --rm "
    if loglevel:
        run_cmd += "-e LOG_LEVEL={} ".format(loglevel)
    if test_name:
        run_cmd += "-e TEST_NAME={} ".format(test_name)
    run_cmd += "tests"
    subprocess.run(build_cmd, shell=True, check=True)
    subprocess.run(down_cmd, shell=True, check=True)
    try:
        if environ.get("NOMIGEN_TEST_JSON_BASE64"):
            write_creds()
        subprocess.run(run_cmd, shell=True, check=True)
    finally:
        subprocess.run(down_cmd, shell=True, check=True)


def build_engine(engine_name, client, tag, disable_cache, docker_file, buildargs):
    _logger.info("----Building {} image----".format(engine_name))
    buildargs["SSH_PRIVATE_KEY"] = get_ssh_key()
    build_logs = client.api.build(
        dockerfile=docker_file,
        tag=":".join([engine_name, tag]),
        nocache=disable_cache,
        path=".",
        pull=True,
        buildargs=buildargs,
    )
    list(stream_output(build_logs, sys.stdout))
    _logger.info("----Finished building {} image----".format(engine_name))
    return ":".join([engine_name, tag])
