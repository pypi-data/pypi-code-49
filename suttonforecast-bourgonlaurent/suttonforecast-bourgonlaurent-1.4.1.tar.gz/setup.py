import setuptools
from suttonforecast import __version__

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="suttonforecast-bourgonlaurent", # Replace with your own username
    version=__version__,
    author="Laurent Bourgon",
    description="A small example package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/BourgonLaurent/TelegramSuttonForecast",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)