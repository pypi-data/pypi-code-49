from distutils.core import setup

setup(
  name = 'fscleaner',
  packages = ['fscleaner'],
  version = "2.0",
  license='MIT',
  description = 'file system folder cleaner and file remover',
  author = 'Subham Kumar',
  author_email = 'subhamkumarchandrawansi@gmail.com',
  url = 'https://github.com/isubham/fscleaner.git',
  download_url = 'https://github.com/isubham/fscleaner/archive/v2.0.tar.gz',
  keywords = ['file rename', 'folder rename', 'delte file with types'],
  install_requires=[],
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'Topic :: Desktop Environment :: File Managers',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3'
  ]
)