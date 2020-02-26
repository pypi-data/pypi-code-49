import setuptools

try:
    from wheel.bdist_wheel import bdist_wheel as _bdist_wheel
    class bdist_wheel(_bdist_wheel):
        def finalize_options(self):
            _bdist_wheel.finalize_options(self)
            self.root_is_pure = False
except ImportError:
    bdist_wheel = None

setuptools.setup(
    name = 'pipinstall',
    version = '1.0.0',
    url = 'https://github.com/gaming32/pipinstall',
    author = 'Gaming32',
    author_email = 'gaming32i64@gmail.com',
    license = 'License :: OSI Approved :: MIT License',
    description = 'Installs pip packages on all your installed Python versions (Windows only)',
    long_description = open('README.md').read(),
    long_description_content_type = 'text/markdown',
    setup_requires = [
        'pip',
    ],
    scripts = [
        'pipinstall.py',
        'pipuninstall.py',
    ],
    py_modules = [
        'pipinstall',
        'pipuninstall',
    ],
    cmdclass = {'bdist_wheel': bdist_wheel}
)