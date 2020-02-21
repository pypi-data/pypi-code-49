from pathlib import Path
from argparse import ArgumentTypeError
from .fixtures import dockerc, dockerc_logs, dockerc_config  # noqa


def pytest_addoption(parser):
    group = parser.getgroup("dockerc", "dockerc")

    def ex(msg):
        raise ArgumentTypeError(msg)

    group._addoption(
        "--dockerc-norun",
        action="store_true",
        help="disable the run and stop commands of docker-compose",
    )
    group._addoption(
        "--dockerc-attach-network",
        action="store_true",
        help=(
            "attach the pytest container to the docker-compose network,"
            "only if pytest is started inside a container"
        ),
    )
    group._addoption(
        "--dockerc-filepath",
        action="store",
        help="set the Compose file path",
        type=lambda x: x if Path(x).is_file() else ex("file `%s` does not exist" % x),
    )
    group._addoption(
        "--dockerc-projectdir",
        action="store",
        help="set the working directory of the Compose project",
        type=lambda x: x if Path(x).is_dir() else ex("dir `%s` does not exist" % x),
    )
    group._addoption(
        "--dockerc-projectname",
        action="store",
        help="set project name of the Compose project",
    )
    group._addoption(
        "--dockerc-build",
        action="store_true",
        help="build images before starting containers",
    )
    group._addoption(
        "--dockerc-services",
        action="append",
        default=None,
        help="select services to run",
    )
