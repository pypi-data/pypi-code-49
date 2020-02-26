import json
from spectre import config
import os
import sys
from spectre.model import entity
from spectre.generation import api_json, proto, liquibase, jhipster

def get_entities(path):

def generate(config):
    with open(config.path, mode='r') as file:
        json_str = file.read()
        entities = json.loads(json_str)
        GENERATOR_MAP = {
            'api.json': api_json.generate,
            'proto': proto.generate,
            'liquibase': liquibase.generate,
            'jhipster': jhipster.generate
        }
        for gen in config.generators:
            GENERATOR_MAP[gen](entities, config)

