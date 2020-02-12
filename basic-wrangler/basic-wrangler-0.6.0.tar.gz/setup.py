import setuptools

setuptools.setup(
    name="basic-wrangler",  # Replace with your own username
    version="0.6.0",
    author="pahandav",
    author_email="34494459+pahandav@users.noreply.github.com",
    description="A BASIC program listing line renumberer/cruncher (aka, a minifier).",
    long_description_content_type="text/markdown",
    url="https://github.com/pahandav/basic-wrangler",
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    package_data={"": ["*.yaml", "*.ico", "*.png"]},
    classifiers=[
        "Development Status :: 4 - Beta",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "Programming Language :: Basic",
        "Topic :: Software Development :: Build Tools",
        "Topic :: Software Development :: Pre-processors",
    ],
    keywords="basic cruncher development",
    project_urls={
        "Documentation": "https://github.com/pahandav/basic-wrangler/blob/master/docs/Manual.asc",
        "Source": "https://github.com/pahandav/basic-wrangler",
        "Issue Tracker": "https://github.com/pahandav/basic-wrangler/issues",
        "Release Thread": "https://atariage.com/forums/topic/297649-basic-wrangler-a-line-cruncherrenumberer/",
        "Blog": "https://oldschoolbasic.blogspot.com/",
    },
    install_requires=["pyperclip", "Gooey", "PyYAML", "duallog"],
    python_requires=">=3.6",
    entry_points={"console_scripts": ["bw = basicwrangler.basicwrangler:main",],},
    long_description=""" # BASIC Wrangler
## Purpose

The purpose of BASIC Wrangler is to allow you to write BASIC programs using labels in a dialect-agnostic way. It also combines and crunches lines to take up the least amount of space on output, thus saving you memory. It is designed to be able to work with almost any dialect of line numbered BASIC.

## Installation

To install with pip, type:

```Batchfile
pip install basic-wrangler
```

## Basic Usage

To load the GUI, type `bw` (a harmless console window might open up behind the main window -- ignore it). Type `bw -h` for CLI help. For more, download [the PDF Manual zip file at the release page](https://github.com/pahandav/basic-wrangler/releases).

## Getting Support

If you have any issues, you can either report them at [the GitHub Issues Tracker](https://github.com/pahandav/basic-wrangler/issues) or you can report them at [the AtariAge Release thread](https://atariage.com/forums/topic/297649-basic-wrangler-a-line-cruncherrenumberer/). There might also be useful information at [my blog](https://oldschoolbasic.blogspot.com/).

## Attribution

Program icon based on an icon made by [Retinaicons](http://www.flaticon.com/authors/retinaicons) from [www.flaticon.com](http://www.flaticon.com).
 """,
)
