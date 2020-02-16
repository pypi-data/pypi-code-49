from distutils.core import setup

setup(
  name = 'null101703074',
  packages = ['null101703074'],
  version = '0.1',
  license='MIT', 
  description = 'Removes null values from data.',
  author = 'Ankita',
  author_email = 'ankitauppal99@gmail.com',
  url = 'https://github.com/ankita987/nullremoval',
  download_url = 'https://github.com/ankita987/nullremoval/archive/v_01.tar.gz',
  keywords = ['NULL REMOVAL', 'ROW REMOVAL', 'NULL',],
  install_requires=[
          'pandas',
          'numpy'
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
    'Programming Language :: Python :: 3.7'
  ],
)