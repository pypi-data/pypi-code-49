from distutils.core import setup

name = "sortlog"

setup(
    name=name,
    packages=[name],
    version="1.0.0",
    license="MIT",
    description="Command Line tool to sort log files based on time",
    author="Shiplu Mokaddim",
    author_email="shiplu@mokadd.im",
    url="https://github.com/shiplu/%s" % name,
    entry_points={"console_scripts": ["sortlog=sortlog.cli:main"]},
    keywords=["log", "sort", "merge"],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Topic :: Software Development :: Debuggers",
        "Topic :: System :: Logging",
        "Topic :: Utilities",
    ],
)
