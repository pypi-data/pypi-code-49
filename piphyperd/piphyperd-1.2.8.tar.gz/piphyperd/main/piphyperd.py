"""
THIS SOFTWARE IS PROVIDED AS IS
and under GNU General Public License. <https://www.gnu.org/licenses/gpl-3.0.en.html>
USE IT AT YOUR OWN RISK.

PipHyperd is a simple python object to leverage pip programmatically.
piphyperd is a wrapper around **pip**; it can provide features like
automation or dependencies control within your workflows.

The module is published on PyPi <https://pypi.org/project/piphyperd/>.

The code is available on GitLab <https://gitlab.com/hyperd/piphyperd>.
"""

from subprocess import Popen, PIPE, CalledProcessError
import sys
from pathlib import Path


class PipHyperd:
    """
    PipHyperd a wrapper class around pip.

    python_path -- Path to the python binary to use

    *pip_options -- pip command options, e.g.: pip {pip_options} uninstall testpypi
    """

    def __init__(self, *pip_options, python_path=None):
        # Path to the python binary to use
        self.python_path = python_path
        # A list of pip packages to install || show || download || uninstall
        self.packages = list()
        # pip command args, e.g.: pip download testpypi {command_args}
        self.command_args = list()
        # pip options, e.g.: pip {pip_options} uninstall testpypi
        self.pip_options = list(pip_options)

    def __subprocess_wrapper(self, command, wait=True):
        """
        A subprocess wrapper allowing to execute pip commands
        from the public methods of the PipModules object.

        command -- The pip command to execute (e.g. "install", or "freeze", etc.)

        wait -- True || False wait for the process to terminate
        """

        try:
            # leverage subprocess.Popen to execute pip commands
            process = Popen(
                [sys.executable if self.python_path is None else self.python_path,
                 "-m", "pip", command]
                + self.pip_options + self.packages + self.command_args, stdout=PIPE, stderr=PIPE)

            # wait for the process to terminate
            if wait:
                process.wait()

            stdout, stderr = process.communicate()

            output = f'{stdout.decode("utf-8")}'
            sys.stdout.write(output)

            outerr = f'{stderr.decode("utf-8")}'
            sys.stderr.write(output)

            return output, outerr, f'Process exited with {process.returncode}'

        except CalledProcessError as called_process_error:
            print(called_process_error)
            process.kill()
            return called_process_error

    def freeze(self):
        """
        Output installed pip packages in requirements format.
        """
        return self.__subprocess_wrapper("freeze", wait=True)

    def list(self, list_outdated=False):
        """
        List installed pip packages.

        list_outdated -- True || False to list or not the outdated packages
        """

        if list_outdated:
            self.command_args.insert(0, "--outdated")

        return self.__subprocess_wrapper("list")

    def show(self, package):
        """
        Show information about installed packages.

        package -- Package to show
        """
        self.packages.append(package)
        return self.__subprocess_wrapper("show")

    def check(self):
        """
        Verify installed packages have compatible dependencies.
        """
        return self.__subprocess_wrapper("check", wait=True)

    def install(self, *packages):
        """
        Install pip packages.

        *packages -- List of packages to install
        """

        self.packages.clear()

        for package in packages:
            self.packages.append(package)

        return self.__subprocess_wrapper("install")

    def uninstall(self, *packages):
        """
        Uninstall pip packages.

        *packages -- List of packages to uninstall
        """
        self.packages.clear()

        for package in packages:
            self.packages.append(package)

        self.pip_options.insert(0, "-y")
        return self.__subprocess_wrapper("uninstall")

    def download(self, *packages, destination=None):
        """
        Download pip packages.

        *packages -- List of packages to download

        destination -- Destination path for the packages download
        """

        self.packages.clear()

        for package in packages:
            self.packages.append(package)

        if destination is not None:
            destination = str(destination).strip()
            self.command_args.append("-d{}".format(Path(destination)))

        return self.__subprocess_wrapper("download")
