import setuptools

with open("README.md", "r") as fh:
	long_description = fh.read()

setuptools.setup(
	name = "nbforms",
	version = "0.5.1",
	author = "Chris Pyles",
	author_email = "cpyles@berkeley.edu",
	description = "Jupyter Notebook forms using ipywidgets",
	long_description = long_description,
	long_description_content_type = "text/markdown",
	url = "https://github.com/chrispyles/nbforms",
	license = "BSD-3-Clause",
	packages = setuptools.find_packages(),
	classifiers = [
		"Programming Language :: Python :: 3",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
	]
)
