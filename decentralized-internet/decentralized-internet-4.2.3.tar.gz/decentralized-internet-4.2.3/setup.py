
import setuptools


def long_description():
    with open('README.md', 'r') as file:
        return file.read()


setuptools.setup(
    name='decentralized-internet',
    version='4.2.3',
    author='The Lonero Foundation',
    author_email='andrew@etherstone.org',
    description='A library for creating distributed web and grid projects',
    long_description=long_description(),
    long_description_content_type='text/markdown',
    url='https://github.com/Lonero-Team/Decentralized-Internet',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
    ],
    python_requires='>=3.7.0',
)
