from distutils.core import setup

setup(name='ctsakim',
      version='1.0.3',
      description='Cts akim okuma',
      url='https://gitlab.com/ctsyazilim/ctsakim.git',
      author='Soner Akarsu',
      author_email='soner.akarsu@cts.com.tr',
      license='MPLv2',
      packages=['projects'],
      scripts=['projects/akim.py'])