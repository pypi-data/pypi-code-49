from setuptools import setup

setup(
   name='hello_python_cli',
   version='0.0.5',
   description='Simple python hello cli program',
   author='Mike Kinney',
   author_email='mike.kinney@gmail.com',
   packages=['hello_module'],
   install_requires=[],
   scripts=['hello'],
)
