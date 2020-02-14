import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="topsis-naveen",
    version="1.3",
    author="Naveen Budhwal",
    author_email="nbudhwal_be17@thapar.edu",
    description="A package used to implement topsis functionality",
    long_description=long_description,
    long_description_content_type="text/markdown",
    py_modules=["topsis_naveen"],
    package_dir={'':'src'},
    entry_points = {
        'console_scripts': ['topsis_naveen=topsis_naveen:main'],
    },
    install_requires=[            
          'numpy',
          'pandas',
      ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)