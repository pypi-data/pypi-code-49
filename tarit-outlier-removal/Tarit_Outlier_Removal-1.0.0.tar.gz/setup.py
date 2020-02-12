import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Tarit_Outlier_Removal", 
    version="1.0.0",
    author="Tarit Kandpal",
    author_email="taritkandpal@gmail.com",
    description="Outlier Removal",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=["requests"],
    entry_points={
    	"console_scripts": [
    		"Tarit_Outlier_Removal=package.outliers:main"
    	]
    },
    python_requires='>=3.6',
)