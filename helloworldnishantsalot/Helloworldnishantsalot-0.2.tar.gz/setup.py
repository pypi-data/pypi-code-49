from setuptools import setup, find_packages

setup(name='Helloworldnishantsalot',
      version='0.2',
      license='MIT',
      author='nishantsalot',
      author_email='nishantsalot@gmail.com',
      description='Add static script_dir() method to Path',
      packages=find_packages(exclude=['tests']),
      zip_safe=False)