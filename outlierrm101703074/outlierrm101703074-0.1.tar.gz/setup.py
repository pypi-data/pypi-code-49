from distutils.core import setup

setup(
  name = 'outlierrm101703074',
  packages = ['outlierrm101703074'],
  version = '0.1',
  license='MIT', 
  description = 'Removes rows containing outliers from data using IQR method or Z-score method.',
  author = 'Ankita',
  author_email = 'ankitauppal99@gmail.com',
  url = 'https://github.com/ankita987/outlier101703074',
  download_url = 'https://github.com/ankita987/outlier101703074/archive/v_1.tar.gz',
  keywords = ['OUTLIER REMOVAL', 'ROW REMOVAL', 'OUTLIER', 'IQR', 'Z-SCORE'],
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