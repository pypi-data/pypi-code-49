import setuptools
from numpy.distutils.core import setup, Extension

# python3 -m pip install --user --upgrade setuptools wheel
# rm -rf build && rm -rf dist && rm -rf *.info
# python3 setup.py sdist bdist_wheel
# python3 -m twine upload --repository-url https://upload.pypi.org/legacy/ dist/*

################################################################################

def setup_package():
    """
    """

    setup(
        name="gematria",
        version="0.0.1",
        author="James Montgomery",
        author_email="jamesoneillmontgomery@gmail.com",
        packages=setuptools.find_packages()
    )

if __name__ == "__main__":
    setup_package()
