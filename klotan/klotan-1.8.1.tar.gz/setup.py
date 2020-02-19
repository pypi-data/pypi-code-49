from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

with open(path.join(here, "klotan", "VERSION"), encoding="utf-8") as f:
    version = f.read()

setup(
    name='klotan',
    version=version,
    description='Structural matching lib for Python',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://sgithub.fr.world.socgen/ktollec111518/klotan',
    author='SG',
    author_email='',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    keywords='matching json',
    packages=find_packages(),
    install_requires=[
    ],
    extras_require={
        'tests': [
            'pytest',
            'flake8'
        ],
    },
    entry_points={
        'console_scripts': [
        ],
    },
    project_urls={
        'Bug Reports': 'https://sgithub.fr.world.socgen/ktollec111518/klotan/issues',
        'Source': 'https://sgithub.fr.world.socgen/ktollec111518/klotan',
    },
)
