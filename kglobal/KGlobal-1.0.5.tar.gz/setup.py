from setuptools import setup
from setuptools.command.install import install as _install

import sys


def _post_install():
    from KGlobal import create_master_salt_key
    create_master_salt_key()


class MyInstall(_install):
    def run(self):
        if self.old_and_unmanageable or self.single_version_externally_managed:
            return _install.run(self)

        caller = sys._getframe(2)
        caller_module = caller.f_globals.get('__name__', '')
        caller_name = caller.f_code.co_name

        if caller_module != 'distutils.dist' or caller_name != 'run_commands':
            _install.run(self)
        else:
            self.do_egg_install()
            self.execute(_post_install, (), msg='Installing Master Salt Key')


setup(
    name='KGlobal',
    version='1.0.5',
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
