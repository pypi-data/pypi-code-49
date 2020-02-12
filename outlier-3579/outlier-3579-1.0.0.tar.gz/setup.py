import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="outlier-3579", # Replace with your own username
    version="1.0.0",
    author="Tanishq Chopra",
    author_email="tanishqtc1980@gmail.com",
    description="Topsis package in Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=" ",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=["requests"],
    entry_points={
	"console_scripts": [
		"outlier-3579 = Package.outliers:main",
	]
    },
    python_requires='>=3.5',
)