"""
Project setup
"""
import os
import setuptools
from variables import NAME, VERSION, AUTHOR, AUTHOR_EMAIL, DESCRIPTION, URL

# read the contents of the README file
CWD = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(CWD, 'README.md'), encoding='utf-8') as f:
    LONG_DESCRIPTION = f.read()


setuptools.setup(
    name=NAME,
    version=VERSION,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    description=DESCRIPTION,
    url=URL,
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    packages=[NAME, NAME + ".main"],
    classifiers=[
        'Operating System :: OS Independent',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 3',
        'Natural Language :: English',
        'Topic :: Software Development :: Libraries',
        'Environment :: Plugins',
    ],
)
