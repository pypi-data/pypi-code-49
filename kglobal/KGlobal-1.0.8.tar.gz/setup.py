from setuptools import setup
from setuptools.command.install import install as _install

import atexit
import sys
import os


def _post_install(dir):
    from subprocess import call
    call([sys.executable, 'create_master_salt.py'], cwd=os.path.join(dir, 'KGlobal'))


class MyInstall(_install):
    def run(self):
        _install.run(self)
        self.execute(_post_install, (self.install_lib,), msg='Installing Master Salt Key')


setup(
    name='KGlobal',
    version='1.0.8',
    author='Kevin Russell',
    packages=['KGlobal', 'KGlobal.data', 'KGlobal.sql'],
    url='https://github.com/KLRussell/Python_KGlobal_Package',
    description='SQL Handling, Object Shelving, Data Encryption, XML Parsing/Writing, E-mail Parsing, Logging',
    install_requires=[
        'pandas',
        'future',
        'sqlalchemy',
        'pyodbc',
        'portalocker',
        'cryptography',
        'independentsoft.msg',
        'exchangelib',
        'bs4',
        'six',
    ],
    zip_safe=False,
    cmdclass={
        "install": MyInstall
    },
)
