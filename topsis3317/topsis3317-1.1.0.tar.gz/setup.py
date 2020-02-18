from setuptools import setup

def readme():
    with open('README.md') as f:
        README = f.read()
    return README


setup(
    name="topsis3317",
    version="1.1.0",
    description="A Python package for topsis analysis.",
    long_description=readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/manaskhatri/Topsis",
    author="Manas Khatri",
    author_email="manaskhatri4534@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=["TOPSIS_101703317"],
    include_package_data=True,
    install_requires=["requests"],
    entry_points={
        "console_scripts": [
            "TOPSIS_101703317=TOPSIS_101703317.Topsis:main",
        ]
    },
)