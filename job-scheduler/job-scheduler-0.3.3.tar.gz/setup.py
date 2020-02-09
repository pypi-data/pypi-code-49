#from distutils.core import setup
from setuptools import setup

setup(
    name='job-scheduler',
    packages=['haydn.scheduler'],
    version='0.3.3',
    description='Simple Scheduler for Python 3.X',
    author='Jason Lee',
    url='https://bitbucket.org/haydn_team/scheduler/',
    download_url='https://bitbucket.org/haydn_team/scheduler.git',
    install_requires=[
        'event-emitter',
    ],
)
