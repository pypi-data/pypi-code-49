from setuptools import setup, find_packages

dependencies = ["requests>=2.22.0", "beautifulsoup4>=4.4.0"]


def read_version(module_name):
    from re import match, S
    from os.path import join, dirname

    f = open(join(dirname(__file__), module_name, "__init__.py"))
    return match(r".*__version__ = (\"|')(.*?)('|\")", f.read(), S).group(2)


setup(
    name="linkpreview",
    version=read_version("linkpreview"),
    author="MeyT",
    install_requires=dependencies,
    packages=find_packages(),
)
