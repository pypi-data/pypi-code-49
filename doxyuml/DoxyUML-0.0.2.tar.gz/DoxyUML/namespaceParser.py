from xml.dom import minidom
from .namespaceObj import Namespace
from .commonParser import parse_operation


def parse_namespace_file(file: str):
    """
    Parse a namespace xml file
    :param file: the file to parse
    :return: a namespace object describing the parsed class
    """

    xml_doc = minidom.parse(file)
    compounddef = xml_doc.getElementsByTagName('compounddef')[0]
    refid = compounddef.attributes["id"].value

    ns_name = compounddef.getElementsByTagName("compoundname")[0].firstChild.nodeValue

    ns = Namespace(refid, ns_name)

    for inner_class in compounddef.getElementsByTagName("innerclass"):
        ns.add_class(inner_class.attributes["refid"].value)

    for memberdef in compounddef.getElementsByTagName("memberdef"):
        ns.add_func(parse_operation(memberdef))

    return ns


if __name__ == "__main__":
    namespace_file = "example/Cpp/Doxygen/xml/namespace_geometry.xml"

    obj = parse_namespace_file(namespace_file)
    print(obj)
