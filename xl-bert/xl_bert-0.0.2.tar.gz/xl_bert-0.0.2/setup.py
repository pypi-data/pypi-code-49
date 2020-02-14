import setuptools


with open('README.md') as f:
    README = f.read()

setuptools.setup(
    author="shivam Panwar",
    author_email="panwar.shivam199@gmail.com",
    name='xl_bert',
    license="MIT",
    description='This lets you find sentence embedding using word embedding from XLNet and Bert',
    version='v0.0.2',
    long_description=README,
    url='https://github.com/Shivampanwar/xl_bert',
    packages=setuptools.find_packages(),
    python_requires=">=3.5",
    install_requires=['torch','transformers','keras'],
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