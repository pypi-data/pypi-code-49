import re
from os import path

from setuptools import setup

github_user = "avryhof"
github_repo_name = "django-suit-redactor"
module_path = "suit_redactor"
author = "Amos Vryhof"
author_email = "amos@vryhofresearch.com"
description = "Imperavi Redactor (WYSIWYG editor) integration app for Django admin. http://imperavi.com/redactor/"


def read(*parts):
    return open(path.join(path.dirname(__file__), *parts)).read()


def find_version(*file_paths):
    version_file = read(*file_paths)
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]", version_file, re.M,)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")


def find_name(*file_paths):
    name_file = read(*file_paths)
    name_match = re.search(r"^__name__ = ['\"]([^'\"]*)['\"]", name_file, re.M,)
    if name_match:
        return name_match.group(1)
    return module_path


setup(
    name="django-suit-redactor-django2",
    version=find_version(module_path, '__init__.py'),
    url='https://github.com/%s/%s' % (github_user, github_repo_name),
    description="Imperavi Redactor (WYSIWYG editor) integration app for Django admin. http://imperavi.com/redactor/",
    long_description=read("README.rst"),
    author="Kaspars Sprogis (darklow) enhanced by Amos Vryhof (avryhof)",
    author_email="info@djangosuit.com",
    packages=["suit_redactor"],
    zip_safe=False,
    include_package_data=True,
    install_requires=["django>2.1,<3.0", "django-suit"],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Framework :: Django",
        "License :: Free for non-commercial use",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "Programming Language :: Python",
        "Environment :: Web Environment",
        "Topic :: Software Development :: User Interfaces",
    ],
)
