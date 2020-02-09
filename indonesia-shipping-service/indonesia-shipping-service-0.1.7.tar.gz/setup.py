import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="indonesia-shipping-service",
    version="0.1.7",
    author="ramdani muksin",
    author_email="ramd4ni@gmail.com",
    description="Indonesia Shipping Service",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/xhijack/indonesia-shipping-service",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)