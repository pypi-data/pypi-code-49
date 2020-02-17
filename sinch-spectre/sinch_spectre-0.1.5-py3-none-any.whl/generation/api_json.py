import collections
import copy
import os
import re
import json
from spectre.generation.templates.api_json_template import *
from spectre.generation import serializer
from spectre.generation.utils import make_form, get_form_name, write_to_file

TEMPLATES_PATH = 'generation/templates'

REST_METHODS = { 'GET', 'POST', 'PUT' }

TEMPLATE = {
  "name": "name",
  "namespace" : "namespace",
  "description": "description",
  "base_url": "base_url",
  "info": {
    "contact": {
      "name": "contact.name",
      "email": "contact.email",
      "url": "contact.url"
    }
  },
  "imports": [
  ],
  "models": {
  },
  "resources": {
  }
}

def write(content, config):

    outfile = f"api.json/{config.name}.json"
    write_to_file(content, outfile, config)

def generate(entities, config):
    spec = TEMPLATE
    set_schema_base(spec, config)
    set_schema_models(spec, entities)
    set_schema_resources(spec, entities)
    write(serializer.to_json(spec), config)

def replace_field(text, field, schema_info):
    placeholder = '%' + field + '%'
    replaced = text.replace(placeholder, schema_info[field])
    return replaced

def set_schema_base(spec_dict, config):
    base_fields = ['name', 'namespace', 'description', 'base_url']
    for field in base_fields:
        spec_dict[field] = getattr(config, field)
    return spec_dict

def set_schema_models(spec, entities):
    models = copy.deepcopy(entities)
    for ent_key in entities.keys():
        form_name = get_form_name(ent_key)
        models[form_name] = (make_form(entities[ent_key]))

    spec['models'] = models

def set_schema_resources(spec, entities):
    resources = {}
    for key in entities.keys():
        resources[key] = make_resource(entities[key], key)
    spec['resources'] = resources

def make_resource(entity, name):
    resource = { 'description': re.sub('_RESOURCE_', name, RESOURCE_DESCRIPTION)}
    operations = []
    for method in REST_METHODS:
        operations.append(make_rest_operation(entity, method, name))
    resource['operations'] = operations
    return resource
        

def make_rest_operation(entity, method, name):
    operation = { 
        'method': method,
        'description': make_rest_description(method, name)
    }

    def get(entity, operation, name):
        required_keys = ['name', 'type']
        params = []
        for f in entity['fields']:
            param = { }
            for key in required_keys:
                param[key] = f[key]
            desc = f.get('description', '')
            if desc:
                param['description'] = desc
            param['required'] = False
            params.append(param)
        operation['parameters'] = params
        operation['responses'] = {
            '200': {
                'type': name
            },
            '404': {
                'type': 'string'
            }
        }
        return operation
    def post(entity, operation, name):
        operation['body'] = { 'type': get_form_name(name)}
        operation['responses'] = {
            '201': {
                'type': name
            },
            '400': {
                'type': 'string'
            }
        }
        return operation
    def put(entity, operation, name):
        return operation

    REST_HANDLER_MAP = {
        'GET': get,
        'POST': post,
        'PUT': put
    }
    
    handler = REST_HANDLER_MAP.get(method)
    output = handler(entity, operation, name)
    return output

def make_rest_description(method, name):
    #define handler callbacks for each REST method
    def get(name):
        return 'Search for a ' + name
    def post(name):
        return 'Create a new ' + name
    def put(name):
        return 'Update a ' + name

    method_handlers = {
        'GET': get,
        'POST': post,
        'PUT': put
    }
    #get appropriate handler
    handler = method_handlers.get(method)
    #get description
    return handler(name)