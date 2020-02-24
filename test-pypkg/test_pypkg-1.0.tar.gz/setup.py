import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
   name='test_pypkg',
   version='1.0',
   description='A test python packaging',
   author='Sangram Keshari Sahu',
   author_email='sangram@bionivid.com',
   packages=setuptools.find_packages(),
   install_requires=['numpy', 'pandas'], #external packages as dependencies
   python_requires='>=3.6', 
)