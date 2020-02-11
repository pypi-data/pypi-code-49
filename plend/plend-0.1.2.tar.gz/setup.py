from setuptools import setup, find_packages


version_dict = {}
exec(open('plend/version.py').read(), version_dict)
VERSION = version_dict['__version__']

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(name='plend',
      version=VERSION,
      desctiption='Python Feed Formulation',
      auhor='Brennen Herbruck',
      author_email='brennen.herbruck@gmail.com',
      license='MIT',
      url='https://github.com/bherbruck/plend',
      install_requires=['PuLP==2.0'],
      packages=['plend', 'plend.presets'],
      python_requires='>=3.6')
