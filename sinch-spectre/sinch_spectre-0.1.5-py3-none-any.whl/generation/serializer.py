import json
import sys
import yaml
from collections import OrderedDict

def to_json(json_obj):
    return json.dumps(json_obj, sort_keys=False,
                 indent=4, separators=(',', ': '))

def to_yaml(yaml_obj):
    return yaml.dump(yaml_obj, default_flow_style=False, sort_keys=False)