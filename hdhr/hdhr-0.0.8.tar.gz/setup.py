from setuptools import setup, find_packages
import sys, os

import os.path
dev_path = os.path.dirname(__file__)
sys.path.insert(0, dev_path)

try:
    import hdhr.libhdhr
except OSError as e:
    print("Could not load HDHomeRun library: %s" % (e))
    sys.exit(1)
else:
    print("HDHomeRun libraries verified.")

long_description = "HDHomeRun interface library. Supports device discovery, " \
                   "channel-scanning, streaming, status inquiries, channel " \
                   "changes, etc.."""

setup(name='hdhr',
      version='0.0.8',
      description="HDHomeRun interface library for Python 3.",
      long_description=long_description,
      classifiers=['Development Status :: 4 - Beta',
                   'Natural Language :: English',
                   'Topic :: Software Development :: Libraries :: Python Modules',
                   'Topic :: Multimedia :: Video :: Capture'],
      keywords='tv television tuner tvtuner hdhomerun',
      author='Nat Burns',
      author_email='nbaccount@burnskids.com',
      url='https://github.com/burnnat/hdhr',
      license='GPL 2',
      packages=['hdhr'],
      include_package_data=True,
      zip_safe=True,
      setup_requires=['wheel'],
      install_requires=['setuptools']
)
