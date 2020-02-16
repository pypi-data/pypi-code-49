
from distutils.core import setup
setup(
  name = 'ankitMissingValues',    
  packages = ['ankitMissingValues'], 
  version = '0.1',      
  license='MIT',        
  description = 'This package is used to handle the missing values in the dataset',  
  author = 'Ankit Sengar',                   
  author_email = 'sengarankit98@gmail.com',     
  url = 'https://github.com/ankit0798/ankitMissingValues',   
  download_url = 'https://github.com/ankit0798/ankitMissingValues/blob/master/ankitMissingValues.py',    
  keywords = ['SOME', 'MEANINGFULL', 'KEYWORDS'],   
  install_requires=[            
          'validators',
          'beautifulsoup4',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      
    'Intended Audience :: Developers',      
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   
    'Programming Language :: Python :: 3',      
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
  ],
)