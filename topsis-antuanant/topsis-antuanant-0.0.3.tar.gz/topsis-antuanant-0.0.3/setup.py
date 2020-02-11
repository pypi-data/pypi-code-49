import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="topsis-antuanant", # Replace with your own username
    version="0.0.3",
    author="Anant",
    author_email="anantchopra95@gmail.com",
    description="Technique for Order Preference by Similarity to Ideal Solution (TOPSIS) originated in the 1980s as a multi-criteria decision making method. TOPSIS chooses the alternative of shortest Euclidean distance from the ideal solution, and greatest distance from the negative-ideal solution",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Anant99-sys/topsis",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)
