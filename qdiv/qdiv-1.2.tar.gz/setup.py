from distutils.core import setup
setup(
  name = 'qdiv',
  packages = ['qdiv'],
  version = '1.2',
  license='GNU General Public License',
  description = 'Microbial diversity calculations',
  author = 'Oskar Modin',
  author_email = 'omvatten@gmail.com',
  url = 'https://github.com/omvatten/qdiv',
  download_url = 'https://github.com/omvatten/qdiv/archive/v1.2.tar.gz',    #Copy address from source code tar.gz on github
  keywords = ['Microbial diversity', 'High-throughput amplicon sequencing'],
  install_requires=['pandas', 'numpy', 'matplotlib', 'python-Levenshtein']
)