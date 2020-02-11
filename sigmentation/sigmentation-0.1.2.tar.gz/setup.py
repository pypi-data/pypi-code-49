# This file is part of the Sigmentation project.
#    https://gitlab.com/sigmentation/sigmentation
#
# Copyright 2020 Zeyd Boukhers <zeyd@boukhers.com>
#                Matthias Lohr <mail@mlohr.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


from setuptools import setup, find_packages

with open('README.md', 'r') as readme:
    long_description = readme.read()

setup(
    name="sigmentation",
    description='Univariate Data Segmentation using Genetic Algorithm',
    long_description=long_description,
    long_description_content_type='text/markdown',
    use_scm_version=True,
    setup_requires=['setuptools_scm'],
    author='Zeyd Boukhers <zeyd@boukhers.com>, Matthias Lohr <mail@mlohr.com>',
    url='https://gitlab.com/sigmentation/sigmentation',
    license='Apache License 2.0',
    install_requires=[
        'numpy',
        'scipy'
    ],
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "nparray2json=sigmentation.cli:nparray2json",
            "sigmentation=sigmentation.cli:main"
        ]
    },
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3',
        'Topic :: Scientific/Engineering',
        'Topic :: Scientific/Engineering :: Information Analysis',
        'Topic :: Scientific/Engineering :: Visualization'
    ],
    project_urls={
        'Documentation': 'https://gitlab.com/sigmentation/sigmentation',
        'Source': 'https://gitlab.com/sigmentation/sigmentation',
        'Tracker': 'https://gitlab.com/sigmentation/sigmentation/issues'
    }
)
