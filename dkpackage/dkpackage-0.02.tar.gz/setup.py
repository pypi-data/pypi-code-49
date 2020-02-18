from distutils.core import setup
setup(
  name = 'dkpackage',
  packages = ['dkpackage'],
  version = '0.02',
  license='MIT',
  description = 'Implementing in python made easy to receive the content you like in just one line of code!',
  author = 'David Kuang',
  author_email = 'davidkuang416@gmail.com',
  url = 'https://github.com/DavidKuangGitHub/dkpackage_yhk',
  download_url = 'https://github.com/DavidKuangGitHub/dkpackage_yhk',
  keywords = ['davidkuang', 'dk','start','stop','before'],
  install_requires=[
          'validators',
          'beautifulsoup4',
      ],
  classifiers=[  
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
  ],
)