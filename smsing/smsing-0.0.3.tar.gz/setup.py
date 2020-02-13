import pathlib
from setuptools import find_packages, setup

HERE = pathlib.Path(__file__).parent

README = (HERE / "README.md").read_text()

setup(
    name="smsing",
    version="0.0.3",
    description="Preprocessing and ML methods for social media",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/roiprez/smsing",
    author="Roi Pérez López",
    author_email="roiprezl@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=find_packages(exclude=["tests", "*.tests", "*.tests.*", "tests.*"]),
    # If your package is a single module, use this instead of 'packages':
    # py_modules=['mypackage'],
    include_package_data=True,
    install_requires=[
        "gensim",
        "scikit-learn",
        "pandas",
        "nltk",
        "spacy",
        "beautifulsoup4",
        "lxml",
    ],
)
