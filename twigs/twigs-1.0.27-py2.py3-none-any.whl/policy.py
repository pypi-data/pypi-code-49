import sys
import platform
import os
import json
import logging

def validate_policy_file(policy_json_file):
    if os.path.isfile(policy_json_file) == False:
        logging.error('Error sepcified file [%s] not found...', policy_json_file)
        sys.exit(1)

    with open(policy_json_file, "r") as fd:
        try:
            policy_json = json.load(fd)
        except json.JSONDecodeError as ex:
            logging.error('Decoding JSON file failed with error [%s]', ex)
            sys.exit(1)

    ret_val = True
    for policy in policy_json:
        temp = validate_policy(policy)
        if ret_val == True:
            ret_val = temp

    if ret_val == False:
        logging.error('One or more policy validations failed...exiting!')
        sys.exit(1)

    return policy_json

def validate_policy(policy):
    if policy.get('name') is None:
        logging.error('Policy is missing field [%s]', policy_field)
        return False
    policy_name = policy['name']
    logging.info('Validating policy [%s]', policy_name)

    policy_fields = ['type', 'conditions', 'actions']
    ret_val = True

    # check required fields exist in policy
    for policy_field in policy_fields:
        if policy.get(policy_field) is None:
            ret_val = False
            logging.error('Policy [%s] is missing field [%s]', policy_name, policy_field)

    condition_fields = ['field', 'operator', 'value']
    for condition in policy['conditions']:
        for cf in condition_fields:
            if condition.get(cf) is None:
                logging.error('Condition [%s] in policy [%s] is missing field [%s]', condition, policy_name, cf)
                ret_val = False

    actions = policy.get('actions')
    if len(actions) == 0:
        logging.error('There are no actions specified in policy [%s]...', policy_name)
        ret_val = False

    if ret_val == False:
        return False

    allowed_fields_by_type = { 
            'vulnerability': {'action bucket': ["do now", "do later"] },
            'license': {'copyleft level': []},
            'code_secret': {'status': [], 'regex':[]},
            'dast': {}
        }

    policy_type = policy['type'].lower()
    if policy_type not in allowed_fields_by_type.keys():
        logging.error('Policy [%s] has invalid type [%s]', policy_name, policy_type)
        return False
    else:
        policy['type'] = policy_type

    allowed_operators = [ '==', '!=', '>', '<', '>=', '<=']

    for condition in policy['conditions']:
        if condition['field'].lower() in allowed_fields_by_type[policy_type].keys():
            condition['field'] = condition['field'].lower()
        else:
            logging.error('Invalid field [%s] specified in condition [%s] in policy [%s]', condition['field'], condition, policy_name)
            return False
        if condition['operator'] not in allowed_operators:
            logging.error('Invalid operator [%s] specified in condition [%s] in policy [%s]', condition['operator'], condition, policy_name)
            ret_val = False
        if len(allowed_fields_by_type[policy_type][condition['field'].lower()]) > 0:
            if condition['value'].lower() not in allowed_fileds_by_type[policy_type][condition['field'].lower()]:
                logging.error('Invalid value [%s] specified in condtion [%s] in policy [%s]', condition['value'], condition, policy_name)
                ret_val = False

    allowed_actions = ['exit_with_code']
    for action in policy['actions'].keys():
        if action.lower() not in allowed_actions:
            logging.error('Invalid action [%s] specified in policy [%s]', action, policy_name)
            ret_val = False
            
    return ret_val

