import os
import sys

from setuptools import find_packages, setup

# This should always be before importing django_audit_events
# We need working directory in sys.path for setuptools.build_meta
# else we get ImportError
sys.path.insert(0, os.path.dirname(__file__))

from django_audit_events import (  # isort:skip
    __author__,
    __doc__,
    __email__,
    __license__,
    __maintainer__,
)

if sys.version_info[0] == 2:
    from io import open


def get_long_description():
    with open("README.md", "r", encoding="utf-8") as fh:
        return fh.read()


setup(
    name="django-audit-events",
    use_scm_version={
        "write_to": "django_audit_events/version.py",
        "write_to_template": '__version__ = "{version}"\n',
    },
    description=__doc__,
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    author=__author__,
    author_email=__email__,
    maintainer=__maintainer__,
    maintainer_email=__email__,
    license=__license__,
    url="https://bitbucket.org/akinonteam/django-audit-events",
    packages=find_packages(exclude=["tests", "tests.*"]),
    platforms="any",
    zip_safe=False,
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Framework :: Django",
        "Framework :: Django :: 1.10",
        "Framework :: Django :: 1.11",
        "Framework :: Django :: 2.0",
        "Framework :: Django :: 2.1",
        "Framework :: Django :: 2.2",
        "Framework :: Django :: 3.0",
    ],
)
