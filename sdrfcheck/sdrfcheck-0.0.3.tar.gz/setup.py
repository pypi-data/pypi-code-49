import io

from setuptools import setup, find_packages


def readme():
    with open('README.md') as f:
        return f.read()

setup(name='sdrfcheck',
      version='0.0.3',
      description='Python tools for SDRF proteomics validation',
      url='http://github.com/bigbio/sdrfcheck',
      long_description=readme(),
      long_description_content_type='text/markdown',
      author='BigBio Team',
      author_email='ypriverol@gmail.com',
      license='LICENSE',
      include_package_data=True,
      install_requires=['requests', 'pandas_schema', 'pandas','ebi-ols-client', 'click'],
      scripts=['sdrfcheck/sdrfchecker.py'],
      packages=find_packages(),
      zip_safe=False)
