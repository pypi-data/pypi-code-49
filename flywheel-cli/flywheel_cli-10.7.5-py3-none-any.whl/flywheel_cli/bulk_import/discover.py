"""Provides Discover DiscoverQueue classes."""

import logging
from multiprocessing import current_process
from queue import Empty, LifoQueue

import fs

from ..walker import create_walker
from .db.models import IngestItem, ScanTask, TaskStatus
from .executor import AbstractQueue
from .template import TERMINAL_NODE
from .importers.config import create_config_from_dict
from .importers.factory import create_importer

log = logging.getLogger(__name__)


class DiscoverQueue(AbstractQueue):  # pylint: disable=too-few-public-methods
    """Class that wraps a DiscoverQueueMapper object and provides methods that necessary for the BulkImportExecutor."""

    def __init__(self, context):
        self.context = context

    def get(self):
        """Get an item from the scan queue table and create an executable task from it.

        Returns:
            Task -- Task object that can be executed.
        """
        worker_id = current_process().name
        task_item = self.context.discover_queue_mapper.get(worker_id)
        if task_item is not None:
            return Discover(task_item,
                            self.context.ingest_factory,
                            self.context.config)
        return None

class VisitTarget:
    """Provides functionality to visit a target"""

    def __init__(self, path, context, template_node):
        self.path = fs.path.forcedir(path)
        self.context = context
        self.template_node = template_node

    @property
    def is_packfile(self):
        """Target is packfile or not

        Returns:
            bool: True if packfile, False otherwise
        """
        return "packfile" in self.context or self.is_terminal

    @property
    def is_scanner(self):
        """Target is scanner or not

        Returns:
            bool: True if scanner, False otherwise
        """
        return not self.is_terminal and self.template_node.node_type == "scanner"

    @property
    def is_terminal(self):
        """Target is terminal node or not

        Returns:
            bool: True if terminal, False otherwise
        """
        return self.template_node in (None, TERMINAL_NODE)

    def visit(self, walker):
        """Visit this target. Find files and next targets

        Args:
            walker (AbstractWalker): Filesystem walker object

        Returns:
            tuple: First item is the found files, second the next targets
        """

        if self.is_scanner:
            return [], []

        found_files = {}
        next_targets = []
        max_depth = 1 if not self.is_packfile else None

        for root, dirs, files in walker.walk(self.path, max_depth=max_depth):
            parent_folder = fs.path.frombase(self.path, root)
            for f in files:
                file_path = fs.path.relpath(walker.combine(parent_folder, f.name))
                found_files.update({file_path: f})

            if self.is_packfile:
                continue

            for _dir in dirs:
                child_path = walker.combine(root, _dir.name)
                child_context = self.context.copy()
                next_node = self.template_node.extract_metadata(
                    _dir.name, child_context, walker, path=child_path
                )
                if next_node in (None, TERMINAL_NODE) and "packfile" not in child_context:
                    child_context["packfile"] = {
                        "type": _dir.name,
                    }

                if not child_context.get("ignore", False):
                    next_targets.append(VisitTarget(child_path, child_context, next_node))

        return found_files, next_targets


class Discover:
    """Discover a filesystem and create the appropriate ingest items and scan tasks."""
    def __init__(self, task_item, ingest_factory, config):
        self.task_item = task_item
        self.config = config
        self.items_mapper = ingest_factory.create_ingest_items_mapper()
        self.ingest_mapper = ingest_factory.create_mapper()
        self.discover_queue_mapper = ingest_factory.create_discover_queue_mapper()
        self.scan_queue_mapper = ingest_factory.create_scan_queue_mapper()

    def execute(self):
        """Execute task"""
        try:
            current_ingest = self.ingest_mapper.find(self.task_item.ingest_id)
            importer_config = create_config_from_dict(current_ingest.config["importer_config"])
            importer = create_importer(importer_config)
            importer.initialize()
            root_node = importer.root_node
            initial_context = importer.initial_context()
            walker = create_walker(importer.config.folder, **importer.config.generate_walker_kwargs())
            ingest_id = current_ingest.ingest_id
            self.discover(root_node, initial_context, walker, ingest_id)
            walker.close()
            self.discover_queue_mapper.update(self.task_item.task_id, status=TaskStatus.complete)
        except Exception as exc:  # pylint: disable=broad-except
            log.exception(exc)
            self.discover_queue_mapper.update(self.task_item.task_id, status=TaskStatus.failed)

    def discover(self, root_node, initial_context, walker, ingest_id):
        """Discover the given filesystem path."""
        queue = LifoQueue()

        # Add initial item
        queue.put(VisitTarget("/", initial_context, root_node))

        # visit all targets
        while True:
            try:
                target = queue.get(False)
                self.visit_target(target, queue, walker, ingest_id)
                queue.task_done()
            except Empty:
                break

    def visit_target(self, target, queue, walker, ingest_id):
        """Discover items in a given directory.
        Create new targets in the queue if necessary and create ingest items and scan tasks.

        Arguments:
            target     (VisitTarget): A target to visit
            queue      (LifoQueue): The queue object
            walker     (AbstractWalker): Filesystem walker object
            ingest_id  (int): Ingest operation id that discovered items relate to
        """
        files, next_targets = target.visit(walker)
        if target.is_packfile:
            packfile_size = sum(f.size for f in files.values())
            ingest_item = IngestItem(
                ingest_id=ingest_id,
                subdir=target.path,
                files=list(files.keys()),
                size=packfile_size,
                item_type="packfile",
                context=target.context
            )
            self.items_mapper.insert(ingest_item)
        elif target.is_scanner:
            scan_task = ScanTask(
                ingest_id=ingest_id,
                path=target.path,
                context=target.context,
                scanner_type=target.template_node.scanner_type
            )
            self.scan_queue_mapper.insert(scan_task)
        else:
            for filepath, f in files.items():
                ingest_item = IngestItem(
                    ingest_id=ingest_id,
                    subdir=target.path,
                    files=[filepath],
                    size=f.size,
                    item_type='file',
                    context=target.context
                )
                self.items_mapper.insert(ingest_item)


        for next_target in next_targets:
            queue.put(next_target)
