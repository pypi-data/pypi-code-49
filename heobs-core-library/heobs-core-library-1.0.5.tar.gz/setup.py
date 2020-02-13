# Copyright (C) 2019 Heritage Observatory.  All rights reserved.
#
# This software is the confidential and proprietary information of
# Heritage Observatory or one of its subsidiaries.  You shall not
# disclose this confidential information and shall use it only in
# accordance with the terms of the license agreement or other applicable
# agreement you entered into with Heritage Observatory.
#
# HERITAGE OBSERVATORY MAKES NO REPRESENTATIONS OR WARRANTIES ABOUT THE
# SUITABILITY OF THE SOFTWARE, EITHER EXPRESS OR IMPLIED, INCLUDING BUT
# NOT LIMITED TO THE IMPLIED WARRANTIES OF MERCHANTABILITY, FITNESS FOR
# A PARTICULAR PURPOSE, OR NON-INFRINGEMENT.  HERITAGE OBSERVATORY SHALL
# NOT BE LIABLE FOR ANY LOSSES OR DAMAGES SUFFERED BY LICENSEE AS A
# RESULT OF USING, MODIFYING OR DISTRIBUTING THIS SOFTWARE OR ITS
# DERIVATIVES.

import os

import pipfile
import setuptools


__author__ = "Daniel CAUNE"
__copyright__ = "Copyright (C) 2019, Heritage Observatory"
__credits__ = ["Daniel CAUNE"]
__email__ = "daniel.caune@heritageobservatory.org"
__license__ = "Copyright (C) 2019 Heritage Observatory. All rights reserved."
__maintainer__ = "Daniel CAUNE"
__status__ = "Production"
__version__ = '1.0.5'


# Base directory where this file is located.
BASE_DIR = os.path.dirname(__file__)


def get_requirements():
    pip_file = pipfile.load()
    return os.linesep.join([
        package_name
        for package_name, package_version in pip_file.data['default'].items()])


def read_file(file_path_name):
    with open(file_path_name, mode='rt', encoding='utf-8') as fd:
        return fd.read()


setuptools.setup(
    author=__author__,
    author_email=__email__,
    classifiers = [
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Development Status :: 5 - Production/Stable',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Programming Language :: Python'
    ],
    description='Heritage Observatory Core Python Library',
    install_requires=get_requirements(),
    license=__license__,
    long_description=read_file(os.path.join(BASE_DIR, 'README.md')),
    long_description_content_type='text/markdown',
    name='heobs-core-library',
    packages=setuptools.find_packages(),
    platforms=['any'],
    python_requires='>=3',
    version=__version__
)
