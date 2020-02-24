from setuptools import setup

setup(
     name='pysdi',
     version='0.2.6.3',
     description='Calculator of non-parametric standardized drought indices.',
     url='https://bitbucket.org/pysdi/pysdi',
     author='R. A. Real-Rangel',
     author_email='rrealr@iingen.unam.mx',
     license='GPL-3.0',
     packages=['pysdi'],
     install_requires=[
         'datetime',
         'dask',
         'netcdf4',
         'numpy',
         'pathlib2',
         'scipy',
         'toml',
         'toolz',
         'xarray',
         ],
     zip_safe=False
     )
    