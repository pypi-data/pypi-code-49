from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name = "pymyransom",
    version = "0.4.3",
    description = "A Module for Ransomware",
    url = "https://github.com/Huntingbear21/pymyransom",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author = "Huntingbear21",
    author_email = "huntingbear21@naver.com",
    install_requires = ['pycryptodomex'],
    packages = find_packages(exclude=[]),
    keywords = ["pymyransom"],
    python_requires = ">=3.5",
    package_data = {},
    zip_safe = False,
    classifiers = [
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8'
    ],
)