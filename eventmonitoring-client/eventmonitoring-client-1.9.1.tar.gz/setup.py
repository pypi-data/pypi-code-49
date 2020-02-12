from setuptools import setup, find_packages
from event_monitoring import __version__

setup(
    name="eventmonitoring-client",
    version=__version__,
    packages=find_packages(),
    install_requires=["requests>=2.18.2", "zappa>=0.47.1"],
)
