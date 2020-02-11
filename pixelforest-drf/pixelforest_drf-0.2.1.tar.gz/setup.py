import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(name='pixelforest_drf',
                 version='0.2.1',
                 description='A compilation of the applications we often use in addition to Django Rest Framework',
                 long_description=long_description,
                 long_description_content_type="text/markdown",
                 url='https://bitbucket.org/pixelforest/pixelforest_drf/',
                 author='PixelForest Dev Team',
                 author_email="devteam@pixelforest.io",
                 packages=setuptools.find_packages(exclude=['*test*']),
                 include_package_data=True,
                 classifiers=[
                     "Development Status :: 2 - Pre-Alpha",
                     "Framework :: Django :: 2.2",
                     "Framework :: Django :: 3.0",
                     "Programming Language :: Python :: 3",
                     "Programming Language :: Python :: 3.5",
                     "Programming Language :: Python :: 3.6",
                     "Programming Language :: Python :: 3.7",
                     "Programming Language :: Python :: 3.8",
                     "Programming Language :: Python :: 3 :: Only",
                     "License :: OSI Approved :: MIT License",
                     "Operating System :: OS Independent",
                 ],
                 python_requires='>=3.5',
                 )
