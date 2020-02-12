import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="outliers_101703013_2", # Replace with your own username
    version="0.0.2",
    author="Aayush Singla",
    author_email="singlaaayush0@gmail.com",
    description="Outliers Removal",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/aayush03041/outliers_101703013",
    download_url = 'https://github.com/aayush03041/outliers_101703013/archive/v_01.tar.gz', 
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)
