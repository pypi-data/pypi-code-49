import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="image_Proc_SHR", # Replace with your own username
    version="0.0.6",
    author="Syed Hamza Rafique",
    author_email="hamzah_shah@hotmail.com",
    description="convolution package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="",
    packages=setuptools.find_packages(),
    classifiers=[],
    python_requires='>=3.6',
)