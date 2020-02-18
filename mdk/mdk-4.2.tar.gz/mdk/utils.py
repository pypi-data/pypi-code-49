"""mdk utility functions & classes"""
import functools
import json
import os
from pathlib import Path
import pkg_resources
from re import findall, fullmatch
from socket import gaierror, gethostbyname, socket
import subprocess
from typing import List, TypeVar, Union
import sys

from click import echo, style

CONFIG_FILENAME: str = "mdk.json"
CONFIG_EXTENSION_FILENAME: str = "ext.mdk.json"
CONFIG_EXTENSION_USER_PATH: str = ".config/mdk/mdk.json"
ReturnCode = int
T = TypeVar('T')
VERSION = pkg_resources.require("mdk")[0].version


def forbid_active_container(func):
    @functools.wraps(func)
    def _active_container(self, *args, **kwargs):
        container_name = self.container_name()
        if self(["container", "inspect", container_name], io=False, log=False) != 0:
            return func(self, *args, **kwargs)
        Log.warning(f"{container_name} is already active (command not executed)")
        sys.exit(1)
    return _active_container


def require_active_container(func):
    @functools.wraps(func)
    def _active_container(self, *args, **kwargs):
        container_name = self.container_name()
        if self(["container", "inspect", container_name], io=False, log=False) != 0:
            Log.warning(f"{container_name} is not active (command not executed)")
            sys.exit(1)
        return func(self, *args, **kwargs)
    return _active_container


def mdk_version_sufficient(compare_version):
    def version_tuple(v):
        return tuple(findall(r"\d+(?=\D|$)", v)[:3])

    return version_tuple(VERSION) >= version_tuple(compare_version)


class DockerCommand():
    def __call__(self, args: List, io=True, log=True) -> ReturnCode:
        cmd = ["docker"] + args
        if log:
            Log.cmd(cmd)
        if io:
            return subprocess.call(cmd)
        return subprocess.call(
            cmd,
            stdin=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            stdout=subprocess.DEVNULL)

    def __init__(self):
        self.conf_root = None
        self.conf_paths = []
        self.conf_data = []

        # find global user conf
        if (Path.home()/CONFIG_EXTENSION_USER_PATH).is_file():
            self.conf_paths.append(Path.home()/CONFIG_EXTENSION_USER_PATH)

        # Find nearest config file & sibling ext conf (add "_" to cwd b/c cwd().parents doesn't include cwd)
        for dir_path in (Path().cwd()/"_").parents:
            if (dir_path/CONFIG_FILENAME).is_file():
                self.conf_root = dir_path
                self.conf_paths.append(dir_path/CONFIG_FILENAME)
                if (dir_path/CONFIG_EXTENSION_FILENAME).is_file():
                    self.conf_paths.append(dir_path/CONFIG_EXTENSION_FILENAME)
                break

        self.conf_data = [json.load(open(conf_path)) for conf_path in self.conf_paths]

        mdk_version_required = self.conf("mdk-version")
        if mdk_version_required and not mdk_version_sufficient(mdk_version_required):
            Log.error(f"mdk version check",
                      f"project requires mdk>={mdk_version_required} (current: {VERSION})")
            sys.exit(1)

    def cli_opts(self) -> List[str]:
        opt_builder: List[str] = []
        for volume in self.conf("volumes", is_list=True):
            vol_str = os.path.expandvars(volume)
            vol_nfs = fullmatch(r"nfs\((?P<host>[-\w\.]+):(?P<remote_dir>[^()]+)\):(?P<target_dir>[^()]+)", vol_str)
            if vol_nfs:
                try:
                    vol_host_ip = gethostbyname(vol_nfs.group("host"))
                    socket().connect((vol_host_ip, 111))
                    opt_builder += ["--mount",
                                    f"type=volume,target={vol_nfs.group('target_dir')},volume-opt=type=nfs4,"
                                    f"volume-opt=device={vol_nfs.group('host')}:{vol_nfs.group('remote_dir')},"
                                    f'"volume-opt=o=fsc,addr={vol_host_ip}"']
                except gaierror:
                    Log.warning(f"Connecting to {vol_nfs.group('host')}\nSkipping volume mount: {vol_str}")
                    break
            else:
                if vol_str.startswith('.'):
                    vol_str = str(self.conf_root) + vol_str.lstrip('.')
                elif vol_str.startswith('~'):
                    vol_str = str(Path.home()) + vol_str.lstrip('~')
                opt_builder += ["-v", vol_str]

        if self.conf("shareX11") is True:
            opt_builder += ["-v", "/tmp/.X11-unix:/tmp/.X11-unix",
                            "-e", f"DISPLAY={os.getenv('DISPLAY')}"]

        for env_var in self.conf("environment", is_list=True):
            env_pair = env_var.split('=')
            if len(env_pair) != 2:
                continue
            if env_pair[1].startswith('$'):
                env_name = env_pair[1].lstrip('$')
                if env_name == "UID":
                    env_pair[1] = str(os.getuid())
                elif env_name == "GID":
                    env_pair[1] = str(os.getgid())
                else:
                    env_pair[1] = os.path.expandvars(env_pair[1])
            if env_pair[1] is not None:
                opt_builder += ["-e", '='.join(env_pair)]

        if self.conf("core-image") is True:
            opt_builder += ["-e", f"HOST_UID={os.getuid()}",
                            "-e", f"DOCKER_CONTAINER_NAME={self.conf('name')}",
                            "-e", f"DOCKER_CONTAINER_ROOT=~/{Path.cwd().relative_to(Path.home())}"]

        if self.conf('workdir'):
            opt_builder += ["-w", self.conf('workdir')]

        if self.conf("options", is_list=True):
            opt_builder += self.conf("options", is_list=True)

        return opt_builder

    @require_active_container
    def container_cmd(self, command: str) -> ReturnCode:
        container_name = self.container_name()
        code = self([command, container_name], io=False)
        if code == 0:
            Log.success(f"{command} -> {container_name}")
        else:
            Log.error(f"{command} -> {container_name}", f"error code {code}")
        return code

    def container_name(self) -> str:
        container_name = self.conf("name")
        if container_name:
            return container_name
        return "mdk" + str(self.conf_root).replace('/', '_')

    def conf(self, key: str, is_list=False) -> Union[T, None]:
        # gather option in all configs
        all_data = [data[key] for data in self.conf_data if key in data]

        # case: conf option not found
        if not all_data:
            return [] if is_list else None

        # case: conf option found as list in each conf
        if isinstance(all_data[-1], list):
            return [el for data in all_data for el in data]

        # standard case
        return all_data[-1]

    def conf_req(self, key: str) -> str:
        if self.conf_root is None:
            Log.error(f"finding config", f"{CONFIG_FILENAME} does not exist in current directory or its parents")
            sys.exit(1)
        val = self.conf(key)
        if val is None:
            Log.error(f"loading config", f"\"{key}\" not assigned in {self.conf_root/CONFIG_FILENAME}")
            sys.exit(1)
        return val

    def output(self, args):
        return subprocess.getoutput("docker " + " ".join(args))

    @require_active_container
    def exec(self, exec_cmd: List[str], interactive=True) -> ReturnCode:
        cmd = ["exec", self.container_name()]
        if interactive:
            cmd.insert(1, "-it")
        return self(cmd + exec_cmd)

    def is_up(self) -> bool:
        return self(["container", "inspect", self.container_name()], io=False, log=False) == 0

    def run(self, run_cmd: List[str], interactive=True) -> ReturnCode:
        cmd = ["run", self.conf_req("image")]
        if interactive:
            cmd.insert(1, "-it")
        return self(cmd + run_cmd)

    def status(self):
        container_name = self.container_name()

        Log.log("Container:")
        Log.log("  {:12}{}".format("Name", container_name))

        if self.is_up:
            status_fields = ["Image", "ID", "Status", "Command", "Size"]
            docker_output = self.output([
                "ps", "-a",
                "--format", "{{." + "}},{{.".join(status_fields) + "}}",
                "--filter", f"name={container_name}",
            ]).strip(" \n")
            status_results = docker_output.split(",") if docker_output else None
            if len(status_results) == len(status_fields):
                for field in status_fields:
                    Log.log("  {:12}{}".format(field, status_results.pop(0)))
        else:
            Log.log("  {:12}{}".format("Image", self.conf_req('image')))
            Log.log("  {:12}{}".format("Status", "container not created"))

    @forbid_active_container
    def up(self, nogpu=False) -> ReturnCode:
        container_name = self.container_name()
        cmd = ["run", "-td", "--name", container_name]
        cmd += self.cli_opts()

        # optionally remove the `--gpus ***` arg
        if nogpu and "--gpus" in cmd:
            gpus_opt_idx = cmd.index("--gpus")
            cmd.pop(gpus_opt_idx)
            cmd.pop(gpus_opt_idx)

        code = self(cmd + [self.conf_req("image")])
        if code == 0:
            Log.success(f"{container_name} is now active")
        else:
            Log.error(f"starting {container_name}", f"error code {code}")
        return code


class Log():
    @staticmethod
    def cmd(args) -> None:
        if args:
            echo(style(f"$ {' '.join(args)}", fg="cyan"))

    @staticmethod
    def error(context, message) -> None:
        echo(f"{style('ERROR:', fg='red')} {context}\n\t{message}")

    @staticmethod
    def log(message) -> None:
        echo(message)

    @staticmethod
    def success(context) -> None:
        echo(f"{style('SUCCESS:', fg='green')} {context}")

    @staticmethod
    def warning(message) -> None:
        echo(f"{style('WARNING:', fg='yellow')} {message}")
