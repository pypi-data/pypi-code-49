from imis.utils import snake_case, generic_property_data_collection_to_dict, dict_to_generic_property_data_collection


GENERIC_ENTITY_DATA = 'Asi.Soa.Core.DataContracts.GenericEntityData, Asi.Contracts'


class GenericEntityDataRecord:

    def __init__(self, api_data):
        if api_data['$type'] != GENERIC_ENTITY_DATA:
            raise ValueError(f'api_data must have "$type" of: {GENERIC_ENTITY_DATA}')
        self._api_data = api_data
        self.simple_data = generic_property_data_collection_to_dict(self._api_data['Properties'])

    @property
    def api_data(self):
        self._api_data['Properties'] = dict_to_generic_property_data_collection(self.simple_data)
        return self._api_data

    @property
    def primary_identifier(self):
        return self._api_data['PrimaryParentIdentity']['IdentityElements']['$values'][0]


class BasicRecord:

    def __init__(self, **kwargs):
        self.__dict__ = {snake_case(k): v for k, v in  kwargs.items()}

    def __getattr__(self, name):
        try:
            return self.__dict__[name.lower()]
        except KeyError:
            raise AttributeError(f'{name} does not exist on this object')

    def __setattr__(self, name, value):
        super().__setattr__(snake_case(name), value)

    def __repr__(self):
        return '<BasicRecord>'

    def __str__(self):
        return repr(self)
