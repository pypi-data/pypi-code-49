import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="outlier_101703382", 
    version="1.0.0",
    author="Paras Arora",
    author_email="parora_be17@thapar.edu",
    description="Outlier Removal Using Z-score or IQR",
    long_description=long_description,
    long_description_content_type="text/markdown",
    py_modules=["outlier_101703382"],
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
    scripts=["bin/outliers_cli"],
    python_requires='>=3.6',
)
