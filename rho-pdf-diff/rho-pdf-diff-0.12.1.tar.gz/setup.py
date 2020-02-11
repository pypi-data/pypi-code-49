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

with open('rho_pdf_diff/__init__.py', 'rb') as f:
    __version__ = str(ast.literal_eval(_version_re.search(
        f.read().decode('utf-8')).group(1)))

setup(
    name='rho-pdf-diff',
    version=__version__,
    description="Rho AI Fork of pdf-diff",
    # long_description=open('README.md', 'r').read(),
    maintainer="Rho AI Corporation",
    license="Commercial",
    url="https://bitbucket.org/rhoai/rho-pdf-diff",
    packages=find_packages(exclude=["tests"]),
    include_package_data=True,
    install_requires=[
        'diff_match_patch_python',
        'cytoolz>=0.9.0.1<1',
        'pdfrw>=0.4<1',
        'lxml>=4.3.0<5.0.0',
        'pillow>=6.0.0<7.0.0',
        'Click>=7.0<8.0.0',
        'attrs',
        'beautifulsoup4>=4.7<5',
        'reportlab>=3.0.0',
        'numpy>=1.0.0<2.0.0'
    ],
    extras_require={
        'dev': [
            'honcho'
        ],
        'test': [
            'pytest==3.2.1',
            'tox>=2,<3',
            'coverage==4.0a5',
            'mock>=2,<3'
        ]
    },
    cmdclass={'test': PyTest},
    entry_points={
        'console_scripts': [
            'pdf-diff=rho_pdf_diff.command_line:main',
            'rho-pdf-diff=rho_pdf_diff.cli.rho_pdf_diff:rho_pdf_diff'
        ],
    },
    zip_safe=False
)
