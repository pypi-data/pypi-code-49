name = "jokepy"
import setuptools 

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="jokepy",
    version="0.0.3",
    author="Akshay T",
    author_email="sup.aks.apps@gmail.com",
    description="A package to retrive jokes from https://sv443.net/jokeapi/v2",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/aksty/Jokepy",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'requests',
    ],
    python_requires='>=3.6',
)
