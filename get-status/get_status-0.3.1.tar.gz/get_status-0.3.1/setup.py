import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="get_status",
    version="0.3.1",
    author="voltis",
    author_email="voltis.discord@gmail.com",
    description="A service that allows you to get the status of any website",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/v0ltis/Get_Status",
    packages=setuptools.find_packages(),
    install_requires=['requests'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
      keywords='python website status code',
    python_requires='>=3.6',
)
