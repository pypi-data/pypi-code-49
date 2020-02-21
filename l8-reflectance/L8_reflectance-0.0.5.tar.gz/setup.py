try:
    from setuptools import setup

    setup_kwargs = {'entry_points': {'console_scripts': ['L8_reflectance=L8_reflectance.L8_reflectance:main']}}
except ImportError:
    from distutils.core import setup

    setup_kwargs = {'scripts': ['bin/L8_reflectance']}

tag = '0.0.5'

setup(name='L8_reflectance',
      version=tag,
      py_modules=['L8_reflectance'],
      description='Convert Landsat 8 from DN to reflectance TOA',
      url='https://github.com/ESRIN-RSS/L8_reflectance',
      author='Roberto Cuccu',
      author_email='roberto.cuccu@esa.int',
      license='GPL',
      zip_safe=False,
      packages=['L8_reflectance'],
      install_requires=['numpy', 'gdal'],
      dependency_links=['https://www.conan.io/source/Gdal/2.1.3/osechet/stable'],
      **setup_kwargs)
