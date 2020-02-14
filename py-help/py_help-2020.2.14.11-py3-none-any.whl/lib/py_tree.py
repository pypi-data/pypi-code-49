# coding=utf-8
import yaml
import os
import codecs
from .CommonLogger import debug, info
from .path_helper import PathHelper
import collections

(S, T) = range(2)


class PyTree(object):
    """
        A Python implementation of Tree data structure
    """

    def __init__(self, key_path="/", data=None, children=None):
        """
        @param data: content of this node
        @param children: sub node(s) of Tree, could be None, child (single) or children (multiple)
        """
        self.data = data
        names_array = key_path.split('/')
        self.name = names_array[-1]
        self.url = key_path
        self.__children = {}
        self.cache_dict = {}
        self.__parent = None  # private parent attribute

        if children:  # construct a Tree with child or children
            if isinstance(children, PyTree):
                self.__children[children.name] = children
                children.__parent = self

            elif isinstance(children, collections.Iterable):
                for child in children:
                    if isinstance(child, PyTree):
                        self.__children[child.name] = child
                        child.__parent = self
                    else:
                        raise TypeError('Child of Tree should be a Tree type.')
            else:
                raise TypeError('Child of Tree should be a Tree type')

    def __setattr__(self, name, value):

        """
            Hide the __parent and __children attribute from using dot assignment.
            To add __children, please use addChild or addChildren method; And
            node's parent isn't assignable
        """

        if name in ('parent', '__parent', 'children'):
            raise AttributeError("To add children, please use addChild or addChildren method.")
        else:
            super(PyTree, self).__setattr__(name, value)

    def __str__(self, *args, **kwargs):
        return "{}--{}".format(self.name, self.data)

    def add_child(self, child):
        """
            Add one single child node to current node
        """
        if isinstance(child, PyTree):
            self.__children[child.name] = child
            child.__parent = self
        elif isinstance(child, list):
            for one_child in child:
                if isinstance(one_child, PyTree):
                    self.__children[one_child.name] = one_child
                    one_child.__parent = self
                else:
                    raise TypeError('Child of Tree should be a Tree type.')
        else:
            raise TypeError('Child of Tree should be a Tree type')

    def get_parent(self):
        """
            Get node's parent node.
        """
        return self.__parent

    def get_child(self, child_name):
        if len(child_name) == 0:
            return self
        return self.__children.get(child_name)

    def get_children(self):
        """
            Get node's all child nodes.
        """
        return self.__children

    def add_by_url(self, url_list, node_data=None):
        """
            用URL来添加对象
        """
        check_node = self.get_root()
        if isinstance(url_list, str):
            url_list = url_list.split('/')
        for idx in range(len(url_list)):
            one_name = url_list[idx]
            one_child = check_node.get_child(one_name)
            if one_child is None:
                key_path = '{}/{}'.format("/".join(url_list[0:idx]), one_name)
                if idx == len(url_list) - 1:
                    the_node = PyTree(key_path, node_data)
                else:
                    the_node = PyTree(key_path)
                check_node.add_child(the_node)
                check_node = the_node
            else:
                if idx == len(url_list) - 1:
                    one_child.data = node_data
                check_node = one_child
        return check_node

    def get_by_url(self, url_list):
        if isinstance(url_list, str):
            url_list = url_list.split('/')
        if len(url_list[0]) == 0:
            debug("从根开始获取url: {}".format(url_list))
            check_node = self.get_root()
            url_list.pop(0)
        else:
            check_node = self
        result_node = None
        for idx in range(len(url_list)):
            one_name = url_list[idx]
            if one_name == '..':
                result_node = check_node.get_parent()
            elif one_name == '.':
                result_node = check_node
            else:
                result_node = check_node.get_child(one_name)
            if result_node is None:
                debug("没有找到 {} -> {} 的节点".format(url_list, one_name))
                break
            else:
                check_node = result_node
        return result_node

    def get_sub_tree_dict_by_url(self, url_list, key_name='name'):
        the_node = self.get_by_url(url_list)
        if the_node is not None:
            return the_node.get_sub_tree_dict(key_name)
        else:
            debug("获取不到url_list:{} 的节点".format(url_list))
            return None

    def get_sub_tree_dict(self, key_name='name'):
        if self.data is not None:
            if isinstance(self.data, str):
                result_dict = {'data': self.data}
            else:
                result_dict = dict(self.data)
        else:
            result_dict = {}
        result_dict[key_name] = self.name
        the_children_list = []
        for v in self.__children.values():
            the_children_list.append(v.get_sub_tree_dict())
        result_dict['children'] = the_children_list
        return result_dict

    def get_root(self):
        """
            Get root of the current node.
        """
        if self.is_root():
            return self
        else:
            return self.get_parent().get_root()

    def is_root(self):
        """
            Determine whether node is a root node or not.
        """
        if self.__parent is None:
            return True
        else:
            return False

    def is_leaf(self):
        """
            Determine whether node is a leaf node or not.
        """
        if len(self.__children) == 0:
            return True
        else:
            return False

    def pretty_tree(self):
        """"
            Another implementation of printing tree using Stack
            Print tree structure in hierarchy style.
            For example:
                Root
                |___ C01
                |     |___ C11
                |          |___ C111
                |          |___ C112
                |___ C02
                |___ C03
                |     |___ C31
            A more elegant way to achieve this function using Stack structure,
            for constructing the Nodes Stack push and pop nodes with additional level info.
        """

        level = 0
        nodes_s = [self, level]  # init Nodes Stack
        result_str = ''

        while nodes_s:
            # head pointer points to the first item of stack, can be a level identifier or tree node
            head = nodes_s.pop()
            if isinstance(head, int):
                level = head
            else:
                result_str += self.__print_label__(head, nodes_s, level)
                children = head.get_children()

                if nodes_s:
                    nodes_s.append(level)  # push level info if stack is not empty

                if children:  # add children if has children nodes
                    nodes_s.extend(children.values())
                    level += 1
                    nodes_s.append(level)
        return result_str

    def nested_tree(self):
        """"
            Print tree structure in nested-list style.
            For example:
            [0] nested-list style
                [Root[C01[C11[C111,C112]],C02,C03[C31]]]
            """

        nested_t = ''
        delimiter_o = '['
        delimiter_c = ']'
        nodes_s = [delimiter_c, self, delimiter_o]

        while nodes_s:
            head = nodes_s.pop()
            if isinstance(head, str):
                nested_t += head
            else:
                nested_t += str(head.data)

                children = head.getChildren()

                if children:  # add children if has children nodes
                    nodes_s.append(delimiter_c)
                    for child in children.values():
                        nodes_s.append(child)
                        nodes_s.append(',')
                    nodes_s.pop()
                    nodes_s.append(delimiter_o)

        return nested_t

    def __print_label__(self, head, nodes_stack, level):
        """
           Print each node
        """
        leading = ''
        lasting = '|___ '

        if level == 0:
            return "{}\n".format(head)
        else:
            for l in range(0, level - 1):
                sibling = False
                parent_t = head.__get_parent__(level - l)
                for c in parent_t.get_children():
                    if c in nodes_stack:
                        sibling = True
                        break
                if sibling:
                    leading += '|     '
                else:
                    leading += '     '

            return '{0}{1}{2}\n'.format(leading, lasting, head)

    def __get_parent__(self, up):
        parent = self
        while up:
            parent = parent.get_parent()
            up -= 1
        return parent
