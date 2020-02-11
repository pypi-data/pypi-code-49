"""
 
 This module use twine for publishing packages.
 
"""

from invoke import run
from invoke import task


@task
def clean(ctxt):
    """
    Clean build directory.
    """
    run('rm dist/*')


@task
def build(ctxt):
    """
    Build package for publishing to PyPI
    """
    run('python setup.py sdist bdist_wheel')


@task
def publish(ctxt):
    """
    Publish package to PyPI
    """
    run('twine upload dist/*')
    print("Remember to publish sources as well if needed.")
