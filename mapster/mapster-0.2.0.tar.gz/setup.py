import re

from setuptools import find_packages, setup


def get_version(filename):
    with open(filename) as fh:
        metadata = dict(re.findall("__([a-z]+)__ = '([^']+)'", fh.read()))
        return metadata['version']

setup(
    name='mapster',
    version=get_version('mapster/__init__.py'),
    url='https://github.com/jedrus2000/mapster',
    license='MIT',
    author='Andrzej Bargański',
    author_email='a.barganski@gmail.com',
    description='An administration tools for maps repository at http://mapywig.org/',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    packages=find_packages(exclude=['tests', 'tests.*']),
    data_files=[('', ['README.md'])],
    zip_safe=False,
    include_package_data=True,
    python_requires='>=3.6',
    keywords='mapster mapywig cli',
    install_requires=[
        'setuptools',
        'Click >= 7.0',
        'toml >= 0.10.0',
        'requests >= 2.22.0',
        'colorama >= 0.4.3'
    ],
    extras_require={  # Optional
        'dev': ['twine', 'wheel'],
    },
    entry_points={  # Optional
        'console_scripts': [
            'mapster=mapster.__main__:cli',
        ],
    },
    project_urls={
        'Source': 'https://github.com/jedrus2000/mapster',
    },
    classifiers=[
        'Environment :: No Input/Output (Daemon)',
        'Intended Audience :: End Users/Desktop',
        'Topic :: Utilities',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
    ],
)
