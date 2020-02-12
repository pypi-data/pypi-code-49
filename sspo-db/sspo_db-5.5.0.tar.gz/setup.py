from setuptools import setup, find_packages
setup(
    name='sspo_db',  # Required
    version="5.5.0",  # Required
    author="Paulo Sergio dos Santo Junior",
    author_email="paulossjuniort@gmail.com",
    description="A lib to access SSPO DB",
 
    packages=find_packages(),
    
    install_requires=[
        'SQLAlchemy', 'SQLAlchemy-Utils', 'mysql-connector-python', 'factory-boy'
    ],

    classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
    setup_requires=['wheel'],
    
)
