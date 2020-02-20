import setuptools

with open("README.md", "r") as f:
    long_desc = f.read()

setuptools.setup(
    name="vhlsrs", # Replace with your own username
    version="0.0.20",
    author="Luc Forget",
    author_email="luc.forget@insa-lyon.fr",
    description="Package to automate the synthesis of vivado HLS components",
    long_description=long_desc,
    long_description_content_type="text/markdown",
    url="https://gitlab.inria.fr/lforget/vhls_rs",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=['plumbum>=1.6'],
)
