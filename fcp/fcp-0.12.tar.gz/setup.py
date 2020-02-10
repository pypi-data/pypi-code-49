from setuptools import setup, find_packages

setup(
    name="fcp",
    description="CAN bus manager",
    version="0.12",
    author="Joao Freitas",
    author_email="joaj.freitas@gmail.com",
    license="GPLv3",
    url="https://github.com/joajfreitas/fcp",
    download_url="https://github.com/joajfreitas/fcp/archive/v0.1.tar.gz",
    packages=find_packages(),
    entry_points={"console_scripts": ["fcp = fcp.__main__:main",],},
    install_requires=["click", "cantools", "PySide2", "jinja2", "ww"],
)
