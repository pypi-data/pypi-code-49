name = "cricbuzz_py"
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="cricbuzz-py",
    version="0.1.2",
    author="Akshay T",
    author_email="sup.aks.apps@gmail.com",
    description="A package to retrive cricket scores",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/aksty/cricbuzz-py",
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
