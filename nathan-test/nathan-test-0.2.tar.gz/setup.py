from setuptools import setup

setup(name='nathan-test',
      version='0.2',
      description='Haze generation',
      author='Nitin Ware',
      author_email='nitinware@gmail.com',
      packages=['amaze', 'amaze.demo'],
      entry_points={
            'console_scripts': [
                  'amaze_demo=amaze.demo.tkdemo:main'
            ]
      },
    )

__author__= 'Nitin Ware'

