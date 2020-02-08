import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Image-Terminals",
    version="2.0.1",
    author="amr a.el latief",
    author_email="amrabdellatief1@gmail.com",
    description="You could use it in your python Image processing project to do basic Calculations on Image pixels",
    long_description="Python Class used on Basic Operations on Image as Getting red Component of Image, or green component ,it gets dx,dy,dxx,dyy of each pixel of image too ,and many other operations",
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/Terminals",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)