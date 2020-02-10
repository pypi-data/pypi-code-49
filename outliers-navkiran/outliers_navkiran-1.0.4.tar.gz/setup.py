import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="outliers_navkiran", 
    version="1.0.4",
    author="Navkiran Singh",
    author_email="nsingh2_be17@thapar.edu",
    description="Outlier Removal Using Z-score or IQR",
    url="https://github.com/navkiran/outliers_navkiran",
    long_description=long_description,
    long_description_content_type="text/markdown",
    py_modules=["outliers_navkiran"],
    package_dir={'':'src'},
    keywords = ['command-line', 'Outliers', 'outlier-removal','row-removal'],  
    install_requires=[            
          'numpy',
          'pandas',
      ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    scripts=["bin/outliers_navkiran_cli"],
    python_requires='>=3.6',
)
