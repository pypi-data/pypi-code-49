
from .indexParser import parse_index
from .classParser import parse_class_file
from .namespaceParser import parse_namespace_file
import os
import sys
from .dotExport import DotExport
from pytermcolor import cprint
import argparse


def main(arg):
    parser = argparse.ArgumentParser()
    parser.add_argument("index", help="path to index.xml")

    args = parser.parse_args()

    # index_file = "example/Cpp/Doxygen/xml/index.xml"

    index_file = args.index
    classes, namespaces = parse_index(index_file)
    doxy_root = os.path.dirname(index_file)

    if not os.path.isfile(index_file):
        cprint("index.xml not found", "red")
        exit(-1)

    dot_exp = DotExport("test")

    for clss in classes:
        obj = parse_class_file(os.path.join(doxy_root, clss[1]+".xml"))
        # print(obj)
        dot_exp.add_class(obj)

    for ns in namespaces:
        obj = parse_namespace_file(os.path.join(doxy_root, ns[1]+".xml"))
        # print(obj)
        dot_exp.add_namespace(obj)

    # print(dot_exp)
    dot_exp.render()
    
    
if __name__ == "__main__":
    main(sys.argv[1:])
