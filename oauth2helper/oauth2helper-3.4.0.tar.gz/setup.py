import os
from setuptools import setup, find_packages

this_dir = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(this_dir, "README.md"), "r") as f:
    long_description = f.read()

setup(
    name="oauth2helper",
    version=open("oauth2helper/version.py").readlines()[-1].split()[-1].strip("\"'"),
    author="Colin Bounouar",
    author_email="colin.bounouar.dev@gmail.com",
    maintainer="Colin Bounouar",
    maintainer_email="colin.bounouar.dev@gmail.com",
    url="https://colin-b.github.io/oauth2helper/",
    description="Validate and extract information from OAuth2 token.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    download_url="https://pypi.org/project/oauth2helper/",
    license="MIT",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Topic :: Software Development :: Build Tools",
    ],
    keywords=["security", "oauth2", "jwt"],
    packages=find_packages(exclude=["tests*"]),
    install_requires=[
        # Used to retrieve keys
        "requests==2.*",
        # Used to decode tokens
        "pyjwt==1.*",
        # Used to handle certificate
        "cryptography==2.*",
    ],
    extras_require={
        "testing": [
            # Used to mock requests
            "pytest-responses==0.4.*",
            # Used to check coverage
            "pytest-cov==2.*",
            # Used to test starlette specifics
            "starlette==0.13.*",
            "requests==2.*",
        ]
    },
    python_requires=">=3.6",
    project_urls={
        "GitHub": "https://github.com/Colin-b/oauth2helper",
        "Changelog": "https://github.com/Colin-b/oauth2helper/blob/master/CHANGELOG.md",
        "Issues": "https://github.com/Colin-b/oauth2helper/issues",
    },
    platforms=["Windows", "Linux"],
)
