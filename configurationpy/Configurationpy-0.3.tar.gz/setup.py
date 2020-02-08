import setuptools

setuptools.setup (
    name='Configurationpy',
    version='0.3',
    description='A cool module for configuration, port of Conf.rb, my other library: https://rubygems.org/gems/confrb',
    author = "Gurjus Bhasin",
    packages = setuptools.find_packages(),
    author_email="gsbhasin84@gmail.com",
    install_requires = ['pyyaml'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires = '>=3.0',
    url = 'https://gitlab.com/Gsbhasin84/configurationpy',
    license = ("MIT"),
    long_description = "# Configurationpy\nConfigurationpy is a small module for configuration. Docs, code examples, etc should be available on https://gitlab.com/Gsbhasin84/configurationpy",
    long_description_content_type = 'text/markdown'
)
