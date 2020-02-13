import os
from setuptools import setup, find_packages

setup(
    name='jphmm_tools',
    packages=find_packages(),
    include_package_data=True,
    package_data={'jphmm_tools': [os.path.join('data', '*.breakpoints'), os.path.join('..', 'README.md')]},
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Topic :: Scientific/Engineering :: Bio-Informatics',
        'Topic :: Software Development',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    version='0.1',
    description='Tools for extracting information from jpHMM (http://jphmm.gobics.de) output.',
    author='Anna Zhukova',
    author_email='anna.zhukova@pasteur.fr',
    url='https://github.com/evolbioinfo/jphmm_tools',
    keywords=['jpHMM', 'HIV', 'subtyping', 'recombinants'],
    install_requires=['pandas', 'numpy', 'biopython'],
    entry_points={
            'console_scripts': [
                'jphmm_align = jphmm_tools.aligner:main',
                'jphmm_subtype = jphmm_tools.subtyper:main'
                'jphmm_ref = jphmm_tools.la_referencer:main'
            ]
    },
)
