from setuptools import setup, find_packages
import io
import scrapy_nc

def read_file(filename):
    with io.open(filename) as fp:
        return fp.read().strip()

def read_requirements(filename):
    return [line.strip() for line in read_file(filename).splitlines()
            if not line.startswith('#')]

setup(
    name='scrapy_nc',
    version='0.0.7',
    url='https://github.com/fantasy/scrapy_nc',
    description='Scrapy plugins in NoCode',
    author='fantasy614@nocode.com',
    packages=['scrapy_nc'],
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        'Framework :: Scrapy',
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Utilities',
        'Framework :: Scrapy',
    ],
    install_requires=['scrapy'],
    requires=['scrapy (>=0.24.5)'],
)
