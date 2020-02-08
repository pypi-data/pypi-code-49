import setuptools

setuptools.setup(
    name="gblpyapi",
    version="0.0.9",
    packages= ["glenbotlist"],
    url="https://glenbotlist.xyz",
    license="MIT",
    author="CoderLamar420",
    author_email="gavynlamar@gmail.com",
    description="glenbotlist.xyz API Wrapper in Python",
    long_desciption=open("README.md").read(),
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent"
    ]
)