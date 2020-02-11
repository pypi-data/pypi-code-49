import re
from spectre.generation import serializer
from spectre.generation.utils import make_form, get_form_name, to_pascal, write_to_file, is_id

CHANGE_SET_COUNTER = 1

def write(doc, config):
    outfile = f"liquibase/changelog.yml"
    yamlstr = serializer.to_yaml(doc)
    write_to_file(yamlstr, outfile, config)

def generate(entities, config):

    changelog = []
    for ent in entities.keys():
        changelog.append( {'changeSet': build_initial_change_set(entities[ent], ent) } )

    doc = { 'databaseChangeLog': changelog }
    write(doc, config)

def build_initial_change_set(ent, name):
    global CHANGE_SET_COUNTER
    change_set = {}
    change_set['id'] = CHANGE_SET_COUNTER
    change_set['author'] = 'spectre'
    change_set['changes'] = [ {'createTable': create_table(ent, name) }]
    CHANGE_SET_COUNTER += 1 
    return change_set

def create_table(ent, name):
    table = {}
    table['tableName'] = name
    columns = []
    for field in ent['fields']:
        
        column = {}
        column['name'] = field['name']
        column['type'] = convert_type(field)
        if is_id(field.get('type', '')):
            column['constraints'] = {
                'primaryKey': True,
                'nullable': False
            }
        columns.append( {'column': column})
    table['columns'] = columns
    return table

def convert_type(field):
    id_type = 'varchar(32)'
    length = field.get('maximum', '')
    type_map = {
        'uuid': id_type,
        'guid': id_type,
        'float': 'double',
        'string': f'varchar({length})',
        '': "TYPE_MISSING"
    }
    t = field.get('type', '')
    #Return mapped value if present, otherwise default to given type
    return type_map.get(t, t)
