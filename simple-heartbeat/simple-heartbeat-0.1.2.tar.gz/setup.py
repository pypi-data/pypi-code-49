import re

from setuptools import setup


def read_file(name):
    with open(name) as fd:
        return fd.read()


def find_metadata(metadata_name, file_name):
    file_data = read_file(file_name)
    regex_pattern = r"^__{}__ = (['\"])([^'\"]*)\1".format(metadata_name)
    if metadata_name is "doc":
        regex_pattern = r"(\"\"\")([\s\S]*?)\1"
    file_match = re.search(
        regex_pattern,
        file_data,
        re.M | re.I
    )
    if file_match:
        return file_match.group(2)
    raise RuntimeError("Unable to find metadata string for {}.".format(metadata_name))


setup(
    name="simple-heartbeat",
    version=find_metadata("version", "./heartbeat.py"),
    author=find_metadata("author", "./heartbeat.py"),
    author_email=find_metadata("email", "./heartbeat.py"),
    description=find_metadata("doc", "./heartbeat.py"),
    url=find_metadata("url", "./heartbeat.py"),
    keywords="heartbeat, monitoring",
    license='MIT',
    py_modules=['heartbeat'],
    install_requires=read_file('requirements.txt').splitlines(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        'Operating System :: OS Independent',
        "Programming Language :: Python",
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Topic :: Software Development',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    long_description=read_file('README.md'),
    long_description_content_type="text/markdown"
)
