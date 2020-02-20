import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="tex2txt",
    version="1.6.9",
    author="Matthias Baumann",
    description="A flexible LaTeX filter",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/matze-dd/Tex2txt",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
        "Topic :: Text Processing :: Markup :: LaTeX",
        "Topic :: Text Processing :: Filters",
    ],
)
