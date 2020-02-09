import setuptools
 
with open("README.md", "r") as fh:
    long_description = fh.read()
 
setuptools.setup(
    #Here is the module name.
    name="NumFunc",
 
    #version of the module
    version="1.0.0",
 
    #Name of Author
    author="Roop Sai Pavan Tej Pendyala",
 
    #your Email address
    author_email="roopsai84@gmail.com",
 
    #Small Description about module
    description="Computations on Numbers",
 
    long_description=long_description,
 
    #Specifying that we are using markdown file for description
    long_description_content_type="text/markdown",
 
    #Any link to reach this module, if you have any webpage or github profile
    url="https://github.com/RoopSai-PavanTej/NumberFunctions",
    packages=setuptools.find_packages(),
 
    #classifiers like program is suitable for python3, just leave as it is.
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
