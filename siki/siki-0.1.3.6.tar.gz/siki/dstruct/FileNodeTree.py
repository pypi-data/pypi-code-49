#!/bin/env python3
"""
It will try to create a file structure consistent 
with the source code structure to hold the required header files
"""

from siki.basics import FileUtils as fu
from siki.basics import Exceptions as exceptions
from siki.basics import SystemUtils as su

class FileNodeTree(object):
    """
    Create a file structure tree and hold the file pathes
    """

    def __init__(self, name="", root=None, leaves=None):
        
        if root is None:
            root = self
        
        if root is not None and type(root) is not FileNodeTree:
            raise exceptions.NullPointerException("root is invalid data type")
        
        if name is None or type(name) is not str:
            raise exceptions.NullPointerException("name cannot be null or invalid data type")
        
        # assign root and leaves to node   
        self.root = None # FileNodeTree type
        self.name = name # string type
        self.leaves = [] # list of FileNodeTree
        
        if leaves is not None and len(leaves) > 0:
            for leaf in leaves:
                self.append_node(leaf)
                
    
    def append_node(self, leaf):
        """
        append leaf to root node
        @param leaf: type of FileNodeTree
        """
        if leaf is None or type(leaf) is not FileNodeTree:
            raise exceptions.InvalidParamException("leaf cannot be null or invalid data type")
        
        # indicate the leaf root to the current root
        leaf.root = self 
        
        # append the leaf
        self.leaves.append(leaf)
        
    
    def delete_node(self, leafname):
        """
        delete a leaf from root node
        @param leaf: the leaf name, string type
        """
        if self.leaves_count() <= 0:
            return None
        
        leaf = self.search_name(leafname)
        if leaf is None:
            # for debug only
            print("nothing could be deleted")
            return None
        else:
            # the root of leaf
            root = leaf.root
            
            if root is None: # delete the root node
                print("root node can not be deleted")
                return self
                
            # delete a leaf in file tree
            if leaf.leaves_count() > 0: # has children leaves, must merge them to the root
                for l in leaf.leaves:
                    root.append_node(l) 
            
            # now remove the node from root
            root.leaves.remove(leaf)
            return leaf
    

    def search_node(self, node, root=None):
        """
        search a leaf from root node, some kind of traversal
        @param node: the node desired, FileNodeTree type
        @param root: traversal from the root node, default is none
        """

        if root is None:
            root = self
        
        if root.leaves_count() <= 0:
            return None
        
        if self == node:
            return self
        
        for leaf in root.leaves:
            if leaf == node: # found the leaf
                return leaf
            
            if leaf.leaves_count() > 0: # traversal the tree by deep search first
                ret = leaf.search_node(node, leaf)
                if ret is not None:
                    return ret
        
        # nothing found
        return None

        
    def search_name(self, leafname, root=None):
        """
        search a leaf from root node, some kind of traversal
        @param leafname: the leaf name, string type
        @param root: traversal from the root node, default is none
        """
        
        if root is None:
            root = self
        
        if root.leaves_count() <= 0:
            return None
        
        if self.name == leafname:
            return self
        
        for leaf in root.leaves:
            if leaf.name == leafname: # found the leaf
                return leaf
            
            if leaf.leaves_count() > 0: # traversal the tree by deep search first
                ret = leaf.search_name(leafname, leaf)
                if ret is not None:
                    return ret
        
        # nothing found
        return None
    
    
    def search_subnode(self, leafname):
        """
        search a sub node from the next leaves, without tree traversal
        """
        for leaf in self.leaves:
            if leaf.name == leafname:
                return leaf
        return None
        
    
    
    def delete_subtree(self, nodename, node=None):
        """
        delete a subtree from root
        @param nodename: the sub node tree which want to delete
        @param node: traversal from the root node, default is none
        """
    
        if node is None:
            node = self
            
        # root node of current node
        root = node.root
        
        # could delete root node by using this method
        if root is None:
            if nodename == node.name:
                print("could not delete the tree node")
                return node;
                
        # sub leaves and sub-root
        if node.name == nodename: # find out the node
            if node.leaves_count() > 0:
                root.leaves.remove(node)
                return node
            
        # else traversal the tree
        for leaf in node.leaves:
            tree = leaf.delete_subtree(nodename, leaf)
            if tree is not None:
                return tree
            
            
    def merge_subtree(self, treeToMerge, ourTree=None):
        """
        @param tree_to_merge: the tree to merge 
        @param tree: our tree, default is none 
        """
        
        # invalid situation
        if treeToMerge is None:
            return None
        
        # set the node to it self
        if ourTree is None:
            ourTree = self # link from top
        
        # merge subtree to tree
        ourLeavesNames = ourTree.leaves_names()
        if ourTree.name != treeToMerge.name:
            if treeToMerge.name not in ourLeavesNames:
                ourTree.append_node(treeToMerge) # append tree to our tree
                return ourTree
                
        for subtree in treeToMerge.leaves:
            if subtree.name not in ourLeavesNames:
                ourTree.append_node(subtree)
            else:
                treeToMerge = subtree
                ourSubTree = ourTree.search_subnode(subtree.name)
                if ourSubTree is not None:
                    ourSubTree.merge_subtree(treeToMerge, ourSubTree)

        return ourTree
                    
                    
    def generate_path(self):
        """
        re-generate file path
        """
        path = ""
        sep = ""
        
        # determine the separator
        if su.is_windows():
            sep = "\\"
        else: # Linux and MacOS shares the same separator
            sep = "/"
            
        # step by step, and back to the upper node to generate the file path
        # path could be absolute path and relative path
        root = self
        
        while root is not None:
            path = sep + root.name + path
            root = root.root

        # delete the first separator
        path = path[1:]
        
        # return to caller
        return path


    def only_files(self, nmode=False, root=None):
        """
        traversal and generate a list with files only    
        """
        flist = []
        if root is None:
            root = self
        
        if len(root.leaves) > 0:
            for node in root.leaves:
                path = node.generate_path()
                if fu.isfile(path):
                    if nmode:
                        flist.append(node)
                    else:
                        flist.append(path)
                else:
                    sub_flist = node.only_files(nmode, node)
                    if len(sub_flist) > 0:
                        flist.extend(sub_flist)
        else:
            path = self.generate_path()
            if fu.isfile(path):
                if nmode:
                    flist.append(self)
                else:
                    flist.append(path)

        return flist

    
    def only_dirs(self, nmode=False, root=None):
        """
        traversal and generate a list with dirs only
        """
        dlist = []
        if root is None:
            root = self
        
        if len(root.leaves) > 0:
            for node in root.leaves:
                path = node.generate_path()
                if fu.isdir(path):
                    if nmode:
                        dlist.append(node)
                    else:
                        dlist.append(path)
                    if len(node.leaves) > 0:
                        sub_dlist = node.only_dirs(nmode, node)
                        if len(sub_dlist) > 0:
                            dlist.extend(sub_dlist)
        else:
            path = self.generate_path()
            if fu.isdir(path):
                if nmode:
                    dlist.append(self)
                else:
                    dlist.append(path)

        return dlist


    
    def leaves_count(self):
        """
        return the leaves count
        """
        return len(self.leaves)
    
    
    def print_leaves(self, node=None):
        """
        for debug only, print out the structure of file directories
        """
        if node == None:
            node = self
        
        # print out the message of current node
        leaves_count = node.leaves_count()
        node.print_self()
        
        for leaf in node.leaves:
            if leaf.leaves_count() > 0:
                node.print_leaves(leaf)
                
                
                
    def print_self(self, node=None):
        """
        for debug only, print out the node itself's information
        """
        if node is None:
            node = self
        
        # leaves count
        leaves_count = node.leaves_count()
        
        # root node
        root = node.root
        
        if root is None:
            # debug message
            print("root node(", node.name, "), with", leaves_count, "leaves: [", node.leaves_names(), "]")
        else:
            print("leaf node(", node.name, "), with", leaves_count, "sub-leaves: [", node.leaves_names(), "]")
        
    
    def leaves_names(self):
        """
        generate a list with names of leaves
        """
        leaves_name_list = []
        if self.leaves_count() > 0:
            for leaf in self.leaves:
                leaves_name_list.append(leaf.name)
        return ", ".join(leaves_name_list)