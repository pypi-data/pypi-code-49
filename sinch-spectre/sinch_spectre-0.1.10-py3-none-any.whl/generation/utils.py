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

def is_camel(text):
    camel_regex = r'^[a-z]+[a-z]*([A-Z][a-z]*)*$'
    if not text:
        return False
    if re.match(camel_regex, text):
        return True
    else:
        return False

def is_pascal(text):
    pascal_regex = r'^[A-Z]+([a-z]*([A-Z]+[a-z]*)*)*$'
    if not text:
        return False
    if len(text) <= 2:
        #Could be acronym like ID, or two letter word like Hi. Must return true as long as first is capitalized
        return str.isupper(text[0])
    return True if re.match(pascal_regex, text) else False

def is_snake(text):
    snake_regex = r'^[a-z]+(_[a-z]+)*$'
    return True if re.match(snake_regex, text) else False

def split_pascal_camel(text):
    """Split a string formatted in PascalCase or camelCase into a list of tokens
    
    Arguments:
        text {str} -- A string in either PascalCase or camelCase
    
    Returns:
        list[str] -- A list of tokens
    """
    return re.sub(r"([A-Z])", r" \1", text).strip().split()

def to_camel(text):
    """Takes text in PascalCase, camelCase or snake_case and converts to camelCase
    
    Arguments:
        text {str} -- The text to convert
    
    Returns:
        str -- the text converted to camelCase
    """
    words = split_by_case(text)
    if not words:
        return text
    output = [words[0].lower()]
    for word in words[1:]:
        output.append(word[0].upper() + word[1:])
    return ''.join(output)

def split_by_case(text):
    if is_snake(text):
        return split_snake(text)
    elif is_pascal(text) or is_camel(text):
        return split_pascal_camel(text)
    else:
        return text

def split_snake(text):
    """Split a string in snake_case and return a list of tokens
    
    Arguments:
        text {str} -- a snake_case formatted string
    
    Returns:
        list[str] -- a list of strings
    """
    return text.split('_')

def to_pascal(text):
    """Takes text in PascalCase, camelCase or snake_case and converts to PascalCase
    
    Arguments:
        text {str} -- The text to convert
    
    Returns:
        str -- the text converted to PascalCase
    """
    words = split_by_case(text)
    output = []
    for word in words:
        if word:
            output.append(word[0].upper() + word[1:].lower())
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
