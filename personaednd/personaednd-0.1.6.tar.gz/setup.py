from setuptools import find_packages, setup

from personaednd.version import __version__


setup(
    name="personaednd",
    version=__version__,
    packages=find_packages(),
    package_data={"personaednd": ["sources/*.yml"]},
    url="https://github.com/sg679/personaednd",
    license="MIT",
    author="Marcus T Taylor",
    description="Randomly generates 5th edition Dungeons & Dragons characters.",
    long_description=open("README.md", "r").read(),
    long_description_content_type="text/markdown",
    install_requires=[
        "beautifulsoup4>=4.8",
        "click>=7.0",
        "lxml>=4.4",
        "numpy>=1.17",
        "PyYAML>=5.1",
    ],
    python_requires=">=3.0",
    entry_points={"console_scripts": ["personaednd=personaednd.shell:main"]},
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Topic :: Games/Entertainment :: Role-Playing",
    ],
)
