import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="deepface",  
    version="0.0.1",
    author="Sefik Ilkin Serengil",
    author_email="serengil@gmail.com",
    description="Deep Face Recognition Framework",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/serengil/deepface",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.5.5',
    install_requires=["numpy>=1.14.0", "matplotlib>=2.2.2", "opencv-python>=3.4.4", "tensorflow>=1.9.0", "keras>=2.2.0", "gdown>=3.10.1"]
)
