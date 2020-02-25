import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="gd-kafka",
    version="0.0.3",
    author="Rishabh Garg",
    author_email="rishabh@greendeck.co",
    description="Greendeck Kafka Package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
    packages=['gd_kafka', 'gd_kafka.src', 'gd_kafka.src.kafka'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'kafka-python', 'tqdm'
    ],
    include_package_data=True,
    zip_safe=False
)
