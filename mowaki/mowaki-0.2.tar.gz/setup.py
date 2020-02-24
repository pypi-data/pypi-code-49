import os
from setuptools import setup, find_packages

version = '0.2'

here = os.path.dirname(__file__)

with open(os.path.join(here, 'README.rst')) as fp:
    longdesc = fp.read()

with open(os.path.join(here, 'CHANGELOG.rst')) as fp:
    longdesc += "\n\n" + fp.read()


setup(
    name='mowaki',
    version=version,
    packages=find_packages(),
    url='https://github.com/rshk/mowaki-py',

    license='BSD License',

    author='Samuele Santi',
    author_email='samuele.santi@reinventsoftware.io',
    description='MoWAKi - Python utilities',
    long_description=longdesc,

    install_requires=[],
    extras_require={
        'aws': ['boto3'],
        'auth': ['pyjwt'],
    },
    # tests_require=tests_require,
    # test_suite='tests',

    classifiers=[
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 3',
        # 'Programming Language :: Python :: 3.0',
        # 'Programming Language :: Python :: 3.1',
        # 'Programming Language :: Python :: 3.2',
        # 'Programming Language :: Python :: 3.3',
        # 'Programming Language :: Python :: 3.4',
        # 'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3 :: Only',

        # 'Programming Language :: Python :: Implementation :: CPython',
        # 'Programming Language :: Python :: Implementation :: IronPython',
        # 'Programming Language :: Python :: Implementation :: Jython',
        # 'Programming Language :: Python :: Implementation :: PyPy',
        # 'Programming Language :: Python :: Implementation :: Stackless',
    ],
    # entry_points={
    #     'console_scripts': ['mowaki=mowaki.cli:main'],
    # },
    package_data={'': ['README.rst', 'CHANGELOG.rst']},
    include_package_data=True,
    zip_safe=False)
