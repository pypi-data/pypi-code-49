import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="onion_gpio_sysfs", # Replace with your own username
    version="0.1.1",
    author="OnionIoT",
    author_email="grizmin@gmail.com",
    description="Libraries to control GPIOs using the sysfs interface",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/grizmin/onion-gpio-sysfs",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.5',
)
