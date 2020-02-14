from setuptools import setup


def get_readme_md_contents():
    with open('README.md') as f:
        desc = f.read()
        return desc


def get_version():
    with open('VERSION') as f:
        version = f.read()
        return version


setup(
    name="restd",
    version=get_version(),
    tests_require=["pytest"],
    install_requires=[
        'pyyaml'
    ],
    packages=[
        'restd',
    ],
    author="Chris O'Connor",
    long_description=get_readme_md_contents(),
    long_description_content_type='text/markdown',
    description="Flexible and extensible REST",
    license="Apache License 2.0",
    url="https://github.com/cdoconno/restd",
    test_suite="tests",
    classifiers=[
        "Development Status :: 1 - Planning",
        "Framework :: Flake8",
        "Framework :: tox",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: POSIX :: Linux",
        "Operating System :: Unix",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ]
)
