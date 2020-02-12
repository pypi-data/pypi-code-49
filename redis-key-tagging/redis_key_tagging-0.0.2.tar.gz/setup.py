import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="redis_key_tagging",
    version="0.0.2",
    author="Consortium Érudit",
    author_email="tech@erudit.org",
    description="A Redis client with key tagging and invalidation by tag features.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/erudit/redis_key_tagging",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=[
        'redis>=3.0,<4.0',
    ],
)
