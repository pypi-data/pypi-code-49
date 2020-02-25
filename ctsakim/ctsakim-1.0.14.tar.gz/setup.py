from setuptools import setup

setup(name='ctsakim',
      version='1.0.14',
      description='Cts akim okuma',
      url='https://gitlab.com/ctsyazilim/ctsakim.git',
      author='Soner Akarsu',
      author_email='soner.akarsu@cts.com.tr',
      license='MIT',
      packages = ['ctsakim'],
      scripts=['ctsakim/ctsakim.py'],
      dependency_links  = ['https://github.com/adafruit/Adafruit_Python_GPIO/tarball/master#egg=Adafruit-GPIO-0.6.5'],
      install_requires=[
          'Adafruit-GPIO>=0.6.5',
      ],
      zip_safe=False)