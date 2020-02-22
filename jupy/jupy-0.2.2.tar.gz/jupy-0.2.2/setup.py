from setuptools import setup, find_packages

LONG_DESCRIPTION="""
jupy - A utility to launch jupyter lab remotely.
================================================

**jupy** is a utility that automatically finds an available port via **ss**, **ssh**
into the server, making an ssh tunnel, calls jupyter lab.

Please install on your computer and host server to automatically
download jupyter lab.

Authors: Apuã Paquola, Kynon Benjamin

Installation
------------

``pip install --user jupy``

Requires: ``ssh`` and ``ss``

Does not currently work for Mac OS.

Manual
------

``usage: jupy [-h] [--host HOST] [--dir DIR] [--username USERNAME] [--default-port DEFAULT_PORT]``

============== ============================ ==========
Flag           Description                  Example
============== ============================ ==========
-–host         server to ssh                1.1.1.1
-–dir          directory to run jupyter lab /ceph
-–username     username on server           myusername
-–default-port localhost port               8888
--version, -v  print version                jupy 0.2.2
============== ============================ ==========

Change logs
-----------
v0.2.2
------

-  Fixed $HOME directory bug. Now, autodetects $HOME

v0.2.1
------

-  Added version flag

v0.2
~~~~

-  Launches jupyter-lab instead of jupyter-notebook
-  added function to specify username, default is to use local username
"""

setup(name='jupy',
      version='0.2.2',
      packages=find_packages(),
      scripts=['jupy'],
      install_requires=[
          'jupyterlab>=1.2.3',
          'argparse>=1.1'
      ],
      author="Kynon Benjamin",
      author_email="kj.benjamin90@gmail.com",
      decription="A utility to launch jupyter lab remotely.",
      long_description=LONG_DESCRIPTION,
      long_description_content_type='text/x-rst',
      package_data={
          '': ['*org'],
      },
      url="https://github.com/KrotosBenjamin/erwin_paquola/tree/master/jupy",
      # license='GPLv3',
      classifiers=[
          "Programming Language :: Python :: 3",
          "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
      ],
      keywords='jupyter jupyterlab ssh remote',
      zip_safe=False)
