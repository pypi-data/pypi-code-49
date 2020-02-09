#!/usr/bin/env python
# setup.py generated by flit for tools that don't yet use PEP 517

from distutils.core import setup

packages = \
['layouts']

package_data = \
{'': ['*'],
 'layouts': ['.pytest_cache/*', '.pytest_cache/v/*', '.pytest_cache/v/cache/*']}

install_requires = \
['requests', 'PyGithub', 'GitPython']

setup(name='layouts',
      version='0.4.10',
      description='Python API for HID-IO HID Layouts Repository',
      author='Jacob Alexander',
      author_email='haata@kiibohd.com',
      url='https://github.com/hid-io/layouts-python',
      packages=packages,
      package_data=package_data,
      install_requires=install_requires,
      python_requires='>=3.5',
     )
