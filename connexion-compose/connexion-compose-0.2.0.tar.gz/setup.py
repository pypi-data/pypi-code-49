import re
from setuptools import find_packages, setup


def read_requirements(req_file):
    return [l for l in re.sub(r"\s*#.*\n", "\n", req_file.read()).splitlines() if l]


with open("requirements/base.txt") as f:
    REQUIREMENTS = read_requirements(f)

with open("requirements/test.txt") as f:
    TEST_REQUIREMENTS = read_requirements(f)

with open("README.md") as f:
    LONG_DESCRIPTION = f.read()

setup(
    name="connexion-compose",
    version="0.2.0",
    description="Create Connexion schema composed from several files in a nested directory structure.",
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    url="https://gitlab.com/jsmesami/connexion-compose",
    author="Ondřej Nejedlý",
    author_email="jsmesami@gmail.com",
    license="MIT",
    packages=find_packages(),
    python_requires=">=3.6",
    install_requires=REQUIREMENTS,
    tests_require=TEST_REQUIREMENTS,
    include_package_data=True,
    keywords="connexion swagger schema compose",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
)
