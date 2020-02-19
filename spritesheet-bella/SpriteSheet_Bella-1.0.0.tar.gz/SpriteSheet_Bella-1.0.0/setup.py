import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

__name__ = 'SpriteSheet_Bella'
__author__ = 'Nhung LAI'
__email__ = 'nhungbella0511@gmail.com'
__version__ = '1.0.0'
__copyright__ = "Copyright (C) 2019, Intek Institute"
__credits__ = "Intek Institute"
__maintainer__ = "Nhung LAI"

setuptools.setup(
    name=__name__,
    author=__author__,
    author_email=__email__,
    maintainer=__maintainer__,
    version=__version__,
    copyright=__copyright__,
    credits=__credits__,
    long_description=long_description,
    packages=setuptools.find_packages(),
    install_requires=[
        'pipenv',
        'Python>=3.7',
        'Numpy',
        'Pillow'
    ],
    python_requires='>=3.7',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],

)
