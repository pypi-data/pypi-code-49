import setuptools

def long_description():
    with open('README.md') as f:
        return f.read()

setuptools.setup(
        name = 'pyven',
        version = '16',
        description = 'Management of PYTHONPATH for simultaneous dev of multiple projects',
        long_description = long_description(),
        long_description_content_type = 'text/markdown',
        url = 'https://github.com/combatopera/pyven',
        author = 'Andrzej Cichocki',
        packages = setuptools.find_packages(),
        py_modules = ['tasks', 'initopt', 'travis_ci', 'tests', 'runtests', 'pkg_resources_lite'],
        install_requires = ['twine', 'aridity'],
        package_data = {'': ['*.pxd', '*.pyx', '*.pyxbld', '*.arid', '*.aridt']},
        scripts = ['bootstrap', 'foreignsyms'],
        entry_points = {'console_scripts': ['initopt=initopt:main_initopt', 'tests=runtests:main_tests', 'tasks=tasks:main_tasks', 'travis_ci=travis_ci:main_travis_ci', 'gclean=pyvenimpl.gclean:main_gclean', 'release=pyvenimpl.release:main_release']})
