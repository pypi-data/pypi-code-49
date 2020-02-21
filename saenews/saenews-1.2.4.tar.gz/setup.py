from setuptools import setup
#from distutils.core import setup
import os
import glob
import requests
pkglist = glob.glob('saenews/*')
#from setuptools import setup, find_packages
from os import path
this_directory = path.abspath(path.dirname('__file__'))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
  package_data      = {'saenews': ['*','fonts/*','fonts/TTF/*','fonts/OTF/*','SM/*'] },
  zip_safe=False,
  include_package_data = True,
  name = 'saenews',        
  packages = ['saenews'],  
  version = '1.2.4',
  license='MIT',        
    # other arguments omitted
  long_description=long_description,
  long_description_content_type='text/markdown',
  description = 'required code for sae.news',   
  author = 'saenews',        
  author_email = 'contact@advaitlabs.com',      # Type in your E-Mail
  url = 'https://github.com/dheerajmpai/saenews/',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/dheerajmpai/saenews/archive/v_033.tar.gz',
  keywords = ['OPENCV', 'IMAGE PROCESSING', 'NEWS'],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
          'beautifulsoup4',
          'opencv-contrib-python',
          'Pillow',
          'matplotlib',
          'requests'
          
      
      ],
  classifiers=[
    'Development Status :: 4 - Beta',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Natural Language :: Hindi',
  ],
)

#print ('HHHHEEEEInstalled')
#url = 'http://127.0.0.1:8000/sae_arc.zip'
#r = requests.get(url)
#f = open('sae.zip', 'wb')
#f.write(r.content)
#f.close()

