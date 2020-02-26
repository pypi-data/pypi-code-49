"""Provides FilenameScanner class."""

import copy
import logging

import fs

from ...importers import match_util
from .. import schemas
from .abstract import AbstractScanner

log = logging.getLogger(__name__)


class FilenameScanner(AbstractScanner):
    """FilenameScanner groups files together by a common prefix.

    This works by looking at the first slash (or if there is no slash, the first dot) in
    each file path, and using that as the acquisition label.
    """

    def _scan(self, dirpath):
        self.validate_opts(self.opts)
        template = match_util.compile_regex(self.opts["pattern"])

        for fileinfo in self.walker.list_files(dirpath):
            filename = fs.path.basename(fileinfo.name)
            file_context = copy.deepcopy(self.context)

            if not match_util.extract_metadata_attributes(filename, template, file_context):
                log.debug(f'File {filename} did not match the template')

            yield schemas.ItemIn(
                type="file",
                dir=dirpath,
                files=[fileinfo.name],
                files_cnt=1,
                bytes_sum=fileinfo.size,
                context=file_context,
            )

    @staticmethod
    def validate_opts(opts):
        if opts is None or 'pattern' not in opts:
            raise ValueError('Filename scanner requires pattern!')

        try:
            match_util.compile_regex(opts['pattern'])
        except Exception as ex:
            log.debug('Cannot compile filename pattern.', exc_info=True)
            raise ValueError(f'Invalid filename pattern: {ex}')
