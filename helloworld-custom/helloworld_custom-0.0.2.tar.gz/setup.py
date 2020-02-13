from setuptools import setup

setup(
    name='helloworld_custom',
    version='0.0.2',
    description='hello world project',
    py_modules=["hello_world"],
    package_dir={'': 'src'},
    author='starting_out',
    author_email='starting_out@xyz.com'
)
