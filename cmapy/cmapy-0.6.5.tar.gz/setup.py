"""Export colormaps from Matplotlib so they can be used
(for exaple) with OpenCV.

See: https://gitlab.com/cvejarano-oss/cmapy/
"""


from setuptools import setup
import os.path
import io
import re


this_file = os.path.abspath(os.path.dirname(__file__))

# Get the long description from the README file
with io.open(os.path.join(this_file, "README.md"), encoding="utf-8") as f:
    long_description = f.read()


# Get the __version__ string from cmapy.py, as in
# https://packaging.python.org/guides/single-sourcing-package-version/
def find_version(file):
    with open(os.path.join(this_file, file), 'r') as fp:
        version_file = fp.read()

    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")


setup(
    name="cmapy",
    version=find_version("cmapy.py"),
    description="Use Matplotlib colormaps with OpenCV in Python.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://gitlab.com/cvejarano-oss/cmapy/",
    author="Camilo Vejarano",
    license="MIT",
    py_modules=["cmapy"],
    keywords=["colormaps", "opencv"],
    python_requires=">=2.7",
    install_requires=["matplotlib", "numpy", "opencv-python>=3.3"],
    project_urls={"Bug Reports": "https://gitlab.com/cvejarano-oss/cmapy/issues/"},
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research ",
        "Topic :: Multimedia :: Graphics",
        "Topic :: Scientific/Engineering",
        "Topic :: Scientific/Engineering :: Visualization",
    ],
)
