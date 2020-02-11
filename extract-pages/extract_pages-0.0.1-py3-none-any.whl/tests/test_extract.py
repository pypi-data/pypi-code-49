import os

from PyPDF2 import PdfFileReader

import extract_pages.tests as tests
from extract_pages import extract_pages, parse_ranges


def test_extract_pages_from_one_file(tmpdir):
    root = os.path.join(os.path.dirname(tests.__file__), 'test_data')

    pages = ['3,9-12']
    input_files = [os.path.join(root, 'fundamentals-set.pdf')]

    pages_list = [parse_ranges(p) for p in pages]

    output_dir = tmpdir.mkdir('test-dir')
    output_file = os.path.join(output_dir, 'test-out.pdf')

    output_files = extract_pages(input_files=input_files, pages=pages,
                                 output_file=output_file, one_file=True)

    assert len(output_files) == len(input_files)

    for output_file in output_files:
        readit = PdfFileReader(open(output_file, 'rb'))
        assert readit.numPages == len(pages_list[0])


def test_extract_pages_from_multiple_files(tmpdir):
    root = os.path.join(os.path.dirname(tests.__file__), 'test_data')

    pages = ['1,4-5', '3,8-12']
    input_files = [os.path.join(root, f)
                   for f in ['fundamentals-set.pdf',
                             'diatonic-harmony-set.pdf']
                   ]

    pages_list = [parse_ranges(p) for p in pages]

    output_dir = tmpdir.mkdir('test-dir')
    output_file = os.path.join(output_dir, 'test-out.pdf')

    output_files = extract_pages(input_files=input_files, pages=pages,
                                 output_file=output_file, one_file=False)

    assert len(output_files) == len(input_files)

    for i, output_file in enumerate(output_files):
        readit = PdfFileReader(open(output_file, 'rb'))
        assert readit.numPages == len(pages_list[i])


def test_parse_ranges():
    res = parse_ranges('1,3-6')
    assert res == [1, 3, 4, 5, 6]
