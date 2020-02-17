from distutils.core import setup
setup(
  name = 'nipunn_datahandler',         
  packages = ['nipunn_datahandler'],   
  version = '0.1',      
  license='MIT',        
  description = 'Helps in filling or removing missing data',   
  author = 'Nipunn Malhotra',                   
  author_email = 'nipunnjg@gmail.com',      
  url = 'https://github.com/nipunnmalhotra/nipunn_datahandler',   
  download_url = 'https://github.com/nipunnmalhotra/nipunn_datahandler/archive/0.1.tar.gz',    
  keywords = ['Model for filling missing data', 'Handling missing data','fill missing data','missing data in python dataset','missing dataset'],   
  install_requires=[           
          'numpy',
        'pandas','statistics','sklearn'
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
  ],
)