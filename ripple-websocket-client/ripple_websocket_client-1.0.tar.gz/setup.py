import setuptools

install_requires = ["websocket_client==0.57.0", "pyjwt==1.7.1", "mqtt_codec==1.0.2"]
with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ripple_websocket_client",
    version="1.0",
    author="Zhenyu Han",
    author_email="hanzy@rippleinfo.com",
    description="websocket client connect and message use mqtt",
    long_description=long_description,
    long_description_content_type="text/markdown",
    # url="",
    python_requires='>=3.0.*',
    packages=["ripple_ws_client"],
    install_requires=install_requires,
    # entry_points={
    #     'console_scripts': [
    #         'test_client=test_client:main'
    #     ],
    # },
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)
