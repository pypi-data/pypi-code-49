from setuptools import setup
from setuptools_rust import Binding, RustExtension


long_description = '\n\n'.join([
    open('README.rst').read(),
    open('CHANGES.rst').read(),
])


setup(
    name="pyruvate",
    version="0.1.0",
    description="WSGI server written in Rust.",
    long_description=long_description,
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: WSGI",
    ],
    keywords='plone named file image blob',
    author='tschorr',
    author_email='t_schorr@gmx.de',
    url='https://gitlab.com/tschorr/pyruvate',
    rust_extensions=[
        RustExtension(
            "pyruvate.pyruvate",
            binding=Binding.PyO3,
            debug=False,
            native=True)],
    packages=["pyruvate"],
    # rust extensions are not zip safe, just like C-extensions.
    zip_safe=False,
    install_requires=[
        'Paste',
    ],
    entry_points={
        'paste.server_runner': [
            'main=pyruvate:serve_paste',
        ],
    },
)
