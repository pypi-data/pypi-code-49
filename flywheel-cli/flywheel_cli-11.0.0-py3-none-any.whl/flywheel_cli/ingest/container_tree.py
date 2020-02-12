"""Provides interface for container creation"""
import logging
import sys
import uuid

import crayons
import fs

log = logging.getLogger(__name__)


class ContainerNode:
    """Represents a container node in the hierarchy"""

    # pylint: disable=bad-continuation, too-few-public-methods, too-many-arguments
    def __init__(
        self,
        level,
        id_=None,
        parent=None,
        src_context=None,
        dst_context=None,
        dst_files=None,
        exists=False,
        bytes_sum=None,
        files_cnt=None,
    ):
        """Initialize ContainerNode"""
        self.id = id_ or uuid.uuid4()  # pylint: disable=invalid-name
        self.level = level
        self.parent = parent
        self.src_context = src_context
        self.dst_context = dst_context
        self.dst_files = dst_files or []
        self.exists = exists or dst_context
        self.children = []
        self.bytes_sum = bytes_sum or 0
        self.files_cnt = files_cnt or 0

    def __str__(self):
        context = self.dst_context or self.src_context
        label = context.get("label") or context.get("_id") or "NO_LABEL"
        filesize = fs.filesize.traditional(self.bytes_sum)
        plural = "s" if self.files_cnt > 1 else ""
        status = "using" if self.exists else "creating"
        parts = [f"{crayons.blue(label)}"]
        if self.bytes_sum and self.files_cnt:  # container w/ files
            parts.append(f"({filesize} / {self.files_cnt} file{plural})")
        elif self.bytes_sum:  # file
            parts.append(f"({filesize})")
        parts.append(f"({status})")
        return " ".join(parts)


class ContainerTree:
    """Container tree class"""

    def __init__(self):
        """Build a container tree which can be printed"""
        # The root container
        self.root = ContainerNode("root", exists=True)
        self.nodes = {
            self.root.id: self.root,
        }

    def add_node(self, id_, parent, level, **kwargs):
        """Rebuild the hierarchy by adding nodes one by one."""
        if id_ in self.nodes:
            return
        node = ContainerNode(id_=id_, level=level, **kwargs)
        self.nodes[node.id] = node
        parent_node = self.nodes[parent] if parent else self.root
        parent_node.children.append(node)
        node.parent = parent_node
        # populate size to parents
        current = parent_node
        while current:
            current.bytes_sum += node.bytes_sum
            current = current.parent
        # track total file count on root node
        self.root.files_cnt += node.files_cnt

    def print_tree(self, fh=sys.stdout):
        """Print hierarchy"""
        utf8 = fh.encoding == "UTF-8"
        none_str = "│  " if utf8 else "|  "
        node_str = "├─ " if utf8 else "|- "
        last_str = "└─ " if utf8 else "`- "

        def pprint_tree(node, prefix="", last=True):
            print(prefix, last_str if last else node_str, node, file=fh, sep="")
            prefix += "   " if last else none_str
            child_count = len(node.children)
            children = node.children
            for i, child in enumerate(children):
                last = i == (child_count - 1)
                pprint_tree(child, prefix, last)

        for child in self.root.children:
            pprint_tree(child)
