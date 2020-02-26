"""Provides ResolveTask class."""

import functools
import logging
import pickle

import flywheel
import fs

from ...util import str_to_filename
from .. import schemas, utils
from .abstract import AbstractTask

log = logging.getLogger(__name__)

CONTAINER_FIELDS = ["id", "label", "uid", "code"]


class ResolveTask(AbstractTask):
    """Resolve containers for review."""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.visited = []

    def _execute(self):
        for item in self.ingest_db.get_items():
            container = self._resolve_item_containers(item.context)
            if not container:
                log.warning(f"Couldn't resolve container for: {item.id}")
                continue
            filename = item.filename or self._get_filename(item, container)
            dst_files = container.dst_context.get("files", []) if container.dst_context else []
            update = {
                "container_id": container.id,
                "existing": filename in dst_files,
            }
            if filename != item.filename:
                update["filename"] = filename
            # update item
            self.ingest_db.update_item(item.id, **update)

    def _after_complete(self):
        self.ingest_db.set_ingest_status(status=schemas.IngestStatus.in_review)
        if self.config.assume_yes:
            # ingest was started with assume yes so accept the review
            self.ingest_db.review_ingest()

    def _after_failed(self):
        self.ingest_db.fail_ingest()

    def _resolve_item_containers(self, item_context):
        last = None
        for c_level in schemas.ContainerLevel:
            if c_level.name in item_context:
                context = item_context[c_level.name]
                kwargs = {}
                if last:
                    kwargs["parent_id"] = last.id
                    kwargs["parent_path"] = last.path
                    kwargs["parent_dst_path"] = last.dst_path
                current = self._resolve_container(
                    c_level,
                    pickle.dumps(context),
                    **kwargs
                )
                if current:
                    last = current
                else:
                    break
        return last

    @functools.lru_cache(2 ** 16)
    def _resolve_container(self, c_level, context, parent_id=None, parent_path=None, parent_dst_path=None):
        context = pickle.loads(context)
        cid = context.get("_id")
        label = context.get("label")

        if not (cid or label):
            return None

        path = fs.path.combine(parent_path or "", utils.get_path_el(c_level, context))
        if path in self.visited:
            # already created container with this path
            return self.ingest_db.get_container_by_path(path)

        # create new container node
        child = schemas.ContainerIn(
            path=path,
            level=c_level,
            src_context=context,
        )

        if parent_id:
            child.parent_id = parent_id

        if not parent_id or parent_dst_path:
            # try to resolve if parent exists
            target, dst_files = None, None

            if cid:
                target, dst_files = self._find_child_by_path(c_level, path)
            elif label and not target:
                # lastly start resolve by label
                target, dst_files = self._find_child_by_path(c_level, path)

            if target:
                child.dst_context = self.get_dst_context(target)
                child.dst_context["files"] = dst_files
                child.dst_path = fs.path.combine(
                    parent_dst_path or "",
                    utils.get_path_el(c_level, child.dst_context, reverse=True)
                )

        self.visited.append(path)
        return self.ingest_db.create_container(child)

    def _find_child_by_path(self, container_type, path):
        """Attempt to find the child."""
        try:
            result = self.fw.resolve(fs.path.combine(path, "files"))
            container = result.path[-1]
            files = list(map(lambda f: f.name, result.children))
            log.debug(f"Resolve {container_type}: {path} - returned: {container.id}")
            return container, files
        except flywheel.ApiException:
            log.debug(f"Resolve {container_type}: {path} - NOT FOUND")
            return None, None

    @staticmethod
    def get_dst_context(container):
        """Get metadata from flywheel container object returned by sdk."""
        src = container.to_dict()
        ctx = {key: src.get(key) for key in CONTAINER_FIELDS if src.get(key)}
        ctx["_id"] = ctx.pop("id")
        return ctx


    @staticmethod
    def _get_filename(item, container):
        if item.type == schemas.ItemType.packfile:
            if container.dst_context:
                label = container.dst_context.get("label")
            else:
                label = container.src_context.get("label")
            packfile_name = str_to_filename(label)
            if item.context["packfile"]["type"] == "zip":
                filename = f"{packfile_name}.zip"
            else:
                filename = f"{packfile_name}.{item.context['packfile']['type']}.zip"
        else:
            filename = fs.path.basename(item.files[0])
        return filename
