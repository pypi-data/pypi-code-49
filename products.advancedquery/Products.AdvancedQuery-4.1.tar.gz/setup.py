from os.path import abspath, dirname, join
try:
  # try to use setuptools
  from setuptools import setup
  setupArgs = dict(
      include_package_data=True,
      namespace_packages=['Products'],
      zip_safe=False, # to let the tests work
      # to keep "buildout" happy
      install_requires = ["setuptools"]
      )
except ImportError:
  # use distutils
  from distutils import setup
  setupArgs = dict(
    )

cd = abspath(dirname(__file__))
pd = join(cd, 'Products', 'AdvancedQuery')

def pread(filename, base=pd): return open(join(base, filename)).read().rstrip()

setup(name='Products.AdvancedQuery',
      version=pread('VERSION.txt').split('\n')[0],
      description='Flexible high level search construction and execution for Zope (>= 4)',
      long_description=pread('README.txt'),
      classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Framework :: Zope',
        'Framework :: Zope :: 4',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Topic :: Utilities',
        ],
      author='Dieter Maurer',
      author_email='dieter@handshake.de',
      url='https://pypi.org/project/Products.AdvancedQuery/',
      packages=['Products', 'Products.AdvancedQuery', 'Products.AdvancedQuery.tests'],
      keywords='Zope, flexible, search, construction, execution',
      license='BSD (see "Products/AdvancedQuery/LICENSE.txt", for details)',
      **setupArgs
      )



