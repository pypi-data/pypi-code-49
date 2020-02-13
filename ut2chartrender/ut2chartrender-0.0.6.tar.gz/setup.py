import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ut2chartrender",
    version="0.0.6",
    author="JC",
    author_email="jencat@ex.ua",
    description="Library that takes as input config and datasets for highcharts, and outputs SVG image of rendered "
                "chart",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://gitlab.com/jc4ut/renderer",
    packages=setuptools.find_packages(),
    install_requires=[
        "wheel==0.33.6",
        "python-highcharts==0.4.2",
        "selenium==3.141.0",
        "beautifulsoup4==4.8.2"
    ],
    python_requires=">=3.7",
)
