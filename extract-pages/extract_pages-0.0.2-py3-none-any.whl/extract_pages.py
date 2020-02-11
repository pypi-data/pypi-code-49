import logging
import argparse
import os
import sys
from collections import OrderedDict
from pathlib import Path

from PyPDF2 import PdfFileReader, PdfFileWriter
from tqdm import tqdm


logger = logging.getLogger(__name__)


def extract_pages(input_files, pages, output_file, one_file=True):
    """Extract pages from a single or multiple .pdf files and combine them.

    Parameters
    ----------
    input_files: list
        a list of input file names
    pages: str
        a list of pages in a string form with no blank spaces, e.g. '1,3-5'
    output_file: str
        an output file location. If the ``one_file=False``, the corresponding
        suffix consisting of the page numbers will be added
    one_file: bool, optional
        a flag to save the outputs into one .pdf file
    """
    pdfs = {}
    for f, p in zip(input_files, pages):
        pdfs[f] = parse_ranges(p)

    pdfs = OrderedDict(sorted(pdfs.items(), reverse=True))
    logger.info(pdfs)

    output_files = []

    if one_file:
        output = PdfFileWriter()

    for pdf_name, pdf_pages in tqdm(pdfs.items()):
        print(pdf_name, pdf_pages)
        full_path = Path(pdf_name)

        inputpdf = PdfFileReader(open(full_path, 'rb'))
        msg = 'specified pages range {} is out of range ({})'
        num_pages = inputpdf.numPages
        for page in pdf_pages:
            assert page <= num_pages, msg.format(pdf_name, num_pages)

        n, e = os.path.splitext(os.path.basename(full_path))
        out_dir = os.path.dirname(os.path.abspath(output_file))
        pages_range = '-'.join([str(x) for x in pdf_pages])
        out_name = os.path.join(out_dir, '{}_{}{}'.format(n, pages_range, e))
        tqdm.write('  Input  file: {} (pages: {} out of total {})'.format(
                   full_path, pages_range, num_pages))

        if not one_file:
            tqdm.write('  Output file: {}'.format(out_name))
            output = PdfFileWriter()

        for i in pdf_pages:
            tqdm.write('      Getting page {}...'.format(i))
            output.addPage(inputpdf.getPage(i-1))

        if not one_file:
            with open(out_name, 'wb') as oStream:
                output_files.append(out_name)
                output.write(oStream)

        tqdm.write('')

    if one_file:
        out_name = output_file
        tqdm.write('\n\tOutput file: {}'.format(out_name))
        with open(out_name, 'wb') as oStream:
            output_files.append(out_name)
            output.write(oStream)

    return output_files


def parse_ranges(string):
    """Parse ranges of numbers, e.g. '1,3-6'
    """
    s_split = [x.replace('-', ',').replace(':', ',')
               for x in string.split(',')]
    ret = []
    for el in s_split:
        nums = [int(x) for x in el.split(',')]
        if len(nums) < 2:
            nums.append(nums[-1])
        nums[-1] += 1
        ret.extend(list(range(*nums)))
    return ret


def main():
    parser = argparse.ArgumentParser(
        description='Extract and combine pages from multiple pdf files')
    parser.add_argument('-i', '--input-files', dest='input_files',
                        default=None, nargs='+',
                        help='blank-separated input pdf-file list')
    parser.add_argument('-p', '--pages', dest='pages',
                        default=None, nargs='+',
                        help='blank-separated list of pages list')
    parser.add_argument('-o', '--output-file', dest='output_file',
                        default='output.pdf',
                        help='output file name')

    args = parser.parse_args()

    if None in [args.input_files, args.pages]:
        parser.print_help()
        parser.exit()

    kwargs = {'input_files': args.input_files,
              'pages': args.pages,
              'output_file': args.output_file}

    extract_pages(**kwargs)


if __name__ == '__main__':
    sys.exit(main())
