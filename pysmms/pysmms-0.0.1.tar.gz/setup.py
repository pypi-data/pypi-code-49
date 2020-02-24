import setuptools


with open("README.md", "r") as f:
    long_description = f.read()


setuptools.setup(
    name="pysmms",
    version="0.0.1",
    author="Jianxun",
    author_email="i@lijianxun.top",
    description="The CLI Tool for SM.MS, based on API v2.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/alpha87/pysmms",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        "requests",
        "pyperclip",
        "terminaltables"
    ],
    entry_points={
        'console_scripts': [
            'pysmms=pysmms.pysmms:app',
        ],
    }
)