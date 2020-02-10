"""A setuptools based setup module.

See:
https://packaging.python.org/guides/distributing-packages-using-setuptools/
https://github.com/pypa/sampleproject
"""

# Always prefer setuptools over distutils
from setuptools import setup, find_packages
from os import path
from io import open

here = path.abspath(path.dirname(__file__))

# Arguments marked as "Required" below must be included for upload to PyPI.
# Fields marked as "Optional" may be commented out.

setup(
    # This is the name of your project. The first time you publish this
    # users can install this project, e.g.:
    # $ pip install sampleproject
    # And where it will live on PyPI: https://pypi.org/project/sampleproject/
    name='kot1',  # Required
    version='2.1.0',  # Required
    description='A sample Python project',  # Optional
    long_description="long description",  # Optional
    long_description_content_type='text/markdown',  # Optional 
    # This should be a valid link to your project's main homepage.
    url='https://github.com/adisoadi/kot1',  # Optional
    author='The Python Packaging Authority',  # Optional
    author_email='pypa-dev@googlegroups.com',  # Optional
    # Classifiers help users find your project by categorizing it.
    classifiers=[  # Optional
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',

        # Pick your license as you wish
        'License :: OSI Approved :: MIT License',

        # Specify the Python versions you support here. In particular, ensure
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],

    # What does your project relate to?
    keywords='sample setuptools development',  # Optional

    # Specify which Python versions you support. In contrast to the
    python_requires='>=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, !=3.4.*, <4',

    # This field lists other packages that your project depends on to run.
    # Any package you put here will be installed by pip 
    install_requires=['peppercorn'],  # Optional

    # List additional groups of dependencies here (e.g. development
    # dependencies
    extras_require={  # Optional
        'dev': ['check-manifest'],
        'test': ['coverage'],
    },

    # If there are data files included in your packages that need to be
    # installed, specify them here.
    package_data={  # Optional
        'sample': ['package_data.dat'],
    },
)
