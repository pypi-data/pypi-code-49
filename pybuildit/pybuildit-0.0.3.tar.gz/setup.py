# -*- coding: utf-8 -*-

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pybuildit",
    version="0.0.3",
    author="SR",
    author_email="sr-dev@smartrobotics.jp",
    description="python API for Buildit Actuator",
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=['crc8','numpy','pyserial', 'matplotlib', 'numpy', 'pyyaml'],
    url="https://github.com/Smartrobotics/Buildit",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_data={'pybuildit': ['gui/imgs/*.gif', 'gui/config/*.yml'] },
    entry_points={
        'console_scripts':[
            'builditctl = pybuildit.cli.builditctl:main',
        ],
        'gui_scripts':[
            'builditctl-gui = pybuildit.gui.builditctl:main',
        ],
    },
)
