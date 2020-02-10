from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    # the name must begin with "fsleyes-plugin-"
    name='fsleyes-plugin-roitools',
    version='0.0.4',
    packages=['fsleyes_plugin_roitools'],
    author="Paul Kuntke",
    author_email="paul.kuntke@tu-dresden.de",
    description="FSLeyes plugin to work with ROIs",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://bitbucket.org/gaunab/fsleyes-plugin-roitool",
    # Views, controls, and tools must be exposed
    # as entry points within groups called
    # "fsleyes_views", "fsleyes_controls" and
    # "fsleyes_tools" respectively.
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points={
        'fsleyes_controls': ['ROI-Tools = fsleyes_plugin_roitools:RoiList'],
    }
)
