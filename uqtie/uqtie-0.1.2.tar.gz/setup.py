import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="uqtie",
    version="0.1.2",
    author="Nik Langrind",
    author_email="langrind@gmail.com",
    description="Utilities for small or throwaway PyQt5 applications",
    license='MIT',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/langrind/uqtie",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    scripts=['example/simple_uqtie.py'],
)
