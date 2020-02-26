#!/usr/bin/env python3

import json
import pkg_resources

def prettify(name: str) -> str:
    names_file = pkg_resources.resource_string(__name__, "names.json")
    names = json.loads(names_file)
    try:
        return names[name]
    except KeyError:
        return name
