import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="mimosa-monomer",
    version="0.0.7",
    author="Dan Hampton",
    description="CLI for Stilt 2 database.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages("src"),
    package_dir={"": "src"},
    classifiers=[
        "Environment :: Console",
        "Programming Language :: Python :: 3",
        "License :: Other/Proprietary License",
        "Operating System :: OS Independent",
        "Topic :: Database",
        "Topic :: Utilities",
    ],
    python_requires=">=3.6",
    install_requires=[
        "attrs>=19",
        "cutie>=0.2",
        "firebase-admin",
        "halo",
        "typer[all]",
    ],
    entry_points={"console_scripts": ["mimosa=mimosa.main:main"],},
)
