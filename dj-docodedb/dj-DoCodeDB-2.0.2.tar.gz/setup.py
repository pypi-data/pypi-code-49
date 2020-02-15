import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    long_description=long_description,
    long_description_content_type="text/markdown",
)

# CONFIGURAICON BASE
# with open("README.md", "r") as fh:
#     long_description = fh.read()

# setuptools.setup(
#     name="dj-DoCodeDB", # Replace with your own username
#     version="0.4",
#     author="DoCode",
#     author_email="mario@docode.com.mx : elias@docode.com.mx",
#     description="App for manage Data Base",
#     long_description=long_description,
#     long_description_content_type="text/markdown",
#     url="https://www.docode.com.mx/",
#     packages=setuptools.find_packages(),
#     classifiers=[
#         "Programming Language :: Python :: 3",
#         "License :: OSI Approved :: MIT License",
#         "Operating System :: OS Independent",
#         "Framework :: Django",
#         "Programming Language :: Python :: 3",
#     ],
#     python_requires='>=3.6',
# )