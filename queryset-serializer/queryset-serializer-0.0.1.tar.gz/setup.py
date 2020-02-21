import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

base_classes = dict(
    QuerySetSerializer='.serializers'
)
config_class = ''
root_file = 'queryset_serializer'

package_settings = dict(
    name='queryset-serializer',
    version='0.0.1',
    packages=setuptools.find_packages(exclude=['tests*']),
    author="Maurice Benink",
    author_email="MauriceBenink@hotmail.com",
    description="Serializer which will automatically prefetch and bypass lazy calls",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="BSD-3-Clause",
    url="https://github.com/MauriceBenink/queryset_serializer",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=['django', 'djangorestframework'],
)

with open(f'{root_file}/__init__.py','w') as init_file:
    for class_name, location in base_classes.items():
        init_file.write(f'from {location} import {class_name}\n')
    init_file.write('\n')

    init_file.write('__all__ = [\n')
    for class_name, location in base_classes.items():
        init_file.write(f'    "{class_name}",\n')
    init_file.write(']\n')
    init_file.write('\n')

    init_file.write(f'__title__ = "{package_settings["name"]}"\n')
    init_file.write(f'__version__ = "{package_settings["version"]}"\n')
    init_file.write(f'__author__ = "{package_settings["author"]}"\n')
    init_file.write(f'__license__ = "{package_settings["license"]}"\n')
    init_file.write(f'__copyright__ = "Copyright {package_settings["author"]}, All Rights Reserved"\n')
    init_file.write('\n')

    init_file.write(f'VERSION = "{package_settings["version"]}"\n')
    if config_class is None:
        config_class = ''.join([x.capitalize() for x in root_file.split('_') + ['config']])
    if config_class:
        init_file.write(f'default_app_config = "{root_file}.apps.{config_class}"\n')
        init_file.write('\n')

setuptools.setup(**package_settings)
