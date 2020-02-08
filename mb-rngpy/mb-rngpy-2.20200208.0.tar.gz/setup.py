#!/usr/bin/env python3
import os
import re
import subprocess
from distutils.core import setup, Command
from distutils.command.sdist import sdist as _sdist
from distutils.command.build import build as _build

REPOSITORY_URL = "https://github.com/metabrainz/mb-rngpy"
DOWNLOAD_URL = "{url}/archive/v-{version}.tar.gz"
VERSION_PATH = "mbrng/__init__.py"

# The following code is taken from
# https://github.com/warner/python-ecdsa/blob/f03abf93968019758c6e00753d1b34b87fecd27e/setup.py
# which is released under the MIT license (see LICENSE for the full license
# text) and (c) 2012 Brian Warner
VERSION_PY = """
# This file is originally generated from Git information by running 'setup.py
# version'. Distribution tarballs contain a pre-generated copy of this file.

__version__ = '%s'
"""


def update_version_py():
    if not os.path.isdir(".git"):
        print("This does not appear to be a Git repository.")
        write_init_py()
        return
    try:
        p = subprocess.Popen(["git", "describe",
                              "--tags", "--dirty", "--always"],
                             stdout=subprocess.PIPE)
    except EnvironmentError:
        print("Unable to run git.")
        write_init_py()
        return
    stdout = p.communicate()[0]
    if p.returncode != 0:
        print("Running git failed.")
        write_init_py()
        return
    version = stdout.decode('utf-8').strip()
    if version.startswith('v-'):
        version = version[2:]
    write_init_py(version)


def write_init_py(version="unknown"):
    if version == "unknown" and os.path.isfile(VERSION_PATH):
        print("Skip erasing version in '{path}'.".format(
            path=VERSION_PATH))
        return
    f = open(VERSION_PATH, "w")
    f.write(VERSION_PY % version)
    f.close()
    print("Set version to '{version}' in '{path}'.".format(
        path=VERSION_PATH, version=version))


def get_version():
    try:
        f = open(VERSION_PATH)
    except IOError as e:
        import errno
        if e.errno == errno.ENOENT:
            update_version_py()
            return get_version()
    except EnvironmentError:
        return None
    for line in f.readlines():
        mo = re.match("__version__ = '([^']+)'", line)
        if mo:
            version = mo.group(1)
            return version
    return None


class Version(Command):
    description = "Update '{path}' from Git repository.".format(
            path=VERSION_PATH)
    user_options = []
    boolean_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        update_version_py()
        print("Version is now '{0}'.".format(get_version()))


class sdist(_sdist):
    def run(self):
        update_version_py()
        # unless we update this, the sdist command will keep using the old
        # version
        self.distribution.metadata.version = get_version()
        return _sdist.run(self)


class build(_build):
    def run(self):
        update_version_py()
        # unless we update this, the build command will keep using the old
        # version
        self.distribution.metadata.version = get_version()
        return _build.run(self)

# Here ends the code taken from Brian Warner


def download_url(version):
    return DOWNLOAD_URL.format(url=REPOSITORY_URL, version=version)


setup(name="mb-rngpy",
      python_requires=">=3",
      version=get_version(),
      author="Wieland Hoffmann",
      author_email="themineo@gmail.com",
      description="Python bindings for the "
                  "MusicBrainz XML Metadata RELAX NG schema",
      long_description="Python bindings for the "
                       "MusicBrainz XML Metadata RELAX NG schema",
      packages=["mbrng"],
      package_dir={"mbrng": "mbrng"},
      install_requires=["lxml==4.3.2"],
      download_url=download_url(get_version()),
      url=REPOSITORY_URL,
      license="MIT",
      classifiers=["Development Status :: 5 - Production/Stable",
                   "License :: OSI Approved :: MIT License",
                   "Natural Language :: English",
                   "Operating System :: OS Independent",
                   "Programming Language :: Python :: 3",
                   "Topic :: Software Development :: Libraries "
                   ":: Python Modules"],
      cmdclass={"version": Version, "sdist": sdist, "build": build}
      )
