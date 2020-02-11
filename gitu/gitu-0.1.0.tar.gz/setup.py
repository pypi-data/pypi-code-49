import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="gitu",
    version="0.1.0",
    author="Howyoung Zhou",
    author_email="howyoungzhou@yahoo.com",
    description="Account manager for git users with multiple accounts.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/HowyoungZhou/gitu",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points={
        "console_scripts": [
            "gitu = gitu.__main__:main"
        ]
    },
    python_requires='>=3.5',
)
