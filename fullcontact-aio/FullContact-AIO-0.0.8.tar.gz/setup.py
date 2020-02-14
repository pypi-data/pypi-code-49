"""
FullContact.py
--------------

Simple Python interface for FullContact, using Requests.

"""
from setuptools import setup


setup(
    name='FullContact-AIO',
    version='0.0.8',
    url='https://github.com/nitanmarcel/fullcontact-aio',
    license='MIT',
    author='Marcel Alexandru Nitan',
    author_email='nitan.marcel@gmail.com',
    description='Simple Python interface for FullContact, using aiohttp',
    long_description='Simple Python interface for FullContact, using aiohttp',
    packages=['fullcontact_aio'],
    zip_safe=False,
    platforms='any',
    install_requires=[
        'aiohttp',
    ],
    include_package_data=True,
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
