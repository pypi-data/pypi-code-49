from setuptools import setup
from django_col import __version__

setup(name='django_col',
      version=__version__,
      description='Django app using colours_library',
      url='https://gitlab.bitcomp.intra/eryk_malczyk/django_col',
      author='ErykMalczyk',
      author_email='eryk.malczyk@bitcomp.fi',
      license='some_license',
      packages=['django_col'],
      install_requires=[
          'colours_library',
          'webcolors==1.3',
          'Pillow',
      ],
      tests_require=['pytest',],
      include_package_data=True,
      zip_safe=False)