#from distutils.core import setup
from setuptools import setup
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='job-scheduler',
    packages=['haydn.scheduler'],
    version='0.3.4',
    description='Simple Scheduler for Python 3.X',
    author='Jason Lee',
    url='https://bitbucket.org/haydn_team/scheduler/',
    download_url='https://bitbucket.org/haydn_team/scheduler.git',
    install_requires=[
        'event-emitter',
    ],
    long_description=long_description,
    long_description_content_type='text/markdown'
)
