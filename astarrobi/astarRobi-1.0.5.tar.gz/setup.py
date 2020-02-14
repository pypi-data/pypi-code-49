import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="astarRobi", # Replace with your own username
    version="1.0.5",
    author="Md Robiuddin",
    author_email="mrrobi040@hotmail.com",
    description="A package for A* Search Algorithm",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Mrrobi/astarSearch",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
