from setuptools import setup


with open('README.md') as f:
    readme = f.read()


setup(name='businessoptics',
      version='0.8.0',
      description='Client for the BusinessOptics API',
      long_description=readme,
      long_description_content_type="text/markdown",
      classifiers=[
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6',
          'Programming Language :: Python :: 3.7',
          'Programming Language :: Python :: 3.8',
      ],
      url='https://github.com/BusinessOptics/businessoptics_client',
      author='BusinessOptics',
      author_email='alex.mojaki@gmail.com',
      license='MIT',
      packages=['businessoptics'],
      install_requires=[
          'requests>=2,<3',
          'future<1',
          'google-api-python-client>=1,<2',
          'oauth2client',
          'boto3',
          'littleutils',
      ],
      tests_require=[
          'pandas',
          'numpy',
          'mock'
      ],
      test_suite='businessoptics.tests',
      include_package_data=True,
      zip_safe=False)
