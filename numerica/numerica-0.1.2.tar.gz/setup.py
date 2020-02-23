from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(name='numerica',
      version='0.1.2',
      description='Numerical Analysis methods with Python (experimental)',
      url='http://github.com/ramesaliyev/numerica',
      author='Rames Aliyev',
      author_email='creator@ramesaliyev.com',
      license='MIT',
      packages=['numerica'],
      zip_safe=False)