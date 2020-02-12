from distutils.core import setup
from setuptools import setup
setup(
  name = 'outlier_removal_101703121',         # How you named your package folder (MyLib)
  packages = ['outlier_removal_101703121'],   # Chose the same as "name"
  version = '0.1',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'Remove Outliers from the dataset',   # Give a short description about your library
  author = 'Atishay jain',                   # Type in your name
  author_email = 'atishay21@gmail.com',   # Provide either the link to your github or to your website
  keywords = [],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
          'pandas',
          'numpy',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3.7',
  ],
)