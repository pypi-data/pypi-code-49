import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="drftypegen",  # Replace with your own username
    version="0.1.6",
    author="Utsob Roy",
    include_package_data=True,
    author_email="roy@codesign.com.bd",
    description="An django app to generate type information for rest_framework.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="Mozilla Public License 2.0 (MPL 2.0)",
    url="https://github.com/pypa/sampleproject",
    packages=setuptools.find_packages(),
    python_requires=">=3.6",
    install_requires=["djangorestframework"],
    classifiers=[
        "Framework :: Django",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
    ],
)
