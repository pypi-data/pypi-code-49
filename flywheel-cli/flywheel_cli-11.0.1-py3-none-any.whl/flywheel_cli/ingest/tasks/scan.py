"""Provides ScanTask class."""

import logging

from ..scanners.factory import create_scanner
from .. import schemas
from .abstract import AbstractTask

log = logging.getLogger(__name__)


class ScanTask(AbstractTask):
    """Scan a given path using the given scanner."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.walker = None

    def _initialize(self):
        self.walker = self.config.create_walker(self.config.src_fs_url)

    def _execute(self):
        """Scan files in a given folder."""
        scanner_type = self.task.context["scanner"]["type"]
        dirpath = self.task.context["scanner"]["dir"]
        opts = self.task.context["scanner"].get("opts")
        scanner = create_scanner(
            scanner_type,
            self.config,
            self.walker,
            opts=opts,
            context=self.task.context,
            get_subject_code_fn=self.ingest_db.resolve_subject,
        )
        for item in scanner.scan(dirpath):
            if isinstance(item, schemas.ItemIn):
                self.ingest_db.create_item(item)
            elif isinstance(item, schemas.TaskIn):
                self.ingest_db.create_task(item)
            else:
                raise Exception(f"Unexpected type: {type(item)}")
        # TODO: cache scanned files and reuse during upload
        self.walker.close()

    def _after_complete(self):
        self.ingest_db.resolve_ingest_after_scan()

    def _after_failed(self):
        self.ingest_db.fail_ingest()
