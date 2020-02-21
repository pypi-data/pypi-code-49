#!/usr/local/bin/python3

import os
from setuptools import setup, find_packages

VERSION='0.0.1-b3'
PYTHON_REQUIRES='3.7'

packagedata=dict()

packagedata['include_package_data']=True
packagedata['name']="snowshu"
packagedata['version']=VERSION
packagedata['author']="Health Union Data Team"
packagedata['author_email']='data@health-union.com'
packagedata['url']='https://snowshu.readthedocs.io/en/master/index.html'
packagedata['description']="Sample image management for data transform TDD."
packagedata['classifiers']=["Development Status :: 4 - Beta", "License :: OSI Approved :: Apache Software License", "Operating System :: OS Independent"]
packagedata['python_requires']=f'>={PYTHON_REQUIRES}'
packagedata['install_requires']=list()
packagedata['packages']=find_packages(exclude=['tests',])
packagedata['entry_points']=dict(console_scripts=['snowshu= snowshu.core.main:cli'])

with open('./README.md','r') as readme:
    packagedata['long_description']=readme.read()
    packagedata['long_description_content_type']='text/markdown'

packagedata['install_requires']=[
'pyyaml==5.3',
'pandas==1.0.1',
'docker==4.2.0',
'click==7.0',
'coloredlogs==14.0',
'networkx==2.4',
'tabulate==0.8.6',
'psycopg2-binary==2.8.4',
'scipy==1.4.1',
'snowflake-sqlalchemy==1.2.1',
'sqlalchemy==1.3.13 ',
'snowflake-connector-python==2.2.1 ',
'azure-common==1.1.24',
'azure-storage-blob==2.1.0',
'boto3==1.11.17',
'botocore==1.14.17',
'docutils==0.15.2 # back-pin for botocore ',
'requests==2.22.0',
'urllib3==1.25.8',
'certifi==2019.11.28',
'pytz==2019.3',
'pycryptodomex==3.9.6',
'pyOpenSSL==19.1.0',
'cffi==1.13.2',
'cryptography==2.8',
'ijson==2.6.1',
'pyjwt==1.7.1',
'idna==2.8',
'oscrypto==1.2.0',
'asn1crypto==1.3.0'
]

setup(**packagedata)
