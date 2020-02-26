from actions.util import (
    STATUS,
    ACTION_TYPE,
    # get_action_docs,
    enrich_actions
)

action_list = []
## -- START ACTION REGISTRY -- ##
action_list.append(('mark_done', ACTION_TYPE.INSTANCE.value, STATUS.ALPHA.value))
## -- END ACTION REGISTRY -- ##

base = '/code/example_app/'
ACTIONS = enrich_actions(
    base,
    { "resource": "todo", "basepath": "/todos/", "actions": {}, },
    action_list
)

print('example_app.actions')
print([action_id for action_id, action_config in ACTIONS.get('actions').items()])
print('------------------------')

