import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="youtube-unlimited-search",
    version="0.3.2",
    author="Hatem Karim",
    author_email="hatemkarimen@gmail.com",
    description="Allow you to search in youtube without care about requests limitation",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/HatemEng/Youtube_Unlimited_Search",
    packages=["youtube_unlimited_search"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    include_package_data=True,
    install_requires=["requests", "beautifulsoup4"],
    python_requires='>=3.6',
)