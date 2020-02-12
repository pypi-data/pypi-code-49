import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="moonroof",
    version="0.0.1",
    author="Input Logic",
    author_email="adriaan@inputlogic.ca",
    description="Client library for moonroof",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/inputlogic/moonroof-django",
    packages=setuptools.find_packages(),
    classifiers=[
        "Development Status :: 1 - Planning",
        "Framework :: Django",
        "Topic :: System :: Monitoring",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'requests',
    ],
    python_requires='>=3.6',
)
