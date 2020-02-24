# -*- coding: utf-8 -*-

from distutils.core import setup

setup(name="music_syn",
      version="2.3",
      description="A simple music synthesizer for Python 3",
      author="Martin C. Doege",
      author_email="mdoege@compuserve.com",
      url="http://mdoege.github.io/PySynth/",
      packages=["music_syn"],
      install_requires=["numpy", "pyglet"])
