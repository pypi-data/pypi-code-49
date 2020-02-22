from setuptools import setup
from setuptools.command.install import install

import atexit


def _post_install():
    print("Installing Master Salt Key")
    from KGlobal import create_master_salt_key
    create_master_salt_key()


class new_install(install):
    def __init__(self, *args, **kwargs):
        super(new_install, self).__init__(*args, **kwargs)
        atexit.register(_post_install)


setup(
    name='KGlobal',
    version='1.0.7',
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
        "install": new_install
    },
)
