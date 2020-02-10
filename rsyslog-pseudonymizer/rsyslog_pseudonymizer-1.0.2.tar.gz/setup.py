from io import open

from setuptools import find_packages, setup

with open('rsyslog_pseudonymizer/__init__.py', 'r') as f:
    for line in f:
        if line.startswith('__version__'):
            version = line.strip().split('=')[1].strip(' \'"')
            break
    else:
        version = '0.0.1'

with open('README.md', 'r', encoding='utf-8') as f:
   readme = f.read()

REQUIRES = [
    'tld >=0.9.2, <1'
]

# same as in tox.ini
TEST_REQUIRES = [
    'coverage',
    'pytest'
]

DEV_REQUIRES = [
    'hatch',
    'tox',
] + TEST_REQUIRES

setup(
    name='rsyslog_pseudonymizer',
    version=version,
    description=readme.split("\n\n")[1].replace("\n", " "),
    long_description=readme,
    long_description_content_type="text/markdown",
    author='iflog',
    author_email='qiensamw@runbox.com',
    maintainer='iflog',
    maintainer_email='qiensamw@runbox.com',
    url='https://framagit.org/iflog/rsyslog_pseudonymizer',
    license='Apache-2.0',

    keywords=[],

    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        'Operating System :: POSIX',
        'Programming Language :: Python :: 3.6',
    ],

    install_requires=REQUIRES,
    extras_require={
        'test': TEST_REQUIRES,
        'dev': DEV_REQUIRES,
    },

    packages=find_packages(
        include=["rsyslog_pseudonymizer", "rsyslog_pseudonymizer.*"],
    ),
    entry_points={
        "console_scripts": [
            "rsyslog_pseudonymizer = " \
                "rsyslog_pseudonymizer.rsyslog_pseudonymizer:main"
        ]
    },
)
