import io
import os
import sys

import pysam
from Cython.Build import cythonize
from Cython.Distutils import build_ext
from setuptools import setup, Extension

ROOT = os.path.dirname(__file__)
BRI = os.path.join(ROOT, 'src/bri/src')

CFLAGS = ['-O3', '-std=c99']


def get_version():
    # Borrowed this method from pysam
    sys.path.insert(0, "camembert")
    import version
    return version.__version__


with io.open(os.path.join(ROOT, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='camembert-bri',
    packages=['camembert'],
    version=get_version(),
    description='Python interface to BRI (Bam Read Index)',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Matej Usaj',
    author_email='m.usaj@utoronto.ca',
    url='https://github.com/usajusaj/camembertpy',
    download_url='https://github.com/usajusaj/camembertpy/archive/master.zip',

    classifiers=[
        'Development Status :: 5 - Production/Stable',

        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering :: Bio-Informatics',

        'License :: OSI Approved :: MIT License',

        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],

    keywords='bri samtools htslib read index',
    setup_requires=[
        'cython',
        'pysam'
    ],
    install_requires=[
        'pysam'
    ],

    entry_points={
        'console_scripts': [
            'camembert=camembert.cli:main',
        ],
    },

    cmdclass={"build_ext": build_ext},
    ext_modules=cythonize([
        Extension(
            name="camembert.bri",
            sources=[
                "src/bri.pyx",
                os.path.join(BRI, 'bri_index.c'),
                os.path.join(BRI, 'bri_get.c'),
                os.path.join(BRI, 'bri_benchmark.c')
            ],
            include_dirs=pysam.get_include() + [
                BRI,
                os.path.join(sys.prefix, 'include')
            ],
            extra_link_args=pysam.get_libraries() + CFLAGS,
            define_macros=pysam.get_defines(),
            extra_compile_args=CFLAGS
        )
    ])
)
