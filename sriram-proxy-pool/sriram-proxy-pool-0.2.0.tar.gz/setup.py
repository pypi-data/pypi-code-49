from setuptools import setup, find_packages
import re
import os


def get_version():
    fn = os.path.join(os.path.dirname(__file__), "scrapy_proxy_pool", "__init__.py")
    with open(fn) as f:
        return re.findall("__version__ = '([\d.\w]+)'", f.read())[0]


def get_long_description():
    readme = open('README.rst').read()
    # return readme

setup(
    name='sriram-proxy-pool',
    version=get_version(),
    author='Sriram Kumar',
    author_email='srirambsk1996@gmail.com',
    license='MIT',
    long_description=get_long_description(),
    description="SDT scrapy proxy pool",
    url='https://github.com/sriramkumar1996/scrapy-proxy-pool',
    packages=find_packages(exclude=['tests']),
    install_requires=[
        'scrapy',
        'sriram-proxyscrape'
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Framework :: Scrapy',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)
