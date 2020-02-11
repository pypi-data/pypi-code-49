import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="python-ffmpeg-video-streaming",
    version="0.0.25",
    author="Amin Yazdanpanah",
    author_email="contact@aminyazdanpanah.com",
    description="Package media content for online streaming(DASH and HLS) using ffmpeg",
    long_description=long_description,
    project_urls={
        "Documentation": "https://video.aminyazdanpanah.com/python",
        "Source": "https://github.com/aminyazdanpanah/python-ffmpeg-video-streaming",
        "Bug Tracker": "https://github.com/aminyazdanpanah/python-ffmpeg-video-streaming/issues",
    },
    keywords='ffmpeg,dash,hls,video,streaming,httplivestreaming,dynamicadaptivestreamingoverhttp,video-streaming',
    long_description_content_type="text/markdown",
    url="https://github.com/aminyazdanpanah/python-ffmpeg-video-streaming",
    packages=setuptools.find_packages(),
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)