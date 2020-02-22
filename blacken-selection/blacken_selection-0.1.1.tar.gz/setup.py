from setuptools import setup

with open("requirements.txt") as f:
    requirements = f.read().splitlines()


setup(
    name="blacken_selection",
    version="0.1.1",
    description="Apply black formatter for a piece of python source code",
    url="",
    author="Balazs Gibizer",
    author_email="gibizer@gmail.com",
    home_page="https://github.com/gibizer/blacken_selection",
    description_file="README.md",
    license="Apache License 2.0",
    packages=["blacken_selection"],
    zip_safe=False,
    python_requires=">=3.6",
    install_requires=requirements,
    entry_points={
        "console_scripts": ["blacken_selection=blacken_selection:main"],
    },
)
