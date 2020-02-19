import sphinx_bootstrap_theme

# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
import parse_cmake.parsing as cmp
#sys.path.insert(0, os.path.abspath('.'))
sys.path.insert(0, os.path.abspath('../topoly'))


def topoly_version():
    # Read CMakeLists and extract version
    with open("../CMakeLists.txt", "r") as myfile:
        data = myfile.readlines()
    res = cmp.parse("".join(data))
    for cmd in res:
        if str(type(cmd)).find("Command")>0 and cmd.name.upper() == 'SET' and cmd.body[0].contents=='CPACK_PACKAGE_VERSION':
            return cmd.body[1].contents.strip().replace('"', '')

# -- Project information -----------------------------------------------------
version = topoly_version()
project = 'Topoly'
copyright = '2020, University of Warsaw, Interdisciplinary Laboratory of Biological Systems Modeling'
author = 'Paweł Dąbrowski-Tumański, Wanda Niemyska, Bartosz Greń, Paweł Rubach, Joanna Sulkowska'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.mathjax',
    'sphinx.ext.autodoc',
    'sphinx.ext.doctest',
    'sphinx.ext.napoleon',
    'sphinx.ext.intersphinx',
    'sphinx.ext.todo',
    'sphinx.ext.imgmath',
    'sphinx.ext.ifconfig',
    'sphinx.ext.viewcode',
    'sphinx.ext.inheritance_diagram',
]

# source_suffix = ['.rst', '.md']
source_suffix = ['.rst', '.md', '.txt']

# The master toctree document.
master_doc = 'index'

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['build', '_skbuild', 'Thumbs.db', '.DS_Store']


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
#html_theme = 'alabaster'
#html_theme = 'sphinxdoc'
html_theme = 'bootstrap'
html_theme_path = sphinx_bootstrap_theme.get_html_theme_path()

htmlhelp_basename = 'Topolydoc'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

pygments_style = 'sphinx'

todo_include_todos = True

autodoc_member_order = 'bysource'
