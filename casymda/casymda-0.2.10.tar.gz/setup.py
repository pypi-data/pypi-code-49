"""setuptools setup"""

from setuptools import find_packages, setup

VERSION = "0.2.10"

setup(
    name="casymda",
    url="",
    author="FFC",
    author_email="fladdi.mir@gmx.de",
    packages=find_packages("src"),
    package_dir={"": "src"},
    package_data={"casymda.visualization.state_icons": ["*.png"]},
    version=VERSION,
    install_requires=["simpy", "xmltodict", "Pillow", "gym", "black", "networkx"],
    zip_safe=False,
    license="MIT",
    description="A simple DES modeling and simulation environment"
    + " based on simpy, camunda modeler, and tkinter / pixi.js;"
    + " easy to be coupled to a gym-compatible RL agent;"
    + " simulation and animation of tilemap-based movements possible",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
    ],
)
