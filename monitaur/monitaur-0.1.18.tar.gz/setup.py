import io
import os

from setuptools import find_packages, setup

from monitaur import __version__


# Package meta-data.
NAME = "monitaur"
DESCRIPTION = "Monitaur Client Library"
EMAIL = "michael@monitaur.ai"
AUTHOR = "Michael Herman"
REQUIRES_PYTHON = ">=3.6, <3.8"
VERSION = __version__

# Which packages are required for this module to be executed?
REQUIRED = [
    "boto3>=1.10.45",
    "dill>=0.3.1.1",
    "requests>=2.22.0",
    "numpy>=1.18.1",
    "joblib>=0.14.1",
]

# The rest you shouldn't have to touch too much :)

here = os.path.abspath(os.path.dirname(__file__))

# Import the README and HISTORY, combine them, use the results as the long-description.
# Note: this will only work if 'README.md' and 'HISTORY.md' are present in your MANIFEST.in file!
try:
    with io.open(os.path.join(here, "README.md"), encoding="utf-8") as readme_file:
        readme = readme_file.read()

    with io.open(os.path.join(here, "HISTORY.md"), encoding="utf-8") as history_file:
        history = history_file.read()
    long_description = readme + "\n\n" + history
except FileNotFoundError:
    long_description = DESCRIPTION

# Load the package's __version__.py module as a dictionary.
about = {}
if not VERSION:
    project_slug = NAME.lower().replace("-", "_").replace(" ", "_")
    with open(os.path.join(here,  project_slug, "__version__.py")) as f:
        exec(f.read(), about)
else:
    about["__version__"] = VERSION


# Where the magic happens:
setup(
    name=NAME,
    version=about["__version__"],
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type="text/markdown",
    author=AUTHOR,
    author_email=EMAIL,
    python_requires=REQUIRES_PYTHON,
    packages=find_packages(exclude=["tests", "_example"]),
    install_requires=REQUIRED,
    include_package_data=True,
    license="MIT",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",  # https://pypi.org/classifiers/
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
    setup_requires=["wheel"],
)
