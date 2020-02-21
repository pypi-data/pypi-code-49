import os
import setuptools

with open(os.path.join(os.path.dirname(__file__), "README.md"), "rt") as fh:
    long_description = fh.read()

test_requires = [
    "pytest>=4.6",
    "pytest-cov",
    "pylint>=1.6.5",
    "pycodestyle",
]

setuptools.setup(
    name="diraccfg",
    use_scm_version=True,
    author="Federico Stagni",
    description="DIRAC cfg files reader",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/DIRACGrid/cfg",
    packages=setuptools.find_packages("src"),
    package_dir={"": "src"},
    license="GPL-3.0-only",
    test_suite="tests",
    setup_requires=["setuptools_scm"],
    install_requires=[],
    extras_require={
        'testing': test_requires,
    },
    entry_points={
        'console_scripts': ['diraccfg=diraccfg.__main__:parseArgs'],
    },
    classifiers=[
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    python_requires=">=2.7,!=3.0.*,!=3.1.*,!=3.2.*,!=3.3.*,!=3.4.*",
)
