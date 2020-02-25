from setuptools import setup, find_packages

setup(name='instrumess',
      version='0.2.0',
      description='Instrument drivers for PhDs in Photonics',
      keywords='photonics measurement instrument automation',
      author='Rastko Pajković',
      author_email='r.pajkovic@tue.nl',
      classifiers=[
          'Development Status :: 3 - Alpha',
          'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
          'Programming Language :: Python :: 3.7',
          'Topic :: Scientific/Engineering :: Human Machine Interfaces',
      ],
      url='https://gitlab.tue.nl/20171304/instrumess.git',
      license='AGNU3',
      packages=find_packages(),
      install_requires=[
          'pyvisa',
          'pandas',
          'pathlib',
      ],
      zip_safe=False)
