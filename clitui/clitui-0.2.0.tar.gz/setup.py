from setuptools import setup
from os import path


def file_README():
    read_path = path.join(path.dirname(path.realpath(__file__)), "README.md")
    with open(read_path) as f:
        return f.read()


setup(
    name="clitui",
    version="0.2.0",
    description="A tool to help make command line drawing easier.",
    long_description=file_README(),
    long_description_content_type="text/markdown",
    url="https://github.com/cowboy8625/CLITUI",
    author="Cowboy8625",
    author_email="cowboy8625@protonmail.com",
    license="Apache License",
    packages=["clitui"],
    scripts=["bin/clitui", "bin/clitui.bat",],
    package_data={
        "clitui": [
            "charsheet.py",
            "curser_control.py",
            "__init__.py",
            "__main__.py",
            "terminal_size.py",
            "displayer.py",
            "font.py",
        ],
    },
    zip_safe=False,
)
