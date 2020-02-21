#!/usr/bin/env python3
from xml.dom import minidom


def get_pretty_xml(xml_string, indent=' ' * 4, newl='\n', xml_declaration=False):
    stripped = ''.join([x.strip() for x in xml_string.split('\n')])
    parsed = minidom.parseString(stripped)
    prettified = parsed.toprettyxml(indent=indent, newl=newl)
    return prettified if xml_declaration else prettified[len('<?xml version="1.0" ?>'):]


def get_child_tags(pom, tag_path):
    tags = set()
    tag_element = pom
    for t in tag_path.split('.'):
        if tag_element:
            found = None
            for child in tag_element.childNodes:
                if child.nodeType == child.ELEMENT_NODE and child.tagName == t:
                    found = child
                    break
            tag_element = found if found else None

    if tag_element:
        for child in tag_element.childNodes:
            if child.nodeType == child.ELEMENT_NODE:
                tags.add(get_pretty_xml(child.toxml(), indent='', newl=''))
    return tags


def merge(pom_paths, tags):
    merged = [(t, set()) for t in tags]

    for pom_path in pom_paths:
        pom = minidom.parse(pom_path)
        for tag, tag_set in merged:
            tag_set.update(get_child_tags(pom, tag))

    return [sorted(tag_set) for tag, tag_set in merged]


def print_xml(merged, tag_paths):
    pom_dict = {}
    for m, t in zip(merged, tag_paths):
        tags = t.split('.')
        tmp_dict = pom_dict
        for key in tags[:-1]:
            if key in tmp_dict:
                tmp_dict = tmp_dict[key]
            else:
                tmp_dict[key] = {}
                tmp_dict = tmp_dict[key]
        tmp_dict[tags[-1]] = ''.join(m)

    def recur(m):
        return ''.join(f'<{k}>{v if isinstance(v, str) else recur(v)}</{k}>' for k, v in m.items())

    print(get_pretty_xml(recur(pom_dict)))


if __name__ == '__main__':
    """ 
    Merges specified tags of specified modules in specified base_dir and prints the result.
    Tags, modules are modified as wanted below.
    The result is intended to be pasted into the pom.xml of a merged mini service.
    """
    modules = [
        'pom.super',
        # 'spring.bean-name',
    ]

    # modules = [
    #     'app.customer.connectcustomertonativeappinstallation.v1_0',
    #     'app.customer.getnativeappinstallation.v1_0'
    # ]
    #
    # modules = [
    #     'app.application.system.getresourcelock.v1_0',
    #     'app.application.system.publishclientcontent.v1_0',
    #     'app.application.system.updateresourcelock.v1_0',
    #     'app.application.system.createclientlog.v1_0',
    # ]

    # modules = [
    #     'app.application.customer.getlatestapponboarding.v1_0',
    #     'app.application.customer.updateonboardedappversion.v1_0',
    # ]

    # modules = [
    #     'app.customer.getarchivedocument.v1_0',
    #     'app.customer.getarchivedocumentids.v1_0',
    #     'app.system.document.getdocument.v1_0',
    # ]

    # modules = [
    #     'app.security.getelectronicids.v1_1',
    #     # 'app.security.getuserorganizations.v1_0',
    # ]

    # modules = [
    #     'app.customer.connectcustomertonativeappinstallation.v1_0',
    #     'app.customer.getnativeappinstallation.v1_0',
    # ]

    base_dir = '/Users/magnus/git-csp-es/CSPES'
    pom_paths = [f'{base_dir}/{m}/pom.xml' for m in modules]

    tags_to_merge = ['project.dependencies', 'project.build.plugins']
    print_xml(merge(pom_paths, tags_to_merge), tags_to_merge)
