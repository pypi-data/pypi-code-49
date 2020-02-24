from xml.dom import minidom
from .classObj import Operation, XRefSect


def parse_operation(member: minidom.Element):
    """
    Parse a xml element and create an Operation class with it
    :param member: a xml element describing a class attribute (member)
    :return:
    """

    mem_name = member.getElementsByTagName("name")[0].firstChild.nodeValue
    mem_privacy = member.getAttribute("prot")
    mem_type = "void"
    if member.getElementsByTagName("type")[0].firstChild is not None:
        mem_type = member.getElementsByTagName("type")[0].firstChild.nodeValue

    mem_args = []
    argsstring = member.getElementsByTagName("argsstring")
    if len(argsstring) > 0:
        mem_args = argsstring[0].firstChild
        if mem_args:
            mem_args = mem_args.nodeValue  # .replace("(", "").replace(")", "")
            mem_args = mem_args.split("(")[1].split(")")[0].split(",")

    res = Operation(mem_name, mem_privacy, mem_type, mem_args)
    brief_desc = ""
    desc = member.getElementsByTagName("briefdescription")
    if len(desc) > 0:
        desc = desc[0].getElementsByTagName("para")
        if len(desc) > 0:
            desc = desc[0].firstChild.nodeValue
            brief_desc = desc
    res.brief_desc = brief_desc

    xrefsect = member.getElementsByTagName("xrefsect")
    for sec in xrefsect:
        id = sec.getAttribute("id")
        title = sec.getElementsByTagName("xreftitle")[0].firstChild.nodeValue
        desc = sec.getElementsByTagName("xrefdescription")[0].getElementsByTagName("para")[0].firstChild.nodeValue
        ref_obj = XRefSect(id, title, desc)
        res.xrefsect.append(ref_obj)

    loc = member.getElementsByTagName("location")[0]
    res.header_location = loc.getAttribute("file")
    res.body_location = loc.getAttribute("bodyfile")

    return res
