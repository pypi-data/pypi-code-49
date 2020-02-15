#!/usr/bin/env python3

"""
This script 'setup' builds the AsciiDoc3 package to be installed via
pip / pip3 from 'https://pypi.org/project/asciidoc3/'.
asciidoc3 makes AsciiDoc3 available both on GNU/Linux (POSIX) and
Windows.
To complete the installation it is strongly recommended (or to say
it in a more accurate word: compelling) to run 'asciidoc3_postinstall'
from the command line immediately subsequently after
'pip3 install --user asciidoc3'. This arranges some reasonable
symlinks for convenient usage.
See https://asciidoc3.org/pypi.html and
https://asciidoc3.org/pypi.html for more information.

Copyright (C) 2018-2020 by Berthold Gehrke <berthold.gehrke@gmail.com>
Free use of this software is granted under the terms of the
GNU General Public License Version 2 or higher (GNU GPLv2+).
"""

from os import name
from sys import version
from setuptools import setup, find_packages

# find current version and location of executable
# e.g.: version = '3.7.2+ (default, Feb  2 2019, 14:31:48) \n[GCC 8.2.0]'
# PRE = '37'
# PRE='Python37/site-packages/'
PRE = version[:1] + version[2:3]
PRE = 'Python' + PRE + '/site-packages/'

# this is to assure right-installing on Windows *and* GNU/Linux
PREFIX_TUPLE = tuple()
if name == 'nt':
    PREFIX_TUPLE = ('', PRE)
elif name == 'posix':
    PREFIX_TUPLE = ('/',)
else: # guess
    PREFIX_TUPLE = ('/',)

datafiles = list()
for dirprefix in PREFIX_TUPLE:
    datafiles.append((dirprefix+'asciidoc3', ['asciidoc3.conf', 'COPYING', 'COPYRIGHT',
                                              'docbook45.conf', 'help.conf', 'html4.conf',
                                              'html5.conf', 'lang-de.conf', 'latex.conf',
                                              'asciidoc3.py', 'a2x3.py', 'asciidoc3api.py',
                                              'LICENSE', 'README.md', 'slidy.conf', 'setup.py',
                                              'text.conf', 'xhtml11.conf', 'BUGS.txt',
                                              'CHANGELOG', 'COPYING', 'COPYRIGHT',
                                              'lang-cs.conf', 'lang-el.conf',
                                              'lang-es.conf', 'lang-fr.conf', 'lang-hu.conf',
                                              'lang-it.conf', 'lang-nl.conf', 'lang-pt-BR.conf',
                                              'lang-ro.conf', 'lang-ru.conf', 'lang-uk.conf',
                                              'lang-en.conf', 'asciidoc3_postinstall.py']))
    datafiles.append((dirprefix+'asciidoc3/stylesheets', ['stylesheets/asciidoc3.css',
                                                          'stylesheets/docbook-xsl.css',
                                                          'stylesheets/pygments.css',
                                                          'stylesheets/slidy.css',
                                                          'stylesheets/toc2.css']))
    datafiles.append((dirprefix+'asciidoc3/dblatex', ['dblatex/asciidoc3-dblatex.sty',
                                                      'dblatex/asciidoc3-dblatex.xsl',
                                                      'dblatex/dblatex-readme.txt']))
    datafiles.append((dirprefix+'asciidoc3/docbook-xsl', ['docbook-xsl/asciidoc3-docbook-xsl.txt',
                                                          'docbook-xsl/chunked.xsl',
                                                          'docbook-xsl/common.xsl',
                                                          'docbook-xsl/epub.xsl',
                                                          'docbook-xsl/fo.xsl',
                                                          'docbook-xsl/htmlhelp.xsl',
                                                          'docbook-xsl/manpage.xsl',
                                                          'docbook-xsl/text.xsl',
                                                          'docbook-xsl/xhtml.xsl']))
    datafiles.append((dirprefix+'asciidoc3/images', ['images/1.png',
                                                     'images/2.png',
                                                     'images/3.png',
                                                     'images/empty.png',
                                                     'images/helloworld.jpg',
                                                     'images/highlighter.png',
                                                     'images/highlight.jpg',
                                                     'images/redsquare.jpg',
                                                     'images/smallnew.png',
                                                     'images/tiger.png']))
    datafiles.append((dirprefix+'asciidoc3/images/icons', ['images/icons/caution.png',
                                                           'images/icons/example.png',
                                                           'images/icons/home.png',
                                                           'images/icons/important.png',
                                                           'images/icons/next.png',
                                                           'images/icons/note.png',
                                                           'images/icons/prev.png',
                                                           'images/icons/README',
                                                           'images/icons/tip.png',
                                                           'images/icons/up.png',
                                                           'images/icons/warning.png']))
    datafiles.append((dirprefix+'asciidoc3/images/icons/callouts', ['images/icons/callouts/1.png',
                                                                    'images/icons/callouts/2.png',
                                                                    'images/icons/callouts/3.png',
                                                                    'images/icons/callouts/4.png',
                                                                    'images/icons/callouts/5.png',
                                                                    'images/icons/callouts/6.png',
                                                                    'images/icons/callouts/7.png',
                                                                    'images/icons/callouts/8.png',
                                                                    'images/icons/callouts/9.png',
                                                                    'images/icons/callouts/10.png',
                                                                    'images/icons/callouts/11.png',
                                                                    'images/icons/callouts/12.png',
                                                                    'images/icons/callouts/13.png',
                                                                    'images/icons/callouts/14.png',
                                                                    'images/icons/callouts/15.png']))
    datafiles.append((dirprefix+'asciidoc3/doc', ['doc/asciidoc3api.txt',
                                                  'doc/asciidoc3.conf',
                                                  'doc/asciidoc3port.txt',
                                                  'doc/article-docinfo.xml',
                                                  'doc/asciimathml.txt',
                                                  'doc/book-multi.txt',
                                                  'doc/book.txt',
                                                  'doc/customers.csv',
                                                  'doc/epub-notes.txt',
                                                  'doc/faq.txt',
                                                  'doc/latex-backend.txt',
                                                  'doc/latex-bugs.txt',
                                                  'doc/latex-filter.txt',
                                                  'doc/latexmathml.txt',
                                                  'doc/latexmath.txt',
                                                  'doc/music-filter.txt',
                                                  'doc/publishing-ebooks-with-asciidoc3.txt',
                                                  'doc/quickstart.txt',
                                                  'doc/READMEdoc.txt',
                                                  'doc/slidy-example.txt',
                                                  'doc/slidy.txt',
                                                  'doc/source-highlight-filter.txt',
                                                  'doc/test.txt',
                                                  'doc/userguide.txt']))
    datafiles.append((dirprefix+'asciidoc3/javascripts', ['javascripts/asciidoc3.js',
                                                          'javascripts/ASCIIMathML.js',
                                                          'javascripts/LaTeXMathML.js',
                                                          'javascripts/slidy.js',
                                                          'javascripts/toc.js']))
    datafiles.append((dirprefix+'asciidoc3/filters/code', ['filters/code/code-filter.conf',
                                                           'filters/code/code-filter.py',
                                                           'filters/code/code-filter-readme.txt',
                                                           'filters/code/code-filter-test.txt']))
    datafiles.append((dirprefix+'asciidoc3/filters/graphviz', ['filters/graphviz/asciidoc3-graphviz-sample.txt',
                                                               'filters/graphviz/graphviz2png.py',
                                                               'filters/graphviz/graphviz-filter.conf']))
    datafiles.append((dirprefix+'asciidoc3/filters/latex', ['filters/latex/latex2png.py',
                                                            'filters/latex/latex-filter.conf']))
    datafiles.append((dirprefix+'asciidoc3/filters/music', ['filters/music/music-filter.conf',
                                                            'filters/music/music-filter-test.txt',
                                                            'filters/music/music2png.py']))
    datafiles.append((dirprefix+'asciidoc3/filters/source', ['filters/source/source-highlight-filter.conf',
                                                             'filters/source/source-highlight-filter-test.txt']))
    datafiles.append((dirprefix+'asciidoc3/themes/flask', ['themes/flask/flask.css']))
    datafiles.append((dirprefix+'asciidoc3/themes/volnitsky', ['themes/volnitsky/volnitsky.css']))
    datafiles.append((dirprefix+'asciidoc3/vim', ['vim/readme-vim.txt']))
    datafiles.append((dirprefix+'asciidoc3/vim/syntax', ['vim/syntax/asciidoc3.vim']))
    datafiles.append((dirprefix+'asciidoc3/man', ['doc/a2x3.1.gz',
                                                  'doc/a2x3.1.txt',
                                                  'doc/asciidoc3.1.gz',
                                                  'doc/asciidoc3.1.txt']))

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="asciidoc3",
    version="3.1.0.post6",
    description="""AsciiDoc3 Python3 GNU/Linux Windows AsciiDoc - see https://asciidoc3.org/pypi.html BEFORE installing""",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords=['text', 'markup', 'Windows', 'asciidoc', 'asciidoc3', 'python3'],
    author="Berthold Gehrke",
    author_email="berthold.gehrke@gmail.com",
    url="https://asciidoc3.org",
    project_urls={
        "Source": "https://gitlab.com/asciidoc3/asciidoc3",
        "Funding": "https://asciidoc3.org/contact.html"
    },
    license='GPLv2+',
    packages=find_packages(),
    entry_points={'console_scripts':
                  ['asciidoc3=asciidoc3.asciidoc3:main',
                   'a2x3=asciidoc3.a2x3:main',
                   'asciidoc3_postinstall=asciidoc3.asciidoc3_postinstall:main']},
    include_package_data=True,
    # 'data_files' do not contain the symlinks to dir 'images'
    # -> run 'asciidoc3_postinstall' after 'pip install --user asciidoc3'
    data_files=datafiles,
    zip_safe=False,
    python_requires=">= 3.5",
    classifiers=[  # for a list of valid classifiers see https://pypi.org/classifiers/
        'Topic :: Text Processing',
        'Topic :: Text Processing :: Markup',
        'License :: OSI Approved :: GNU General Public License v2 or later (GPLv2+)',
        'Natural Language :: English',
        'Operating System :: POSIX',
        'Operating System :: Microsoft :: Windows',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Development Status :: 5 - Production/Stable',
    ],
)

