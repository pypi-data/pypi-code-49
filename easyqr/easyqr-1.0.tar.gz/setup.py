import setuptools

with open("readme.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="easyqr", # Replace with your own username
    version="1.0",
    author="Mr.right",
    author_email="1003582810@qq.com",
    description="QR code conversion tool",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://gitee.com/Rt_hum/Easyqr",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        'lxml',
        'requests',
        'requests_toolbelt',
    ]
)