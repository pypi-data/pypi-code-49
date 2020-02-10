import setuptools

with open("README.md", "r", encoding="UTF-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="NucDetect",
    version="0.11.14",
    description=("Module to identify intranuclear proteins on basis of "
                 "fluorescence images."),
    author="Romano Weiss",
    url="https://github.com/SilMon/NucDetect",
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Programming Language :: Python :: 3.7"
    ],
    include_package_data=True,
    packages=setuptools.find_packages(),
    install_requires=[
        "tensorflow>=2.0"
        "scipy>=0.11",
        "numpy>=1.13.3",
        "scikit-image>=0.15",
        "matplotlib>=3.0.2",
        "pyqt5>=5.11.3",
        "numba>=0.45.1",
        "pillow",
        "qtawesome",
        "piexif>=1.1.2",
    ]
)
