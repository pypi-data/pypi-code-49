from setuptools import setup, find_packages


with open("README.md", "r") as fh:
    long_description = fh.read()


setup(
    name="salt-os10",
    version="0.0.2",
    description="Small salt module providing os10.managed, to apply basic config on dell OS10 switches",
    author="Maximilien Cuony",
    author_email="maximilien.cuony@arcanite.ch",
    url='https://github.com/ArcaniteSolutions/salt-os10',
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires='sh',
    license="MPL",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)",
        "Operating System :: Other OS",
        "Programming Language :: Python",
        "Topic :: System :: Networking",
    ],
    entry_points='''
    [salt.loader]
    states_dirs = salt_os10.loader:states_dirs
    '''
)
