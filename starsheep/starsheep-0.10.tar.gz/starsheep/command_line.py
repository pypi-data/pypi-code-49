
import logging
import os
import sys
import urllib.request
import yaml

from starsheep.scripts.script import Script
from starsheep.variables.variable import Variable
from starsheep.listeners.listener import Listener
from starsheep.models.model import Model


def get_url(path):
    p = path
    if path.startswith('/'):
        p = 'file://' + path
    elif os.path.exists(path):
        p = 'file://' + os.getcwd() + '/' + path

    logging.debug('Opening file from ' + p)
    return p


def check_version(document, context):
    logging.info('Loading application')
    if 'version' not in document:
        print('missing schema version')
        sys.exit(1)

    if str(document['version']) not in ['2020.02']:
        print('Unsupported version')
        sys.exit(1)


def load_application(document, context):
    logging.info('Loading application')

    if 'application' in document:
        if 'variables' in document['application']:
            context.variables.update(Variable.load(document['application']['variables'], context))

        if 'scripts' in document['application']:
            Script.load(document['application']['scripts'], context)

        if 'listeners' in document['application']:
            Listener.load(document['application']['listeners'], context)

        if 'models' in document['application']:
            Model.load(document['application']['models'], context)


def import_application(document, context):
    if 'import' in document:
        if type(document['import']) == str:
            f = urllib.request.urlopen(get_url(document['import']))
            new_document = yaml.load(f)
            f.close()
            check_version(new_document, context)
            load_application(new_document, context)
        elif type(document['import']) == list:
            for i in document['import']:
                f = urllib.request.urlopen(get_url(i))
                new_document = yaml.load(f)
                f.close()

                check_version(new_document, context)
                load_application(new_document, context)


def apply_data(document, context):
    logging.info('Loading data')

    if 'data' in document:
        for model in document['data'].keys():
            if type(document['data'][model]) == dict:
                Model.apply(model, document['data'][model], context)
            elif type(document['data'][model]) == list:
                for item in document['data'][model]:
                    Model.apply(model, item, context)
            else:
                raise Exception('Unknown type of model')


def import_data(document, context):
    if 'import' in document:
        if type(document['import']) == str:
            f = urllib.request.urlopen(get_url(document['import']))
            new_document = yaml.load(f)
            f.close()

            check_version(new_document, context)
            apply_data(new_document, context)
        elif type(document['import']) == list:
            for i in document['import']:
                f = urllib.request.urlopen(get_url(i))
                new_document = yaml.load(f)
                f.close()

                check_version(new_document, context)
                apply_data(new_document, context)

