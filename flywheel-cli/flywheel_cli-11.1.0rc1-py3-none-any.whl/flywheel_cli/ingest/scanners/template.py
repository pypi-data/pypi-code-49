"""Provides TemplateScanner class"""

import copy
import logging
from collections import deque

import fs

from ..strategies.factory import create_ingest_strategy
from ..template import TERMINAL_NODE
from .. import schemas
from .abstract import AbstractScanner

log = logging.getLogger(__name__)


class TemplateScanner(AbstractScanner):
    """Template scanner"""

    def _scan(self, dirpath):
        import_strategy = create_ingest_strategy(self.config.strategy_type, self.config)
        import_strategy.initialize()
        initial_context = import_strategy.initial_context()
        root_node = import_strategy.root_node

        prev_dir = None
        prev_node = root_node
        prev_context = copy.deepcopy(initial_context)
        files = {}

        if root_node.node_type == "scanner":
            for item in self.create_task_or_item(dirpath, root_node, initial_context, {}):
                yield item
            return
        # TODO: determine according to the hierarcy how walk the input folder
        for fileinfo in self.walker.list_files(dirpath):
            context = copy.deepcopy(initial_context)
            path_parts = deque(fileinfo.name.split("/"))
            node = root_node
            parent_dirpath = "/"
            while len(path_parts) > 1:
                dirname = path_parts.popleft()
                parent_dirpath = fs.path.combine(parent_dirpath, dirname)
                node = node.extract_metadata(
                    dirname, context, self.walker, path=parent_dirpath
                )
                if node in (None, TERMINAL_NODE):
                    break

            if prev_dir and prev_dir != parent_dirpath:
                for item in self.create_task_or_item(prev_dir, prev_node, prev_context, files):
                    yield item
                files = {}

            rel_filepath = fs.path.join(*path_parts)
            files[rel_filepath] = fileinfo
            prev_dir = parent_dirpath
            prev_node = node
            prev_context = context

        for item in self.create_task_or_item(prev_dir, prev_node, prev_context, files):
            yield item

    def create_task_or_item(self, dirpath, node, context, files):
        """Create ingest item or scan task according to the node type"""
        if node not in (None, TERMINAL_NODE) and node.node_type == "scanner":
            scan_context = copy.deepcopy(context)
            scan_context["scanner"] = {
                "type": node.scanner_type,
                "dir": dirpath,
                "opts": node.opts,
            }
            yield schemas.TaskIn(
                type=schemas.TaskType.scan,
                context=scan_context,
            )
            return

        # Merge subject and session if one of them is missing
        if self.config.no_subjects or self.config.no_sessions:
            self.context_merge_subject_and_session(context)

        if node in (None, TERMINAL_NODE) and "packfile" in context:
            packfile_size = sum(f.size for f in files.values())
            yield schemas.ItemIn(
                type="packfile",
                dir=dirpath,
                files=list(files.keys()),
                files_cnt=len(files),
                bytes_sum=packfile_size,
                context=context,
            )
        else:
            for filepath, fileinfo in files.items():
                yield schemas.ItemIn(
                    type="file",
                    dir=dirpath,
                    files=[filepath],
                    files_cnt=1,
                    bytes_sum=fileinfo.size,
                    context=context,
                )
