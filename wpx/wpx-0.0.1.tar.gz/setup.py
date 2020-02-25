
import io
import re
import setuptools
import sys

with io.open('src/wpx/__init__.py', encoding='utf8') as fp:
  version = re.search(r"__version__\s*=\s*'(.*)'", fp.read()).group(1)

with io.open('README.md', encoding='utf8') as fp:
  long_description = fp.read()

requirements = ['beautifulsoup4 >=4.8.2,<5.0.0', 'nr.interface >=0.0.1,<0.1.0', 'nr.databind >=0.0.1,<0.1.0', 'requests >=2.22.0,<3.0.0', 'PyYAML >=5.3,<6.0.0']

setuptools.setup(
  name = 'wpx',
  version = version,
  author = 'Niklas Rosenstein',
  author_email = 'rosensteinniklas@gmail.com',
  description = '💻 Wpx is a wallpaper downloader.',
  long_description = long_description,
  long_description_content_type = 'text/markdown',
  url = None,
  license = 'MIT',
  packages = setuptools.find_packages('src', ['test', 'test.*', 'docs', 'docs.*']),
  package_dir = {'': 'src'},
  include_package_data = False,
  install_requires = requirements,
  extras_require = {},
  tests_require = [],
  python_requires = None, # TODO: '>=3.5,<4.0.0',
  data_files = [],
  entry_points = {
    'console_scripts': [
      'wpx = wpx.__main__:_entry_main',
    ],
    'wpx.providers': [
      'bing = wpx.providers.bing:BingImageProvider',
      'wallpapershome = wpx.providers.wallpapershome:WallpapersHomeProvider',
    ]
  },
  cmdclass = {}
)
