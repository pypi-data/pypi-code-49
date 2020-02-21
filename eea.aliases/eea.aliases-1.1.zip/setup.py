""" EEA Cache Installer
"""
import os
from setuptools import setup, find_packages

NAME = 'eea.aliases'
PATH = NAME.split('.') + ['version.txt']
VERSION = open(os.path.join(*PATH)).read().strip()

setup(name=NAME,
      version=VERSION,
      description="zodbupdate aliases",
      long_description_content_type="text/x-rst",
      long_description=open("README.rst").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # https://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
          "Framework :: Plone :: 4.0",
          "Framework :: Plone :: 4.1",
          "Framework :: Plone :: 4.2",
          "Framework :: Plone :: 4.3",
          "Framework :: Plone :: 5.1",
          "Framework :: Plone :: 5.2",
          "Framework :: Plone :: Addon",
          "Framework :: Zope :: 2",
          "Framework :: Zope :: 4",
          "Framework :: Zope",
          "Programming Language :: Python :: 2.7",
          "Programming Language :: Python :: 3.6",
          "Programming Language :: Python :: 3.7",
          "Programming Language :: Python",
          "Topic :: Software Development :: Libraries :: Python Modules",
          "License :: OSI Approved :: GNU General Public License (GPL)",
      ],
      keywords='EEA Aliases zodbverify zodbupdate',
      author='European Environment Agency: IDM2 A-Team',
      author_email="eea-edw-a-team-alerts@googlegroups.com",
      download_url="https://pypi.python.org/pypi/eea.aliases",
      url='https://github.com/eea/eea.aliases',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['eea'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
        'setuptools',
      ],
      extras_require={
        'test': ['plone.app.testing']
      },
      entry_points="""
      [z3c.autoinclude.plugin]
      target = plone

      [zodbupdate]
      renames = eea.aliases:rename_dict
      """
      )
