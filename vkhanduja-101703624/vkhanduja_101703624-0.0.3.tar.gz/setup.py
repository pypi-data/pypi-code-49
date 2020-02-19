import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="vkhanduja_101703624", # Replace with your own username
    version="0.0.3",
    author="Vivek Khanduja",
    author_email="vkhanduja28@gmail.com",
    description="Missing Values",
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
         	"vkhanduja_101703624=Missingvalues.missingValuesVivek:removeMissingValues",
	]
    },		
    python_requires='>=3.6',
)