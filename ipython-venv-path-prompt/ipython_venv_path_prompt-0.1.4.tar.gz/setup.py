from setuptools import setup

setup(
    name="ipython_venv_path_prompt",
    version="0.1.4",
    packages=["ipython_venv_path_prompt"],
    license="MIT",
    author="Javier Dehesa",
    author_email="javidcf@gmail.com",
    url="https://github.com/javidcf/ipython_venv_path_prompt",
    description="A simple IPython extension to show the path and virtualenv in the prompt.",
    long_description=open("README.rst").read(),
    keywords="ipython venv virtualenv path cwd prompt",
    install_requires = ['ipython'],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Framework :: IPython",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Topic :: Utilities",
    ],
)
