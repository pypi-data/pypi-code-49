import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Jepy",
    version="0.1.16.1",
    author="JECO",
    author_email="support@je.zendesk.com",
    description="A simple Python wrapper to access the Johns Eastern Company API.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/JECO/jepy",
    packages=setuptools.find_packages(),
    install_requires=[
          'requests',
      ],
    classifiers=[
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Programming Language :: Python :: 3.7",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.4',
)
