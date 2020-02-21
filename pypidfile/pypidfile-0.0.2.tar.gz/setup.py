from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
      name='pypidfile',
      version='0.0.2',
      url='https://github.com/pietrogiuffrida/pypidfile/',
      author='Pietro Giuffrida',
      author_email='pietro.giuffri@gmail.com',
      license='MIT',
      packages=['pypidfile'],
      zip_safe=False,
      install_requires=["psutil>=5.7.0"],
      classifiers=[
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent",
      ],
      description='Pid file management',
      long_description=long_description,
      long_description_content_type='text/markdown',
)
