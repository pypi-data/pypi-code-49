from setuptools import setup, find_packages

setup(
    name='knight-bus',
    version='0.0.1',
    description=(
        'Transport your python objects from one computer to another!'
    ),
    long_description="This project is like knight bus in HP that can **safely** and **losslessly** transport "
                     "your python objects from one computer to another. \n\n"
                     "It operates on internet but no middleman is able to read the python objects due to its "
                     "asymmetric signature and encryption mechanism. ",
    author='loopyme',
    author_email='peter@mail.loopy.tech',
    license='MIT License',
    packages=find_packages(),
    url='https://github.com/loopyme/knight-bus',
    install_requires=[
        'loopyCryptor>=0.1.1',
    ]
)
