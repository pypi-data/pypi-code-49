import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="missing_data_navkiran", 
    version="1.0.4",
    author="Navkiran Singh",
    author_email="nsingh2_be17@thapar.edu",
    description="Handle Missing Data By Either Dropping Rows/Columns, Forward/Backward Filling or Imputing with Mean, Median or Mode",
    url="https://github.com/navkiran/Missing_data_navkiran.git",
    long_description=long_description,
    long_description_content_type="text/markdown",
    py_modules=["missing_data_navkiran","missing_data_navkiran_cli"],
    package_dir={'':'src'},
    entry_points = {
        'console_scripts': ['missing_data_navkiran_cli=missing_data_navkiran_cli:main'],
    },
    keywords = ['command-line', 'Missing-Data'],  
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
