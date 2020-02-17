import sys

from setuptools import setup

# Require pytest-runner only when running tests
pytest_runner = (['pytest-runner>=2.0,<3dev']
                 if any(arg in sys.argv for arg in ('pytest', 'test'))
                 else [])

setup_requires = pytest_runner

setup(
    name="culebrita",
    version="0.0.1",
    description="Minimalistic and Pythonistic web framework ",
    author='Joseph Mendoza',
    license="MIT",
    packages=['culebrita'],
    tests_require=['pytest'],
    setup_requires=setup_requires
)
