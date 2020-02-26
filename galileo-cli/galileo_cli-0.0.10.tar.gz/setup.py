from setuptools import find_packages, setup

install_requires = [
    "requests>=2.21.0",
    "python-socketio",
    "termcolor==1.1.0",
    "colorama==0.4.3",
    "pyfiglet",
    "click",
    "click-shell",
    "pandas==1.0.1",
    "galileo-sdk==0.0.13",
    "halo"
]

setup(
    name="galileo_cli",
    long_description="Galileo is a hub for modeling, simulations, and data analysis that functions as a quick and "
                     "easy portal to cloud resources.  The application streamlines computing infrastructure, "
                     "saving engineers and researchers weeks of cloud setup time.  Team and station features allow "
                     "teams to collaborate efficiently by sharing projects and results, flexibly controlling "
                     "permissions, and easily tracking their model version histories.\nThe Galileo CLI is an "
                     "application that utilizes the Galileo SDK to view jobs without a GUI",
    author="Hypernet Labs",
    version="0.0.10",
    license="MIT",
    packages=find_packages(),
    entry_points={"console_scripts": ["galileo-cli = galileo_cli.cli:main",]},
    python_requires=">=3.6.7",
    install_requires=install_requires,
    extras_require={"docs": ["sphinx>=2.2.0", "sphinx-material"]},
    setup_requires=["pytest-runner", "black", "isort"],
    tests_require=["pytest", "mock"],
)
