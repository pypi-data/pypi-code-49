#from model.data_type import DataType

field_keys = [ 'name', 'type', 'description', 'required', 'example', 'maximum' ]

def from_dict(ents):
    output_list = []
    for ent_key in ents.keys():
        ent_dict = ents[ent_key]
        try:
            ent = build_entity(ent_dict, ent_key)
            output_list.append(ent)
        except EntityException as e:
            print('Caught an error while generating entity: ' + e.name)
            print(e.__cause__)
    return output_list

def build_entity(ent_dict, name):
    #Represent as dicts instead of objects for now to avoid serialization problems
    #Might need to solve this eventually
    #Want name at first place, put placeholder to preserve order
    ent = { 'name': 'placeholder'}
    ent.update(ent_dict)
    ent['name'] = name
    return ent

#TODO: Validate input to verify that object corresponds to a valid entity
def validate_entity(entity):
    return True

class EntityException(Exception):

    def __init__(self, message, ent_dict, name = 'unknown'):
        super(EntityException, self).__init__(message)
        self.name = name
        self.entity_dict = ent_dict