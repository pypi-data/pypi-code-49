# -*- coding: utf-8 -*-

import os
import codecs
import hjson
from setuptools import setup, find_packages

def get_key (data, key, defaultValue=None):
  result = defaultValue
  if data is not None and key in data:
    result = data[key]
  return result

path = os.path.dirname(os.path.realpath(__file__))
if path.endswith(os.path.sep):
  path = path[0:-1]
fpath = os.path.join(path, "project.properties")
print(fpath)
if os.path.isfile(fpath):
  fp = codecs.open(fpath, mode='r', encoding='utf-8')
  properties = hjson.load(fp)
  
  property_name = get_key(properties, "name")#pypublish
  property_version = get_key(properties, "version")#'0.0.34'
  property_username = get_key(properties, "username")#'tuaplicacionpropia'
  property_author_name = get_key(properties, "author_name")#'tuaplicacionpropia.com'
  property_author_email = get_key(properties, "author_email")#'tuaplicacionpropia@gmail.com'
  property_description = get_key(properties, "description")#'Python library for generate files with jinja and hjson.'
  property_long_description = get_key(properties, "long_description")#'Python library for generate files with jinja and hjson.'
  property_keywords = get_key(properties, "keywords")#'jinja, hjson, files, generate'
  property_commands = get_key(properties, "commands")#publish, help
  scripts = []
  if property_commands is not None:
    for cmd in property_commands:
      scripts.append('bin/' + property_name + '_' + cmd + '.cmd')
      scripts.append('bin/' + property_name + '_' + cmd + '')
  property_requires = get_key(properties, "requires")#['hjson>=2.0.2']
  
  versionA, versionB, versionC = property_version.split(".")
  versionA = int(versionA)
  versionB = int(versionB)
  versionC = int(versionC)
  status_development = 'Development Status :: 4 - Beta'
  if versionA <= 0 and versionB <= 0:
    status_development = 'Development Status :: 1 - Planning'
  elif versionA <= 0 and versionB <= 1:
    status_development = 'Development Status :: 2 - Pre-Alpha'
  elif versionA <= 0 and versionB <= 2:
    status_development = 'Development Status :: 3 - Alpha'
  elif versionA <= 0 and versionB <= 4:
    status_development = 'Development Status :: 4 - Beta'
  elif versionA == 1:
    status_development = 'Development Status :: 5 - Production/Stable'
  elif versionA > 1:
    status_development = 'Development Status :: 6 - Mature'

  property_classifier = get_key(properties, "classifier")#'Topic :: Multimedia :: Graphics'
  
  property_classifiers = []
  if status_development is not None:
    property_classifiers.append(status_development)
  property_classifiers.append('License :: OSI Approved :: MIT License')
  property_classifiers.append('Programming Language :: Python')
  property_classifiers.append('Programming Language :: Python :: 3')
  property_classifiers.append('Intended Audience :: Developers')
  if property_classifier is not None:
    property_classifiers.append(property_classifier)
  
  property_packageData = get_key(properties, "packageData")#['templates/*.txt', 'templates/*.hjson']
  if property_packageData is not None:
    property_packageData = {property_name: property_packageData}
  
  print("setting ...")
  setup(
    name=property_name,
    version=property_version,
    url='https://github.com/' + property_username +'/' + property_name + '',
    download_url='https://github.com/' + property_username + '/' + property_name + '/archive/master.zip',
    author=property_author_name,
    author_email=property_author_email,
    description=property_description,
    long_description=property_long_description,
    keywords=property_keywords,
    classifiers=property_classifiers,
    scripts=scripts,
    packages=find_packages(exclude=['tests']),
    #package_data={},
    #package_data={'': ['license.txt']},
    package_data=property_packageData,
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    license='MIT',
    install_requires=property_requires,
  )
else:
  raise ValueError('A very specific bad thing happened.')
