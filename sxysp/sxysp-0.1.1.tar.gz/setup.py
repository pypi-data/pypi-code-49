from setuptools import setup, find_packages

VERSION = '0.1.1'

setup(name='sxysp',
      version=VERSION,
      description='SXYSP Cli Toolbox',
      long_description='SXYSP Cli Toolbox',
      classifiers=[],
      keywords='sxysp',
      author='sunxyw',
      author_email='xy2496419818@gmail.com',
      url='https://github.com/xxx',
      license='MIT',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=True,
      install_requires=[
          'Click',
          'PyYAML',
          'Requests',
          'Speedtest-cli'
      ],
      python_requires='>=2.7, <4',
      entry_points={
          'console_scripts': [
              'sxysp = index:cli'
          ]
      })
