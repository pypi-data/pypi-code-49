
import json

from copy import deepcopy


def create(environment, options):  # noqa: unused-argument
    env = deepcopy(environment)
    env['date_analyzed'] = env['date_analyzed'].isoformat().split('.')[0]
    return json.dumps(env)

