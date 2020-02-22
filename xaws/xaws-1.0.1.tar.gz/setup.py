from setuptools import setup, find_packages

setup(
    name='xaws',
    url='https://bitbucket.org/csusb/python-xaws',
    maintainer='ISET, California State University San Bernardino',
    maintainer_email='iset-ops@csusb.edu',
    version=open('VERSION').read().strip(),
    description="Library for encrypting/decrypting files using AWS KMS",
    long_description=open('README.md', 'r').read(),
    long_description_content_type='text/markdown',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'xaws-encrypt=xaws.command:encrypt',
            'xaws-decrypt=xaws.command:decrypt',
        ]
    },
    python_requires='>=3.6',
    install_requires = [
        'boto3~=1.12',
        'M2Crypto~=0.35',
        'pyasn1~=0.4',
    ]
)
