import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="outlier-naveen",
    version="1.1",
    author="Naveen Budhwal",
    author_email="nbudhwal_be17@thapar.edu",
    description="Package for outlier removal",
    long_description=long_description,
    long_description_content_type="text/markdown",
    py_modules=["outlier_naveen"],
    package_dir={'':'src'},
    entry_points = {
        'console_scripts': ['outlier_naveen=outlier_naveen:main'],
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