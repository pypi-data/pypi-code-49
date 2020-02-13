from setuptools import setup, find_packages

setup(
      name="nobiserviceslib",
      version="0.1.2",
      author="Guava and Nobi",
      email="tsrn398696366@gmail.com",
      maintainer="Guava and Nobi",
      url="https://github.com/GuavaAndNobi/NobiServicesLib-Python",
      license="LGPL",
      description="NobiServices Python API.",
      platforms='all',
      install_requires=[
            "dnspython >= 1.16.0",
            "pycryptodome >= 3.9.6",
      ],
      packages=find_packages(),
      scripts=[],
      )