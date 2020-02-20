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
    name = "tgp",
    version = "0.0.1",
    author = "Kieran Wood",
    author_email = "kieran@canadiancoding.ca",
    description = "A platform for building terminal games",
    #TODO: Uncomment on first release; long_description = get_content("README.md", "CHANGELOG.md"),
    long_description = get_content("README.md"),
    long_description_content_type = "text/markdown",
    url = "https://github.com/cli-games/launcher",
    include_package_data = True,
    packages = setuptools.find_packages(),
    # entry_points = { 
    #        'console_scripts': [' tgp= ...']
    #    },

    install_requires = [
    "docopt", # Used for argument parsing
      ],
    extras_require = {
        "dev" : ["nox",    # Used to run automated processes
                 "pytest", # Used to run the test code in the tests directory
                 "mkdocs", # Used to create HTML versions of the markdown docs in the docs directory
                 "mkdocs-bootstrap386"],
    },
    classifiers = [
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "Development Status :: 1 - Planning",
    ],
)