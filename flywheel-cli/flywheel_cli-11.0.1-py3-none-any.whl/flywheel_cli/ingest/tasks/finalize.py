"""Provides FinalizeTask class"""

import logging
import os
import tempfile

from ... import util
from .. import schemas
from .abstract import AbstractTask

log = logging.getLogger(__name__)


class FinalizeTask(AbstractTask):
    """Finalize ingest. Currently uploading audit log to target projects."""

    def _execute(self):
        """Upload audit log to every project that we identified
        TODO: group logs by project
        """
        if self.config.no_audit_log:
            log.debug("Audit log turned off, so skip uploading it")
            return
        with tempfile.TemporaryDirectory() as tmp_dir:
            filepath = util.get_filepath(tmp_dir, prefix="audit_log")
            filename = os.path.basename(filepath)
            with open(filepath, "w") as fp:
                for log_line in self.ingest_db.get_audit_logs():
                    fp.write(log_line)
            with open(filepath, "r") as fp:
                project_containers = self.ingest_db.get_containers(
                    level=schemas.ContainerLevel.project
                )
                for container in project_containers:
                    self.fw.upload(
                        container.level.name,
                        container.dst_context.get("_id"),
                        filename,
                        fp,
                    )

    def _after_complete(self):
        self.ingest_db.finish_ingest()

    def _after_failed(self):
        self.ingest_db.fail_ingest()
