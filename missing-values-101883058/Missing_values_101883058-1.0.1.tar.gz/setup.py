from setuptools import setup

def readme():
    with open('README.md') as f:
        README = f.read()
    return README


setup(
    name="Missing_values_101883058",
    version="1.0.1",
    description="Replacing missing values in the dataset with the mean of that particular column using SimpleImputer class.",
    long_description=readme(),
    long_description_content_type="text/markdown",
    author="Pritpal Singh Pruthi",
    author_email="psp.ps001@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
        "Programming Language :: Python :: 3.7",
    ],
    packages=["missing_python"],
    include_package_data=True,
    install_requires=["numpy","pandas"],
    entry_points={
        "console_scripts": [
            "missing_values=missing_python.missing_values:main"]},
)
