# -*-coding:utf-8-*-
import io

from setuptools import setup, find_packages
from setuptools.command.install import install


class InstallWrapper(install):

    def run(self):
        raise Exception("using internal PyPi to install sage-cli, 请使用内网 PyPi 安装。")


with io.open("README.md", "r", encoding="UTF-8") as fh:
    long_description = fh.read()

setup(
    name='sage-cli',
    version='0.0.4',
    description="sage cli",
    long_description=long_description,
    packages=find_packages(),
    install_requires=[
        'requests',
        'future',
        'python-dateutil',
        'wrapt',
        'pandas>=0.22.0',
        'numpy>=1.14.2',
        'enum34',
        'tzlocal',
        'Flask',
    ],
    cmdclass={
        'install': InstallWrapper
    },
    python_requires='>=3.7',
)
