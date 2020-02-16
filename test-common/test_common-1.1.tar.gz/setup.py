import os
from setuptools import setup, find_packages  # Always prefer setuptools over distutilss

VERSION = "1.1"

with open("README.md") as readme:
    LONG_DESCRIPTION = readme.read()


def find_folders_with_this_name(dir_name: str) -> str:
    """ Look for folder with given name, searching from current working dir.

    :param dir_name: Folder name to look for.
    :return: Relative path, from current working dir, where folder is.
    """
    for dir, dirs, files in os.walk('.'):
        if dir_name in dirs:
            yield os.path.relpath(os.path.join(dir, dir_name))


setup(name="test_common",
      version=VERSION,
      description="Common functions useful for tests.",
      long_description=LONG_DESCRIPTION,
      long_description_content_type="text/markdown",
      author="Dante Signal31",
      author_email="dante.signal31@gmail.com",
      license="BSD-3",
      url="https://github.com/dante-signal31/test_common_python",
      download_url="https://pypi.org/project/test-common/",
      packages=find_packages(),
      classifiers=['Development Status :: 4 - Beta',
                   'Intended Audience :: Developers',
                   'Intended Audience :: Other Audience',
                   'Topic :: System',
                   'License :: OSI Approved :: BSD License',
                   'Operating System :: POSIX :: Linux',
                   'Programming Language :: Python :: 3',
                   'Programming Language :: Python :: 3.7'],
      keywords="test",
      install_requires=[],
      zip_safe=False
      )