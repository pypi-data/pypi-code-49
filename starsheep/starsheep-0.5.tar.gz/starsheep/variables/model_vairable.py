import dinemic
from starsheep.variables.variable import Variable
import logging

class ModelVariable(Variable):
    model_name = None
    field_name = None
    list_name = None
    dict_name = None

    read_as = None

    def __init__(self, variable_name, document, context):
        super(ModelVariable, self).__init__(variable_name, document, context)
        if 'from_object' not in document:
            raise Exception('Missing "from_object" in variable definition ' + variable_name)

        if 'model' not in document['from_object']:
            raise Exception('Missing "model" in variable ' + variable_name)

        if 'field' not in document['from_object'] and 'list' not in document['from_object'] and 'dict' not in document['from_object']:
            raise Exception('Missing one of: "field", "list" or "dict" in variable ' + variable_name)

        self.model_name = document['from_object']['model']

        if 'field' in document:
            self.field_name = document['from_object']['field']
        elif 'list' in document:
            self.list_name = document['from_object']['list']
        elif 'dict' in document:
            self.dict_name = document['from_object']['dict']

        if 'read_as' in document:
            self.read_as = document['from_object']['read_as']
        else:
            self.read_as = ''


    @property
    def value(self):
        model = None
        read_as = None

        if self.read_as.startswith('@'):
            models = dinemic.object_list_owned(self.read_as[1:] + ':[ID]')

            if not models:
                # TODO: Raise exception or return empty value?
                raise Exception('No owned model with name ' + self.model_name)

            read_as = models[0]
        else:
            read_as = self.read_as

        if self.model_name.startswith('@'):
            models = dinemic.object_list_owned(self.model_name[1:] + ':[ID]')

            if not models:
                raise Exception('No owned model with name ' + self.model_name)

            model = dinemic.DModel(models[0], read_as)
        else:
            model = dinemic.DModel(self.model_name, read_as)

        # TODO: update encrypted to get information from model(s)
        encrypted = False
        if read_as != '':
            encrypted = True

        if self.field_name is not None:
            if self.field_name == 'id':
                return model.get_db_id()

            setattr(model, self.field_name, dinemic.DField(self.field_name, encrypted))
            getattr(model, self.field_name)._object_id = model.get_db_id()
            getattr(model, self.field_name)._caller_id = read_as

            value = getattr(model, self.field_name).get('')

            logging.debug('Calculated value for ' + self.variable_name + ': ' + value)
            return value
        elif self.list_name is not None:
            if ',' not in self.list_name:
                raise Exception('Malformed "list" selector. Use: list_name,index')

            list_name = self.list_name.split(',')[0]
            list_index = self.list_name.split(',')[1]

            setattr(model, list_name, dinemic.DList(list_name, encrypted))
            getattr(model, list_name)._object_id = model.get_db_id()
            getattr(model, list_name)._caller_id = read_as

            value = getattr(model, list_name).at(list_index)

            logging.debug('Calculated value for ' + self.variable_name + ': ' + value)
            return value
        elif self.dict_name is not None:
            if ',' not in self.list_name:
                raise Exception('Malformed "dict" selector. Use: dict_name,key')

            dict_name = self.dict_name.split(',')[0]
            dict_key = self.dict_name.split(',')[1]

            setattr(model, dict_name, dinemic.DList(dict_name, encrypted))
            getattr(model, dict_name)._object_id = model.get_db_id()
            getattr(model, dict_name)._caller_id = read_as

            value = getattr(model, dict_name).get(dict_key, '')
            logging.debug('Calculated value for ' + self.variable_name + ': ' + value)
            return value
        else:
            raise Exception('Missing one of "field", "list" or "dict"')
