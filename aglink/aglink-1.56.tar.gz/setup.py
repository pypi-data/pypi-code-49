import io
import re
from setuptools import setup

import os
import shutil
try:
    os.remove(os.path.join('aglink', '__version__.py'))
except:
    pass
shutil.copy2('__version__.py', 'aglink')

with io.open("README.rst", "rt", encoding="utf8") as f:
    readme = f.read()

# with io.open("__version__.py", "rt", encoding="utf8") as f:
    # version = re.search(r"version = \'(.*?)\'", f.read()).group(1)
import __version__
version = __version__.version

setup(
    name="aglink",
    version=version,
    url="https://bitbucket.org/licface/aglink",
    project_urls={
        "Documentation": "https://bitbucket.org/licface/aglink",
        "Code": "https://bitbucket.org/licface/aglink",
    },
    license="BSD",
    author="Hadi Cahyadi LD",
    author_email="cumulus13@gmail.com",
    maintainer="cumulus13 Team",
    maintainer_email="cumulus13@gmail.com",
    description="Generator Links",
    long_description=readme,
    long_description_content_type="text/markdown",
    packages=["aglink"],
    install_requires=[
        'requests',
        'cfscrape',
        'bs4',
        'argparse',
        'clipboard',
        'idm',
        'vping',
        'make_colors>=3.12',
        'make_colors_tc',
        'colorama',
        'termcolor',
        'configset',
        'cmdw',
        'configparser',
        'pywget',
        'pydebugger'
    ],
    entry_points = {
         "console_scripts": [
             "aglink = aglink.__main__:usage",
             "agl = aglink.__main__:usage",
         ]
    },
    data_files=['aglink/__version__.py', 'README.rst', 'LICENSE.rst', 'aglink/aglink.ini'],
    include_package_data=True,
    python_requires=">=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
    ],
)
