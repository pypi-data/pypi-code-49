from setuptools import setup, find_packages

setup(
    name='xaws',
    url='https://bitbucket.org/csusb/python-xaws',
    maintainer='ISET, California State University San Bernardino',
    maintainer_email='iset-ops@csusb.edu',
    version=open('VERSION').read().strip(),
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'xaws-encrypt=xaws.command:encrypt',
            'xaws-decrypt=xaws.command:decrypt',
        ]
    },
    install_requires = [
        'boto3~=1.12',
        'M2Crypto~=0.35',
        'pyasn1~=0.4',
    ]
)
