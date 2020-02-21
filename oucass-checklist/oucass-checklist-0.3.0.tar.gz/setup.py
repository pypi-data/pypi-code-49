import setuptools

# If the package is being updated (and not installed for the first time),
# save user-defined data.
try:
    import checklist
    update = True
except ModuleNotFoundError:
    update = False

if update:
    import os
    import pickle
    dir = os.path.join(os.path.dirname(checklist.__file__), 'user_settings')
    files = {}
    for file in os.listdir(dir):
        if ".pkl" in file:
            files[file] = pickle.load(open(os.path.join(dir, file), "rb"))

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="oucass-checklist",
    version="0.3.0",
    author="Jessica Blunt, Brian Greene",
    author_email="cass@ou.edu",
    description="Program to manage safety checks and create metadata files compatible with oucass-profiles in the field",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/oucass/Checklist",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    entry_points='''
        [console_scripts]
        checklist=checklist.checklist:cli
    ''',
    install_requires=["click"],
    python_requires='>=3.7',
    package_data={"checklist":["user_settings/*.pkl"]},
    include_package_data=True,
)

if update:
    for key in files:
        pickle.dump(files[key], open(os.path.join(dir, key), "wb"))
