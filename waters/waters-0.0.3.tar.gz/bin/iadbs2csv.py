#! /usr/bin/python
import argparse
from pprint import pprint

p = argparse.ArgumentParser(description="Get information on iaDBs.")
p.add_argument("paths",
               nargs="+",
               help="Paths to outputs of the iaDBs. If ending with '.xml', will use directly. If supplied folders, these will be searched recursively for files ending with '**/*_IA_workflow.xml'.")

args = p.parse_args()

try:
    print('Parsing iaDBs outputs to csvs.')
    from fs_ops.paths import find_suffixed_files
    from waters.parsers import iaDBsXMLparser

    xmls = list(find_suffixed_files(args.paths,
                                    ['**/*_IA_workflow.xml'],
                                    ['.xml']))

    print('Supplied paths:')
    pprint(xmls)

    for xml in xmls:
        XML = iaDBsXMLparser(xml)
        info = XML.info()
        pprint(info)
        print('dumping to csv')
        XML.query_masses().to_csv(xml.parent/'query_masses.csv')
        XML.proteins().to_csv(xml.parent/'proteins.csv')
        XML.products().to_csv(xml.parent/'products.csv')

except Exception as e:
    print(e)


print()
print('Avoid tricks of Loki.')
print('And have a nice day..')
input('press ENTER')