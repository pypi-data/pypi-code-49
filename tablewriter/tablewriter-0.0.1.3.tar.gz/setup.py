import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="tablewriter",
    version="0.0.1.3",
    author="cottephi",
    author_email="cottephi@gmail.com",
    description="latex table generator",
    long_description=long_description,
    long_description_content_type='text/markdown',
    url="https://gitlab.com/cottephi/latextablegenerator",
    py_modules=["tablewriter"],
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "Operating System :: Unix",
    ],
)

