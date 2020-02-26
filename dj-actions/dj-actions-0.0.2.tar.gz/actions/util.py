from enum import Enum
from django.template import engines
import yaml, json, os

class STATUS(Enum):
    TODO = 'todo'
    ALPHA = 'alpha'
    BETA = 'beta'
    PROD = 'prod'

class ACTION_TYPE(Enum):
    BULK = 'bulk'
    INSTANCE = 'instance'

def get_action_form(registry, action_id):
    from django.utils.module_loading import import_string
    return import_string(registry.get('actions').get(action_id).get('form'))

def get_instance_action_path(context, collection, id, action):
    return '/api/v3/{}/{}/{}/actions/{}/'.format(
        context,
        collection,
        id,
        action
    )

def get_action_docs(base_path, action_id):
    paths_to_check = [
        # legacy format:
        '{}/actiondocs/{}.yaml'.format(base_path, action_id),
        # new format:
        '{}/actions/{}/definition.yaml'.format(base_path, action_id),
    ]
    rendered = None
    for filepath in paths_to_check:
        try:
            file = open(filepath)
            parsed_yml = yaml.load(file, Loader=yaml.FullLoader)
            json_string = json.dumps(parsed_yml)
            django_engine = engines['django']
            template = django_engine.from_string(json_string)
            rendered = template.render(context={})
            file.close()
        except FileNotFoundError:
            pass
    if rendered is None:
        raise Exception('Could not find definition yaml file. Tried: '.format(paths_to_check))
    return json.loads(rendered)

def enrich_actions(base_path, ACTIONS, action_list, environment = {}):
    for action, action_type, action_status in action_list:
        data = get_action_docs(base_path, action)
        data.update(environment)
        data.update({
            "id": action,
            "type": action_type,
            "status": action_status,
        })
        ACTIONS.get('actions').update({action: data})
    return ACTIONS