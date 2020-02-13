#! /usr/bin/python
import argparse
from pprint import pprint

from fs_ops.csv import rows2csv
from fs_ops.paths import find_suffixed_files

from waters.parsers import paths2xmls, iaDBsXMLparser


p = argparse.ArgumentParser(description="Get information on iaDBs.")
p.add_argument("paths",
               nargs="+",
               help="Paths to outputs of the iaDBs. If ending with '.xml', will use directly. If supplied folders, these will be searched recursively for files like '**/*_IA_workflow.xml'.")

args = p.parse_args()
xmls = list(find_suffixed_files(args.paths,
                                ['**/*_IA_workflow.xml'],
                                ['.xml']))

print('Supplied paths:')
pprint(xmls)

try:
    for xml in xmls:
        XML = iaDBsXMLparser(xml)
        info = XML.info()
        pprint(info)
        print('dumping to csv')
        rows2csv(xml.parent/'stats.csv', info.items())
except Exception as e:
    print(e)

print()
print('Let Thor enlight your path with lightnings!')
print('And have a nice day..')
input('press ENTER')