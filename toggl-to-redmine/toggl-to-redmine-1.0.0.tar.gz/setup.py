import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="toggl-to-redmine", # Replace with your own username
    version="1.0.0",
    author="Eduardo Canellas",
    author_email="eduardocanellas@id.uff.br",
    description="Easily import time entries from Toggl to Redmine",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/eduardocanellas/toggl-to-redmine",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)