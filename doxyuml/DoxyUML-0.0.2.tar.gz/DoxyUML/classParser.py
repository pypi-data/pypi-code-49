from xml.dom import minidom

from .classObj import ObjClass, Attribute
from .commonParser import parse_operation


def parse_attribute(member: minidom.Element):
    """
    Parse a xml element and create a Member class with it
    :param member: a xml element describing a class attribute (member)
    :return: a Attribute class object, a list of aggregations refid and a list of composition refid
    """

    mem_name = member.getElementsByTagName("name")[0].firstChild.nodeValue
    mem_privacy = member.getAttribute("prot")
    mem_type = ""

    aggreg = []
    compo = []
    for type in member.getElementsByTagName("type"):
        ref = type.getElementsByTagName("ref")
        if len(ref) > 0:
            ref = ref[0]
            mem_type = ref.firstChild.nodeValue
            if ref.hasAttribute("type"):
                if ref.getAttribute("type") in ["*","&","_ptr","pointer"]:
                    aggreg.append(ref.getAttribute("refid"))
            else:
                compo.append(ref.getAttribute("refid"))
        else:
            mem_type = type.firstChild.nodeValue

    res = Attribute(mem_name, mem_privacy, mem_type)
    brief_desc = ""
    desc = member.getElementsByTagName("briefdescription")
    if len(desc) > 0:
        desc = desc[0].getElementsByTagName("para")
        if len(desc) > 0:
            desc = desc[0].firstChild.nodeValue
            brief_desc = desc
    res.brief_desc = brief_desc
    return res, aggreg, compo


def parse_class_file(file: str):
    """
    Parse a class xml file
    :param file: the file to parse
    :return: an class object describing the parsed class
    """
    xml_doc = minidom.parse(file)

    compounddef = xml_doc.getElementsByTagName('compounddef')[0]
    refid = compounddef.attributes["id"].value

    class_name = compounddef.getElementsByTagName("compoundname")[0].firstChild.nodeValue
    obj_class = ObjClass(refid, class_name)

    stereotype = ""
    kind = compounddef.attributes["kind"].value
    if kind in ["interface","protocol","exception"]:
        stereotype = kind
    if compounddef.hasAttribute("abstract"):
        if compounddef.attributes["abstract"].value == "yes":
            if len(stereotype) > 0:
                stereotype = "abstract "+stereotype
            else:
                stereotype = "abstract"

    obj_class.stereotype = stereotype

    gens = []
    basecompounds = compounddef.getElementsByTagName("basecompoundref")
    for cop in basecompounds:
        if cop.hasAttribute("refid"):
            gen_refid = cop.attributes["refid"].value
            gens.append(gen_refid)
    obj_class.add_generalizations(gens)

    sections = compounddef.getElementsByTagName("sectiondef")
    # print("nb section", len(sections))
    for i,section in enumerate(sections,0):
        # print("Section",i)
        for member in section.getElementsByTagName("memberdef"):
            if member.attributes["kind"].value in ["property","variable"]:
                # print("  do_attribute",member.getElementsByTagName("name")[0].firstChild.nodeValue)
                att, agg, comp = parse_attribute(member)
                obj_class.add_attributes([att])
                obj_class.add_aggregations([agg])
                obj_class.add_compositions([comp])
            elif member.attributes["kind"].value in ["event","function","signal","prototype","friend","slot"]:
                # print("  do_operation", member.getElementsByTagName("name")[0].firstChild.nodeValue)
                obj_class.add_operations(parse_operation(member))

    return obj_class


if __name__ == "__main__":
    class_file = "example/Cpp/Doxygen/xml/class_geometry_1_1_rectangle.xml"

    obj = parse_class_file(class_file)
    print(obj)

