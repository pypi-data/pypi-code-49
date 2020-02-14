from time import sleep
import click
from mdk.utils import DockerCommand, VERSION


def mdk(*args, **kwargs):
    @click.group()
    @click.version_option(version=VERSION)
    @click.pass_context
    def cli(ctx, prog_name="mdk"):
        ctx.obj = DockerCommand()

    pass_docker = click.make_pass_decorator(DockerCommand)

    @cli.command(name="bash")
    @click.option("--nogpu", default=False, is_flag=True)
    @pass_docker
    def mdk_bash(docker, nogpu):
        if not docker.is_up():
            docker.up(nogpu=nogpu)
            sleep(1)
        docker.exec(["bash"])

    @cli.command(name="down")
    @pass_docker
    def mdk_down(docker):
        if docker.is_up():
            docker.container_cmd("stop")
        docker.container_cmd("rm")

    @cli.command(name="exec", context_settings=dict(ignore_unknown_options=True))
    @click.argument("command", nargs=-1, type=click.UNPROCESSED)
    @click.option("--interactive/--non-interactive", "-it", default=True, is_flag=True)
    @pass_docker
    def mdk_exec(docker, command, interactive):
        docker.exec(list(command), interactive)

    @cli.command(name="ls")
    @click.option("-v", "--verbose", is_flag=True)
    @pass_docker
    def mdk_ls(docker, verbose):
        if verbose:
            docker(["ps", "-a"])
            docker(["images"])
        else:
            docker(["ps", "-a", "--format", "table {{.Names}}\t{{.Image}}\t{{.Status}}\t{{.Created}}"])
            docker(["images", "--format", "table {{.ID}}\t{{.Repository}}\t{{.Tag}}\t{{.Size}}"])
        docker(["volume", "ls"])

    @cli.command(name="lsc")
    @click.option("-v", "--verbose", is_flag=True)
    @pass_docker
    def mdk_lsc(docker, verbose):
        cmd = ["ps", "-a"]
        if not verbose:
            cmd.extend([
                "--format",
                "table {{.Names}}\t{{.Image}}\t{{.Status}}\t{{.Created}}"])
        docker(cmd)

    @cli.command(name="lsi")
    @click.option("-v", "--verbose", is_flag=True)
    @pass_docker
    def mdk_lsi(docker, verbose):
        cmd = ["images"]
        if not verbose:
            cmd.extend([
                "--format",
                "table {{.ID}}\t{{.Repository}}\t{{.Tag}}\t{{.Size}}"])
        docker(cmd)

    @cli.command(name="lsv")
    @pass_docker
    def mdk_lsv(docker):
        docker(["volume", "ls"])

    @cli.command(name="pause")
    @pass_docker
    def mdk_pause(docker):
        docker.container_cmd("pause")

    @cli.command(name="prune")
    @click.option("-v", "--volumes", is_flag=True)
    @pass_docker
    def mdk_prune(docker, volumes):
        cmd = ["system", "prune", "-a"]
        if volumes:
            cmd.append("--volumes")
        docker(cmd)

    @cli.command(name="rm")
    @pass_docker
    def mdk_rm(docker):
        docker.container_cmd("rm")

    @cli.command(name="run", context_settings=dict(ignore_unknown_options=True))
    @click.argument("command", nargs=-1, type=click.UNPROCESSED)
    @click.option("--interactive/--non-interactive", "-it", default=True, is_flag=True)
    @pass_docker
    def mdk_run(docker, command, interactive):
        docker.run(list(command), interactive)

    @cli.command(name="sh")
    @click.option("--nogpu", default=False, is_flag=True)
    @pass_docker
    def mdk_sh(docker, nogpu):
        if not docker.is_up:
            docker.up(nogpu=nogpu)
            sleep(1)
        docker.exec(["sh"])

    @cli.command(name="start")
    @pass_docker
    def mdk_start(docker):
        docker.container_cmd("start")

    @cli.command(name="stop")
    @pass_docker
    def mdk_stop(docker):
        docker.container_cmd("stop")

    @cli.command(name="status")
    @pass_docker
    def mdk_status(docker):
        docker.status()

    @cli.command(name="unpause")
    @pass_docker
    def mdk_unpause(docker):
        docker.container_cmd("unpause")

    @cli.command(name="up")
    @click.option("--nogpu", default=False, is_flag=True)
    @pass_docker
    def mdk_up(docker, nogpu):
        docker.up(nogpu=nogpu)

    @cli.command(name="zsh")
    @click.option("--nogpu", default=False, is_flag=True)
    @pass_docker
    def mdk_zsh(docker, nogpu):
        if not docker.is_up():
            docker.up(nogpu=nogpu)
            sleep(1)
        docker.exec(["zsh"])

    cli(*args, **kwargs)
