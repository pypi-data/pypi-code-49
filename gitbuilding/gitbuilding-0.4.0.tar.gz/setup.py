'''Setup for the module'''

__author__ = 'Julian Stirling'

import sys
from os import path
import glob
from setuptools import setup, find_packages

def install():
    '''The installer'''

    if sys.version_info[0] == 2:
        sys.exit("Sorry, Python 2 is not supported")

    #Globbing all of the static files and then removing `gitbuilding/` from the start
    package_data_location = glob.glob('gitbuilding/static/**/*', recursive=True)
    package_data_location = [package[12:] for package in package_data_location]
    licenses = glob.glob('gitbuilding/licenses/*', recursive=True)
    for lic in licenses:
        package_data_location.append(lic[12:])

    this_directory = path.abspath(path.dirname(__file__))
    with open(path.join(this_directory, 'README.md'), encoding='utf-8') as file_id:
        long_description = file_id.read()
    short_description = ('For documenting hardware projects with minimal effort,'
                         'so you can stop writing and git building.')

    setup(name='gitbuilding',
          version='0.4.0',
          license="GPLv3",
          description=short_description,
          long_description=long_description,
          long_description_content_type='text/markdown',
          author='Julian Stirling',
          author_email='julian@julianstirling.co.uk',
          packages=find_packages(),
          package_data={'gitbuilding': package_data_location},
          keywords=['Documentation', 'Hardware'],
          zip_safe=False,
          url='https://gitbuilding.io/',
          project_urls={
              "Bug Tracker": "https://gitlab.com/bath_open_instrumentation_group/git-building/issues",
              "Source Code": "https://gitlab.com/bath_open_instrumentation_group/git-building",
              },
          classifiers=[
              'Development Status :: 5 - Production/Stable',
              'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
              'Programming Language :: Python :: 3.6'
              ],
          install_requires=['argparse', 'pyyaml>=5.1', 'flask', 'flask_cors', 'requests', 'markdown', 'colorama'],
          python_requires=">=3.6",
          entry_points={'console_scripts': ['gitbuilding = gitbuilding.__main__:main']},
          )

if __name__ == "__main__":
    install()
