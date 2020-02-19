from distutils.core import setup
setup(
  name = 'missing-101703016-abhinav',         # How you named your package folder (MyLib)
  packages = ['missing-101703016-abhinav'],   # Chose the same as "name"
  version = '6.9',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'Handling missing values in a dataset',   # Give a short description about your library
  author = 'Abhinav Jain',                   # Type in your name
  author_email = 'jainabhinav1299@gmail.com',      # Type in your E-Mail
  url = 'https://github.com/abhinavjain12',   # Provide either the link to your github or to your website
  keywords = ['MISSING', 'Statistics'],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
          'pandas', 'numpy','sys', 'datawig' ,
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
  ],
)