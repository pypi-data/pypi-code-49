import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="kstoolbox", # Replace with your own username
    version="0.0.2",
    author="Rian Touchent",
    author_email="riantouchent@gmail.com",
    description="Small toolbox for AI Hackathon",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Rian-T/kstoolbox",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
