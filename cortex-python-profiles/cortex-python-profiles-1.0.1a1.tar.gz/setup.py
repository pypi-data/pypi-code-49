"""
Copyright 2019 Cognitive Scale, Inc. All Rights Reserved.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

   http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

from setuptools import find_packages
from setuptools import setup

# Idea from here: https://stackoverflow.com/questions/29870629/pip-install-test-dependencies-for-tox-from-setup-py
tests_require = [
    'mocket>=2.5.0,<3',
    'mock>=2,<3',
    'pipdeptree',
    'tox>=2.9.1,<3',
    'pytest-cov==2.5.1',
    'pytest>=3.2.5,<4',
]

dev_requires = [
    'twine>=1.12.1,<2',
    'setuptools',
    'wheel',
    'pipdeptree',
    'mypy==0.720',
    'pylint>=2.3.0,<3',
]

docs_require = [
    'Sphinx>=1.8.3,<2',
    'sphinxcontrib-restbuilder==0.2',
    'nbconvert==5.4.0',
]


with open('README.md') as f:
    long_description = f.read()


setup(name='cortex-python-profiles',
      description="Profile of 1 Extension for the Base Python Module of the Cortex Cognitive Platform",
      long_description=long_description,
      long_description_content_type='text/markdown',
      version='1.0.1',
      author='CognitiveScale',
      author_email='info@cognitivescale.com',
      url='https://github.com/CognitiveScale/cortex-python-profiles',
      license='Apache License Version 2.0',
      platforms=['linux', 'osx'],
      packages=find_packages(),
      include_package_data=True,
      install_requires=[
          'cortex-python[builders]>=1.0.0,<1.2',
          'pydash>=4.7.3,<4.8',
          'arrow>=0.12.1,<0.13',
          'pandas>=0.23.4',
          'attrs==18.2.0',
          'objectpath==0.6.1',
          'deprecation==2.0.6',
      ],
      extras_require={
          'dev': dev_requires,
          'test': tests_require,
          'docs': docs_require,
          'viz': [
              'cortex-python[jupyter]>=1.0.0,<1.2',
              'psutil',
          ],
          "synthetic": [
            "iso3166==1.0",
            'Faker==2.0.0',
          ],
          "bulk": [
              "pymongo>=3.10.1,<3.11"
          ]
      },
      tests_require=tests_require,
      classifiers=[
          'Operating System :: MacOS :: MacOS X',
          'Operating System :: POSIX',
          'Programming Language :: Python :: 3.6',
      ])
