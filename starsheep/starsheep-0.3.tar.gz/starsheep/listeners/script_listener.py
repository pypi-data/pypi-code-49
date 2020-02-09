import dinemic
import logging
from starsheep.listeners.listener import Listener


class ScriptListener(Listener):
    ''' Name of script to execute '''
    script_name = None

    ''' ID of object or name of owned model to decrypt additional models '''
    read_as = None

    ''' List of objects which should be read as variables (fields only). Caller_id is set to read_as '''
    related_objects = None

    def __init__(self, listener_name, document, context):
        super(ScriptListener, self).__init__(listener_name, document, context)

        if 'script_name' not in document:
            raise Exception('Missing "script" or "script_name" in listener ' + listener_name)

        self.script_name = document['script_name']

        if 'read_as' in document:
            self.read_as = document['read_as']

        if 'related_objects' in document:
            self.related_objects = document['related_objects']

    def starsheep_apply(self, filter_name):
        if isinstance(filter_name, str):
            self.apply(filter_name)
        elif isinstance(filter_name, list):
            for f in filter_name:
                self.apply(f)

    def call_script(self, **kwargs):
        from starsheep.models.model import Model

        if self.context is None:
            raise Exception('No script assigned')

        if self.script_name not in self.context.scripts:
            raise Exception('Script ' + str(self.script_name) + ' not found')

        variables = kwargs

        if self.read_as is None:
            # Read as updated object
            logging.debug('Obtaining data from ' + kwargs['object_id'] + ' anonymously')
            read_as = kwargs['object_id']
        elif self.read_as.startswith('@'):
            # Read as owned object
            models = dinemic.object_list_owned(self.read_as[1:] + ':[ID]')
            if not models:
                raise Exception('Not found owned model ' + self.read_as[1:] + 'for listener ' + self.listener_name)

            read_as = models[0]
            logging.debug('Obtaining data from ' + kwargs['object_id'] + ' as ' + read_as)
        else:
            # Read as predefined ID of object
            read_as = self.read_as
            logging.debug('Obtaining data from ' + kwargs['object_id'] + ' as ' + read_as)

        model = Model.get_object(kwargs['object_id'], read_as, self.context)

        for field_name in self.context.models[model.get_model()].fields:
            variables['DINEMIC_CONTEXT_' + field_name] = getattr(model, field_name).get()

        variables['DINEMIC_CONTEXT_MODEL'] = model.get_model()
        variables['DINEMIC_CONTEXT_OBJECT_ID'] = model.get_db_id()

        if self.related_objects is None:
            related_objects = []
        elif self.related_objects.startswith('@'):
            related_objects = dinemic.object_list_owned(self.related_objects[1:] + ':[ID]')
        else:
            related_objects = self.related_objects

        logging.debug('Reading related objects for ' + kwargs['object_id'] + ': ' + str(related_objects))
        for obj_id in related_objects:
            m = Model.get_object(obj_id, read_as, self.context)

            if self.context.models[m.get_model()].fields is not None:
                logging.debug('Reading field variables from model ' + m.get_model() + ' for listener ' + self.listener_name)
                for field_name in self.context.models[m.get_model()].fields:
                    variables['DINEMIC_MODEL_FIELD_' + field_name] = getattr(m, field_name).get()

            if self.context.models[m.get_model()].lists is not None:
                logging.debug('Reading list variables from model ' + model.get_model() + ' for listener ' + self.listener_name)
                for list_name in self.context.models[m.get_model()].lists:
                    for list_item in range(getattr(m, list_name).length()):
                        variables['DINEMIC_MODEL_LIST_' + list_name + '_' + str(list_item)] = getattr(m, list_name).at(list_item)

            if self.context.models[m.get_model()].dicts is not None:
                logging.debug('Reading dict variables from model ' + model.get_model() + ' for listener ' + self.listener_name)
                for dict_name in self.context.models[m.get_model()].dicts:
                    for dict_item in getattr(m, dict_name).keys():
                        variables['DINEMIC_MODEL_DICT_' + dict_name + '_' + dict_item] = getattr(m, dict_name).get(dict_item, '')

        self.context.scripts[self.script_name].execute(variables)

    def on_create(self, object_id, key):
        if 'create' in self.call_on:
            self.call_script(object_id=object_id, key=key)

    def on_created(self, object_id, key):
        if 'created' in self.call_on:
            self.call_script(object_id=object_id, key=key)

    def on_owned_create(self, object_id, key):
        if 'owned_created' in self.call_on:
            self.call_script(object_id=object_id, key=key)

    # Before update
    def on_update(self, object_id, field, old_value, new_value):
        if 'update' in self.call_on:
            self.call_script(object_id=object_id, field=field, old_value=old_value, new_value=new_value)

    def on_owned_update(self, object_id, field, old_value, new_value):
        if 'owned_update' in self.call_on:
            self.call_script(object_id=object_id, field=field, old_value=old_value, new_value=new_value)

    def on_authorized_update(self, object_id, field, old_value, new_value):
        if 'authorized_update' in self.call_on:
            self.call_script(object_id=object_id, field=field, old_value=old_value, new_value=new_value)

    def on_unauthorized_update(self, object_id, field, old_value, new_value):
        if 'unauthorized_update' in self.call_on:
            self.call_script(object_id=object_id, field=field, old_value=old_value, new_value=new_value)

    # After updated
    def on_updated(self, object_id, field, old_value, new_value):
        if 'updated' in self.call_on:
            self.call_script(object_id=object_id, field=field, old_value=old_value, new_value=new_value)

    def on_owned_updated(self, object_id, field, old_value, new_value):
        if 'owned_updated' in self.call_on:
            self.call_script(object_id=object_id, field=field, old_value=old_value, new_value=new_value)

    def on_authorized_updated(self, object_id, field, old_value, new_value):
        if 'authorized_updated' in self.call_on:
            self.call_script(object_id=object_id, field=field, old_value=old_value, new_value=new_value)

    def on_unauthorized_updated(self, object_id, field, old_value, new_value):
        if 'unauthorized_updated' in self.call_on:
            self.call_script(object_id=object_id, field=field, old_value=old_value, new_value=new_value)

    # Before field delete
    def on_delete(self, object_id, field, value):
        if 'delete' in self.call_on:
            self.call_script(object_id=object_id, field=field, value=value)

    def on_owned_delete(self, object_id, field, value):
        if 'owned_delete' in self.call_on:
            self.call_script(object_id=object_id, field=field, value=value)

    def on_authorized_delete(self, object_id, field, value):
        if 'authorized_delete' in self.call_on:
            self.call_script(object_id=object_id, field=field, value=value)

    def on_unauthorized_delete(self, object_id, field, value):
        if 'unauthorized_delete' in self.call_on:
            self.call_script(object_id=object_id, field=field, value=value)

    # After field deleted
    def on_deleted(self, object_id, field, value):
        if 'deleted' in self.call_on:
            self.call_script(object_id=object_id, field=field, value=value)

    def on_owned_deleted(self, object_id, field, value):
        if 'owned_deleted' in self.call_on:
            self.call_script(object_id=object_id, field=field, value=value)

    def on_authorized_deleted(self, object_id, field, value):
        if 'authorized_deleted' in self.call_on:
            self.call_script(object_id=object_id, field=field, value=value)

    def on_unauthorized_deleted(self, object_id, field, value):
        if 'unauthorized_deleted' in self.call_on:
            self.call_script(object_id=object_id, field=field, value=value)

    # Before whole object removed
    def on_remove(self, object_id):
        if 'remove' in self.call_on:
            self.call_script(object_id=object_id)

    def on_owned_remove(self, object_id):
        if 'owned_remove' in self.call_on:
            self.call_script(object_id=object_id)

    def on_authorized_remove(self, object_id):
        if 'authorized_remove' in self.call_on:
            self.call_script(object_id=object_id)

    def on_unauthorized_remove(self, object_id):
        if 'unauthorized_remove' in self.call_on:
            self.call_script(object_id=object_id)
