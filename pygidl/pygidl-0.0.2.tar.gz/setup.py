import os
import setuptools


PACKAGE_NAME = "pygidl"


def get_long_description() -> str:
    """Read long description from README.md file."""
    with open("README.md", "r") as readme_file:
        long_description = readme_file.read()
    return long_description


def get_package_version() -> str:
    """Extract version information from package."""
    version = {}
    with open(os.path.join("src", PACKAGE_NAME, "version.py")) as version_file:
        exec(version_file.read(), version)
    return version["__version__"]


setuptools.setup(
    name=PACKAGE_NAME,
    version=get_package_version(),
    author="Cameron Carpenter",
    author_email="parameter.concern@gmail.com",
    description="Asynchronously download Google Images search results",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    url="https://github.com/parameter-concern/pygidl",
    download_url="https://github.com/parameter-concern/pygidl/releases/",
    project_urls={
        "Bug Tracker": "https://github.com/parameter-concern/pygidl/issues/",
        "Source Code": "https://github.com/parameter-concern/pygidl/",
    },
    license="MIT",
    packages=[PACKAGE_NAME],
    package_dir={"": "src"},
    include_package_data=True,
    install_requires=[
        "aiohttp[speedups]",
        "beautifulsoup4",
        "python-slugify[unidecode]",
        "tqdm",
    ],
    setup_requires=["pytest-runner"],
    tests_require=["pytest", "pytest-mock", "pytest-cov", "pylint", "black"],
    entry_points={
        "console_scripts": [f"{PACKAGE_NAME}={PACKAGE_NAME}.__main__:main"]
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: MIT License",
    ],
    python_requires=">=3.7",
)
