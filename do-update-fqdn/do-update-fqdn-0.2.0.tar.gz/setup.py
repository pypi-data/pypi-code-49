import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="do-update-fqdn",
    version="0.2.0",
    author="Aljoscha Vollmerhaus",
    author_email='pydev@aljoscha.vollmerhaus.net',
    description="Update or create a dns record through the DigitalOcean API.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/avollmerhaus/do-update-fqdn",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX :: Linux",
        "Environment :: Console"
    ],
    packages=setuptools.find_packages('src'),
    package_dir={'': 'src'},
    entry_points={
        'console_scripts': ['do-update-fqdn = do_update_fqdn.do_update_fqdn:cli_interface'],
    },
)
