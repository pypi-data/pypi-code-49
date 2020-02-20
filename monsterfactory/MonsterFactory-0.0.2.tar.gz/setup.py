from setuptools import setup


with open("README.md", "r") as f:
    long_description = f.read()

dev_status = {
    "Planning": "Development Status :: 1 - Planning",
    "Pre": "Development Status :: 2 - Pre-Alpha",
    "Alpha": "Development Status :: 3 - Alpha",
    "Beta": "Development Status :: 4 - Beta",
    "Pro": "Development Status :: 5 - Production/Stable",
    "Mature": "Development Status :: 6 - Mature",
    "Inactive": "Development Status :: 7 - Inactive",
}

setup(
    name="MonsterFactory",
    packages=["MonsterFactory"],
    install_requires=['Fortuna'],
    author="Robert Sharp",
    author_email="webmaster@sharpdesigndigital.com",
    version="0.0.2",
    description="D&D Monster Generator",
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        dev_status["Alpha"],
        "Programming Language :: Python :: 3.8",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    keywords=[
    ],
    python_requires='>=3.6',
)
