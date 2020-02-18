#
# This command is python2 and 3 compatible
#

from __future__ import print_function

import os
import shutil
import subprocess
import sys
import textwrap

from cloudmesh.common.console import Console
from cloudmesh.configuration.Config import Config
from docopt import docopt
from pathlib import Path

from cloudmesh_cmsd.cmsd.__version__ import version
from cloudmesh.common.Shell import Shell

DOCKERFILE = """
FROM python:3.8.1-buster

RUN apt-get -y update
RUN apt-get -y upgrade
RUN apt-get -y --no-install-recommends install \
    build-essential \
    git \
    curl \
    wget \
    sudo \
    net-tools \
    gnupg

RUN wget -qO - https://www.mongodb.org/static/pgp/server-4.2.asc | sudo apt-key add -
RUN echo "deb http://repo.mongodb.org/apt/debian buster/mongodb-org/4.2 main" | sudo tee /etc/apt/sources.list.d/mongodb-org-4.2.list

RUN apt-get -y update
RUN apt-get install -y mongodb-org-shell

RUN pip install cloudmesh-installer

RUN mkdir cm
WORKDIR cm

RUN cloudmesh-installer git clone cloud
RUN cloudmesh-installer git clone aws
RUN cloudmesh-installer git clone azure

RUN cloudmesh-installer install cloud
RUN cloudmesh-installer install azure
RUN cloudmesh-installer install aws

RUN mkdir $HOME/.cloudmesh
RUN mkdir $HOME/.ssh

COPY init.sh /
RUN chmod +x /init.sh

ENTRYPOINT /bin/bash /init.sh; /bin/bash

#docker run --rm -d -v /aux/github/cm/docker/mongo_data:/data/db -p 127.0.0.1:27017:27017/tcp --name mongos mongo:4.2
#docker run --rm -it -v /aux/github/cm/docker/cloudmesh_home:/root/.cloudmesh -v ~/.ssh:/root/.ssh --net host --name cms-container cloudmesh-cms
"""

INIT_SH = """
#!/bin/bash

cloudmesh-installer git pull cloud
cloudmesh-installer git pull aws
cloudmesh-installer git pull azure
"""

entry = """
db.createUser(
    {
        user: "<your-username>",
        pwd: "<your-password>",
        roles: [
            {
                role: "readWrite",
                db: "cloudmesh"
            }
        ]
    }
);
"""

DEFAULT_CLOUDMESH_HOME_DIR = os.path.expanduser("~/.cloudmesh")
DEFAULT_SSH_DIR = os.path.expanduser("~/.ssh")
CMS_CONTAINER_NAME = "cloudmesh-cms-container"
MONGO_CONTAINER_NAME = "cloudmesh-mongo-container"
CMS_IMAGE_NAME = "cloudmesh/cms"

def _run_os_command(cmd_str):
    print("command:", cmd_str)
    out = subprocess.check_output(cmd_str).decode("utf-8")
    return out.strip() if not None else None


def _docker_exec(cmd_str, container_name=CMS_CONTAINER_NAME):
    if isinstance(cmd_str, list):
        cmd = ["docker", "exec", container_name]
        cmd.extend(cmd_str)
        return _run_os_command(cmd)
    else:
        os.system(f"docker exec {container_name} " + cmd_str)


def _is_container_running(name):
    output = _run_os_command(["docker", "container", "ls",
                              "--filter", f"name={name}",
                              "--format", "\"{{.Names}}\""])

    return name in output


# you can use writefile(filename, entry) to for example write a file. make
# sure to use path_expand and than create a dir. you can resuse commands form
# cloudmesh.common, but no other class

class CmsdCommand:

    def __init__(self):
        self.config_path = os.path.expanduser("~/.cloudmesh/cmsd")
        self.compose = f'docker-compose -f {self.config_path}/docker-compose.yml'
        self.username = ''
        self.password = ''

    def docker_compose(self, command):
        os.system(f'{self.compose} {command}')

    def update(self):
        self.docker_compose("down")

        self.delete_image()
        try:
            os.system("docker rmi {CMS_IMAGE_NAME}")
        except:
            pass
        self.clean()
        self.setup()
        self.up()
        self.create_image()

    def create_image(self):
        """
        reates image locally
        :return:
        """
        self.docker_compose('build')

    def download_image(self):
        """
        downloads image from dockerhub
        :return:
        """
        self.docker_compose('pull mongo')

    def delete_image(self):
        """
        deletes the cloudmesh image locally
        :return:
        """
        self.docker_compose('rm')

    def run(self, command=""):
        """
        run the command via the docker container

        :param command: the cms command to be run in the container
        """
        _docker_exec(command)

    def cms(self, command=""):
        """
        run the command via the docker container

        :param command: the cms command to be run in the container
        """
        _docker_exec("cms " + command)

    def up(self):
        """
        starts up the containers for cms
        """
        os.system(f"docker start {CMS_CONTAINER_NAME} {MONGO_CONTAINER_NAME}")

    def ps(self):
        """
        docker-compose ps
        """
        os.system(f"docker ps")

    def stop(self):
        """
        docker-compose stop
        """
        os.system(f"docker stop {CMS_CONTAINER_NAME} {MONGO_CONTAINER_NAME}")

    def shell(self):
        """
        docker-compose stop
        """
        os.system(f"docker exec -it {CMS_CONTAINER_NAME} /bin/bash")

    def setup(self, cloudmesh_home_dir=None):
        """
        this will copy the docker compose yaml and json file into the config_path
        only if the files do not yet esixt
        :param cloudmesh_home_dir:
        :return:
        """
        if cloudmesh_home_dir is None:
            cloudmesh_home_dir = DEFAULT_CLOUDMESH_HOME_DIR

        if not os.path.exists(cloudmesh_home_dir):
            os.mkdir(cloudmesh_home_dir)

        os.system("cms debug off") # there is a bug in the stdout buffer if we do not do this

        output = _run_os_command(["docker", "images", "--format",
                                  "\"{{lower .Repository}}\"", CMS_IMAGE_NAME])

        if CMS_IMAGE_NAME in output:
            print(f"{CMS_IMAGE_NAME} image available!")
        else:
            print(f"{CMS_IMAGE_NAME} image not found! Building...")

            temp_dir = cloudmesh_home_dir + '/temp'
            os.mkdir(temp_dir)

            with open(temp_dir + '/Dockerfile', 'w') as f:
                f.write(DOCKERFILE)

            with open(temp_dir + '/init.sh', 'w') as f:
                f.write(INIT_SH)

            os.system(f"docker build -t {CMS_IMAGE_NAME} {temp_dir}")

            shutil.rmtree(temp_dir)

        if _is_container_running(CMS_CONTAINER_NAME):
            print(f"{CMS_CONTAINER_NAME} container running!")
        else:
            print(f"{CMS_CONTAINER_NAME} container not running! Starting...")
            os.system(f"docker run -d -it "
                      f"-v {cloudmesh_home_dir}:/root/.cloudmesh "
                      f"-v ~/.ssh:/root/.ssh --net host "
                      f"--name {CMS_CONTAINER_NAME} {CMS_IMAGE_NAME}")

        _docker_exec(f"cms help")

        if _is_container_running(MONGO_CONTAINER_NAME):
            print(f"{MONGO_CONTAINER_NAME} container running!")
        else:
            print(f"{MONGO_CONTAINER_NAME} container not running! Starting...")
            mongo_pw = _docker_exec(["cms", "config", "value",
                                     "cloudmesh.data.mongo.MONGO_PASSWORD"])
            Console.ok("mongo password set")
            if "TBD" in mongo_pw:
                Console.warning(f"Please set MONGO_PASSWORD in {cloudmesh_home_dir}"
                      f"/cloudmesh.yaml file and rerun setup!")
            else:

                if os.name == 'nt':
                    print(f"Running on windows... creating a separate volume for mongodb")
                    monogo_data_path = "cms_mongodb"
                    os.system(f"docker volume create {monogo_data_path}")
                else:
                    monogo_data_path = cloudmesh_home_dir + "/mongodb"
                    if not os.path.exists(monogo_data_path):
                        os.mkdir(monogo_data_path)


                _docker_exec("cms config set cloudmesh.data.mongo.MODE=running")
                Console.ok("Set mongo to runing")

                print ("IIII", CMS_IMAGE_NAME)

                command = f"docker run -d --name {MONGO_CONTAINER_NAME} " \
                          f"-v {monogo_data_path}:/data/db " \
                          f"-p 127.0.0.1:27017:27017/tcp " \
                          f"-e MONGO_INITDB_ROOT_USERNAME=admin " \
                          f"-e MONGO_INITDB_ROOT_PASSWORD={mongo_pw} " \
                          f" mongo:4.2 " \
                          f"{CMS_IMAGE_NAME}"

                print ("CCC>>>>>", command, "<<<<<")


                os.system(command)


    def clean(self):
        """
        remove the ~/.cloudmesh/cmsd dir
        :return:
        """

        # data dir had to be deleted through the container as we dont have
        # permission to delete the directory through the host OS
        print("Removing mongoDB data dir")
        _docker_exec("/bin/bash -c \"mongod --shutdown; rm -rf /data/db/*\"",
                     container_name=MONGO_CONTAINER_NAME)
        Console.warning("Please clean up CLOUDMESH_HOME_DIR/mongodb "
              "if not empty!")

        print("Stopping containers...")
        self.stop()

        print("Removing containers...")
        os.system(f"docker container rm {CMS_CONTAINER_NAME} "
                  f"{MONGO_CONTAINER_NAME}")

    def list_images(self):
        os.system("docker images | fgrep {CMS_IMAGE_NAME}")


    def version(self):
        os.system("docker images | fgrep {CMS_IMAGE_NAME}")

    def check_dir(self, directory):
        if os.path.isdir(directory):
            Console.ok(f"Directory found: {directory}")
        else:
            Console.error(f"Directory not found: {directory}")


    def check(self):
        if 'CLOUDMESH_HOME_DIR' in os.environ:
            directory = os.environ['CLOUDMESH_HOME_DIR']
            Console.ok(f'CLOUDMESH_HOME_DIR={directory}')
        else:
            directory = DEFAULT_CLOUDMESH_HOME_DIR

        self.check_dir(directory)

        mongodir= Path(directory) / 'mongodb'

        self.check_dir(mongodir)


        yamlfile = str(Path(directory) / "cloudmesh.yaml")
        config = Config(config_path=yamlfile)

        if config["cloudmesh.data.mongo.MODE"] != 'running':
            Console.error("cloudmesh.data.mongo.MODE!='running'")

        if config["cloudmesh.data.mongo.MONGO_PASSWORD"] != 'TBD':
            Console.ok("cloudmesh.data.mongo.PASSWORD is set")


    def do_cmsd(self):
        """
        ::

          Usage:
                cmsd --help
                cmsd --yaml (native | docker)
                cmsd --setup [CLOUDMESH_HOME_DIR] [--download]
                cmsd --check
                cmsd --clean
                cmsd --version
                cmsd --update
                cmsd --image
                cmsd --start
                cmsd --stop
                cmsd --ps
                cmsd --shell
                cmsd COMMAND... [--refresh]
                cmsd


          This command passes the arguments to a docker container
          that runs cloudmesh.

          Arguments:
              COMMAND the commands we bass along

          Description:

            cmsd --help

                prints this manual page

            cmsd --yaml (native | docker)

                switches the cloudmesh.yaml file to be used in native or docker
                mode, for cmsd to work, it must be in docker mode.


            cmsd --image

                list the container

            cmsd --setup [--download]

                downloads the source distribution, installes the image loaclly

                [--download is not yet supported, and will be implemented when the
                source setup works]

            cmsd --clean

                removes the container form docker

            cmsd --version

                prints out the verison of cmsd and the version of the container

            cmsd --update

                gets a new container form dockerhub

            cmsd COMMAND

                The command will be executed within the container, just as in
                case of cms.

            cmsd

                When no command is specified cms will be run in interactive
                mode.


        """

        doc = textwrap.dedent(self.do_cmsd.__doc__)
        arguments = docopt(doc, help=False)


        config = Config()

        #
        # check for yaml file consistency for mongo
        #

        # ok
        # if config["cloudmesh.data.mongo.MODE"] != "docker" and \
        #         config["cloudmesh.data.mongo.MONGO_HOST"] != "mongo":
        #     print(
        #         "ERROR: The cloudmesh.yaml file is not configured for docker. Please use")
        #     print()
        #     print(" cmsd --yaml docker")
        #     print()
        #     return ""

        if arguments["--yaml"] and arguments["native"]:
            # implemented not tested

            print("switch to native cms mode")

            config["cloudmesh.data.mongo.MODE"] = "native"
            config["cloudmesh.data.mongo.MONGO_HOST"] = "127.0.0.1"
            config.save()

        elif arguments["--yaml"] and arguments["docker"]:
            # implemented not tested

            print("switch to docker cms mode")
            config["cloudmesh.data.mongo.MODE"] = "docker"
            config["cloudmesh.data.mongo.MONGO_HOST"] = "mongo"
            config.save()

        elif arguments["--setup"]:
            self.setup(cloudmesh_home_dir=arguments['CLOUDMESH_HOME_DIR'])

        elif arguments["--version"]:
            print("cmsd:", version)
            self.version()

        elif arguments["--clean"]:
            self.clean()

        elif arguments['--help']:
            print(doc)

        elif arguments['--image']:
            #
            # BUG does not work on windows. fix
            #
            if sys.platform == 'win32':
                raise NotImplementedError
            print(
                "REPOSITORY                              TAG                 IMAGE ID            CREATED             SIZE")
            self.list_images()

        elif arguments["--stop"]:
            self.stop()

        elif arguments["--start"]:
            self.up()

        elif arguments["--ps"]:
            self.ps()

        elif arguments["--update"]:
            self.update()

        elif arguments["--shell"]:
            self.shell()

        elif arguments["COMMAND"]:
            command = ' '.join(sys.argv[1:])
            self.cms(command)

        elif arguments["COMMAND"] is None:
            print("start cms interactively")
            os.system("docker exec -ti cmsd /bin/bash")
            # self.docker_compose("exec cmsd /bin/bash")

        elif arguments["--check"]:
            self.check()

        else:
            print(doc)

        return ""


def main():
    command = CmsdCommand()
    command.do_cmsd()


if __name__ == "__main__":
    main()
