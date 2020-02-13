#!/usr/bin/python3
#  -*- coding: utf-8 -*-

from distutils.core import setup

setup(
    name="jhSitemapgenerator",
    version="0.1.4",
    description="A multithreaded commandline tool to create sitemap.xml|.gz|.txt files from a website.",
    license="GPL3+",
    author="Jan Helbling",
    author_email="jh@jan-helbling.ch",
    url="https://github.com/JanHelbling/jhSitemapgenerator",
    platforms=["linux", "freebsd", "netbsd", "unixware7", "openbsd", "windows"],
    scripts=["bin/jhSitemapgenerator.py"],
)
