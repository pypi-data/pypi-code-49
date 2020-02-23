from setuptools import setup, find_packages
import subprocess
from subprocess import CalledProcessError


def get_version():
    try:
        out = subprocess.check_output(['git', 'describe',
                                       '--tags', '--abbrev=0'])
        version = out.decode('utf-8').strip()
    except CalledProcessError:
        version = 'no-tag'
    return version


reqs = ['daiquiri',
        'requests',
        'pyyaml',
        'simple_salesforce']

test_reqs = ['ipython',
             'pytest',
             'pytest-sugar',
             'pytest-cov',
             'pylint']

setup(
    name='heartcrm',
    description='A Python utility for generating reports from the HEART CRM.',
    author='Matt Robinson',
    author_email='matt@fiddleranalytics.com',
    packages=find_packages(),
    version=get_version(),
    install_requires=reqs,
    extras_require={'test': test_reqs},
    entry_points={'console_scripts': 'heartcrm=hearcrm.cli:main'}
)
