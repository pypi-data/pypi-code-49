'''
rm -rf build/
rm -rf dist/
python3 setup.py sdist bdist_wheel
twine upload --repository-url https://upload.pypi.org/legacy/ dist/*

user: __token__
pwd: pypi-AgEIcHlwaS5vcmcCJDA0NGM2OTA1LTYxNGQtNGYyNC04N2E5LTY3NTIwYjZiNzUwYgACJXsicGVybWlzc2lvbnMiOiAidXNlciIsICJ2ZXJzaW9uIjogMX0AAAYgQML8aZmY247uVBhnFyO2cZZE6VAxwnrol64i0zHNjjY
'''

from setuptools import setup

setup(name='cautil',
      version='2.0',
      description='The UTILITY for Cloud Agnostic',
      url='http://github.com/whirldata/cautil',
      author='Whirldata',
      author_email='info@whirldatascience.com.com',
      license='MIT',
      packages=['cautil'],
      zip_safe=False)