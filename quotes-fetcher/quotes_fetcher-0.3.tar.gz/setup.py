from distutils.core import setup
setup(
  name = 'quotes_fetcher',
  packages = ['quotes_fetcher'],
  version = '0.3',
  license='MIT',
  description = 'quote_fetcher is a toy app that provides you with an option to fetch exchange market data and calculate some metrics ',
  author = 'Ruslan Danila',
  author_email = 'daniloruslan@yahoo.com',
  url = 'https://github.com/user/daniloruslan',
  download_url = 'https://github.com/daniloruslan/quotes_fetcher/archive/v0.3.tar.gz',
  keywords = ['exchange', 'data', 'quotes'],
  install_requires=[
          'yfinance',
          'pandas',
          'numpy',
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