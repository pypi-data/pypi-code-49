import setuptools

with open("requirements.txt") as f:
    required = f.read().splitlines()

setup = dict(
    name="toy18_uvvis",
    version="0.1",
    author="Julian Kimmig",
    author_email="julian-kimmig@gmx.net",
    description="Toy18 UVVis Detector",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/JulianKimmig/toy18_uvvis",
    include_package_data=True,
    scripts=["toy18_uvvis"],
    install_requires=required,
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
if __name__ == "__main__":
    setuptools.setup(**setup)
