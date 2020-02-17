from setuptools import setup

def readme():
    with open('README.md') as f:
        README = f.read()
    return README


setup(
    name="test_topsis",
    version="1.0.0",
    description="A Python package to implement Topsis",
    long_description=readme(),
    long_description_content_type="text/markdown",
    author="Rajat Verma",
    author_email="rajatv864@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=["script"],
    include_package_data=True,
    install_requires=["numpy", "pandas"],
    entry_points={
        "console_scripts": [
            "test_topsis=script.cli:main",
        ]
    },
)