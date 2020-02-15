import setuptools
import sqlite3
with open("README.md", "r") as fh:
    long_description = fh.read()
def get_name():
    conn = sqlite3.connect(".setupinfo.db3")
    c = conn.cursor()
    c.execute(f'SELECT name FROM info')
    c=c.fetchone()
    return str(c[0])
def get_version():
    conn = sqlite3.connect(".setupinfo.db3")
    c = conn.cursor()
    c.execute(f'SELECT version FROM info')
    c=c.fetchone()
    return str(c[0])
setuptools.setup(
    name=get_name(),
    version=get_version(),
    author="pyslow_riding",
    author_email="slowridingytb@gmail.com",
    description="console line tool to add function to be independent!",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)