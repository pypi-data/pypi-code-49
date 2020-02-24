import setuptools

def long_description():
    with open('README.md') as f:
        return f.read()

setuptools.setup(
        name = 'aridity',
        version = '15',
        description = 'DRY config and template system',
        long_description = long_description(),
        long_description_content_type = 'text/markdown',
        url = 'https://github.com/combatopera/aridity',
        author = 'Andrzej Cichocki',
        packages = setuptools.find_packages(),
        py_modules = ['arid_config', 'aridity', 'processtemplate'],
        install_requires = ['pyparsing'],
        package_data = {'': ['*.pxd', '*.pyx', '*.pyxbld', '*.arid', '*.aridt']},
        scripts = ['arid-config'],
        entry_points = {'console_scripts': ['arid_config=arid_config:main_arid_config', 'aridity=aridity:main_aridity', 'processtemplate=processtemplate:main_processtemplate']})
