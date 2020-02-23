from os import path

import setuptools

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_descr = f.read()

setuptools.setup(
    name='atl_cache_warmer',
    version='0.1',
    packages=['atl_cache_warmer'],
    entry_points={
        'console_scripts': [
            'atlwarmer = atl_cache_warmer.cache_builder:main'
        ]
    },
    url='',
    long_description=long_descr,
    long_description_content_type='text/markdown',
    license='MIT',
    author='np-at',
    author_email='',
    description='Little script to warm up confluence and jira caches to make it more responsive',
    install_requires=['requests'],
    python_requires='>=3.6'
)
