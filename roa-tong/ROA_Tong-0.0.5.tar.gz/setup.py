import setuptools

with open("README.md", "r") as fh:
  long_description = fh.read()

setuptools.setup(
  name="ROA_Tong",
  version="0.0.5",
  author="Tong Wu",
  author_email="tongwu@wustl.edu",
  description="Generating Rectangluar Occlusion Attacks",
  long_description= "See Defending against Physically Realizable Attacks on Image Classification",
  long_description_content_type="text/markdown",
  url="https://tongwu2020.github.io/tongwu/",
  packages=setuptools.find_packages(),
  classifiers=[
  "Programming Language :: Python :: 3",
#  "License :: OSI Approved :: MIT License",
  "Operating System :: OS Independent",
  ],
)