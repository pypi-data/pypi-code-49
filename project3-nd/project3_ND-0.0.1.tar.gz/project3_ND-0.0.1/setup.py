import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="project3_ND",
    version="0.0.1",
    author="Nishant Dhanda",
    author_email="ndhanda_be17@thapar.edu",
    description="Handling missing values in python",
	url='',
	long_description=long_description,
	long_description_content_type="text/markdown",
	packages=setuptools.find_packages(),
	entry_points = {
        'console_scripts': ['HMVcli=hmvlib.hmvcli:main'],
    },
	keywords = ['CLI', 'missing', 'Data', 'HMV'], 
	python_requires='>=2.7', 
)
