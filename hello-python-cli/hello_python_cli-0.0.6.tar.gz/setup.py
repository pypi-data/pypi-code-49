from setuptools import setup

from io import open

# Extract version info without importing entire package
version_data = {}
with open('version.py') as f:
    exec(f.read(), version_data)

setup(
   name='hello_python_cli',
   version=version_data['__version__'],
   description='Simple python hello cli program',
   author='Mike Kinney',
   author_email='mike.kinney@gmail.com',
   packages=['hello_module'],
   install_requires=[],
   scripts=['hello'],
)
