from setuptools import setup
from setuptools.command.bdist_egg import bdist_egg as _bdist_egg

import sys


class MyInstall(_bdist_egg):
    def run(self):
        self._post_install()
        _bdist_egg.run(self)

    @staticmethod
    def _post_install():
        from KGlobal import create_master_salt_key
        create_master_salt_key()


setup(
    name='KGlobal',
    version='1.0.6',
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
        "bdist_egg": MyInstall
    },
)
