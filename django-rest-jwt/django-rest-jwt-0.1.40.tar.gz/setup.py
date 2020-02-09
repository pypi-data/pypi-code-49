from setuptools import setup, find_packages

# Get the long description from the README file
with open('README.md', 'r') as f:
    long_description = f.read()


setup(
    name='django-rest-jwt',
    version='0.1.40',
    description='simple jwt handling for django REST Framework',
    author='Pythux',
    # author_email='',
    # packages=['drf_jwt'],  # same as name, change '⁻' to '_'
    packages=find_packages(),
    # install_requires=[],  # external packages as dependencies

    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Pythux/drf-jwt",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)

# install in dev mode:
# pip install --editable .
