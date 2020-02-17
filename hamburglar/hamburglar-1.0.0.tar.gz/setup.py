from distutils.core import setup
import setuptools

with open("README.md","r") as fh:
    long_description = fh.read()


setup(
  name = 'hamburglar', 
  packages = ['hamburglar'],   
  version = '1.0.0',      
  license='GNU',        
  description = 'command line tool to collect useful information from urls, directories, and files',   # Give a short description about your library
  author = 'Adam Musciano',
  author_email = 'amusciano@gmail.com',
  url = 'https://github.com/needmorecowbell/Hamburglar',
  download_url = 'https://github.com/needmorecowbell/Hamburglar/archive/Hamburglar-1.0.tar.gz',
  long_description_content_type="text/markdown",
  long_description=long_description,
  keywords = ["Forensics", "Static File Analysis"],
  entry_points = {
    'console_scripts': ['hamburglar = hamburglar.hamburglar:main'],
  },
  install_requires=[            
    "beautifulsoup4==4.7.1",
    "certifi==2019.6.16",
    "cffi==1.13.2",
    "chardet==3.0.4",
    "cryptography==2.8",
    "cssselect==1.0.3",
    "feedfinder2==0.0.4",
    "feedparser==5.2.1",
    "idna==2.8",
    "iocextract==1.13.1",
    "jieba3k==0.35.1",
    "lxml==4.3.4",
    "newspaper3k==0.2.8",
    "nltk==3.4.5",
    "numpy==1.17.4",
    "pandas==0.25.3",
    "Pillow==6.0.0",
    "pycparser==2.19",
    "PyMySQL==0.9.3",
    "python-dateutil==2.8.0",
    "pytz==2019.3",
    "PyYAML==5.1.1",
    "regex==2019.6.8",
    "requests==2.22.0",
    "requests-file==1.4.3",
    "six==1.12.0",
    "soupsieve==1.9.1",
    "SQLAlchemy==1.3.5",
    "tinysegmenter==0.3",
    "tldextract==2.2.1",
    "urllib3==1.25.3",
    "yara-python==3.11.0"
  ],
  classifiers=[
    'Development Status :: 4 - Beta',      
    'Intended Audience :: Information Technology',      
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
    'Programming Language :: Python :: 3', 
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',

  ],
)
