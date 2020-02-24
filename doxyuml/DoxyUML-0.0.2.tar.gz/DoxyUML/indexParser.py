from xml.dom import minidom
from typing import List, Tuple
from .classParser import parse_class_file
from .classObj import ObjClass
import os


def parse_index(index: str):
    """
    Parse index file to get classes and namespace ids
    :param index: index.xml path
    :type index: str
    :return: classes and namespaces (name, refid)
    :rtype: List[Tuple[str, str]], List[Tuple[str, str]]
    """
    xml_doc = minidom.parse(index)

    compounds = xml_doc.getElementsByTagName('compound')

    classes = []
    namespaces = []

    for s in compounds:
        kind = s.attributes["kind"].value
        if kind in ["class","struct","interface","protocol","exception"]:
            # print(kind)
            # print(s.getElementsByTagName('name')[0].firstChild.nodeValue)
            classes.append((s.getElementsByTagName('name')[0].firstChild.nodeValue, s.attributes["refid"].value))
        if kind in ["namespace"]:
            # print(s.getElementsByTagName('name')[0].firstChild.nodeValue)
            namespaces.append((s.getElementsByTagName('name')[0].firstChild.nodeValue, s.attributes["refid"].value))

    return classes, namespaces


def parse_classes(class_list: List[Tuple[str, str]], doxy_root: str) -> List[ObjClass]:
    """
    Parse the classes xml
    :param class_list: the list of classes (name, refid) to parse
    :type class_list: List[Tuple[str, str]]
    :param doxy_root: the root path of the doxygen doc
    :type doxy_root: str
    :return: the classes objects in a list
    :rtype: List[ObjClass]
    """
    classes = []
    for clss in class_list:
        obj = parse_class_file(os.path.join(doxy_root, clss[1] + ".xml"))
        classes.append(obj)

    return classes


if __name__ == "__main__":
    index = "example/Cpp/Doxygen/xml/index.xml"
    doxy_root = os.path.dirname(index)
    classes, _ = parse_index(index)

    classes = parse_classes(classes, doxy_root)

    for clss in classes:
        print(clss)
