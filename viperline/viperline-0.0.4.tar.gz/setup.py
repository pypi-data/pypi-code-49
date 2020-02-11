import setuptools

setuptools.setup(
    name="viperline",
    version="0.0.4",
    author="Eduardo J. Velasco",
    author_email="velasco810@gmail.com",
    description="Build performant and resilient data pipelines",
    long_description="Build performant and resilient data pipelines",
    long_description_content_type="text/markdown",
    url="https://github.com/ejvelasco/viperline",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)