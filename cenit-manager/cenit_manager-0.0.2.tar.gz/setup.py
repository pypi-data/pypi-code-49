import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="cenit_manager", # Replace with your own username
    version="0.0.2",
    author="richar santiago Muñico Samaniego",
    author_email="granlinux@gmail.com",
    description="Mini Tool for Admin Cenit Account",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/cenit_manager",
    packages=setuptools.find_packages(),
    install_requires=[],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    include_package_data=True,
    python_requires='>=3.5',
    py_modules=["cenit_manager"],
    package_data={},
    data_files=[('Scripts', ['cenit_manager']), ("", ["cenit_manager"])],  # Optional
    entry_points={  # Optional
        'console_scripts': [
            'cenit_manager=cenit_manager:main',
        ],
    },
)
#python setup.py sdist bdist_wheel
#twine upload dist/*
