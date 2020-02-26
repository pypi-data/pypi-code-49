import setuptools

with open("./README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="dj-actions",
    version="0.0.2",
    author="Christo Crampton",
    author_email="info@38.co.za",
    description="",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://gitlab.com/schoolorchestration/libs/dj-actions",
    packages=setuptools.find_packages(
        exclude=('example_project', 'example_app',)
    ),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
)