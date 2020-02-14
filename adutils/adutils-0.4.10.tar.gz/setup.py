# coding=utf-8

from setuptools import setup

setup(
    name="adutils",
    # version='0.4.10',
    license="MIT",
    url="http://github.com/benleb/adutils",
    author="Ben Lebherz",
    author_email="git@benleb.de",
    description="Helper and utilities for AppDaemon apps",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    packages=["adutils"],
    zip_safe=False,
    platforms="any",
    setup_requires=["setuptools_scm"],
    use_scm_version={
        "version_scheme": "python-simplified-semver",
        "local_scheme": lambda v: "",
    },
    classifiers=[
        "Topic :: Software Development",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
