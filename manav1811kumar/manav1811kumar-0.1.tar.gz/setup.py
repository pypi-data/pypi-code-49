from distutils.core import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
  name = 'manav1811kumar',         # How you named your package folder (MyLib)
  packages = ['Outliers_101703319'],   # Chose the same as "name"
  version = '0.1',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'This library has got the implementation for Outlier Removal',   # Give a short description about your library
  long_description=long_description,
  long_description_content_type="text/markdown",
  author = 'Manav Kumar',                   # Type in your name
  author_email = 'manav1811kumar@gmail.com',      # Type in your E-Mail
  url = "",   
  download_url = '',    # I explain this later on
  keywords = ['Outliers', 'manav', '101703319'],   # Keywords that define your package best
  install_requires=[
          'numpy', 'pandas', 'os', 'csv', 'sys'
      ],
  include_package_data = True,
  py_modules=['Outliers_101703319.py'],
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
  entry_points={"console_scripts":["Outliers_101703319=Outliers_101703319.Outliers_101703319:main"]}
)