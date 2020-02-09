from setuptools import setup, find_namespace_packages

setup(name='enjoyml',
      version='0.2.6',
      description='',
      url='https://github.com/ByMyTry/enjoyml.git',
      author='anton-taleckij',
      author_email='anton.taleckij.job@gmail.com',
      license='MIT',
      packages=find_namespace_packages(include=['enjoyml.*']),
      install_requires=[
          'numpy',
          'pandas',
          'scikit-learn',
      ],
      zip_safe=False)
