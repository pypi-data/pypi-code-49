from setuptools import setup

def readme():
    with open('README.md') as f:
        README = f.read()
    return README


setup(
    name="topsis101703038",
    version="1.0.2",
    description="A Python package for topsis analysis.",
    long_description=readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/kiliumnatta/Topsis",
    author="Aditya Tomar",
    author_email="aditya65921@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=["TOPSIS101703038"],
    include_package_data=True,
    install_requires=["requests"],
    entry_points={
        "console_scripts": [
            "TOPSIS101703038=TOPSIS101703038.Topsis:do_work",
        ]
    },
)