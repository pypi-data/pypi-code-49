"""Swagger mapper and unifier"""

import argparse
import getpass
import logging
from collections import OrderedDict
from pathlib import Path
from pprint import pformat
from typing import Dict, List
from urllib.parse import urljoin
from urllib.request import urlopen

import requests

from deepdiff import DeepDiff
from ruamel.yaml import YAML

logging.basicConfig(level=logging.WARNING)


def deepupdate(result, update):
    """
    Recursively update a dict.
    Subdict's won't be overwritten but also updated.
    """
    for key, value in update.items():
        if key not in result:
            result[key] = value
        elif isinstance(value, dict):
            deepupdate(result[key], value)
    return result


def get_auth():
    """Get username password"""
    username = input('Username: ')
    password = getpass.getpass('Password: ')
    if len(username) == 0 and len(password) == 0:
        return None
    return (username, password)


def merge_swagger(inputs: List[str], operations_map: Dict[str, str], session: requests.Session,
                  remove_tags: bool = False):
    """Merger swaggers from url/file list. Apply optional operationId mapping"""
    apis = OrderedDict()  # type: Dict[str, Dict]
    base = Path.cwd().as_uri() + "/"
    mapped = set()
    for input in inputs:
        url = urljoin(base, input)
        if url.startswith('http:') or url.startswith('https:'):
            res = session.get(url)
            res.raise_for_status()
            res.encoding = 'utf-8'
            swagger = res.text
        else:
            swagger = urlopen(url)
        api = YAML().load(swagger)
        apis[input] = api
        if operations_map and 'paths' in api:
            xoctrl = operations_map.get("x-openapi-router-controller")
            xsctrl = operations_map.get("x-swagger-router-controller")
            for path, value in api['paths'].items():
                for method, mvalue in value.items():
                    if remove_tags and 'tags' in api['paths'][path][method]:
                        del api['paths'][path][method]['tags']
                    try:
                        operationId = api['paths'][path][method]['operationId']
                    except KeyError:
                        logging.critical("Missing operationId {} {}".format(method.upper(), path))
                    if operationId in operations_map['operationIds']:
                        api['paths'][path][method]['operationId'] = operations_map['operationIds'][operationId]
                        mapped.add(operationId)
                        if xoctrl or xsctrl:
                            pos = 1
                            for key in api['paths'][path][method]:
                                if key == 'operationId':
                                    break
                                pos += 1
                            if xoctrl:
                                api['paths'][path][method].insert(pos, "x-openapi-router-controller", xoctrl)
                            else:
                                api['paths'][path][method].insert(pos, "x-swagger-router-controller", xsctrl)
                    else:
                        logging.warning("Unmapped operationId: " + operationId)
    not_mapped = mapped.symmetric_difference(operations_map['operationIds'])
    if not_mapped:
        logging.critical("Mapped opertionIds not used %s", not_mapped)
    for name1, data1 in apis.items():
        logging.info("Collecting definitions for %s", name1)
        def1 = data1.get('definitions', {})
        keys1 = frozenset(def1.keys())
        for name2, data2 in apis.items():
            def2 = data2.get('definitions', {})
            keys2 = frozenset(def2.keys())
            all_keys = keys1 | keys2
            logging.debug("Definitions: %s", all_keys)
            for key in all_keys:
                if key in def1 and key in def2:
                    logging.info("Cross-check %s", key)
                    diff = DeepDiff(def1[key], def2[key], ignore_order=True, view="tree")
                    if diff:
                        logging.error("%s and %s has different %s", name1, name2, key)
                        logging.error("diff:\n%s", pformat(diff))

    result = None
    for _, data in apis.items():
        if result:
            deepupdate(result, data)
        else:
            result = data
    return result


def strict_objects(input: Dict) -> None:
    """Set 'additionalProperties' to false on all objects that don't specify it"""
    add_attr = False
    for key, val in input.items():
        if key == 'type' and val == 'object' and 'properties' in input and 'additionalProperties' not in input:
            add_attr = True
        elif isinstance(val, dict):
            strict_objects(val)
    if add_attr:
        input['additionalProperties'] = False


def main():
    """ Main function"""
    parser = argparse.ArgumentParser(description='Merge swagger files and check for conflicts')

    parser.add_argument('--strictobjects',
                        action='store_true',
                        help='Set additionalProperties to false for all objects in swagger file')
    parser.add_argument('--tags',
                        action='store_true',
                        help='Remove tags from YAML file')
    parser.add_argument('--operations',
                        metavar='operations.yaml',
                        help='Swagger operations mapper YAML file')
    parser.add_argument('--output',
                        metavar='output file',
                        help='Swagger output file')
    parser.add_argument('--exclude',
                        dest='exclude',
                        metavar='properties',
                        help="Exclude properties")
    parser.add_argument('--auth',
                        action='store_true',
                        help="Enable authentication")
    parser.add_argument('swagger', metavar='swagger_file_or_url', nargs='+', help='Swagger filenames and/or urls')
    args = parser.parse_args()

    yaml = YAML()
    yaml.indent(offset=2, sequence=4)

    if args.operations:
        with open(args.operations, "rt") as file:
            operations = yaml.load(file)
    else:
        operations = None

    session = requests.Session()
    if args.auth:
        session.auth = get_auth()

    result = merge_swagger(args.swagger, operations, session, args.tags)
    if args.strictobjects:
        strict_objects(result)

    if args.exclude:
        for tag in args.exclude.split(','):
            result.pop(tag, None)

    if args.output:
        with open(args.output, "wt") as output:
            yaml.dump(result, output)
    else:
        yaml.dump(result, sys.stdout)


if __name__ == "__main__":
    main()
