from distutils.core import setup
setup(
  name = 'outliers_101703382',         # How you named your package folder (MyLib)
  packages = ['outliers_101703382'],   # Chose the same as "name"
  version = '1.0',      # Start with a small number and increase it with every change you make
  license='MIT', 
  entry_points ={ 
    'console_scripts': [ 
        'remove_outliers = outliers_101703382.remove_outliers:main'
    ] 
  }, 
  description = 'outliers removal',   # Give a short description about your library
  author = 'Paras Arora',                   # Type in your name
  author_email = 'parora_be17@thapar.edu',      # Type in your E-Mail
  keywords = ['outliers removal', 'remove outliers'],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
          'numpy',
          'pandas',
          'scipy',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.6',
    
  ],
)

