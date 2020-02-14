from setuptools import setup, find_packages
from os import path

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, "README.md"), encoding="utf-8") as readme_md:
    long_description = readme_md.read()

extras_require = {
    "develop": [
        "check-manifest",
        "pytest~=5.2",
        "pytest-cov~=2.8",
        "pytest-console-scripts~=0.2",
        "bumpversion~=0.5",
        "pyflakes",
        "pre-commit",
        "black",
        "twine",
    ],
}
extras_require["complete"] = sorted(set(sum(extras_require.values(), [])))

setup(
    name="pymela",
    version="0.0.1",
    description="Pure-Python Matrix Element Likelihood Analysis",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/scailfin/pyMELA",
    author="Matthew Feickert",
    author_email="matthew.feickert@cern.ch",
    license="Apache",
    keywords="python physics matrix-element",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    include_package_data=True,
    install_requires=["click>=6.0"],
    python_requires=">=3.6",
    extras_require=extras_require,
    entry_points={"console_scripts": ["pymela=pymela.commandline:pymela"]},
)
