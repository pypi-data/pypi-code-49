import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="amap_poi", # Replace with your own username
    version="0.0.2",
    author="liangyali",
    author_email="me@liangyali.com",
    description="高德地图POI导出",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/liangyali/amap-poi",
    packages=setuptools.find_packages(),
    classifiers=[
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    python_requires='>=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, !=3.4.*',
    scripts=['bin/amap-poi'],
)