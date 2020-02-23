from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()


setup(
    name="blacken-selection",
    version="0.1.3",
    description="Apply black formatter for a piece of python source code",
    author="Balazs Gibizer",
    author_email="gibizer@gmail.com",
    url="https://github.com/gibizer/blacken_selection",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="Apache License 2.0",
    packages=["blacken_selection"],
    zip_safe=False,
    python_requires=">=3.6",
    install_requires=["black"],
    entry_points={
        "console_scripts": ["blacken-selection=blacken_selection:main"],
    },
)
