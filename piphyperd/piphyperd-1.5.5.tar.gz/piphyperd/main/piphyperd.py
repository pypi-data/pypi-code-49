"""THIS SOFTWARE IS PROVIDED AS IS.

Released under GNU General Public License:
<https://www.gnu.org/licenses/gpl-3.0.en.html>

USE IT AT YOUR OWN RISK.

PipHyperd is a simple python object to leverage pip programmatically.
It can provide automation and dependencies control within your workflows.

The module is published on PyPi: <https://pypi.org/project/piphyperd/>.
The code is available on GitLab: <https://gitlab.com/hyperd/piphyperd>.
"""

from subprocess import Popen, PIPE, CalledProcessError
import sys
from pathlib import Path
from typing import Optional, List, Tuple, Any, Union


class PipHyperd:
    """Wrapper class around pip.

    python_path -- Path to the python binary to use

    *pip_options -- command options, e.g.: pip {pip_options} uninstall testpypi
    """

    def __init__(self, *pip_options: Any, python_path: Optional[Path] = None):
        """Init method"""
        # Path to the python binary to use
        self.python_path: Optional[Path] = python_path
        # A list of pip packages to install || show || download || uninstall
        self.packages: List[str] = list()
        # pip command args, e.g.: pip download testpypi {command_args}
        self.command_args: List[str] = list()
        # pip options, e.g.: pip {pip_options} uninstall testpypi
        self.pip_options: List[str] = list(pip_options)

    def __subprocess_wrapper(self, command: str,
                             wait: bool = True) -> Tuple[str, str, int]:
        """Subprocess wrapper allowing to execute pip commands.

        command -- The pip command to execute (e.g. "install", "freeze", [..])
        wait -- True || False wait for the process to terminate
        """
        try:
            # leverage subprocess.Popen to execute pip commands
            pip_full_cmd: Union[Any] = sorted(
                self.pip_options + self.packages + self.command_args)

            process = Popen(
                [sys.executable if self.python_path is None else self.python_path,
                 "-m", "pip", command] + pip_full_cmd, stdout=PIPE, stderr=PIPE)

            # wait for the process to terminate
            if wait:
                process.wait()

            stdout, stderr = process.communicate()

            output = f'{stdout.decode("utf-8")}'
            sys.stdout.write(output)

            outerr = f'{stderr.decode("utf-8")}'
            sys.stderr.write(outerr)

            return output, outerr, process.returncode

        except CalledProcessError as called_process_error:
            print(called_process_error)
            process.kill()
            exception_output: str = f'Error output:\n{called_process_error.output}'
            exception_cmd: str = f'cmd:\n{called_process_error.cmd}'
            return exception_output, exception_cmd, called_process_error.returncode

    def freeze(self) -> Tuple[str, str, int]:
        """Return installed pip packages in requirements format."""
        return self.__subprocess_wrapper("freeze", wait=True)

    def list_packages(self,
                      list_outdated: bool = False) -> Tuple[str, str, int]:
        """List installed pip packages.

        list_outdated -- True || False to list or not the outdated packages
        """
        if list_outdated:
            self.command_args.insert(0, "--outdated")

        return self.__subprocess_wrapper("list")

    def show(self, package: str) -> Tuple[str, str, int]:
        """Show information about installed packages.

        package -- Package to show
        """
        self.packages.append(package)
        return self.__subprocess_wrapper("show")

    def check(self) -> Tuple[str, str, int]:
        """Verify installed packages have compatible dependencies."""
        return self.__subprocess_wrapper("check", wait=True)

    def install(self, *packages: List[str]) -> Tuple[str, str, int]:
        """Install pip packages.

        *packages -- List of packages to install
        """
        self.packages.clear()

        for package in packages:
            self.packages.append(str(package))

        return self.__subprocess_wrapper("install")

    def uninstall(self, *packages: List[str]) -> Tuple[str, str, int]:
        """Uninstall pip packages.

        *packages -- List of packages to uninstall
        """
        self.packages.clear()

        for package in packages:
            self.packages.append(str(package))

        self.pip_options.insert(0, "-y")
        return self.__subprocess_wrapper("uninstall")

    def download(self, *packages: List[str],
                 destination: Optional[Path] = None) -> Tuple[str, str, int]:
        """Download pip packages.

        *packages -- List of packages to download

        destination -- Destination path for the packages download
        """

        self.packages.clear()

        for package in packages:
            self.packages.append(str(package))

        if destination is not None:
            destination = Path(str(destination).strip())
            self.command_args.append("-d{}".format(destination))

        return self.__subprocess_wrapper("download")
