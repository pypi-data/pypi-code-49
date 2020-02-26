from setuptools import Extension, setup


setup(
    name="cymock",
    author="Nekoka.tt",
    python_requires=">=3.8",
    zip_safe=False,
    include_package_data=True,
    ext_modules=[
        Extension("cymock", ["cymock.c"])
    ],
    version="2020.2.26.2",
)
