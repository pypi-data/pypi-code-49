from setuptools import setup

def readme():
    with open('README.md') as f:
        README = f.read()
    return README


setup(
    name="missing-101703139",
    version="1.0.2",
    description="A Python package to handle missing data.",
    long_description=readme(),
    long_description_content_type="text/markdown",
    url="",
    author="Bharat Chauhan",
    author_email="bharatchauhan752000@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=["missing_101703139"],
    include_package_data=True,
    install_requires=["pandas"],
    entry_points={
        "console_scripts": [
            "missing-101703139=missing_101703139.missing:main",
        ]
    },
)