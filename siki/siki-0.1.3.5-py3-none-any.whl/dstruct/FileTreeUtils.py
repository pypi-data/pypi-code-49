#!/bin/env python3
"""
This file provides extension methods of FileNodeTree
"""

from siki.basics import FileUtils as fu
from siki.basics import SystemUtils as su
from siki.basics import Exceptions as excepts
from FileNodeTree import FileNodeTree

def _convert_path(path):
    if not fu.exists(path):
        raise excepts.InvalidParamException("path is not valid")

    if su.is_windows():
        return path.split("\\")
    else:
        return path.split("/")


def _merge_to_tree(f_tokens, main_tree):
    if len(f_tokens) <= 0:
        return None # do nothing

    tree = None
    for token in f_tokens:
        node = FileNodeTree(token)

        if tree is not None:
            tree.append_node(node)
        
        tree = node

    if tree is None:
        print("tree is NONE!")

    if main_tree is None:
        print("main tree is NONE!")

    # back to the top
    while tree.root is not None:
        tree = tree.root

    if type(main_tree) is FileNodeTree:
        main_tree.merge_subtree(tree)
    else:
        raise InvalidParamException("main_tree is not FileNodeTree")


def traversal_dir(path, pattern="*"):
    """
    @param path: path to traversal or scanning
    @return: FileNodeTree with dirs and files 
    """

    files = fu.search_files(path, pattern)

    if len(files) <= 0:
        return None # do nothing

    # file tree
    tree = FileNodeTree(_convert_path(path)[0])

    # append files to tree
    for f in files:
        _merge_to_tree(_convert_path(f), tree)

    return tree


def generate_list(tree):
    """
    generate a list from tree
    """
    #pattern = re.compile(pattern)
    pathes = []
    
    if len(tree.leaves) > 0: # has children
        for leaf in tree.leaves:
            if len(leaf.leaves) <= 0:
                pathes.append(leaf.generate_path())
            else:
                sub_pathes = generate_list(leaf)
                pathes.extend(sub_pathes)
    else:
        pathes.append(tree.generate_path())
    
    return pathes


def copy_tree(tree):

    # create a main node with the same name of tree
    mainTree = FileNodeTree(tree.name)

    for leaf in tree.leaves:
        if len(leaf.leaves) > 0:
            subTree = copy_tree(leaf)
            mainTree.append_node(subTree)
        else:
            subLeaf = FileNodeTree(leaf.name)
            mainTree.append_node(subLeaf)
    
    return mainTree



if __name__ == "__main__":
    tree = None

    if su.is_windows():
        tree = traversal_dir(r"D:\Repository\Siki", r"\.py$")
    else:
        tree = traversal_dir("/mnt/d/Repository/Siki", r"\.py$")

    files = tree.only_files()
    for f in files:
        print(f)