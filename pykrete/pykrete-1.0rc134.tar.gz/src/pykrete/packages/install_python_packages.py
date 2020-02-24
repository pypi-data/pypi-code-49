"""
Python package installation
Author: Shai Bennathan - shai.bennathan@gmail.com
(C) 2020
"""
import subprocess


def install_python_packages(logger, *args):
    """Installs the specified pip packages

    :param logger: Optional logger for debug print(s)
    :param args: The packages to install
    """
    packages = list(args)
    if logger:
        logger.debug('Installing packages %s', str(packages))
    subprocess.check_call(['python', '-m', 'pip', 'install'] + packages)
