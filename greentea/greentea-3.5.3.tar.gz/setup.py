"""Information of greentea."""
from setuptools import setup, find_packages


setup(name='greentea',
      version="3.5.3",
      description=(
          'A microframework for abstraction.'),
      python_requires='>=3.7.0',
      url='https://github.com/nryotaro/greentea',
      author='Nakamura, Ryotaro',
      author_email='nakamura.ryotaro.kzs@gmail.com',
      license='MIT License',
      classifiers=['Programming Language :: Python :: 3.7'],
      packages=find_packages(exclude=["tests", "tests.*"]),
      install_requires=[
      ],
      extras_require={
          'test': [
              'pytest'
          ],
          'dev': [
              'ipython',
              'python-language-server[all]'
          ],
          'doc': [
              'sphinx',
              'sphinx_rtd_theme']})
