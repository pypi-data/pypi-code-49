from setuptools import setup

setup(
    name='KGlobal',
    version='1.0.9',
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
)
