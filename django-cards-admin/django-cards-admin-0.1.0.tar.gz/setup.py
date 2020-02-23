# -*- coding: utf-8 -*-
import os
from io import open
from setuptools import setup
from setuptools import find_packages

here = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(here, "README.md"), "r", encoding="utf-8") as fobj:
    long_description = fobj.read()

requires = [
    "django",
    "django-simple-tags>=0.2.0",
]

setup(
    name="django-cards-admin",
    version="0.1.0",
    description="Show cards in changelist instead of table for django admin site.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="zencore",
    author_email="dobetter@zencore.cn",
    license="MIT",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
    ],
    keywords=["django admin extentions", "django cards admin"],
    install_requires=requires,
    packages=find_packages(".", exclude=["django_cards_admin_example", "django_cards_admin_example.migrations", "django_cards_admin_demo"]),
    py_modules=["django_cards_admin"],
    zip_safe=False,
    include_package_data=True,
)