# -*- coding: utf-8 -*-
from setuptools import setup, find_packages


setup(
    name='evolut',
    version="1.2",
    packages=find_packages(),
    author="megadose",
    install_requires=["cfscrape","urllib3","requests","fake_headers","beautifulsoup4"],
    author_email="anonymous@notmymail.com",
    description="Permet de recupéré des informations que un compte evolut",
    long_description="",
    include_package_data=True,
    url='http://github.com/megadose/evolut',
    classifiers=[
        "Programming Language :: Python",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    ],
)
