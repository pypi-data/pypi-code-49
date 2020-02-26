#!/usr/bin/env python
# -*- encoding: utf-8 -*-
from __future__ import absolute_import, print_function

import io
from os.path import dirname, join

from setuptools import Command, find_packages, setup


def read(*names, **kwargs):
    with io.open(
        join(dirname(__file__), *names),
        encoding=kwargs.get("encoding", "utf8"),
    ) as fh:
        return fh.read()


class Upload(Command):
    user_options = [("package=", "p", "File to upload to PyPI")]

    def initialize_options(self):
        self.package = None

    def finalize_options(self):
        pass

    def run(self):
        from twine import settings
        from twine.commands import upload

        upload_settings = settings.Settings()
        upload.upload(
            upload_settings, dists=[self.package],
        )


setup(
    name="httpapi",
    use_scm_version={
        "local_scheme": "dirty-tag",
        "write_to": "httpapi/_version.py",
        "fallback_version": "0.0.0",
    },
    cmdclass={"upload": Upload,},
    description="Pythonic helpers for HTTP APIs with long URLs.",
    author="Ross Fenning",
    author_email="github@rossfenning.co.uk",
    url="https://github.com/avengerpenguin/httpapi",
    packages=find_packages("httpapi"),
    package_dir={"": "httpapi"},
    classifiers=[
        # complete classifier list: http://pypi.python.org/pypi?%3Aaction=list_classifiers
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Operating System :: Unix",
        "Operating System :: POSIX",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: Implementation :: CPython",
        "Topic :: Internet :: WWW/HTTP",
    ],
    project_urls={
        "Issue Tracker": "https://github.com/avengerpenguin/httpapi/issues",
    },
    keywords=[
        # eg: 'keyword1', 'keyword2', 'keyword3',
    ],
    requires=["requests"],
    setup_requires=["pytest-runner", "setuptools_scm>=3.3.1", "twine"],
)
