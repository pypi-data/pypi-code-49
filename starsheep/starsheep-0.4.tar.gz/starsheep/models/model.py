import dinemic
import logging


class Field(object):
    is_encrypted = None
    is_protected = None
    name = None


class List(Field):
    is_encrypted = None
    is_protected = None
    name = None


class Dict(Field):
    is_encrypted = None
    is_protected = None
    name = None


class Model(object):
    context = None
    model_name = None
    model = None
    fields = None
    lists = None
    dicts = None
    unique = None
    instances = None

    def __init__(self, model_name, document, context):
        from starsheep.listeners.reject_listener import RejectListener

        self.context = context
        self.model_name = model_name

        if 'fields' in document:
            self.fields = {}
            for field_name in document['fields']:
                f = Field()
                if document['fields'][field_name]['can_read'] == 'all':
                    f.is_encrypted = False
                else:
                    f.is_encrypted = True

                if document['fields'][field_name]['can_update'] == 'all':
                    f.is_protected = False
                else:
                    f.is_protected = True
                    listener = RejectListener('reject_' + self.model_name + '_field_' + field_name,
                                              {'reason': 'not authorized',
                                               'action': 'reject',
                                               'trigger': self.model_name + ':[ID]:value_' + field_name,
                                               'call_on': ['unauthorized_update', 'unauthorized_delete', 'unauthorized_remove']},
                                              context)
                    listener.starsheep_apply(self.model_name + ':[ID]:value_' + field_name)
                self.fields[field_name] = f
                logging.debug('Registered field ' + field_name + ' for model ' + model_name)

        if 'lists' in document:
            self.lists = {}
            for list_name in document['lists']:
                l = List()
                if document['lists'][list_name]['can_read'] == 'all':
                    l.is_encrypted = False
                else:
                    l.is_encrypted = True

                if document['lists'][list_name]['can_update'] == 'all':
                    l.is_protected = False
                else:
                    l.is_protected = True
                    listener = RejectListener('reject_' + self.model_name + '_list_' + list_name,
                                              {'reason': 'not authorized',
                                               'action': 'reject',
                                               'trigger': self.model_name + ':[ID]:list_' + list_name,
                                               'call_on': ['unauthorized_update', 'unauthorized_delete', 'unauthorized_remove']},
                                              context)
                    listener.starsheep_apply(self.model_name + ':[ID]:list_' + list_name)
                self.lists[list_name] = l
                logging.debug('Registered list ' + list_name + ' for model ' + model_name)

        if 'dicts' in document:
            self.dicts = {}
            for dict_name in document['dicts']:
                d = Dict()
                if document['dicts'][dict_name]['can_read'] == 'all':
                    f.is_encrypted = False
                else:
                    f.is_encrypted = True

                if document['dicts'][dict_name]['can_update'] == 'all':
                    f.is_protected = False
                else:
                    f.is_protected = True
                    listener = RejectListener('reject_' + self.model_name + '_dict_' + dict_name,
                                              {'reason': 'not authorized',
                                               'action': 'reject',
                                               'trigger': self.model_name + ':[ID]:dict_' + dict_name,
                                               'call_on': ['unauthorized_update', 'unauthorized_delete', 'unauthorized_remove']},
                                              context)
                    listener.starsheep_apply(self.model_name + ':[ID]:dict_' + dict_name)
                self.dicts[dict_name] = d
                logging.debug('Registered dict ' + dict_name + ' for model ' + model_name)

        if 'unique' in document:
            if document['unique'] not in self.fields:
                raise Exception('Unique "' + document['unique'] + '" does not refer to any field of model ' + model_name)
            self.unique = document['unique']
            logging.debug('Model ' + self.model_name + ' will be unique by field ' + self.unique)

        if 'instances' in document:
            self.instances = document['instances']

        logging.info('Registered model ' + model_name)

    def __str__(self):
        return self.model_name

    @staticmethod
    def get_object(object_id, caller_id, context):
        model = dinemic.DModel(object_id, caller_id)
        if model.get_model() not in context.models:
            raise Exception('Model ' + model.get_model() + ' is not defined')

        if context.models[model.get_model()].fields is not None:
            for f in context.models[model.get_model()].fields.keys():
                setattr(model, f,
                        dinemic.DField(f, context.models[model.get_model()].fields[f].is_encrypted))
                getattr(model, f)._object_id = model.get_db_id()
                getattr(model, f)._caller_id = model.get_db_id()

        if context.models[model.get_model()].lists is not None:
            for l in context.models[model.get_model()].lists.keys():
                setattr(model, l,
                        dinemic.DList(l, context.models[model.get_model()].lists[l].is_encrypted))
                getattr(model, l)._object_id = model.get_db_id()
                getattr(model, l)._caller_id = model.get_db_id()

        if context.models[model.get_model()].dicts is not None:
            for d in context.models[model.get_model()].dicts.keys():
                setattr(model, d,
                        dinemic.DField(f, context.models[model.get_model()].dicts[d].is_encrypted))
                getattr(model, d)._object_id = model.get_db_id()
                getattr(model, d)._caller_id = model.get_db_id()

        logging.debug('Recreated object ' + model.get_db_id())
        return model

    @staticmethod
    def create_object(model_name, authorized_objects, context):
        if model_name not in context.models:
            raise Exception('Model ' + model_name + ' is not defined')

        class TmpModel(dinemic.DModel):
            pass
        TmpModel.__name__ = model_name

        model = TmpModel(authorized_objects)

        if context.models[model.get_model()].fields is not None:
            for f in context.models[model.get_model()].fields.keys():
                setattr(model, f,
                        dinemic.DField(f, context.models[model.get_model()].fields[f].is_encrypted))
                getattr(model, f)._object_id = model.get_db_id()
                getattr(model, f)._caller_id = model.get_db_id()

        if context.models[model.get_model()].lists is not None:
            for l in context.models[model.get_model()].lists.keys():
                setattr(model, l,
                        dinemic.DList(l, context.models[model.get_model()].lists[l].is_encrypted))
                getattr(model, l)._object_id = model.get_db_id()
                getattr(model, l)._caller_id = model.get_db_id()

        if context.models[model.get_model()].dicts is not None:
            for d in context.models[model.get_model()].dicts.keys():
                setattr(model, d,
                        dinemic.DField(f, context.models[model.get_model()].dicts[d].is_encrypted))
                getattr(model, d)._object_id = model.get_db_id()
                getattr(model, d)._caller_id = model.get_db_id()

        logging.debug('Created object ' + model.get_db_id())
        return model

    @staticmethod
    def load(document, context):
        models = {}

        for model_name in document.keys():
            models[model_name] = Model(model_name, document[model_name], context)

        context.models = models

    @staticmethod
    def apply(model_name, document, context):
        logging.debug(str(document))
        from starsheep.variables.variable import Variable

        if model_name not in context.models.keys():
            raise Exception('Unknown model ' + model_name + '. Define it first in application section')

        model = None
        model_definition = context.models[model_name]

        authorized_objects = []
        if 'authorized_objects' in document:
            for obj in document['authorized_objects']:
                if obj.startswith('@'):
                    models = dinemic.object_list_owned(obj[1:] + ':*')
                    if not models:
                        raise Exception('Required authorized object is missing on this machine: ' + obj[1:])
                    authorized_objects.append(models[0])
                else:
                    authorized_objects.append(obj)

        models = dinemic.object_list_owned(model_name + ':[ID]')

        if model_definition.instances == '0' and len(models) == 0:
            logging.info('Not creating model ' + model_name + '. Not required')
            return
        elif model_definition.instances == '1' and len(models) > 1:
            for model_id in models[1:]:
                m = dinemic.DModel(model_id)
                m.remove()
                logging.warn("Removed excessed object " + model_name)
        logging.debug('Continuing with existing instance(s)')

        if not models:
            # No existing models on local machine
            model = Model.create_object(model_name, authorized_objects, context)
            logging.info('Created new object of ' + model_name + ' with ' + str(len(authorized_objects)) + ' authorized objects')
        else:
            # Check if there is model with unique field. If yes, then update that one
            if model_definition.unique is not None or model_definition.unique == '':
                if 'fields' not in document and model_definition.unique not in document['fields']:
                    raise Exception('No unique field "' + model_definition.unique + '" in new data. Please add one to model data ' + model_name)

                # Check for first occurance of object with unique field that equals new value
                unique_value = Variable.load({'value': document['fields'][model_definition.unique]}, context)['value'].value

                for model_id in models:
                    tmp_model = Model.get_object(model_id, model_id, context)
                    if getattr(tmp_model, model_definition.unique).get() == unique_value:
                        model = Model.get_object(model_id, model_id, context)
                        logging.debug('Got existing object with unique ' + context.models[model_name].unique + ': ' + unique_value)
                        break

                # Model was not found in above loop
                if model is None:
                    model = Model.create_object(model_name, authorized_objects, context)
            else:
                # If no unique is set, then just get first occurance of model
                model = Model.get_object(models[0], models[0], context)

        ignore_duplicates = True
        if 'ignore_duplicates' in document:
            ignore_duplicates = document['ignore_duplicates']

        if 'fields' in document:
            for field_name in document['fields'].keys():
                if field_name not in context.models[model_name].fields.keys():
                    raise Exception('Field "' + field_name + '" not in defined fields of model ' + model_name)

                if 'value' in document['fields'][field_name]:
                    # TODO: Ignore duplicates
                    value = str(document['fields'][field_name]['value'])
                    logging.debug('Setting variable to: ' + value)
                    getattr(model, field_name).set(value)
                elif 'from_variable' in document['fields'][field_name]:
                    if document['fields'][field_name]['from_variable'] not in context.variables:
                        raise Exception('Variable "' + document['fields'][field_name]['from_variable'] + '" was not defined and used in model ' + model_name)
                    value = context.variables[document['fields'][field_name]['from_variable']].value
                    # TODO: Ignore duplicates
                    logging.debug('Setting variable to: ' + value)
                    getattr(model, field_name).set(value)
                elif 'from_script' in document['fields'][field_name]:
                    #TODO
                    pass
                else:
                    raise Exception('Missing value for field ' + field_name + ' in model ' + model_name)

        if 'lists' in document:
            for list_name in document['lists'].keys():
                if list_name not in context.models[model_name].lists.keys():
                    raise Exception('List "' + list_name + '" not in defined lists of model ' + model_name)

                for item in document['lists'][list_name]:
                    logging.debug('Setting value for list ' + list_name)
                    if 'value' in item:
                        value = str(item['value'])
                        if getattr(model, list_name).index(value) < 0 or not ignore_duplicates:
                            getattr(model, list_name).append(value)
                        else:
                            logging.debug('Value already exists in list')
                    elif 'from_variable' in item:
                        if item['from_variable'] not in context.variables:
                            raise Exception('Variable "' + item['from_variable'] + '" was not defined and used in model ' + model_name)

                        value = str(context.variables[item['from_variable']].value)
                        if getattr(model, list_name).index(value) < 0 or not ignore_duplicates:
                            getattr(model, list_name).append(value)
                        else:
                            logging.debug('Value already exists in list')
                    elif 'from_script' in document['fields'][field_name]:
                        #TODO
                        pass
                    else:
                        raise Exception('Missing value for list ' + field_name + ' in model ' + model_name)

        if 'dicts' in document:
            for dict_name in document['dicts'].keys():
                if dict_name not in context.models[model_name].dicts.keys():
                    raise Exception('Dict "' + dict_name + '" not in defined dicts of model ' + model_name)

                for dict_key in document['dicts'][dict_name].keys():
                    logging.debug('Setting key ' + dict_key + ' for dict ' + dict_name + ' in model ' + model_name)
                    if 'value' in document['dicts'][dict_name][dict_key]:
                        # TODO: Ignore duplicates
                        value = str(document['dicts'][dict_name][dict_key]['value'])
                        getattr(model, field_name).set(value)
                    elif 'from_variable' in document['dicts'][dict_name][dict_key]:
                        if item['from_variable'] not in context.variables:
                            raise Exception('Variable "' + item['from_variable'] + '" was not defined and used in model ' + model_name)
                        value = str(context.variables[document['dicts'][dict_name][dict_key]['from_variable']].value)
                        # TODO: Ignore duplicates
                        getattr(model, dict_name).set(value)
                    elif 'from_script' in document['dicts'][dict_name][dict_key]:
                        #TODO
                        pass
                    else:
                        raise Exception('Missing value for dict ' + field_name + ' in model ' + model_name)

        logging.info('Updated object ' + model.get_db_id() + ' of model ' + model_name)
