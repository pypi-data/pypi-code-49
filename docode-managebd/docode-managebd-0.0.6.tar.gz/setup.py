import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="docode-managebd", # Replace with your own username
    version="0.0.6",
    author="DoCode",
    author_email="mario@docode.com.mx : elias@docode.com.mx",
    description="libreria para el manejo de base de datos",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/DoCodeSoft/docode-managebd",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Framework :: Django",
        "Programming Language :: Python :: 3",
    ],
    python_requires='>=3.6',
)