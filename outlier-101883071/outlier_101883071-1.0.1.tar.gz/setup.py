from setuptools import setup

def readme():
    with open('README.md') as f:
        README = f.read()
    return README


setup(
    name="outlier_101883071",
    version="1.0.1",
    description="Python package to remove outliers from dataset",
    long_description=readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/",
    author="Yogesh",
    author_email="ysingla001@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=["outlier_101883071"],
    include_package_data=True,
    install_requires=[],
    entry_points={
        "console_scripts": [
            "outlier_101883071=outlier_101883071.__init__:main",
        ]
    },
)
