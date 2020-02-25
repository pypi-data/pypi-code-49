import setuptools


with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
    name="ScriptorQL",
    version="0.0.3",
    author="Arne Goossens",
    author_email="FortuneCandy99@gmail.com",
    description=("Generates SQL insert values script for data"),
    license="GNU GENERAL PUBLIC LICENSE Version 3",
    keywords="Generate SQL insert values script",
    packages=setuptools.find_packages(),
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/FortuneCandy/ScriptorQL",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent"
    ],
)
