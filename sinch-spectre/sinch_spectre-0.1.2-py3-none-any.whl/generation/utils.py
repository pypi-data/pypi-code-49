import copy
import json
from spectre import model
from spectre.config import Config
import os
import re

def read_entities(path):
    with open(path, mode='r') as file:
        json_str = file.read()
        entities_dict = json.loads(json_str)
        entities = []
        for name_key, entity_dict in entities_dict.items():
            entity = model.Entity.from_dict(name_key, entity_dict)
            entities.append(entity)
        return entities

def make_form(entity):
    form = copy.deepcopy(entity)
    form.name = get_form_name(entity.name)
    fields = form.fields
    for field in fields:
        if field.type is model.SpectreType.UUID:
            fields.remove(field)
            break
    return form

def is_id(field_name):
    id_pattern = r'(?:^(?:uu|gu)?id.*|.*(?:uu|gu)?id$)'
    if re.match(id_pattern, field_name):
        return True
    else:
        return False

def get_form_name(ent_name):
    return ent_name.lower() + '_form'

def to_camel(text):
    '''
    Takes text in PascalCase and converts to camelCase
    '''
    words = re.sub(r"([A-Z])", r" \1", text).split()
    output = [words[0].lower()]
    for word in words[1:]:
        output.append(word[0].upper() + word[1:])
    return ''.join(output)

def to_camel_from_snake(text):
    words = text.split('_')
    output = [words[0].lower()]
    for word in words[1:]:
        output.append(word[0].upper() + word[1:])
    return ''.join(output)

def to_pascal(text):
    '''
    Takes text in snake_case and converts to PascalCase
    '''
    words = text.split('_')
    output = []
    for word in words:
        output.append(word[0].upper() + word[1:])
    return ''.join(output)

def write_to_file(content, outfile, config: Config):
    '''
    Writes the string content to path outfile.
    '''
    def get_file_path(outfile):
        out_dir = f'{config.spectre_dir}/out'
        path = f'{out_dir}/{outfile}'
        path = os.path.abspath(path)
        return path

    def make_directory(file_path):
        dirpath = os.path.dirname(file_path)
        if not os.path.isdir(dirpath):
            os.makedirs(dirpath)

    file_path = get_file_path(outfile)
    make_directory(file_path)
    try:
        with open(file_path, 'w') as outfile:
            outfile.write(content)
        return file_path
    except:
        print(f'I/O error while writing {file_path}')
