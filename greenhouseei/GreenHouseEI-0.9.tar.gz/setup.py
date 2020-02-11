import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="GreenHouseEI",
    version="0.9",
    author="Zhenghui Su, Yifeng Yu, Yinchao He, Phillip Nguyen, Collin Cornman",
    long_description = long_description,
    long_description_content_type='text/markdown',
    author_email="zsu@huskers.unl.edu",
    description="unzip compressed files that contain plant images, and covert the images into numpy arrays",
    url="https://github.com/cseseniordesign/plant-phenotyping/tree/master/greenhouseEI",
    license='APACHE2.0',
    packages=setuptools.find_packages(),
    zip_safe=True	
 
)