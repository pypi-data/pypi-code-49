import setuptools
with open("README.md", "r") as fh:
    long_description = fh.read()
setuptools.setup(
     name='kMeansBCMAssessment-cwildenb',
     version='0.3',
     scripts=['kMeansBCMAssessment'] ,
     author="Chelsey Wildenborg",
     author_email="wildenborgchelsey@gmail.com",
     description="A Kmeans implementation using only NumPy",
     long_description=long_description,
   long_description_content_type="text/markdown",
     url="https://github.com/cwilden/kMeans/blob/master/kMeans.py",
     packages=setuptools.find_packages(),
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
 )