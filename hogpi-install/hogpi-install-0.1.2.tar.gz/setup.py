import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="hogpi-install",  # Replace with your own username
    version="0.1.2",
    author="Jack Whitehorn",
    author_email="jackwh.whitehorn@gmail.com",
    description="The official tech4nature installer",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=['click==7.0', 'PyInquirer==1.0.3'],
    python_requires='>=3.6',
    py_modules=['main'],
    entry_points='''
        [console_scripts]
        hogpi-install=main:cli
    ''',
)
set
