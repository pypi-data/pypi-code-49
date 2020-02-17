from setuptools import setup, find_packages
import acsecure as app

with open('README.md', 'r') as f:
  long_description = f.read()


setup(
  name='django-acsecure',
  version=app.__version__,
  description='django access secure middleware',
  long_description=long_description,
  author='Xin Jin',
  author_email='opposcript@gmail.com',
  license='MIT',
  platforms=['OS Independent'],
  keywords='django, log, anti-spam',
  url='https://www.logsecure.io',
  python_requires='>=3.6',
  packages=find_packages(),
  install_requires=[
    'requests>=2.22.0',
  ],
)