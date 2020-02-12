import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="info_serie_tv", # Replace with your own username
    version="1.0.0.1",
    author="King Kaito Kid",
    author_email="djstrix@me.com",
    description="SerieTvItaly_bot API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/KingKaitoKid/info_serie_tv",
    packages=setuptools.find_packages(),
    install_requires=["requests"],
    entry_points={
    'console_scripts': [
        'info_serie_tv=info_serie_tv.info_serie_tv:main',
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)