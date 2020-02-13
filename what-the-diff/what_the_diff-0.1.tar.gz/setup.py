from setuptools import setup

setup(name='what_the_diff',
      version='0.1',
      description='Unix diff implementation in python',
      url='http://github.com/hskang9/what_the_diff',
      author='Hyungsuk Kang',
      author_email='hskang9@gmail.com',
      license='MIT',
      packages=['what_the_diff'],
      zip_safe=False,
      install_requires=[
          'termcolor',
          'nltk'
      ],
      long_description_content_type="text/markdown",
      long_description=open('./README.md').read())
