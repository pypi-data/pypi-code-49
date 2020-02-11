"""
Description:
    Contains all the configuration for the package on pip
"""
import setuptools

def get_content(*filename):
    """ Gets the content of a file and returns it as a string
    Args:
        filename(str): Name of file to pull content from
    Returns:
        str: Content from file
    """
    content = ""
    for file in filename:
        with open(file, "r") as full_description:
            content += full_description.read()
    return content

setuptools.setup(
    name = "ahd",
    version = "0.4.0",
    author = "Kieran Wood",
    author_email = "kieran@canadiancoding.ca",
    description = "Create ad-hoc commands to be dispatched in their own namespace.",
    long_description = get_content("README.md", "CHANGELOG.md"),
    long_description_content_type = "text/markdown",
    project_urls = {
        "User Docs" :      "https://ahd.readthedocs.io/en/latest/",
        "API Docs"  :      "https://kieranwood.ca/ahd",
        "Source" :         "https://github.com/Descent098/ahd",
        "Bug Report":      "https://github.com/Descent098/ahd/issues/new?assignees=Descent098&labels=bug&template=bug_report.md&title=%5BBUG%5D",
        "Feature Request": "https://github.com/Descent098/ahd/issues/new?assignees=Descent098&labels=enhancement&template=feature_request.md&title=%5BFeature%5D",
        "Roadmap":         "https://github.com/Descent098/ahd/projects/1"
    },
    include_package_data = True,
    packages = setuptools.find_packages(),
    entry_points = { 
           'console_scripts': ['ahd = ahd.cli:main']
       },
    install_requires = [
    "docopt", # Used for argument parsing
    "colored" # Used to color terminal output
      ],
    extras_require = {
        "dev" : ["nox",    # Used to run automated processes
                 "pytest", # Used to run the test code in the tests directory
                 "mkdocs", # Used to create HTML versions of the markdown docs in the docs directory
                 "pdoc3"], # Used for building API documentation

    },
    classifiers = [
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "Development Status :: 4 - Beta"
    ],
)
