import setuptools

setuptools.setup(
    name = 'ejcli',
    version = '1.3.0',
    description = 'A testing system console client',
    long_description = open('README.md').read(),
    long_description_content_type = 'text/markdown',
    packages = setuptools.find_packages(),
    entry_points = {
        'console_scripts': ['ejcli = ejcli.__main__:_']
    }
)
