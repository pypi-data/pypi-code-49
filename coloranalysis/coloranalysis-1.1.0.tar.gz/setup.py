import setuptools


with open('README.md') as f:
    README = f.read()

setuptools.setup(
    author="Sravya Sree Dhulipala",
    author_email="shravs.15feb@gmail.com",
    name='coloranalysis',
    license="MIT",
    description='coloranalysis is a package for calculating area of one or more colors in an image, provided the HEX codes.',
    version='v1.1.0',
    long_description=README,
    url='https://github.com/sravyadhulipala/coloranalysis',
    packages=setuptools.find_packages(),
    python_requires=">=3.5",
    install_requires=['requests'],
    classifiers=[
        # Trove classifiers
        # (https://pypi.python.org/pypi?%3Aaction=list_classifiers)
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Intended Audience :: Developers',
    ],
)