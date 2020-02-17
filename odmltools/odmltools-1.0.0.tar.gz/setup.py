import json
import os

try:
    from setuptools import setup
except ImportError as ex:
    from distutils.core import setup

with open(os.path.join("odmltools", "info.json")) as infofile:
    infodict = json.load(infofile)

VERSION = infodict["VERSION"]
AUTHOR = infodict["AUTHOR"]
COPYRIGHT = infodict["COPYRIGHT"]
CONTACT = infodict["CONTACT"]
HOMEPAGE = infodict["HOMEPAGE"]
CLASSIFIERS = infodict["CLASSIFIERS"]


packages = [
    'odmltools',
    'odmltools.importers'
]

with open('README.md') as f:
    description_text = f.read()

install_req = ["odml", "docopt", "xmltodict"]

setup(
    name='odmltools',
    version=VERSION,
    description='open metadata Markup Language convenience tools',
    author=AUTHOR,
    author_email=CONTACT,
    url=HOMEPAGE,
    packages=packages,
    install_requires=install_req,
    include_package_data=True,
    long_description=description_text,
    long_description_content_type="text/markdown",
    classifiers=CLASSIFIERS,
    license="BSD",
    entry_points={'console_scripts':
                      ['odmlimportdatacite=odmltools.importers.import_datacite:main']}
)
