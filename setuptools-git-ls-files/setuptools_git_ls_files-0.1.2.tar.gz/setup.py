from pkg_resources import DistributionNotFound, load_entry_point, working_set
import setuptools
from shutil import rmtree


ENTRY_GROUP = "setuptools.file_finders"
ENTRY_NAME = "setuptools_git_ls_files"
ENTRY_POINT = ENTRY_NAME + " = setuptools_git_ls_files:find_files"


with open("README.md") as fp:
    long_description = fp.read()


setup_params = dict(
    name="setuptools_git_ls_files",
    url="https://github.com/anthrotype/setuptools_git_ls_files/",
    zip_safe=True,
    author="Cosimo Lupo",
    author_email="cosimo@anthrotype.com",
    description="Use git to list all files, including submodules",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="MIT",
    use_scm_version=True,
    py_modules=["setuptools_git_ls_files"],
    setup_requires=["setuptools-scm"],
    entry_points={ENTRY_GROUP: ENTRY_POINT},
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Version Control",
        "Topic :: System :: Software Distribution",
        "Topic :: Utilities",
    ],
)

# Clean up first, old eggs seem to confuse setuptools_scm
rmtree(setup_params["name"] + ".egg-info", ignore_errors=True)

# Bootstrap
try:
    load_entry_point(setup_params["name"], ENTRY_GROUP, ENTRY_NAME)
except (DistributionNotFound, ImportError):
    working_set.add_entry(".")


if __name__ == "__main__":
    setuptools.setup(**setup_params)
