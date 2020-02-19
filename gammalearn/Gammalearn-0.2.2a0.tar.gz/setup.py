import setuptools

# with open("README.rst", "r") as fh:
#     long_description = fh.read()

exec(open('gammalearn/version.py').read())

setuptools.setup(
    name="Gammalearn",
    version=__version__,
    author="M. Jacquemont, T. Vuillaume",
    author_email="jacquemont@lapp.in2p3.fr",
    description="A framework to easily train deep learning model on Imaging Atmospheric Cherenkov Telescopes data",
    # long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://gitlab.lapp.in2p3.fr/GammaLearn/GammaLearn",
    install_requires=[
        "torch>=1.2",
        "tensorboard",
        "torchvision",
        "numpy",
        "tensorboardx",
        "matplotlib",
        "tables",
        "sphinxcontrib-katex",
        "pytorch-ignite",
        "indexedconv",
        "ctapipe",
        "ctaplot",
        ""

    ],
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    license='MIT',
    entry_points={
        'console_scripts': {
            'gammalearn = gammalearn.experiment_runner:main',
            'gexplore-net = gammalearn.explore_trained_net_features:main',
        }
    },
    include_package_data=True,
    package_data={'': ['data/camera_parameters.h5', 'data/nice_lst.npy', 'tests/lapp_cleaning.h5']},

)
