#!/usr/bin/python3

import argparse
from datetime import datetime
import json
import logging
import os
import subprocess
from typing import List, Union, Optional

log = logging.getLogger("python-deploy")


class DeployError(RuntimeError):
    pass


def flatten(items: List[Union[str, List[str]]]) -> List[str]:
    return [
        item
        for sublist in items
        for item in (sublist if isinstance(sublist, list) else [sublist])
    ]


def check_call(params: List[Union[str, List[str]]]) -> Optional[bytes]:
    try:
        params = flatten(params)
        log.debug(f"> {' '.join(params)}")
        result = subprocess.check_output(params, stderr=subprocess.STDOUT)
        log.debug(f"$ {result.decode()}")
        return result
    except subprocess.CalledProcessError as exc:
        log.error("Called process error:")
        log.error(exc.output.decode())
        raise DeployError(f"Command {params[0]} failed.")


def has_git_repo() -> bool:
    return os.path.isdir(".git")


def is_clean_repo() -> bool:
    status = check_call(["git", "status", "--short"])
    return status.strip() == b""


def get_current_git_hash() -> str:
    return check_call(["git", "rev-parse", "HEAD"]).strip().decode("utf-8")


def tag_docker_image(
    existing_image: str, new_tag: str, push: bool = False
) -> None:
    check_call(["docker", "tag", existing_image, new_tag])
    if push:
        push_image(new_tag)


def build_image(image_cfg: dict, tags: List[str], no_cache: bool):
    check_call(
        [
            "docker",
            "image",
            "build",
            image_cfg.get("dir", "src"),
            flatten([["-t", tag] for tag in tags]),
            "-f",
            image_cfg.get("dockerfile", "deploy/docker/Dockerfile"),
            ["--no-cache"] if no_cache else [],
        ]
    )


def push_image(tag):
    check_call(["docker", "image", "push", tag])


def pull_image(tag: str) -> None:
    check_call(["docker", "image", "pull", tag])


def run_image_command(tag: str, params: List[str]) -> None:
    check_call(
        [
            "docker",
            "run",
            tag,
            params
        ])


def set_current_image(k8s_config, tag):
    check_call(
        [
            "kubectl",
            "set",
            "image",
            "--namespace",
            k8s_config["namespace"],
            "deployment/{}".format(k8s_config["deployment"]),
            "{}={}".format(k8s_config["container"], tag),
        ]
    )


def get_current_image(k8s_config):
    container = k8s_config["container"]
    jsonpath = f'{{..containers[?(@.name=="{container}")].image}}'

    return check_call(
        [
            "kubectl",
            "get",
            "deployment",
            "--namespace",
            k8s_config["namespace"],
            f"-o=jsonpath={jsonpath}",
        ]
    ).decode("utf-8")


def get_k8s_namespaces():
    ns_bytes = check_call(["kubectl", "get", "namespaces"])
    ns_text = ns_bytes.decode("utf-8")
    namespaces = []
    for line in ns_text.split("\n")[1:]:
        if not line.strip():
            continue
        namespaces.append(line.split()[0])
    return namespaces


class Deploy(object):
    def __init__(self, args):
        self.args = args
        if not os.path.isfile("deploy/deploy.json"):
            raise DeployError(
                "Configuration file deploy/deploy.json not found. "
                "Check your CWD."
            )
        with open("deploy/deploy.json", "r") as configfile:
            self.config = json.loads(configfile.read())
        if self.args.service:
            for srv in self.args.service:
                if srv not in self.config.keys():
                    raise DeployError(f"Unknown service: {srv}")
            self.config = {
                k: v for k, v in self.config.items() if k in self.args.service
            }
        self.version = self._check_version()

    def _check_version(self):
        if not self.args.force:
            if not has_git_repo():
                raise DeployError(
                    "There is no Git repository available. "
                    "Use --force if you don't care about it"
                )
            if not is_clean_repo():
                raise DeployError(
                    "Git repository is dirty. Commit your changes "
                    "or use --force if you don't care about it"
                )
        else:
            log.warning("Used --force. I hope you know what you are doing.")
        if self.args.version == "commit":
            try:
                return get_current_git_hash()
            except subprocess.CalledProcessError:
                ci_commit_sha = os.getenv("CI_COMMIT_SHA")
                if ci_commit_sha:
                    log.warning("Can't determine commit hash: "
                                "getting version from $CI_COMMIT_SHA.")
                    return ci_commit_sha
                else:
                    raise DeployError(
                        "Can't determine commit hash. Use alternative "
                        "--version variant."
                    )
        elif self.args.version == "date":
            return datetime.utcnow().strftime("v%Y%m%d%H%M%S")
        elif self.args.version == "latest":
            return "latest"
        else:
            raise RuntimeError("Unknown version variant.")

    def _version_tag(self, config):
        return f"{config['image']}:f{self.version}"

    def _tags(self, config):
        return [self._version_tag(config)] + [
            f"{config['image']}:f{tag}"
            for tag in (self.args.tag or [])
            if ":" not in tag
        ]

    def _build(self, service):
        config = self.config[service]["docker"]
        log.info(f"Building image {self._version_tag(config)}")
        build_image(config, self._tags(config), self.args.no_cache)

    def build(self):
        for service in self.config.keys():
            self._build(service)

    def _push(self, service):
        config = self.config[service]["docker"]
        for tag in self._tags(config):
            log.info(f"Pushing image {tag}")
            push_image(tag)

    def push(self):
        self.build()
        for service in self.config.keys():
            self._push(service)

    def pull(self):
        for service in self.config.keys():
            config = self.config[service]["docker"]
            version_tag = self._version_tag(config)
            log.info(f"Pulling image {version_tag}")
            pull_image(version_tag)

    def _deploy(self, service, environment):
        if environment not in self.config[service]:
            raise DeployError(
                f"There is no {environment} key defined "
                f"for {service} service"
            )
        config = self.config[service]["docker"]
        version_tag = self._version_tag(config)
        if environment == "k8s":
            tag = f"{config['image']}:master"
            log.info(f"Tagging image {version_tag} as {tag}")
            tag_docker_image(version_tag, tag, push=True)
        tag = f"{config['image']}:latest"
        log.info(f"Tagging image {version_tag} as {tag}")
        tag_docker_image(version_tag, tag, push=True)
        log.info(
            f"Setting image {version_tag} for {environment} environment"
        )
        set_current_image(self.config[service][environment], version_tag)

    def production(self):
        if not self.args.deploy_only:
            self.push()
        for service in self.config.keys():
            self._deploy(service, "k8s")

    def staging(self):
        if not self.args.deploy_only:
            self.push()
        for service in self.config.keys():
            self._deploy(service, "k8s-staging")

    def image(self):
        for service in self.config.keys():
            config = self.config[service]["docker"]
            version_tag = self._version_tag(config)
            print(version_tag)

    def run(self):
        for service in self.config.keys():
            config = self.config[service]["docker"]
            version_tag = self._version_tag(config)
            run_image_command(version_tag, self.args.cmd)

    def perform(self):
        return getattr(self, self.args.command)()


def main():
    parser = argparse.ArgumentParser(description="Deploy the application.")

    service_subparser = argparse.ArgumentParser(add_help=False)
    service_subparser.add_argument(
        "--service",
        "-s",
        action="append",
        help="Specify services to perform action (default: all)",
    )
    service_subparser.add_argument(
        "--force",
        "-f",
        action="store_true",
        help="Don't perform check-ups, force deploy (not recommended)",
    )
    service_subparser.add_argument(
        "--verbose",
        "-v",
        action="store_true",
        help="Print spawned subcommands and their outputs",
    )
    service_subparser.add_argument(
        "--version",
        help="Alternative version tag",
        default="commit",
        choices=["commit", "date", "latest"],
    )

    build_subparser = argparse.ArgumentParser(add_help=False)
    build_subparser.add_argument(
        "--tag", "-t", action="append", help="Alternative tags for image"
    )
    build_subparser.add_argument(
        "--no-cache",
        action="store_true",
        help="Pass --no-cache to docker build",
    )

    deploy_subparser = argparse.ArgumentParser(add_help=False)
    deploy_subparser.add_argument(
        "--deploy-only", action="store_true",
        help="Don't build and push, just set k8s image"
    )

    commands = parser.add_subparsers(help="Deploy commands", dest="command")
    commands.required = True
    commands.add_parser(
        "build",
        parents=[build_subparser, service_subparser],
        help="Only build images",
    )
    commands.add_parser(
        "push",
        parents=[build_subparser, service_subparser],
        help="Build and push images",
    )
    commands.add_parser(
        "pull", parents=[service_subparser], help="Pull images from registry"
    )
    commands.add_parser(
        "staging",
        parents=[build_subparser, service_subparser, deploy_subparser],
        help="Build, push and deploy images to the staging environment",
    )
    commands.add_parser(
        "production",
        parents=[build_subparser, service_subparser, deploy_subparser],
        help="Build, push and deploy images to the PRODUCTION environment",
    )
    commands.add_parser(
        "image",
        parents=[service_subparser],
        help="Show image names"
    )
    run_command = commands.add_parser(
        "run",
        parents=[service_subparser],
        help="Run interactive command for service images"
    )
    run_command.add_argument("cmd", nargs="*")
    args = parser.parse_args()
    logging.basicConfig(
        level=logging.DEBUG if args.verbose else logging.INFO,
        format="[%(levelname)s] %(message)s",
    )
    try:
        Deploy(args).perform()
    except DeployError as e:
        raise SystemExit(f"[!] {e.args[0]}")


if __name__ == "__main__":
    main()
