import setuptools
with open("README.md", "r") as fh:
    long_description = fh.read()
    
setuptools.setup(
     name='ObjTerm',  
     version='0.9',
     author="Craig Hickman",
     author_email="craig.hickman@ukaea.uk",
     description="A interactive terminal to call methods on python objects",
     long_description=long_description,
     long_description_content_type="text/markdown",
     url="https://gitlab.com/craigukaea/objterm",
     packages=setuptools.find_packages(),
     install_requires=['PyInquirer'],
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ]
 )
