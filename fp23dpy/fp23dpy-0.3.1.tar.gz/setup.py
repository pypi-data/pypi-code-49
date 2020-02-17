import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="fp23dpy",
    version="0.3.1",
    author="Adrian Roth",
    author_email="adrian.roth@forbrf.lth.se",
    description="Package for 3D reconstruction of Fringe Patterns captured using the Fringe Projection - Laser Induced Fluorescence technique.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://spray-imaging.com/fp-lif.html",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points = {
            "console_scripts": [
                "fp23d = fp23dpy.__main__:main",
            ]
    },
    install_requires = ['numpy', 'scipy', 'scikit-image', 'matplotlib', 'trimesh'],
    python_requires='>=3.6',
)
