from setuptools import setup, find_packages

__name__ = 'tinyrouter'
__version__ = '0.1.4' # TODO: Adopt a standard versioning

__author__ = 'Tarcisio Cantalice'
__author_email__ = 'tarcisiocantalice@gmail.com'

__requirements__ = ['flask']

__url__ = 'https://github.com/tcantalice/tiny-router'

with open('README.md', 'r') as readme:
    __long_description__ = readme.read()

__license__ = 'MIT'

setup(
    name=__name__,
    version=__version__,
    packages=find_packages(),
    install_requires=__requirements__,
    author=__author__,
    author_email=__author_email__,
    long_description=__long_description__,
    license=__license__,
    classifiers=[
        'Framework :: Flask',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
    ],
    url=__url__,
    long_description_content_type='text/markdown'
)