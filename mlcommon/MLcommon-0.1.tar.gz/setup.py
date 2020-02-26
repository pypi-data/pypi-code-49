from distutils.core import setup
setup(
  name = 'MLcommon',
  packages = ['MLcommon'],
  version = '0.1',
  license= '',
  description = 'Common interface for Machine Learning models with explicit model protocol',
  author = 'Juan Carlos Arbeláez',
  author_email = 'juanarbelaez@vaico.com.co',
  url = 'https://jarbest@bitbucket.org/jarbest/mlcommon.git',
  download_url = 'https://bitbucket.org/jarbest/mlcommon/get/v01.tar.gz',
  keywords = ['VAICO', 'COMMON', 'ML'],
  install_requires=[],
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ]
)