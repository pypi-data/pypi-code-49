"""A setuptools based setup module.

See:
https://packaging.python.org/en/latest/distributing.html
https://github.com/pypa/sampleproject
"""

# Always prefer setuptools over distutils
from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='eidanagios',

    # Versions should comply with PEP440.  For a discussion on single-sourcing
    # the version across setup.py and the project code, see
    # https://packaging.python.org/en/latest/single_source_version.html
    version='0.1a6',

    description='eidanagios: Nagios plugins and test code for EIDA services',
    long_description=long_description,
    long_description_content_type="text/markdown",

    # The project's main homepage.
    url='https://gitext.gfz-potsdam.de/javier/eidanagios',

    # Author details
    author='Javier Quinteros',
    author_email='javier@gfz-potsdam.de',

    # Choose your license
    license='GPLv3',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: System Administrators',

        # Indicate who your project is intended for
        # 'Intended Audience :: Seismologists',

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Natural Language :: English',
        'Operating System :: POSIX :: Linux',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: System :: Monitoring'
    ],

    # What does your project relate to?
    keywords='EIDA services Nagios',

    # You can just specify the packages manually here if your project is
    # simple. Or you can use find_packages().
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),

    # Run tests
    test_suite = 'tests',

    # Alternatively, if you want to distribute just a my_module.py, uncomment
    # this:
    # py_modules=["whatever"],
    provides=["eidanagios"],

    # List run-time dependencies here.  These will be installed by pip when
    # your project is installed. For an analysis of "install_requires" vs pip's
    # requirements files see:
    # https://packaging.python.org/en/latest/requirements.html
    install_requires=['requests'],

    python_requires='>=3',
    # List additional groups of dependencies here (e.g. development
    # dependencies). You can install these using the following syntax,
    # for example:
    # $ pip install -e .[dev,test]
    # extras_require={
    #     'dev': ['check-manifest'],
    #     'test': ['coverage'],
    # },

    # If there are data files included in your packages that need to be
    # installed, specify them here.  If using Python 2.6 or less, then these
    # have to be included in MANIFEST.in as well.
    # package_data={},
    # include_package_data=True,
    # Although 'package_data' is the preferred approach, in some case you may
    # need to place data files outside of your packages. See:
    # http://docs.python.org/3.4/distutils/setupscript.html#installing-additional-files # noqa
    # In this case, 'data_file' will be installed into '<sys.prefix>/my_data'
    # data_files=[(path.join('/', path.expanduser('~'), '.owndc'), ['owndc.cfg']),
    #             (path.join('/', path.expanduser('~'), '.owndc', 'data'), ['data/owndc-routes.xml']),
    #             (path.join('/', path.expanduser('~'), '.owndc', 'data'), ['data/masterTable.xml'])
    #             ],

    # To provide executable scripts, use entry points in preference to the
    # "scripts" keyword. Entry points provide cross-platform support and allow
    # pip to create the appropriate form of executable for the target platform.
    entry_points='''
        [console_scripts]
        check_EIDA_auth=eidanagios.check_EIDA_auth:main
        check_EIDA_alparray=eidanagios.check_EIDA_alparray:main
    '''
)
