#!/usr/bin/env python3
from xml.dom import minidom, Node


def get_pretty_xml(node, indent=' ' * 4, newline='\n', xml_declaration=False):
    stripped = ''.join([x.strip() for x in node.toxml().split('\n')])
    parsed = minidom.parseString(stripped)
    prettified = parsed.toprettyxml(indent=indent, newl=newline)
    return prettified if xml_declaration else prettified[len('<?xml version="1.0" ?>'):]


def get_nodes(nodes, node_path, node_type=Node.ELEMENT_NODE):
    if not node_path:
        return nodes

    found_nodes = []
    ''.split('.', maxsplit=1)
    split = node_path.split('.', maxsplit=1)

    for node in nodes:
        for child in node.childNodes:
            if child.nodeType == node_type and child.tagName == split[0]:
                found_nodes.append(child)

    return get_nodes(found_nodes, split[1] if len(split) > 1 else '')


def get_text(node):
    if node.nodeType == Node.TEXT_NODE:
        return node.data
    if node.nodeType == Node.ELEMENT_NODE:
        return get_text(node.firstChild)
    return ''

