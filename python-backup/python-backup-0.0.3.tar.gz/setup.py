import setuptools

with open("README.md", 'r') as f:
    long_description = f.read()

with open("requirements.txt", 'r') as f:
    install_requires = list(f.read().splitlines())

setuptools.setup(
    name="python-backup",
    version_format='{tag}.{commitcount}',
    author="Nathaniel van Diepen",
    author_email="python-backup@eeems.email",
    description="Configuration file based file backup",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://eeems.codes/Eeems/python-backup",
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Intended Audience :: Information Technology",
        "Intended Audience :: End Users/Desktop",
        "Natural Language :: English",
        "Topic :: System :: Archiving :: Backup"
    ],
    entry_points={
        'console_scripts': ['backup=backup.command_line:main'],
    },
    python_requires='>=3.6.9',
    packages=setuptools.find_packages(),
    setup_requires=['setuptools-git-version'],
    install_requires=install_requires
)
