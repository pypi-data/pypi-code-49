"""
tweettr
=======

Very thin wrapper around (a few) twitter objects

Author: Andreas Poehlmann
Email: andreas@poehlmann.io
"""
from setuptools import setup, find_packages


setup(
    name='tweettr',
    author='Andreas Poehlmann',
    author_email='andreas@poehlmann.io',
    url='https://github.com/ap--/tweettr',
    license='MIT',
    use_scm_version={
        'write_to': 'src/tweettr/_version.py',
        'write_to_template': '__version__ = "{version}"',
        'tag_regex': r'^(?P<prefix>v)?(?P<version>[^\+]+)(?P<suffix>.*)?$',
    },
    setup_requires=[
        'setuptools_scm',
        'pytest-runner'
    ],
    python_requires='>=3.8',
    tests_require=[
        'pytest',
    ],
    packages=find_packages(where='src'),
    package_dir={
        '': 'src'
    },
    description='tweettr is a `attrdict` like wrapper around (a few) Twitter JSON objects.',
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    classifiers=[
        'Programming Language :: Python :: 3.8',
    ]
)
