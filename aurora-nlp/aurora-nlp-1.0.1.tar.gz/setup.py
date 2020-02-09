import setuptools

with open("README.md", "r") as rm:
    long_description = rm.read()
setuptools.setup(
    name="aurora-nlp",
    version="1.0.1",
    author="Nga Vu",
    author_email="ngavu28091994@gmail.com",
    description="A small lib for reprocessing text",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.5',
    keywords="aurora"

)
