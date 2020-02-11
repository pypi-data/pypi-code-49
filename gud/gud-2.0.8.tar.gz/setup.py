from setuptools import setup
from codecs import open
from os import path
from greengo import __version__

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='gud',
    version=__version__,
    description='AWS Greengrass file-based setup tool based on greengo by d',
    long_description=long_description,
    long_description_content_type='text/markdown',
    keywords=['AWS', 'IoT', 'Greengrass', 'Lambda'],
    url='https://gitlab.com/doopnz/gud',
    author='Dmitri Zimine modified by James Whiteman',
    author_email='james.whiteman@gmail.com',
    license='MIT',
    packages=['greengo'],
    install_requires=[
        'fire',
        'boto3',
        'botocore',
        'pyyaml'
    ],
    setup_requires=['pytest-runner'],
    tests_require=['pytest', 'mock'],
    entry_points={
        'console_scripts': ['gud=greengo.greengo:main'],
    },
    zip_safe=False
)
