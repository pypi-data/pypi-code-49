from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="fa-common",
    description="FastAPI Common Framework",
    long_description=long_description,
    long_description_content_type="text/markdown",
    version="0.2.3",
    packages=["fa_common"],
    maintainer="Samuel Bradley",
    maintainer_email="sam.bradley@csiro.au",
    python_requires=">=3.5, <4",
    install_requires=[
        "pyjwt",
        "python-jose",
        "python-dotenv",
        "loguru",
        "python-multipart",
        "email-validator",
        "six",
        "fastapi",
        "aiohttp",
        "ujson",
    ],
    extras_require={
        "sentry": ["sentry_sdk"],
        "mongo": ["motor", "pymongo"],
        "gcp": [
            "google-cloud-storage",
            "google-cloud-logging",
            "firebase-admin",
            "requests",
        ],
        "minio": ["minio"],
        "windows": ["win32-setctime"],
    },
    include_package_data=True,
    license="MIT",
    url="https://gitlab.com/csiro-geoanalytics/python-shared/fastapi-common-framework",
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        "Development Status :: 4 - Beta",
        # Indicate who your project is intended for
        "Intended Audience :: Science/Research",
        # Pick your license as you wish (should match "license" above)
        "License :: OSI Approved :: MIT License",
        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
)
