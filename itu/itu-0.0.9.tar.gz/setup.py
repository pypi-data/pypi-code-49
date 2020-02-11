import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='itu',
    version='0.0.9',
    author='Ismail Sunni',
    author_email='imajimatika@gmail.com',
    description='Indonesia version of import this.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='http://github.com/ismailsunni/itu',
    license='MIT',
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Education"]
        )
