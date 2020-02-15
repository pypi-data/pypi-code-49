import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="xlsToCsv", 
    version="0.1.0",
    author="Atul Sharma",
    author_email="atulsharma131@gmail.com",
    description="This script converts excel files to CSV",
    long_description="""
        This script converts excel files to CSV
    """,
    long_description_content_type="text/markdown",
    url="https://github.com/atul-shr/xlsToCsv",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)