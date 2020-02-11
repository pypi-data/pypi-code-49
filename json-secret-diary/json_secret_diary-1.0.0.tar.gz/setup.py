import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="json_secret_diary", # Replace with your own username
    version="1.0.0",
    author="King Kaito Kid",
    author_email="djstrix@me.com",
    description="Simple secret diary based on JSON and AES encryption",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/KingKaitoKid/secret_diary",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)