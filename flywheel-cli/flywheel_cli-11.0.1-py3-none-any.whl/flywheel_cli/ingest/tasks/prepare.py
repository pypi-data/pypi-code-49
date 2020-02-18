"""Provides PrepareTask class."""
import copy
import logging
import functools

import fs

from .. import schemas, utils
from .abstract import AbstractTask

log = logging.getLogger(__name__)


class PrepareTask(AbstractTask):
    """Preprocessing work."""

    def _execute(self):
        """Process review, create and enqueue upload tasks"""
        # build hierarchy
        for container in self.ingest_db.get_containers():
            if not container.dst_context:
                self._create_container(container)

        self.ingest_db.set_ingest_status(status=schemas.IngestStatus.uploading)
        for item in self.ingest_db.get_items():
            if self.config.skip_existing and item.existing:
                self.ingest_db.update_item(
                    item_id=item.id,
                    skipped=True,
                )
                log.debug(f"Skipped item {item.id} because it already exists")
                continue
            self.ingest_db.create_task(schemas.TaskIn(
                type=schemas.TaskType.upload,
                item_id=item.id,
            ))

    def _create_container(self, container):
        c_level = container.level.name
        create_fn = getattr(self.fw, f"add_{c_level}", None)
        parent = None
        if container.parent_id:
            parent = self._get_parent_container(container.parent_id)
        if not create_fn:
            raise ValueError(f"Unsupported container type: {c_level}")
        create_doc = copy.deepcopy(container.src_context)
        if c_level == "session":
            # Add subject to session
            project_cont = self._get_parent_container(parent.parent_id)
            create_doc["project"] = project_cont.dst_context["_id"]
            create_doc["subject"] = copy.deepcopy(parent.src_context)
            create_doc["subject"]["_id"] = parent.dst_context["_id"]
            create_doc["subject"].setdefault("code", create_doc["subject"].get("label"))
        elif parent:
            create_doc[parent.level.name] = parent.dst_context["_id"]
        if c_level == "subject":
            create_doc.setdefault("code", create_doc.get("label"))
        new_id = create_fn(create_doc)
        log.debug(f"Created {c_level} container: {create_doc} as {new_id}")
        # update container with dst_context and dst_path
        dst_context = copy.deepcopy(container.src_context)
        dst_context["_id"] = new_id
        parent_dst_path = parent.dst_path if parent else ""
        dst_path = fs.path.combine(
            parent_dst_path,
            utils.get_path_el(c_level, dst_context, reverse=True)
        )
        self.ingest_db.update_container(
            container.id,
            dst_context=dst_context,
            dst_path=dst_path,
        )

    @functools.lru_cache(1000)
    def _get_parent_container(self, cid):
        return self.ingest_db.get_container(cid)

    def _after_complete(self):
        # possible that no upload tasks were created - finalize
        self.ingest_db.finalize_ingest_after_upload()

    def _after_failed(self):
        self.ingest_db.fail_ingest()
