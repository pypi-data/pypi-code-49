# -*- coding: utf-8 -*-

import os
import re
import subprocess
import sys


def _git_url():
    try:
        with open(os.devnull, "wb") as devnull:
            out = subprocess.check_output(
                ["git", "remote", "get-url", "origin"],
                cwd=".",
                universal_newlines=True,
                stderr=devnull,
            )
        return out.strip()
    except subprocess.CalledProcessError:
        # git returned error, we are not in a git repo
        return "TODO"
    except OSError:
        # git command not found, probably
        return "TODO"


s3_bucket = "tag_images_for_google_drive".replace('_', '-')
# For git clone ...
git_url = _git_url()
# Project home
home_url = re.sub(r".*@(.*):(.*).git", r"http://\1/\2", _git_url())

sys.path.insert(0, os.path.abspath('..'))

extensions = [
    'sphinx.ext.autodoc',
    # 'sphinx.ext.coverage',
    'sphinx.ext.githubpages',
    'sphinx.ext.ifconfig',
    'sphinx.ext.mathjax',
    'sphinx.ext.napoleon',
    'sphinx.ext.todo',
    'sphinx.ext.viewcode',

    'sphinx.ext.autosectionlabel',
    'recommonmark',
]
autosectionlabel_prefix_document = True

templates_path = ['_templates']

master_doc = 'index'

project = 'tag_images_for_google_drive'

version = subprocess.Popen(['python', 'setup.py', '--version'],
                           cwd="..",
                           stdout=subprocess.PIPE) \
    .stdout.read().decode("utf-8").strip()

release = version

exclude_patterns = ['../tests']
exclude_patterns += ['_build', '**.ipynb_checkpoints']

show_authors = True

pygments_style = 'sphinx'

if not os.environ.get('READTHEDOCS', None) == 'True':  # only set the theme if we're building docs locally
    html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

html_use_index = True

html_show_sourcelink = False

html_show_copyright = True
# noinspection PyShadowingBuiltins
copyright = 'Philippe PRADOS'

html_use_opensearch = ''

htmlhelp_basename = 'tag_images_for_google_drive'

latex_engine = 'pdflatex'
latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    'papersize': 'a4paper',

    # The font size ('10pt', '11pt' or '12pt').
    'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    # 'preamble': '',
}

latex_documents = [
    (
        master_doc,  # Doc name
        'tagimagesforgdrive.tex',  # targetname
        'tag_images_for_google_drive Documentation',  # title
        'tagimagesforgdrive',  # author
        'manual',  # documentclass
        # 'howto',  # documentclass
        False,  # toctree_only
    ),
]

man_pages = [
    ('index',
     'tag_images_for_google_drive',
     'tag_images_for_google_drive Documentation',
     ['Philippe PRADOS'], 1)
]

texinfo_documents = [
    ('index',
     'tag_images_for_google_drive',
     'tag_images_for_google_drive Documentation',
     'Philippe PRADOS',
     ),
]

todo_include_todos = True

applehelp_disable_external_tools = False

rst_prolog = f"""
.. |giturl| replace:: {git_url}
.. |homeurl| replace:: {home_url}
.. |s3_bucket| replace:: {s3_bucket}
"""

# The suffix of source filenames.
source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}
