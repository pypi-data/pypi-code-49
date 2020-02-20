import platform
from setuptools import find_packages, setup

install_requires = [
    "requests>=2.21.0",
    "python-socketio",
    "termcolor",
    "pyfiglet",
    "click",
    "click-shell",
    "pandas==1.0.1",
    "galileo-sdk==0.0.13",
]

# if platform.system() == "Windows":
#     install_requires.extend(["click-shell[windows]", "pyreadline"])
# else:
#     install_requires.extend(["click-shell[readline]", "gnureadline"])

setup(
    name="galileo_cli",
    version="0.0.6",
    license="MIT",
    packages=find_packages(),
    entry_points={"console_scripts": ["galileo-cli = galileo_cli.cli:main",]},
    python_requires=">=3.6.7",
    install_requires=install_requires,
    extras_require={"docs": ["sphinx>=2.2.0", "sphinx-material"]},
    setup_requires=["pytest-runner", "black", "isort"],
    tests_require=["pytest", "mock"],
)
