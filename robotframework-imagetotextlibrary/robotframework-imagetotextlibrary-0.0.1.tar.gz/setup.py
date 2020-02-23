from os.path import abspath, dirname, join as path_join
from setuptools import setup
from ImageToTextLibrary.version import VERSION

CURDIR = abspath(dirname(__file__))

KEYWORDS = ('tesseractlibrary')

SHORT_DESC = ('Robot Framework library for coverting image to text')

with open(path_join(CURDIR, 'README.rst'), 'r') as readme:
    LONG_DESCRIPTION = readme.read()

CLASSIFIERS = [
    'Development Status :: 2 - Pre-Alpha',
    'Programming Language :: Python :: 2',
    'Programming Language :: Python :: 3',
    'Operating System :: OS Independent',
    'Topic :: Software Development :: Testing',
    'License :: OSI Approved :: MIT License'
]

setup(name='robotframework-imagetotextlibrary',
      author='Alvin Galang Citaka',
      author_email='alvingalangcitaka@gmail.com',
      url='https://github.com/alvingalangcitaka/robotframework-imagetotextlibrary',
      license='MIT',
      install_requires=[
          'robotframework>=2.8',
          'pytesseract>=0.3.0'
      ],
      packages=[
          'ImageToTextLibrary'
      ],
      keywords=KEYWORDS,
      classifiers=CLASSIFIERS,
      version=VERSION,
      description=SHORT_DESC,
      long_description=LONG_DESCRIPTION)
