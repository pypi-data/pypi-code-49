#!/usr/bin/env python

"""
setup.py file readim

run python setup.py [operation]

operations
----------
swig    : Rerun swig. Not required unless changes to code.
build | install | bdist_wheel | sdist etc: typical build commands.
test: run the test suite.
sdist for distribution.

note to deploy:
update version info in setup.py

python setup.py bdist_wheel sdist

to upload to pypi (needs credentials) :
twine upload dist/*

"""

version = '0.8.4'

from setuptools import setup, Extension

import subprocess, sys, os
import glob
import io


script_args = sys.argv[1:]

if script_args[0] == 'test':
    from numpy.testing import run_module_suite
# Remove the current directory so that ReadIM will load properly
    pth = sys.path.pop(0)
    testFileDir = os.path.abspath(os.path.join(os.path.dirname(__file__), 'ReadIM/tests'))
    assert os.path.isdir(testFileDir)
    sys.path.insert(0, testFileDir)

    import test_ReadIM
    run_module_suite('test_ReadIM', ['-f'])

elif script_args[0] == 'swig':
    try:
        args = ['swig', '-python','-c++' ,'-IReadIM/src','ReadIM/core.i']
        p= subprocess.check_call(args)
    except:
        print ('unable to run swig! is it installed?')

else:


    scs = ['ReadIMX.cpp', 'ReadIM7.cpp', 'swigExtras.cpp',
            'zlib/adler32.c','zlib/deflate.c','zlib/infcodes.c',
            'zlib/inflate.c','zlib/infutil.c', 'zlib/uncompr.c',
             'zlib/compress.c','zlib/infblock.c','zlib/inffast.c',
            'zlib/inftrees.c','zlib/trees.c','zlib/zutil.c']

    scs = ['ReadIM/src/'+s for s in scs]
    scs = ['ReadIM/core_wrap.cxx'] + scs
    for s in scs:
        assert os.path.isfile(s)

    extra_compile_args  =['-IReadIM/src']

    here = os.path.abspath(os.path.dirname(__file__))


    ReadIMX_module = Extension('ReadIM._core',
    # Auto SWIG doesn't work because the files are outputs 'core.py' to the current directory not ReadIM
    ##                            ['core.i'], swig_opts=['-c++', '-IReadIM/src'],
    # Manual SWIG
                                sources=scs,
                                extra_compile_args = extra_compile_args,
                                )

    description      = 'Read and write native DaVis images and vectors filetypes VC7 and IM7'
    # Get the long description from the relevant file
    try:
        with io.open(os.path.join(here, 'README.md')) as f:
            long_description = f.read()
    except:
        long_description = description

    setup (name = 'ReadIM',
            description = description,
           version      = version,
           url          = 'https://bitbucket.org/fleming79/readim',
           ext_modules  = [ReadIMX_module],
           packages     = ['ReadIM'],
           package_data = {'ReadIM':['./ReadIM/sample_files/*.*']},
           include_package_data = True,
           script_args          = script_args,
           long_description_content_type = 'text/markdown',
        long_description=long_description,
    license='MIT',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 4 - Beta',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: MIT License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.

        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8'
    ],
    keywords = 'IM7 VC7 DaVis LaVision FileIO PIV',
           )



