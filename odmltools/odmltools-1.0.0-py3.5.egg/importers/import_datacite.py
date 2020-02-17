"""odmlImportDatacite

Convenience script to parse a datacite XML file or whole directories
containing datacite XML files and create odML files with the parsed
information.

Usage: odmlimportdatacite [-f FORMAT] [-o OUT] [-n NAMESPACE ...] [-r] [-p] INPUT

Arguments:
    INPUT    Path and filename of the datacite XML file to be parsed.
             If used with the [-r] flag, INPUT should be a directory;
             all datacite XML files within this directory and any sub
             directories will be parsed to odML.

Options:
    -f FORMAT       odML output file format. Available formats are
                      'XML', 'JSON', 'YAML', 'RDF'. Default format is 'XML'.
    -o OUT          Output directory. Must exist if specified.
                      If not specified, output files will be written to the
                      current directory.
    -r              [Optional] Walk recursively through a repository.
                      and convert all datacite files found.
    -n NAMESPACE    [Optional] By default only the namespace 'http://datacite.org/schema/kernel-4'
                    is properly handled. Use this option to add any additional namespaces
                      your DataCite files contain so they can be properly parsed and handled.
                      The option can be used multiple times.
    -p              [Optional] Print the parsed document tree(s) to the command line.
                      Default is False.
    -h --help       Show this screen.
    --version       Show version number.
"""

import os
import pathlib
import re
import sys

from datetime import date
from xml.parsers.expat import errors as exp_err
from xml.parsers.expat import ExpatError

import xmltodict

from docopt import docopt
from odml import Document, Section, Property
from odml.fileio import save as save_odml
from odml.dtypes import DType
from odml.tools.parser_utils import SUPPORTED_PARSERS


VERSION = "0.1.0"
# DataCite namespaces that need to be removed from the individual XML tags before the
# XML file can be properly processed.
COLLAPSE_NS = ['http://datacite.org/schema/kernel-4']


class ParserException(Exception):
    """
    Exception wrapper used by various odML parsers.
    """
    pass


class DataCiteItem(object):
    def __init__(self, sec_name, attribute_map, func, container_name=None, item_func=None):
        self.section_name = sec_name
        self.attribute_map = attribute_map
        self.func = func
        self.container_name = container_name
        self.item_func = item_func


def camel_to_snake(in_string):
    tmp = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', in_string)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', tmp).lower()


def dict_from_xml(xml_file, extra_ns=None):
    """
    Parse the contents of an xml file into a python dictionary.

    :param xml_file: Location of the xml file to be parsed.
    :param extra_ns: Custom namespaces to collapse.
    :return: dictionary containing the contents of the xml file.
    """

    remove_nspaces = {}
    for nspace in COLLAPSE_NS:
        remove_nspaces[nspace] = None

    if extra_ns:
        for nspace in extra_ns:
            remove_nspaces[nspace] = None

    try:
        with open(xml_file) as file:
            doc = xmltodict.parse(file.read(),
                                  process_namespaces=True, namespaces=remove_nspaces)
    except ExpatError as exc:
        msg = "[Error] Could not load file '%s': %s" % (xml_file,
                                                        exp_err.messages[exc.code])
        raise ParserException(msg)

    return doc


def handle_container(helper, node, root_sec):
    if not node or helper.section_name not in node:
        return

    sec_cont_type = "datacite/%s" % camel_to_snake(helper.container_name)
    sub_sec_type = "datacite/%s" % camel_to_snake(helper.section_name)

    sec = Section(name=helper.container_name, type=sec_cont_type, parent=root_sec)

    handle_sub_container(helper, node, sec, sub_sec_type)


def handle_sub_container(helper, node, sec, sub_sec_type):
    # We might need to handle the case, when a container holds
    # only the content of one xml element and does not contain
    # the content and attributes of this xml element as a sole
    # list element but as many elements within an OrderedDict.
    if isinstance(node[helper.section_name], list):
        for (idx, title_node) in enumerate(node[helper.section_name]):
            sec_name = "%s_%d" % (helper.section_name, idx + 1)
            sub_sec = Section(name=sec_name, type=sub_sec_type, parent=sec)
            helper.item_func(helper, title_node, sub_sec)
    else:
        sub_sec_name = "%s_1" % helper.section_name
        sub_sec = Section(name=sub_sec_name, type=sub_sec_type, parent=sec)
        helper.item_func(helper, node[helper.section_name], sub_sec)


def handle_sec(helper, node, root_sec):
    if not node:
        return

    sec_type = "datacite/%s" % camel_to_snake(helper.section_name)
    sec = Section(name=helper.section_name, type=sec_type, parent=root_sec)

    handle_props(helper, node, sec)


def handle_props(helper, node, sec):
    if not node:
        return

    # Handle special case if a node is just the string content of an XML element.
    if isinstance(node, str):
        Property(name=helper.section_name, values=node, parent=sec)
    else:
        for sub in node:
            if sub in helper.attribute_map:
                dtype = DType.string
                if isinstance(sub, str) and sub.endswith("URI"):
                    dtype = DType.url

                Property(name=helper.attribute_map[sub], dtype=dtype,
                         values=node[sub], parent=sec)
            else:
                print("[Warning] Ignoring node '%s/%s'" % (sec.name, sub))


def handle_name_identifiers(sub, node, sub_type_base, sec):
    name_identifier_map = {
        "#text": "nameIdentifier",
        "@schemeURI": "schemeURI",
        "@nameIdentifierScheme": "nameIdentifierScheme"
    }
    name_identifier_helper = DataCiteItem(sec_name=sub,
                                          attribute_map=name_identifier_map,
                                          func=None,
                                          item_func=handle_props)
    sub_sec_type = "%s/named_identifier" % sub_type_base
    handle_sub_container(name_identifier_helper, node, sec, sub_sec_type)


def handle_affiliations(sub, node, sub_type_base, sec):
    affiliation_map = {
        "#text": "affiliation",
        "@affiliationIdentifier": "affiliationIdentifier",
        "@affiliationIdentifierScheme": "affiliationIdentifierScheme",
        "@schemeURI": "schemeURI"
    }
    affiliation_helper = DataCiteItem(sec_name=sub,
                                      attribute_map=affiliation_map,
                                      func=None,
                                      item_func=handle_props)
    sub_sec_type = "%s/affiliation" % sub_type_base
    handle_sub_container(affiliation_helper, node, sec, sub_sec_type)


def handle_creators_item(_, node, sec):
    sub_type_base = "datacite/creator"

    for sub in node:
        if sub == "creatorName":
            creator_name_map = {
                "#text": "creatorName",
                "@nameType": "nameType"
            }
            creator_name_helper = DataCiteItem(sec_name=sub,
                                               attribute_map=creator_name_map,
                                               func=None)
            handle_props(creator_name_helper, node[sub], sec)
        elif sub in ["givenName", "familyName"]:
            if isinstance(node[sub], str):
                Property(name=sub, values=node[sub], parent=sec)
            elif "#text" in node[sub]:
                Property(name=sub, values=node[sub]["#text"], parent=sec)
            else:
                print("[Warning] Could not parse '%s/%s'" % (sub_type_base, sub))
        elif sub == "nameIdentifier":
            handle_name_identifiers(sub, node, sub_type_base, sec)
        elif sub == "affiliation":
            handle_affiliations(sub, node, sub_type_base, sec)
        else:
            print("[Warning] Ignoring unsupported attribute '%s'" % sub)


def handle_contributors_item(_, node, sec):
    sub_type_base = "datacite/contributor"

    for sub in node:
        if sub in ["contributorName", "givenName", "familyName"]:
            if isinstance(node[sub], str):
                Property(name=sub, values=node[sub], parent=sec)
            elif "#text" in node[sub]:
                Property(name=sub, values=node[sub]["#text"], parent=sec)
            else:
                print("[Warning] Could not parse '%s/%s'" % (sub_type_base, sub))
        elif sub == "@contributorType":
            Property(name="contributorType", values=node[sub], parent=sec)
        elif sub == "nameIdentifier":
            handle_name_identifiers(sub, node, sub_type_base, sec)
        elif sub == "affiliation":
            handle_affiliations(sub, node, sub_type_base, sec)
        else:
            print("[Warning] Ignoring unsupported attribute '%s'" % sub)


def handle_geo_entry(helper_list, node, sec, sub_sec_name, sub_sec_type):
    sub_sec = Section(name=sub_sec_name, type=sub_sec_type, parent=sec)

    for entry in node:
        if entry in helper_list:
            try:
                Property(name=entry, dtype=DType.float,
                         values=node[entry], parent=sub_sec)
            except ValueError:
                print("[Warning] Skipping invalid '%s' value '%s'" %
                      (entry, node[entry]))


def handle_geo_locations(_, node, sec):
    sub_type_base = "datacite/geo_location"

    point_list = ["pointLongitude", "pointLatitude"]
    box_list = ["westBoundLongitude", "eastBoundLongitude",
                "southBoundLatitude", "northBoundLatitude"]

    for elem in node:
        if elem == "geoLocationPlace":
            Property(name=elem, values=node[elem], parent=sec)
        elif elem == "geoLocationPoint":
            sec_type = "%s/%s" % (sub_type_base, camel_to_snake(elem))
            handle_geo_entry(point_list, node[elem], sec, elem, sec_type)
        elif elem == "geoLocationBox":
            sec_type = "%s/%s" % (sub_type_base, camel_to_snake(elem))
            handle_geo_entry(box_list, node[elem], sec, elem, sec_type)
        elif elem == "geoLocationPolygon":
            sub_type = "%s/%s" % (sub_type_base, camel_to_snake(elem))
            sub_sec = Section(name=elem, type=sub_type, parent=sec)

            for (idx, point) in enumerate(node[elem]["polygonPoint"]):
                point_name = "polygonPoint_%d" % (idx + 1)
                sec_type = "%s/%s" % (sub_type_base, camel_to_snake("polygonPoint"))
                handle_geo_entry(point_list, point, sub_sec, point_name, sec_type)


def handle_funding_references(_, node, sec):
    for sub in node:
        if sub in ["funderName", "awardTitle"]:
            Property(name=sub, values=node[sub], parent=sec)
        elif sub == "awardNumber":
            award_number_map = {"#text": "awardNumber", "@awardURI": "awardURI"}
            award_number_helper = DataCiteItem(sec_name=sub,
                                               attribute_map=award_number_map,
                                               func=None)
            handle_props(award_number_helper, node[sub], sec)
        elif sub == "funderIdentifier":
            funder_identifier_map = {
                "#text": "funderIdentifier",
                "@funderIdentifierType": "funderIdentifierType",
                "@schemeURI": "schemeURI"}
            funder_identifier_helper = DataCiteItem(sec_name=sub,
                                                    attribute_map=funder_identifier_map,
                                                    func=None)
            handle_props(funder_identifier_helper, node[sub], sec)


def setup_supported_tags():
    identifier_map = {
        "#text": "identifier",
        "@identifierType": "identifierType"
    }
    identifier_helper = DataCiteItem(sec_name="identifier",
                                     attribute_map=identifier_map,
                                     func=handle_sec)

    creators_helper = DataCiteItem(sec_name="creator",
                                   attribute_map=None,
                                   func=handle_container,
                                   container_name="creators",
                                   item_func=handle_creators_item)

    title_map = {
        "#text": "title",
        "@titleType": "titleType"
    }
    title_helper = DataCiteItem(sec_name="title",
                                attribute_map=title_map,
                                func=handle_container,
                                container_name="titles",
                                item_func=handle_props)

    publisher_helper = DataCiteItem(sec_name="publisher",
                                    attribute_map={"#text": "publisher"},
                                    func=handle_props)

    publication_year_helper = DataCiteItem(sec_name="publicationYear",
                                           attribute_map={"#text": "publicationYear"},
                                           func=handle_props)

    subjects_map = {
        "#text": "subject",
        "@schemeURI": "schemeURI",
        "@subjectScheme": "subjectScheme",
        "@valueURI": "valueURI"
    }
    subjects_helper = DataCiteItem(sec_name="subject",
                                   attribute_map=subjects_map,
                                   func=handle_container,
                                   container_name="subjects",
                                   item_func=handle_props)

    contributors_helper = DataCiteItem(sec_name="contributor",
                                       attribute_map=None,
                                       func=handle_container,
                                       container_name="contributors",
                                       item_func=handle_contributors_item)

    dates_map = {
        "#text": "date",
        "@dateType": "dateType",
        "@dateInformation": "dateInformation"
    }
    dates_helper = DataCiteItem(sec_name="date",
                                attribute_map=dates_map,
                                func=handle_container,
                                container_name="dates",
                                item_func=handle_props)

    language_helper = DataCiteItem(sec_name="language",
                                   attribute_map={"#text": "language"},
                                   func=handle_props)

    res_type_map = {
        "#text": "resourceType",
        "@resourceTypeGeneral": "resourceTypeGeneral"
    }
    res_type_helper = DataCiteItem(sec_name="resourceType",
                                   attribute_map=res_type_map,
                                   func=handle_sec)

    alternate_identifiers_map = {
        "#text": "alternateIdentifier",
        "@alternateIdentifierType": "alternateIdentifierType"
    }
    alternate_identifiers_helper = DataCiteItem(sec_name="alternateIdentifier",
                                                attribute_map=alternate_identifiers_map,
                                                func=handle_container,
                                                container_name="alternateIdentifiers",
                                                item_func=handle_props)

    related_identifiers_map = {
        "#text": "relatedIdentifier",
        "@relatedIdentifierType": "relatedIdentifierType",
        "@relationType": "relationType",
        "@relatedMetadataScheme": "relatedMetadataScheme",
        "@schemeURI": "schemeURI",
        "@schemeType": "schemeType",
        "@resourceTypeGeneral": "resourceTypeGeneral"
    }
    related_identifiers_helper = DataCiteItem(sec_name="relatedIdentifier",
                                              attribute_map=related_identifiers_map,
                                              func=handle_container,
                                              container_name="relatedIdentifiers",
                                              item_func=handle_props)

    sizes_helper = DataCiteItem(sec_name="size",
                                attribute_map={"#text": "size"},
                                func=handle_container,
                                container_name="sizes",
                                item_func=handle_props)

    formats_helper = DataCiteItem(sec_name="format",
                                  attribute_map={"#text": "format"},
                                  func=handle_container,
                                  container_name="formats",
                                  item_func=handle_props)

    version_helper = DataCiteItem(sec_name="version",
                                  attribute_map={"#text": "version"},
                                  func=handle_props)

    rights_map = {
        "@schemeURI": "schemeURI",
        "@rightsIdentifierScheme": "rightsIdentifierScheme",
        "@rightsIdentifier": "rightsIdentifier",
        "@rightsURI": "rightsURI"
    }
    rights_helper = DataCiteItem(sec_name="rights",
                                 attribute_map=rights_map,
                                 func=handle_container,
                                 container_name="rightsList",
                                 item_func=handle_props)

    descriptions_map = {
        "#text": "description",
        "@descriptionType": "descriptionType"
    }
    descriptions_helper = DataCiteItem(sec_name="description",
                                       attribute_map=descriptions_map,
                                       func=handle_container,
                                       container_name="descriptions",
                                       item_func=handle_props)

    geo_locations_helper = DataCiteItem(sec_name="geoLocation",
                                        attribute_map=None,
                                        func=handle_container,
                                        container_name="geoLocations",
                                        item_func=handle_geo_locations)

    funding_references_helper = DataCiteItem(sec_name="fundingReference",
                                             attribute_map=None,
                                             func=handle_container,
                                             container_name="fundingReferences",
                                             item_func=handle_funding_references)

    supported_tags = {
        "identifier": identifier_helper,
        "creators": creators_helper,
        "titles": title_helper,
        "publisher": publisher_helper,
        "publicationYear": publication_year_helper,
        "subjects": subjects_helper,
        "contributors": contributors_helper,
        "dates": dates_helper,
        "language": language_helper,
        "resourceType": res_type_helper,
        "alternateIdentifiers": alternate_identifiers_helper,
        "relatedIdentifiers": related_identifiers_helper,
        "sizes": sizes_helper,
        "formats": formats_helper,
        "version": version_helper,
        "rightsList": rights_helper,
        "descriptions": descriptions_helper,
        "geoLocations": geo_locations_helper,
        "fundingReferences": funding_references_helper
    }

    return supported_tags


def parse_datacite_dict(doc):
    """
    :param doc: python dict containing datacite conform data to
                be parsed.
    """
    if not doc or "resource" not in doc:
        msg = "Could not find root. "
        msg += "Please escape any XML namespace using the '-n' command line option."
        raise ParserException(msg)

    datacite_root = doc["resource"]
    if "identifier" not in datacite_root:
        raise ParserException("Could not find identifier (DOI) node")

    odml_doc = Document()
    odml_doc.repository = "https://terminologies.g-node.org/v1.1/terminologies.xml"
    odml_doc.date = date.today().isoformat()

    root_sec = Section(name="DataCite", type="data_reference", parent=odml_doc)

    supported_tags = setup_supported_tags()
    for node_tag in datacite_root:
        if node_tag in supported_tags:
            helper = supported_tags[node_tag]
            helper.func(helper, datacite_root[node_tag], root_sec)
        else:
            print("[Warning] Ignoring unsupported root node '%s'" % node_tag)

    return odml_doc


def handle_document(cite_in, out_root, backend="XML", print_doc=False, extra_ns=None):
    print("[INFO] Handling file '%s'" % cite_in)

    # Read document from input file
    doc = None
    try:
        doc = dict_from_xml(cite_in, extra_ns)
    except ParserException as exc:
        exc_message = "[Error] Could not parse datacite file '%s'\n\t%s" % (cite_in, exc)
        raise ParserException(exc_message)

    # Parse input to an odML document
    try:
        odml_doc = parse_datacite_dict(doc)
    except ParserException as exc:
        exc_message = "[Error] Could not parse datacite file '%s'\n\t%s" % (cite_in, exc)
        raise ParserException(exc_message)

    if print_doc:
        print()
        print(odml_doc.pprint(max_depth=5))

    out_name = os.path.splitext(os.path.basename(cite_in))[0]
    out_file = os.path.join(out_root, "%s.%s" % (out_name, backend.lower()))

    # Do not overwrite existing files
    if os.path.isfile(out_file):
        out_file = os.path.join(out_root, "%s(copy).%s" % (out_name, backend.lower()))

    # Provide original file name
    odml_doc._origin_file_name = os.path.basename(cite_in)
    save_odml(odml_doc, out_file, backend)


def main(args=None):
    parser = docopt(__doc__, argv=args, version=VERSION)

    recursive = parser["-r"]
    cite_in = parser["INPUT"]

    if not recursive and not os.path.isfile(cite_in):
        print("[Error] Could not access input file '%s'\n" % cite_in)
        return exit(1)
    elif recursive and not os.path.isdir(cite_in):
        print("[Error] Could not access input directory '%s'\n" % cite_in)
        return exit(1)

    # Handle output file format
    backend = "XML"
    if parser["-f"]:
        backend = parser["-f"].upper()
        if backend not in SUPPORTED_PARSERS:
            print("[Error] Output format '%s' is not supported. \n" % backend)
            print(docopt(__doc__, "-h"))
            return exit(1)

    # Handle output directory
    out_root = os.getcwd()
    if parser["-o"]:
        if not os.path.isdir(parser["-o"]):
            print("[Error] Could not find output directory '%s'" % parser["-o"])
            return exit(1)

        out_root = parser["-o"]

    print_file = parser["-p"]

    # Add extra XML namespaces to collapse
    extra_ns = []
    if parser["-n"]:
        for namespace in parser["-n"]:
            extra_ns.append(namespace)

    # File conversion
    if recursive:
        xfiles = list(pathlib.Path(cite_in).rglob('*.xml'))
        for file in xfiles:
            try:
                handle_document(file, out_root, backend, print_file, extra_ns)
            except ParserException as exc:
                print(exc)
    else:
        try:
            handle_document(cite_in, out_root, backend, print_file, extra_ns)
        except ParserException as exc:
            print(exc)
            return exit(1)

    return exit(0)


if __name__ == "__main__":
    main(sys.argv[1:])
