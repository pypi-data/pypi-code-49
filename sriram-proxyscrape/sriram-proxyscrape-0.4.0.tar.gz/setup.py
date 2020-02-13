from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.rst')) as f:
    long_description = f.read()

with open(path.join(here, 'proxyscrape/VERSION'), 'rb') as f:
    version = f.read().decode('ascii').strip()

setup(
    name='sriram-proxyscrape',
    version=version,
    description='A library for retrieving free proxies (HTTP, HTTPS, SOCKS4, SOCKS5).',
    long_description=long_description,
    url='https://github.com/sriramkumar1996/proxyscrape',
    author='Sriram Kumar Boinpalli',
    author_email='srirambsk1996@gmail.com',
    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: Implementation :: CPython',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities'
    ],
    keywords='proxyscrape proxy scrape scraper',
    # packages=['proxyscrape'],
    packages=find_packages(exclude=['tests']),
    include_package_data=True,
    test_suite='tests',
    install_requires=[
        'BeautifulSoup4',
        'requests',
    ]
)
