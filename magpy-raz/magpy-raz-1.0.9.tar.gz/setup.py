import setuptools

# Increase version number
with open("version.txt", "r") as vf:
    current_version = vf.read()
    major, minor, patch = current_version.split('.')

with open("version.txt", "w") as vf:
    # Major Release
    # major = int(major) + 1
    # minor = 0
    # patch = 0

    # Minor Release
    # minor = int(minor) + 1
    # patch = 0

    # Patch Release
    patch = int(patch) + 1

    current_version = f'{major}.{minor}.{patch}'
    vf.write(current_version)

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="magpy-raz",
    version=current_version,
    author="Raz Nitzan",
    author_email="raz.nitzan@gmail.com",
    description="Extract project data from GitLab",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://gitlab.com/Razinka/magpy",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
