# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['staplelib']

package_data = \
{'': ['*'], 'staplelib': ['testfiles/*']}

install_requires = \
['PyPDF2>=1.26', 'more-itertools>=2.2,<6.0.0']

entry_points = \
{'console_scripts': ['pdf-stapler = staplelib:main',
                     'stapler = staplelib:main']}

setup_kwargs = {
    'name': 'stapler',
    'version': '1.0.0b1',
    'description': 'Manipulate PDF documents from the command line',
    'long_description': "Stapler\n=======\n\nStapler is a pure Python alternative to\n`PDFtk <http://www.pdfhacks.com/pdftk/>`__, a tool for manipulating PDF\ndocuments from the command line.\n\nHistory\n-------\n\nPDFtk was written in Java and C++, and is natively compiled with gcj.\nSadly, it has been discontinued a few years ago and bitrot is setting in\n(e.g., it does not compile easily on a number of platforms).\n\nPhilip Stark decided to look for an alternative and found pypdf, a PDF\nlibrary written in pure Python. He couldn't find a tool which actually\nused the library, so he started writing his own.\n\nVersion 0.3 of stapler was completely refactored by Fred Wenzel. He also\nadded tests and awesome functionality.\n\nLike pdftk, stapler is a command-line tool. If you would like to add a\nGUI, compile it into a binary for your favorite platform, or contribute\nanything else, feel free to fork and send a pull request.\n\nContributors and Authorship\n---------------------------\n\nStapler version 0.2 was written in 2009 by Philip Stark. Stapler version\n0.3 was written in 2010 by Fred Wenzel.\n\nFor a list of contributors, check the ``CONTRIBUTORS`` file.\n\nChange log (sorta)\n------------------\n\n- **1.0.0** Port to Python 3. Replace OptionParser with more\n  modern ArgumentParser. Cleaning up repository.\n\n- **0.3.3** include try-except blocks for supporting legacy pyPdf\n  if needed. Also fixes some PyPI issues like the missing License Trove\n  classifier and some dependencies.\n\n- **0.3.0** Refactoring by Fred Wenzel and now using PyPDF2\n\n- **0.2.0** Feature completeness using original pyPdf\n\nLicense\n-------\n\nStapler is distributed under a BSD license. A copy of the BSD Style\nLicense used can be found in the file ``LICENSE``.\n\nUsage\n-----\n\nThere are the following modes in Stapler:\n\nselect/delete (called with ``sel`` and ``del``, respectively)\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n``sel`` is also available as ``cat`` for compatibility with my\npersonal muscle memory. :)\n\nWith select, you can cherry-pick pages from pdfs and concatenate them\ninto a new pdf file.\n\nInput files can be associated with handles for use with ranges later.\nA handle is a single, upper-case letter:\n\n::\n\n    <input handle>=<input>\n\nSyntax:\n\n::\n\n    stapler sel input1 page_or_range [page_or_range ...] [input2 p_o_r ...]\n\nExamples:\n\n::\n\n    # concatenate a and b into output.pdf\n    stapler sel a.pdf b.pdf output.pdf\n\n    # generate a pdf file called output.pdf with the following pages:\n    # 1, 4-8 in 180° (D for down), 20-40 from a.pdf, 1-5 from b.pdf in \n    # this order\n    stapler sel a.pdf 1 4-8D 20-40 b.pdf 1-5 output.pdf\n\n    # the same example with a handle for b.pdf\n    stapler sel B=b.pdf a.pdf 1 4-8D 20-40 B1-5 output.pdf\n\n    # generate a pdf file called output.pdf with the following pages:\n    # 1 from a.pdf, 1-5 from b.pdf, 4-8 in 180° (D for down), 20-40 from a.pdf\n    # this order\n    stapler sel A=a.pdf B=b.pdf A1 B1-5 A4-8D A20-40 output.pdf\n\n    # reverse some of the pages in a.pdf by specifying a negative range\n    stapler sel a.pdf 1-3 9-6 10 output.pdf\n\nThe delete command works almost exactly the same as select, but inverse.\nIt uses the pages and ranges which you *didn't* specify.\n\nsplit/burst:\n~~~~~~~~~~~~\n\nSplits the specified pdf files into their single pages and writes each\npage into it's own pdf file with this naming scheme:\n\n::\n\n    ${origname}_${zero-padded page no}.pdf\n\nSyntax:\n\n::\n\n    stapler split input1 [input2 input3 ...]\n\nExample for a file foobar.pdf with 20 pages:\n\n::\n\n    $ stapler split foobar.pdf\n    $ ls\n    foobar_01.pdf foobar_02.pdf ... foobar_19.pdf foobar_20.pdf\n\nMultiple files can be specified, they will be processed as if you called\nsingle instances of stapler.\n\nzip:\n~~~~\n\nWith zip, you can cherry-pick pages from pdfs (like select). The pages\nfrom each pdf are merged together in an interleaving manner. This can be\nused to collate a pdf with odd pages and a pdf with even pages into a\nsingle file.\n\nSyntax: stapler zip input1 [range[rotation]] [range ...] [input2\n[range...] ...] out\n\nExamples:\n\n::\n\n    # combine a pdf with odd pages and a pdf with even pages into output.pdf\n    stapler zip odd.pdf even.pdf output.pdf\n\n    # combine a.pdf b.pdf and c.pdf, but use only some pages of c.pdf and\n    #  rotate b.pdf right (90° clockwise) and rotate c.pdf left (90° counter-\n    # clockwise)\n    stapler zip a.pdf b.pdf 1-endR c.pdf 1-3L output.pdf\n\nIf one of the ranges is shorter than the others, stapler will continue\nto merge the remaining pages.\n\ninfo:\n~~~~~\n\nShows information on the metadata stored inside a PDF file.\n\nSyntax:\n\n::\n\n    stapler info foo.pdf\n\nExample output:\n\n::\n\n    \\*\\*\\* Metadata for foo.pdf\n\n    /ModDate:  D:20100313082451+01'00'\n    /CreationDate:  D:20100313082451+01'00'\n    /Producer:  GPL Ghostscript 8.70\n    /Title:  foo.pdf\n    /Creator:  PDFCreator Version 0.9.9\n    /Keywords:\n    /Author:  John Doe\n    /Subject:\n\nlist-logical:\n~~~~~~~~~~~~~\n\nShows each logical page number and the associated physical page number.\n\nSyntax:\n\n::\n\n    stapler list-logical foo.pdf\n\nExample output:\n\n::\n\n    A-1\t1\n    C-1\t2\n    D-1\t3\n    D-2\t4\n    D-3\t5\n    D-4\t6\n",
    'author': 'Philip Stark',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.4,<4.0',
}


setup(**setup_kwargs)
