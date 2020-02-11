#!/usr/bin/env python3
import traceback
import sys
from dogtail.tree import root
from qecore.utility import QE_DEVELOPMENT

if QE_DEVELOPMENT:
    try:
        from termcolor import colored
    except ModuleNotFoundError:
        QE_DEVELOPMENT = False


class GetNode:
    def __init__(self, context, name, role_name, description,
                 m_btn, attr, a11y_root_name, retry, expect_positive):
        """
        Initiate GetNode instance.
        Workhorse for most of the :py:mod:`common_steps`.

        :type context: <behave.runner.Context>
        :param context: Context object that is passed from common steps.

        :type name: str
        :param name: Node.name

        :type role_name: str
        :param role_name: Node.roleName

        :type description: str
        :param description: Node.description

        :type m_btn: str
        :param m_btn: Mouse click after node identification.
            Accepted values are "Left", "Middle" and "Right".

        :type attr: str
        :param attr: Node identification: attribute.
            The most used options are: ["showing", "visible", "checked", "focused", "sensitive"]

        :type intance_root_name: str
        :param intance_root_name: Application name.
            Application name to be found in context.<app_name> or in accessibility tree.
            If search of accessibility tree fails the context object will be examined
            for Application instance.

        :type retry: bool
        :param retry: Option to give search function to look again a few times if search fails.
            Used for slower applications. User might want to click right away but window can
            have a few secods delay.

        :type expect_positive: bool
        :param expect_positive: Option to pass the common step call if the node is not found.
            Some steps might want the node not to be found.

        .. note::

            This class serves only for the purposes of the :py:mod:`common_steps` implementation.
        """

        a11y_roots = {x.name: x for x in root.applications()}

        if a11y_root_name in a11y_roots:
            self.root = a11y_roots[a11y_root_name]
        elif a11y_root_name is not None and hasattr(context, a11y_root_name):
            self.root = getattr(context, a11y_root_name).instance
        else:
            self.root = None

        if self.root is None:
            try:
                self.root = context.sandbox.default_application.instance
            except AttributeError:
                assert False, "".join((
                    "\nYou need to define a default application ",
                    "if you are using steps without root."
                ))

        mouse_map = {
            "Left": 1,
            "Middle": 2,
            "Right": 3,
            "None": None
        }
        try:
            self.m_btn = mouse_map[str(m_btn)]
        except KeyError:
            assert False, "\nUnknown mouse button! Check your feature file!"

        self.name = ("".join(name) if name != "Empty" else "") \
            if name != "None" else None
        self.role_name = ("".join(role_name) if role_name != "Empty" else "") \
            if role_name != "None" else None
        self.description = None if description is None else "".join(description) \
            if description != "Empty" else ""

        defined_attributes = ["showing", "visible", "checked", "focused", "sensitive"]
        self.attr = attr if attr in defined_attributes else None if attr is None else False
        assert self.attr is not False, "\n".join((
            "\nUnknown attribute. Check your feature file!",
            f"Attributes defined are {str(defined_attributes)}."
        ))

        self.retry = retry if isinstance(retry, bool) else None
        assert self.retry is not None, "\nUnknown retry state. Check your feature file!"

        self.expect_positive = expect_positive if isinstance(expect_positive, bool) else None
        assert self.expect_positive is not None, "".join((
            f"\nUnknown expect_positive state: {self.expect_positive}. ",
            f"Check your feature file!"
        ))


    def __enter__(self):
        try:
            found_node = self.root.findChild(lambda x: \
                ((not self.name is not None) or self.name in repr(x.name)) and \
                ((not self.role_name is not None) or self.role_name == x.roleName) and \
                ((not self.description is not None) or self.description in x.description) and \
                ((not self.attr is not None) or getattr(x, self.attr)) and \
                x.position[0] >= 0 and \
                x.size[0] > 0, \
                retry=self.retry)
        except Exception as error:
            if self.expect_positive:
                assert False, get_error_message(self, error)
            else:
                found_node = None
        return (self, found_node)


    def __exit__(self, exc_type, exc_value, trcb):
        if exc_type is not None:
            traceback.print_exc(file=sys.stdout)
            return False
        return True


def get_center(node):
    """
    Simple utility to get the center of the node.

    :type node: <dogtail.tree.Node>
    :param node: Node passed to the function.

    :rtype: tuple
    :return: Tuple with coordinates of the center of a Node.
    """
    return (node.position[0] + node.size[0]/2, node.position[1] + node.size[1]/2)


def get_formated_duplicates(list_size, list_of_duplicates, attr):
    """
    Take list of duplicates and format them for error message.

    :type list_size: int
    :param list_size: Size of the list_of_duplicates.

    :type list_of_duplicates: list
    :param list_of_duplicates: List of Nodes to handle for error message.

    :type attr: string
    :param attr: Node passed to the function.

    :rtype: string
    :return: Formatted string output.

    .. note::

        This serves only for the purpose of formatted error message upon search fail.
        Used by :py:func:`get_error_message`.
    """

    return "".join(sorted(set(["\t{0}: '{1}' {2}: '{3}' {4}: '{5}' {6}: '{7}' {8}: '{9}'\n".format(
        colored("name", "yellow") if QE_DEVELOPMENT else "name", repr(node.name),
        colored("roleName", "yellow") if QE_DEVELOPMENT else "roleName", node.roleName,
        colored("position", "yellow") if QE_DEVELOPMENT else "position", node.position,
        colored("size", "yellow") if QE_DEVELOPMENT else "size", node.size,
        colored(f"{attr}", "yellow") if QE_DEVELOPMENT else f"{attr}" \
            if attr else "attribute", getattr(node, attr) if attr else "None") \
    for node in list_of_duplicates]), key=str.lower)) if list_size != 0 else "\tNone\n"


def get_formated_error_message(error,
                               node_name, same_name_items,
                               node_role_name, same_role_name_items):
    """
    Take lists of duplicates with name and roleName and format them for error message.

    :type error: string
    :param error: Error - reason why the search for Node failed.

    :type node_name: string
    :param node_name: Node.name that was searched for.

    :type same_name_items: list
    :param same_name_items: List of all items with the name node_name.

    :type node_role_name: string
    :param node_role_name: Node.roleName that was searched for.

    :type same_role_name_items: list
    :param same_role_name_items: List of all items with the roleName node_role_name.

    :rtype: string
    :return: Formatted string output of all :py:func:`get_formated_duplicates`

    .. note::

        This serves only for the purpose of formatted error message upon search fail.
        Used by :py:func:`get_error_message`.
    """

    return "".join(["\n\n{0}: {1}\n\n{2}: {3}:\n{4}\n{5}: {6}:\n{7}\n".format(
        colored("Item was not found", "yellow", attrs=["bold"]) \
            if QE_DEVELOPMENT else "Item was not found", error,
        colored("Items with name", "yellow", attrs=["bold"]) \
            if QE_DEVELOPMENT else "Items with name", repr(node_name), same_name_items,
        colored("Items with roleName", "yellow", attrs=["bold"]) \
            if QE_DEVELOPMENT else "Items with roleName", node_role_name, same_role_name_items)])


def get_error_message(node, error):
    """
    Main handler for error message with :py:func:`get_formated_error_message` and
    :py:func:`get_formated_duplicates` being used to get desired result.

    :type node: GetNode
    :param node: Instanced GetNode to have all data needed about the error.

    :type error: string
    :param error: Error message as to why the search failed.

    .. note::

        This serves only for the purpose of formatted error message upon search fail
        when using :py:mod:`common_steps`.
    """

    nodes_with_name = node.root.findChildren(lambda x: \
        node.name in x.name and (not (node.name != "") or x.name != ""))
    nodes_with_name_size = len(nodes_with_name)
    nodes_with_name_formatted = get_formated_duplicates(nodes_with_name_size,
                                                        nodes_with_name,
                                                        node.attr)

    nodes_with_role_name = node.root.findChildren(lambda x: x.roleName == node.role_name)
    nodes_with_role_name_size = len(nodes_with_role_name)
    nodes_with_role_name_formatted = get_formated_duplicates(nodes_with_role_name_size,
                                                             nodes_with_role_name,
                                                             node.attr)

    return get_formated_error_message(error,
                                      node.name,
                                      nodes_with_name_formatted,
                                      node.role_name,
                                      nodes_with_role_name_formatted)
