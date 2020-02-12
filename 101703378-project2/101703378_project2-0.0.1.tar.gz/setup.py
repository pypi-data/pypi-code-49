import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="101703378_project2",
    version="0.0.1",
    author="Nitin",
    author_email="nnitin_be17@thapar.edu",
    description="Removing outliers from a pandas dataframe",
	long_description=long_description,
	long_description_content_type="text/markdown",
	packages=setuptools.find_packages(),
	entry_points = {
        'console_scripts': ['Project2=pro2.outcli:main'],
    },
	python_requires='>=2.7', 
)
