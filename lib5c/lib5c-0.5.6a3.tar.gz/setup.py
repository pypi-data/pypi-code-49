from setuptools import setup, find_packages

from lib5c._version import version_scheme, local_scheme

with open('README.md') as fobj:
    long_description = fobj.read()

extras_require = {
    'bsub': ['bsub>=0.3.5'],
    'iced': ['iced>=0.4.0'],
    'pyBigWig': ['pyBigWig>=0.3.4'],
    'test': ['nose>=1.3.7', 'nose-exclude>=0.5.0', 'flake8>=3.4.1'],
    'docs': ['Sphinx>=1.7.2', 'sphinx-rtd-theme>=0.3.0',
             'sphinxcontrib-apidoc>=0.3.0'],
    'tutorials': ['ipykernel>=4.10.0,<6.0', 'nbconvert>=5.4.0',
                  'nbformat>=4.4.0', 'nbstripout>=0.3.5']
}
extras_require['complete'] = sorted(set(sum(extras_require.values(), [])))

setup(
    name='lib5c',
    use_scm_version={
        'version_scheme': version_scheme,
        'local_scheme': local_scheme,
    },
    description='5C analysis library',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Thomas Gilgenast',
    url='https://bitbucket.org/creminslab/lib5c',
    packages=find_packages(exclude=["*.tests"]),
    package_data={
        'lib5c.plotters': ['gene_tracks/*/*.bed', 'gene_tracks/*.gz']
    },
    entry_points={
        'console_scripts': [
            'lib5c = lib5c.tools.lib5c_toolbox:lib5c_toolbox'
        ]
    },
    setup_requires=['setuptools_scm'],
    install_requires=[
        'python-daemon>=2.1.1,<2.2.0',
        'numpy>=1.10.4',
        'scipy>=0.16.1',
        'matplotlib>=2.1.0',
        'pandas>=0.18.0',
        'seaborn>=0.8.0',
        'statsmodels>=0.6.1,<=0.10.2;python_version<"3.5"',
        'statsmodels>=0.6.1;python_version>="3.5"',
        'dill>=0.2.5',
        'decorator>=4.0.10',
        'luigi>=2.1.1',
        'scikit-learn>=0.17.1',
        'interlap>=0.2.3',
        'powerlaw>=1.4.3',
        'importlib_metadata>=1.5.0;python_version<"3.8"',
    ],
    extras_require=extras_require,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Science/Research',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Topic :: Scientific/Engineering :: Bio-Informatics'
    ],
)
