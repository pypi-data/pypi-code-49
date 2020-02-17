import setuptools

# with open("README.md", "r") as f:
#     long_description = f.read()


setuptools.setup(
    name="neuralsalience",
    version="0.0.1",
    author="Maixent Chenebaux",
    author_email="max.chbx@gmail.com",
    description="Embeddings ponderation scheme, freely adapted from the paper : 'Learning Neural Word Salience Scores' https://arxiv.org/pdf/1709.01186.pdf",
    url="https://github.com/kerighan/neuralsalience",
    packages=setuptools.find_packages(),
    include_package_data=True,
    install_requires=["keras", "numpy"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.5"
)
