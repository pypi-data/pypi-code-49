from setuptools import setup, find_packages

setup(
    name='zoetrope',
    version='0.2',
    description='A templating tool that creates unit tests from an arbitrary file.',
    python_requires='~=3.6',
    packages=find_packages(),
    scripts=['zoetrope/zoetrope'],
    install_requires=[
        'mock'
    ]
)
