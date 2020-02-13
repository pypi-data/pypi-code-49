from setuptools import setup, find_packages

import pyplottr


def read_deps(filename):
    with open(filename) as f:
        deps = f.read().split('\n')
        deps.remove("")
    return deps


setup(name="pyplottr",
      version=pyplottr.__version__,
      description="Matplotlib for humans",
      url="http://github.com/toaarnio/pyplottr",
      author="Tomi Aarnio",
      author_email="tomi.p.aarnio@gmail.com",
      license="Apache License 2.0",
      py_modules=["pyplottr"],
      packages=find_packages(),
      install_requires=read_deps("requirements.txt"),
      zip_safe=True)
