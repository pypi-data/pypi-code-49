import setuptools
with open("README.md", "r") as fh:
    long_description = fh.read()
setuptools.setup(
     name='LindexURI',  
     version='0.1',
     packages=['LindexURI'] ,
     author="Alessio Palma",
     author_email="ozw1z5rd@gmail.com",
     description="Hadoop URI utility",
     long_description=long_description,
     long_description_content_type="text/markdown",
     url="https://github.com/ozw1z5rd/LindexURI.git",
     classifiers=[
         "Programming Language :: Python :: 2",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
 )
