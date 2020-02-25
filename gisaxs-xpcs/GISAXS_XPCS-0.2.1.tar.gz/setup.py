from setuptools import setup, find_packages

setup(name='GISAXS_XPCS',
      version='0.2.1',
      description='Package for GISAXS-XPCS analysis. For internal use within Shreiber lab.',
      author='Vladimir Starostin',
      author_email='vladimir.starostin@uni-tuebingen.de',
      license='MIT',
      packages=find_packages(),
      install_requires=[
          'numpy', 'pandas', 'matplotlib', 'scipy', 'h5py', 'tqdm', 'jupyter'
      ],
      include_package_data=True,
      zip_safe=False)
