
from setuptools import setup, find_packages

version = '0.1.11'

with open('README.md') as f:
    long_description = f.read()

setup(
    name="athena-cli",
    version=version,
    description='Presto-like CLI for AWS Athena',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/satterly/athena-cli',
    license='Apache License 2.0',
    author='Nick Satterly',
    author_email='nick.satterly@gmail.com',
    packages=find_packages(),
    py_modules=[
        'athena_cli'
    ],
    install_requires=[
        'boto3>=1.4.4',
        'cmd2>=0.9.0.1',
        'tabulate>=0.8.1'
    ],
    include_package_data=True,
    zip_safe=True,
    entry_points={
        'console_scripts': [
            'athena = athena_cli:main'
        ]
    },
    keywords='aws athena presto cli',
    classifiers=[
        'Topic :: Utilities'
    ],
    python_requires='>=3.5'
)
