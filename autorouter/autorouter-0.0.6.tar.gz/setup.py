import setuptools

setuptools.setup(
    name="autorouter",
    version="0.0.6",
    author="svinerus",
    author_email="svinerus@gmail.com",
    description="small client-server url router",
    long_description="small client-server url router",
    long_description_content_type="text/markdown",
    url="https://github.com/svinerus/autorouter",
    packages=setuptools.find_packages(),
    install_requires=['websockets'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
