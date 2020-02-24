from setuptools import setup, find_packages
import os


def extras_require():
    with open('requirements-test.txt') as fp:
        return {'test': fp.read()}


def long_description():
    with open('README.rst') as readme:
        return readme.read()


def version():
    version = os.environ.get('TRAVIS_TAG', '')
    if not version:
        version = os.popen('git describe --match "[0-9]*" --tags HEAD').read()
    return version.strip()


setup(
    name='colltools',
    version=version(),
    python_requires='>=3.6',
    description='Tools for iterating and working with collections',
    long_description=long_description(),
    long_description_content_type='text/x-rst',
    url='https://github.com/JakubTesarek/colltools',
    author='Jakub Tesárek',
    author_email='jakub@tesarek.me',
    license='APACHE LICENSE 2.0',
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: Apache Software License',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7'
    ],
    keywords='itertools collections iteration',
    packages=find_packages(),
    extras_require=extras_require()
)
