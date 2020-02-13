import os

from setuptools import setup
setup(
    name="EL Status",
    version="1.0",
    author="Kevin Czupryński",
    author_email="kewin.czuprynski@elpassion.pl",
    description="Hackathon 2020 Winter",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url="http://www.elpassion.pl/",
    packages=['api', 'model', 'serializer'],
    license="MIT",
)

