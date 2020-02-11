import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="matchup-ir",
    version="0.0.2",
    author="Marcos Pontes",
    author_email="marcos.rezende@aluno.ufop.com",
    description="A IR simple library",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/marcosfpr/match_up_lib",
    packages=setuptools.find_packages(exclude=['tests']),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)