# Version is automatically set from git
# More details here : https://pypi.org/project/setuptools-scm/

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="assistant_lib", 
    author="Fritz",
    author_email="fritz.smh@gmail.com",
    description="The Assistant python library",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://gitlab.com/goassistant/assistant-client-python",
    
    # Version from git
    use_scm_version=True,
    setup_requires=['setuptools_scm'],

    # Requirements
    install_requires=[
        "python-json-logger",
    ],
    
    # Commands available from $PATH
    #entry_points = {
    #},
    
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)

