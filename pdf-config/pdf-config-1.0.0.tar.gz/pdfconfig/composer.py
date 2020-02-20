import logging
import os
from collections import namedtuple

from PyPDF4 import PdfFileMerger

from .utils import expand_path, get_pdf_info, get_meta_dict, get_config_pdf_version

LevelInfo = namedtuple('LevelInfo', ['num_pages', 'max_pdf_version'])

log = logging.getLogger()


class PdfFileComposer:
    """
    Wraps a PyPDF.PdfFileMerger for simplifying the merge process of multiple PDF files into a single PDF,
    defined by a configuration.

    :param contents: Content dictionary, optional with nested bookmark structure.
    :param metadata: Output PDF meta data.
    :param search_paths: List of search paths to look up files without any path specification.
    """
    def __init__(self, contents: dict, metadata: dict, search_paths: list):
        self._contents = contents
        if metadata:
            self._output_version = metadata.pop('version', 'auto')
            self._metadata = metadata
        else:
            self._output_version = 'auto'
            self._metadata = None
        self._merger = PdfFileMerger()
        self._resolve_paths = list(map(expand_path, search_paths or ()))

    def _resolve_file(self, filename: str) -> str:
        if os.path.sep in filename:
            return expand_path(filename)
        elif self._resolve_paths:
            log.debug("Looking up file %s", filename)
            # First try in the current directory.
            if os.path.isfile(filename):
                return filename
            for path in self._resolve_paths:
                try_filename = os.path.join(path, filename)
                if os.path.isfile(try_filename):
                    return try_filename
        return filename

    def _set_version(self, max_input_version: str):
        pdf_version = get_config_pdf_version(self._output_version, max_input_version)
        log.debug("Using PDF version %s", pdf_version)
        self._merger.output._header = '%PDF-{0}'.format(pdf_version).encode('utf-8')

    def _set_metadata(self):
        if not self._metadata:
            log.info("No metadata specified; using defaults.")
            return
        meta_dict = get_meta_dict(self._metadata)
        if meta_dict:
            self._merger.addMetadata(meta_dict)

    def _append_content(self, contents: dict, level_base_page: int, parent_bookmark) -> LevelInfo:
        merger = self._merger
        level_pages = 0
        max_pdf_version = ''
        for item in contents:
            bookmark_title = item.get('bookmark')
            if bookmark_title:
                log.info("Inserting bookmark '%s' on page %d", bookmark_title, level_base_page + level_pages)
                this_bookmark = merger.addBookmark(bookmark_title, level_base_page + level_pages,
                                                   parent=parent_bookmark)
            else:
                this_bookmark = parent_bookmark
            document_filename = item.get('document')
            if document_filename:
                resolved_name = self._resolve_file(document_filename)
                log.info("Adding file %s", resolved_name)
                with open(resolved_name, 'rb') as input_pdf:
                    pdf_info = get_pdf_info(input_pdf)
                    max_pdf_version = max(max_pdf_version, pdf_info.pdf_version)
                    level_pages += pdf_info.num_pages
                    merger.append(input_pdf)
                    log.info("%d pages appended", pdf_info.num_pages)
            nested_contents = item.get('contents')
            if nested_contents:
                nested_info = self._append_content(nested_contents, level_base_page + level_pages, this_bookmark)
                max_pdf_version = max(max_pdf_version, nested_info.max_pdf_version)
                level_pages += nested_info.num_pages
        return LevelInfo(level_pages, max_pdf_version)

    def write(self, output_filename: str):
        """
        Merges the configured files into one PDF and writes the result into the specified path.

        :param output_filename: Output PDF name.
        """
        self._set_metadata()
        try:
            res = self._append_content(self._contents, 0, None)
            log.info("Total pages %d - Max PDF version: %s", res.num_pages, res.max_pdf_version)
            if res.num_pages == 0:
                log.warning("No pages have been added.")
            self._set_version(res.max_pdf_version)
            log.info("Writing to file %s", output_filename)
            with open(output_filename, 'wb') as out_file:
                self._merger.write(out_file)
        finally:
            self._merger.close()
