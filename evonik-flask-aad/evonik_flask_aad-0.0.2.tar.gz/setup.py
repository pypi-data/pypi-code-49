import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="evonik_flask_aad",
    version="0.0.2",
    author="Sven Igl",
    author_email="sven-alexander.igl@evonik.com",
    description="Azure Active Directory Helper for Flask or connexion applications",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://www.evonik.com",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=["python-jose", "six", "flask"]
)
