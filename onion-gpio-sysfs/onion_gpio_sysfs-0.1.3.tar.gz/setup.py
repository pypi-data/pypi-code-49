import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="onion_gpio_sysfs", # Replace with your own username
    version="0.1.3",
    author="Grizmin",
    author_email="grizmin@gmail.com",
    description="Libraries to control GPIOs using the sysfs interface",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/grizmin/onion-gpio-sysfs",
    package_dir={'': 'python'},
    py_modules=["onionGpio"],
    packages=setuptools.find_packages(where='python'),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8'
    ],
    keywords='onion omega IoT',
    python_requires='>=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, !=3.4.*, <4',
)
