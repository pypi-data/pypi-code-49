import re
import ast
import sys

from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand


class PyTest(TestCommand):
    user_options = [
        ('pytest-args=', 'a', "Arguments to pass to py.test")]

    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.pytest_args = []

    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        import coverage
        import pytest

        if self.pytest_args and len(self.pytest_args) > 0:
            self.test_args.extend(self.pytest_args.strip().split(' '))
            self.test_args.append('tests/')

        cov = coverage.Coverage()
        cov.start()
        errno = pytest.main(self.test_args)
        cov.stop()
        cov.report()
        cov.html_report()
        print("Wrote coverage report to htmlcov directory")
        sys.exit(errno)


_version_re = re.compile(r'__version__\s+=\s+(.*)')

with open('sermos_utils/__init__.py', 'rb') as f:
    __version__ = str(ast.literal_eval(_version_re.search(
        f.read().decode('utf-8')).group(1)))

with open('requirements.txt', 'r') as f:
    install_requires = f.read().splitlines()


setup(
    name='sermos-utils',
    version=__version__,
    description="Sermos Utilities",
    long_description=open('README.md', 'r').read(),
    long_description_content_type='text/markdown',
    maintainer="Rho AI",
    license="MIT",
    url="https://bitbucket.org/rhoai/sermos-utils",
    packages=find_packages(exclude=["tests"]),
    include_package_data=True,
    install_requires=install_requires,
    extras_require={
        'dev': [
            'honcho',
            'twine'
        ],
        'test': [
            'pytest>=5.2.4,<6',
            'tox>=3.14.1,<4',
            'coverage>=4.5,<5',
            'mock>=1,<2',
            'responses>=0.10.7,<11',
            'moto>=1.3'
        ]
    },
    cmdclass={'test': PyTest},
    entry_points="""
    [console_scripts]
    sermos_validate=sermos_utils.cli.deploy:validate
    sermos_deploy=sermos_utils.cli.deploy:deploy
    sermos_status=sermos_utils.cli.deploy:status
    """,
)
