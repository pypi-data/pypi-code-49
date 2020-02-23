import os, setuptools


def copy_dir():
    dir_path = '/Users/benjamindaghir1/Documents/eduroam-pi/dist/mail'
    base_dir = os.path.join('', dir_path)
    for (dirpath, dirnames, files) in os.walk(base_dir):
        for f in files:
            yield os.path.join(dirpath.split('/', 1)[1], f)


with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
    name="eduroam-pi",
    version="0.5.0",
    author="Benjamin Ryan Daghir",
    author_email="daghirb@gmail.com",
    description="Networking package to connect to enterprise eduroam and obtain"
                + "IP for ssh connection.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.5',
    entry_points = {
        'console_scripts': ['eduroam-config=eduroam_config.entry_point:main'],
    }
)
