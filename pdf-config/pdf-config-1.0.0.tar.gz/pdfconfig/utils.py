from collections import namedtuple
import logging
import os
import re

from PyPDF4 import PdfFileReader
from PyPDF4.utils import PdfReadError

PdfInfo = namedtuple('PdfInfo', ['num_pages', 'pdf_version'])

PDF_VERSION_PATTERN = re.compile(r'\d\.\d')
PDF_HEADER_PATTERN = re.compile(r'%PDF-(\d\.\d)')

META_ATTRIBUTES = [
    'author',
    'creator',
    'keywords',
    'producer',
    'subject',
    'title',
]
META_ATTRIBUTE_KEYS = {
    kw: '/{0}'.format(kw.capitalize())
    for kw in META_ATTRIBUTES
}

log = logging.getLogger()


def expand_path(filename: str) -> str:
    """
    Expands variables (user and environment) in a file name.

    :param filename: File name, possibly containing variables.
    :return: File name with variables expanded.
    """
    return os.path.expandvars(os.path.expanduser(filename))


def get_meta_dict(cfg_meta: dict) -> dict:
    """
    Generates a dictionary of metadata that can be added to a PDF file. Invalid keys are skipped with a warning.

    >>> get_meta_dict({'author': 'TheAuthor', 'subject': 'TheSubject', 'title': 'TheTitle', 'invalid': 'Invalid'})
    {'/Author': 'TheAuthor', '/Subject': 'TheSubject', '/Title': 'TheTitle'}

    :param cfg_meta: Input keys and values from config.
    :return: Dictionary containing valid entries for PDF meta data.
    """
    meta_dict = {}
    for k, v in cfg_meta.items():
        meta_key = META_ATTRIBUTE_KEYS.get(k)
        if meta_key:
            meta_dict[meta_key] = v
        else:
            log.warning("Unrecognized metadata key '%s'", meta_key)
    return meta_dict


def get_output_filename(cfg_filename: str) -> str:
    """
    Derives a PDF output file name from the input configuration file name.

    >>> get_output_filename('sample.yaml')
    'sample.pdf'
    >>> get_output_filename('path/to/sample.yaml')
    'path/to/sample.pdf'

    :param cfg_filename: Name and path of the configuration file.
    :return: Same file name and path, with the extension changed to ``.pdf``.
    """
    cfg_base = os.path.splitext(cfg_filename)[0]
    return '{0}.pdf'.format(cfg_base)


def get_pdf_info(input_pdf) -> PdfInfo:
    """
    Checks the version header and retrieves some metadata from the input PDF stream.

    :param input_pdf: File-like object with PDF data.
    :return: A PdfInfo tuple with the number of pages and the PDF version.
    :raises PyPDF4.utils.PdfReadError: If the header of the PDF seems to be invalid.
    """
    raw_header = input_pdf.read(8)
    try:
        header_str = raw_header.decode('utf-8')
    except UnicodeDecodeError:
        raise PdfReadError("PDF header not found")
    header_match = PDF_HEADER_PATTERN.fullmatch(header_str)
    if not header_match:
        raise PdfReadError("PDF header does not seem to be valid")
    pdf_version = header_match.group(1)
    reader = PdfFileReader(input_pdf)
    log.debug("PDF version %s with %d pages", pdf_version, reader.numPages)
    return PdfInfo(reader.numPages, pdf_version)


def get_config_pdf_version(config_version: str, max_input_version: str) -> str:
    """
    From the PDF version as set in the configuration and the maximum version of all input files, checks for
    the best PDF output version. Logs a warning, if the version set in the configuration is lower than any of the
    input files.

    >>> get_config_pdf_version('auto', '1.6')
    '1.6'
    >>> get_config_pdf_version('1.3', '1.5')
    '1.3'
    >>> get_config_pdf_version('1.x', '1.5')
    Traceback (most recent call last):
      ...
    ValueError: ('Invalid PDF version in configuration', '1.x')

    :param config_version: Version string from the configuration. Set to ``auto`` to just use ``max_input_version``.
    :param max_input_version: Maximum version from all input files.
    :return: ``config_version``, unless set to ``auto``, then ``max_input_version``. However, the automatic version
     setting will never be lower than ``1.3``.
    :raises ValueError: If the configuration-set version is an invalid pattern.
    """
    if config_version == 'auto':
        return max(max_input_version, '1.3')
    if not PDF_VERSION_PATTERN.fullmatch(config_version):
        raise ValueError("Invalid PDF version in configuration", config_version)
    if max_input_version > config_version:
        log.warning("PDF version specified in config (%s) is lower than at least one of the input documents (%s). "
                    "The resulting PDF may not be displayed correctly in all viewers.",
                    config_version, max_input_version)
    return config_version
