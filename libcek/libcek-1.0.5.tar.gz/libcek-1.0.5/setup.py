# Copyright (C) 2018 Aceinna Navigation System Open Source Project
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an "AS IS"
# BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
# or implied. See the License for the specific language governing
# permissions and limitations under the License.

from setuptools import find_packages, setup


setup(
    name="libcek", # Replace with your own username
    version="1.0.5",
    author="cek",
    author_email="erkuo521@126.com",
    description="cek's lib",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/erkuo521/libcek",    
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    # entry_points={
    #     "console_scripts": [
    #         "libcek = libcek.__main__:main",
    #     ]
    # }
)
