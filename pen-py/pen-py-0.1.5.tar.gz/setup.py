from setuptools import setup, find_packages

setup(name='pen-py',
    version='0.1.5',
    description='Penbox utils for python',
    url='http://github.com/storborg/funniest',
    author='Chris Castan',
    author_email='chris@penbox.io',
    license='MIT',
    packages=find_packages(),
    install_requires=['dotmap>=1.3'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        ],
    python_requires='>=3.6',
    zip_safe=False
)