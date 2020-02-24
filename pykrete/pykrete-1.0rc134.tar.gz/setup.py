"""
Pykrete module build script
Author: Shai Bennathan - shai.bennathan@gmail.com
(C) 2020
"""
from setuptools import setup, find_packages
from src.pykrete.packages import PythonPackage
from src.pykrete.distrib import TwineCommand
from src.pykrete.distrib.pylint import SelfTestCommand, ProjectTestCommand


PACKAGE = PythonPackage('pykrete')
print(f'Handling pip package: {PACKAGE}')
setup(
    name='pykrete',
    version=PACKAGE.version,
    license='MIT',
    author='Shai A. Bennathan',
    author_email='shai.bennathan@intel.com',
    description='Build script foundation',
    long_description=PACKAGE.get_long_description(),
    long_description_content_type='text/markdown',
    url='http://ait-tool-center.iil.intel.com/',
    packages=find_packages(),
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3.6',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    test_suite='nose.collector',
    tests_require=['nose'],
    cmdclass={
        'pylint_self': SelfTestCommand,
        'pylint': ProjectTestCommand,
        'twine': TwineCommand
    }
    # install_requires=[],
)
