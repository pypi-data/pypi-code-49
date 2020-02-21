import os
import subprocess
import socket
import uuid
import pytest
from compose.cli.main import TopLevelCommand
from compose.cli.main import project_from_options
from compose.cli.docopt_command import DocoptDispatcher
from compose.project import Project
from compose.container import Container


# {{{ Compose hooks


def compose_project_Project___getitem__(self, key):
    """ get a docker compose service
    """
    project = "com.docker.compose.project"
    service = "com.docker.compose.service"

    for cnt in self.containers():
        if (
            project in cnt.labels
            and cnt.labels[project] == self.name
            and cnt.labels[service] == key
        ):
            return cnt
    raise KeyError


def compose_container_Container__addr(self):
    """ get the container address of a service
    """
    networks = self.get("NetworkSettings.Networks")
    assert len(networks) == 1
    network = next(iter(networks.values()))
    return network["IPAddress"]


def compose_container_Container__port(self):
    """ get exposed ports of service

    Return a port or a list of ports
    """
    ports = [int(p.split("/")[0]) for p in self.get("NetworkSettings.Ports")]
    return ports[0] if len(ports) == 1 else ports


def compose_container_Container___getattr__(self, name):
    """ expose addr and port hooks as attribute
    """
    if name == "port":
        return self._port()
    elif name == "addr":
        return self._addr()
    raise AttributeError("Invalid attribute name {}".format(name))


Project.__getitem__ = compose_project_Project___getitem__
Container._addr = compose_container_Container__addr
del Container.ports
Container._port = compose_container_Container__port
Container.__getattr__ = compose_container_Container___getattr__


# }}}


class DockercConfig:
    """ Format pytest options to docker-compose parameters
    """

    def __init__(self, config):
        opts = config.option
        self.run = not opts.dockerc_norun
        self.attach_network = opts.dockerc_attach_network
        self.options = {}
        self.up_options = {}

        self.projectdir = opts.dockerc_projectdir or str(config.rootdir)
        self.options["--project-directory"] = self.projectdir
        if self.run and opts.dockerc_projectname is None:
            self.options["--project-name"] = self.generate_project_name()
        elif opts.dockerc_projectname:
            self.options["--project-name"] = opts.dockerc_projectname
        if opts.dockerc_filepath:
            self.options["--file"] = [opts.dockerc_filepath]

        if opts.dockerc_build is True:
            self.up_options["--build"] = True
        if opts.dockerc_services:
            self.up_options["SERVICE"] = opts.dockerc_services
        self.up_options["--detach"] = True

    def generate_project_name(self):
        """ Create a compose project

        The basename of the compose directory is used plus a random suffix, in order
        to run several tests suites in the same hosts.
        """
        return "{0}-{1}".format(
            os.path.basename(self.options["--project-directory"]),
            str(uuid.uuid4()).split("-")[0],
        )


def link_network(project, detach=False):
    """ In Docker outside of Docker (DooD) mode, a network connection is
    required to the docker-compose networks. The aim is to be able to perform
    requests from pytest to the docker-compose services.
    """
    containerid = None
    hostname = socket.gethostname()

    if detach:
        link = project.client.disconnect_container_from_network
    else:
        link = project.client.connect_container_to_network

    # check that the host is inside a container
    for container in project.client.containers():
        if container["Id"].startswith(hostname) or (
            any(hostname in n for n in container["Names"])
        ):
            containerid = container["Id"]

    # attach/detach the container pytest to the docker compose network
    if containerid is not None:
        for network in project.networks.networks.values():
            link(containerid, network.full_name)


@pytest.fixture(scope="session")
def dockerc_config(request):
    """ Return config parameter to init Compose project
    """
    return DockercConfig(request.config)


@pytest.fixture(scope="session")
def dockerc(dockerc_config):
    """ Run, manage and stop Docker Compose project from Docker API

    This fixture loads the `docker-compose.yml` file, then it runs
    command like `docker-compose up --build` at the beginning of the fixture,
    and `docker-compose down` at the end.

    Return a `compose.project.Project`_ object to deal with your containers.

    .. _compose.project.Project: https://github.com/docker/compose/blob/master/compose/project.py

    """  # noqa
    docopt = DocoptDispatcher(TopLevelCommand, {})
    project = project_from_options(
        dockerc_config.projectdir, options=dockerc_config.options
    )
    cmd = TopLevelCommand(project)

    if dockerc_config.run:
        opts = docopt.parse("up")[2]
        opts.update(dockerc_config.up_options)
        cmd.up(opts)

        if dockerc_config.attach_network:
            link_network(project)

    yield project

    if dockerc_config.run:
        if dockerc_config.attach_network:
            link_network(project, detach=True)

        cmd.down(docopt.parse("down")[2])


@pytest.fixture(scope="session")
def dockerc_logs(dockerc_config):
    """ Display the logs of the Compose project
    """
    if dockerc_config.run:
        cmd = ["docker-compose"]
        for k, v in dockerc_config.options.items():
            if k == "--file":
                for f in v:
                    cmd.append(k)
                    cmd.append(f)
            else:
                cmd.append(k)
                cmd.append(v)
        cmd.extend(["logs", "-f"])

        proc = subprocess.Popen(cmd)
        yield proc
        proc.terminate()
    else:
        yield
