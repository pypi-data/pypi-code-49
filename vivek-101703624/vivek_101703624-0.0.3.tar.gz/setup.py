import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="vivek_101703624", # Replace with your own username
    version="0.0.3",
    author="Vivek Khanduja",
    author_email="vkhanduja28@gmail.com",
    description="Outliers",
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
         	"vivek_101703624=Project.outliers:main",
	]
    },		
    python_requires='>=3.6',
)