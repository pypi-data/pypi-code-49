import setuptools
  
# reading long description from file 
with open('README.md', 'r') as file: 
    long_description = file.read() 
   
# calling the setup function  
setuptools.setup(name='contort', 
      version='0.1.2', 
      description='COnTROT (COmprehensive Transcriptomic ORganizational Tool) is a program that will download and organize all expression data in GEO related to a search result, commonly an organism.', 
      long_description=long_description,
      long_description_content_type="text/markdown", 
      url='https://github.com/GLBRC/contort', 
      author='Kevin Myers', 
      author_email='kmyers2@wisc.edu', 
      license='MIT',
      packages=setuptools.find_packages(),
      install_requires=[
              'markdown>=3.1.1',
              'biopython>=1.74',
              'pandas>=0.25.1',
              ],    
      include_package_data=True, 
      entry_points ={
              'console_scripts': [
                     'contort=contort.contort:main'
                     ]
              },
      classifiers=[
              "Programming Language :: Python :: 3.6",
              "Programming Language :: R",
              "License :: OSI Approved :: MIT License",
              "Operating System :: OS Independent",
              "Intended Audience :: Science/Research",
              "Topic :: Scientific/Engineering :: Bio-Informatics",
      ],
    python_requires='>=3.6',
)