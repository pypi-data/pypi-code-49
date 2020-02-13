ASI_GENERIC_PROPERTY_DATA_COLLECTION = 'Asi.Soa.Core.DataContracts.GenericPropertyDataCollection, Asi.Contracts'
ASI_GENERIC_PROPERTY_DATA = 'Asi.Soa.Core.DataContracts.GenericPropertyData, Asi.Contracts'
ASI_GENERIC_PROPERTY_DATA_TYPES = (
    (str, None),
    (float, 'System.Decimal'),
    (int, 'System.Int32'),
    (bool, 'System.Boolean'),
)


def generic_property_data(name, value):
    data = {
        '$type': ASI_GENERIC_PROPERTY_DATA,
        'Name': name
    }
    for instance_type, asi_type_label in ASI_GENERIC_PROPERTY_DATA_TYPES:
        if isinstance(value, instance_type):
            if asi_type_label is None:
                data['Value'] = value
            else:
                data['Value'] = {
                    '$type': asi_type_label,
                    '$value': value
                }
            return data
    raise ValueError('value arg is not of a supported type: str, float, int, bool')


def generic_property_data_collection_to_dict(collection):
    if collection['$type'] != ASI_GENERIC_PROPERTY_DATA_COLLECTION:
        msg = 'Input must be: {0}'.format(ASI_GENERIC_PROPERTY_DATA_COLLECTION)
        raise ValueError(msg)
    output = {}
    for prop in collection['$values']:
        k = prop['Name']
        try:
            output[k] = prop['Value']['$value']
        except TypeError:
            output[k] = prop['Value']
        except KeyError:
            output[k] = None
    return output


def dict_to_generic_property_data_collection(d):
    return {
        '$type': ASI_GENERIC_PROPERTY_DATA_COLLECTION,
        '$values': [generic_property_data(k, v) for k, v in d.items()]
    }



def snake_case(string):
    out = []
    for part in string.split():
        part_chars = []
        for index, s in enumerate(part):
            if index == 0:
                part_chars.append(s.lower())
            else:
                if s.isupper():
                    if string[index - 1].islower():
                        part_chars.append('_')
                part_chars.append(s.lower())
        out.append(''.join(part_chars))
    return '_'.join(out)
