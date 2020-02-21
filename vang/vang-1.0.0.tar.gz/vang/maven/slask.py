#!/usr/bin/env python3
import logging
import re
from glob import glob
from os import makedirs
from os.path import isfile
from pprint import pprint
from shutil import copyfile

logging.basicConfig(level=logging.INFO)


def copy_template_files(templates_src, templates_sink, templates):
    copied_template_files = []
    for template in templates:
        sink_path = f'{templates_sink}{template[len(templates_src):]}'
        makedirs(sink_path.rsplit('/', maxsplit=1)[0], exist_ok=True)
        copyfile(template, sink_path)
        copied_template_files.append((template, sink_path))
    return copied_template_files


def map_to_property_file(templates_src, placeholder):
    property_files = []
    property_file = placeholder[2:-1].rsplit('.', maxsplit=1)[0]
    valid_endings = ['-env.properties', '.properties']
    for ending in valid_endings:
        src_path = f'{templates_src}/{property_file}{ending}'
        if isfile(src_path):
            property_files.append(src_path)
    if not property_files:
        logging.critical('No template found for placeholder: %s', placeholder)
    return property_files


def find_templates_in_file(templates_src, file_path, encoding='utf-8'):
    found_templates_in_file = set()
    try:
        with open(file_path, 'rt', encoding=encoding) as f:
            for line in f.readlines():
                m = re.findall(r'@{[\-_.a-zA-Z0-9/]+?}', line)
                if m:
                    for r in m:
                        property_files = map_to_property_file(templates_src, r)
                        if property_files:
                            for property_file in property_files:
                                found_templates_in_file.add(property_file)
                                found_templates_in_file.update(find_templates_in_file(templates_src, property_file))
    except UnicodeDecodeError as e:
        if encoding == 'utf-8':
            logging.critical('%s is not utf-8 encoded', file_path)
            return find_templates_in_file(templates_src, file_path, 'iso-8859-1')
        else:
            logging.error('Can not read %s with utf-8 or iso-8859-1', file_path)
            print(f'Can not read {file_path}', e)
    return found_templates_in_file


def find_templates(glob_pattern, templates_src, endings=('java', 'groovy', 'xml', 'properties')):
    found_templates = set()
    for file_path in glob(glob_pattern, recursive=True):
        if isfile(file_path) and file_path.rsplit('.', maxsplit=1)[1] in endings:
            found_templates.update(find_templates_in_file(templates_src, file_path))
    return found_templates


the_templates_sink = '/Users/magnus/slask/crap/tmp/src/main/templates'
the_templates_src = '/Users/magnus/slask/crap/configuration.war.es/src/main/templates'
code_glob = '/Users/magnus/slask/crap/CSPES/**/src/main/**/*'

the_templates = find_templates(code_glob, the_templates_src)

copied = copy_template_files(the_templates_src, the_templates_sink, the_templates)
logging.info('Copied %d files: %s', len(copied), copied)
