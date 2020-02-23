from distutils.core import setup
setup(
  name = 'pyfolio_v0p5p3',         # How you named your package folder (MyLib)
  packages = ['pyfolio_v0p5p3'],   # Chose the same as "name"
  version = '0.5.3',      # Start with a small number and increase it with every change you make
  license='Apache License, Version 2.0',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'Updates to conda v0.5.1 pyfolio package with fixes for how Pandas handles dates/time in v1.0',   # Give a short description about your library
  author = 'Layne Berge',                   # Type in your name
  author_email = 'layneberge@gmail.com',      # Type in your E-Mail
  url = 'https://github.com/laberge1/pyfolio_v0p5p3',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/laberge1/pyfolio_v0p5p3/archive/v0.5.3.tar.gz',    # I explain this later on
  keywords = ['pyfolio', 'finance', 'stock analysis','stock','back testing'],   # Keywords that define your package best
  install_requires = [
    'matplotlib>=1.4.0',
    'numpy>=1.11.1',
    'pandas>=0.18.1',
    'pytz>=2014.10',
    'scipy>=0.14.0',
    'scikit-learn>=0.16.1',
    'seaborn>=0.7.1',
    'empyrical>=0.5.0',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: Apache Software License',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.7',
  ],
)
