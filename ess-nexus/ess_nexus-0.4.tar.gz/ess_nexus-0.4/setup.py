import setuptools

with open("README.md", "r") as fh:

    long_description = fh.read()

setuptools.setup(

     name='ess_nexus',

     version='0.4',

     author='Natalia Milas',

     author_email='natalia.milas@ess.eu',

     license='MIT',

     description='Utility class for saving nexus files on ESS data format',

     long_description='Simple class that creates an hdf5 file according to a predifined format to be used internally at ESS Accelerator division',

     long_description_content_type="text/markdown",

     packages=setuptools.find_packages(),

     classifiers=[

         "Programming Language :: Python :: 3",

         "License :: OSI Approved :: MIT License",

         "Operating System :: OS Independent",

     ],

 )