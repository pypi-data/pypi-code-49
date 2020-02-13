from setuptools import setup
setup(
  name = 'auchanTestTools',         # How you named your package folder (MyLib)
  packages = ['auchanTestTools'],   # Chose the same as "name"
  version = '0.2',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'Testing tools/ In development',   # Give a short description about your library
  author="Pavel Doroshenko",                   # Type in your name
  author_email="p.doroshenko@auchan.ru",      # Type in your E-Mail
  install_requires=[            # I get to this in a second
          'pysftp==0.2.8',
          'fnmatch',
          'shutil',
          'subproces',
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
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
  ],
)