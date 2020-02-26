from .utils.common import process_dict
from .data_types import TypeCollection


class PortType:
    def __init__(self, types: TypeCollection, config):
        self._types = types
        self.config = config

    def __getitem__(self, item):
        return self.config[item]

    def __contains__(self, item):
        return item in self.config

    def generate_component_function(self, port):
        return self.create_component_functions(port)

    def declare_functions(self, port):
        raise NotImplementedError

    def create_component_functions(self, port):
        raise NotImplementedError

    def create_runtime_functions(self, port):
        raise NotImplementedError

    def process_port(self, cn, pn, port_data):

        attributes = self.config['def_attributes']
        port_data = port_data.copy()
        port_type = port_data['port_type']
        del port_data['port_type']
        return Port(cn, pn, {
            'port_type': port_type,
            **attributes['static'],
            **process_dict(port_data, attributes['required'], attributes['optional'])
        }, self)


class Port:
    def __init__(self, component_name, port_name, port_data, port_type):
        self.port_name = port_name
        self.component_name = component_name
        self.port_type = port_type
        self.port_data = port_data

        self._full_name = f'{component_name}/{port_name}'

        self.functions = port_type.declare_functions(self)

    @property
    def full_name(self):
        return self._full_name

    @property
    def is_consumer(self):
        return 'consumes' in self.port_type and self.port_type['consumes']

    def __getitem__(self, item):
        return self.port_data[item]

    def __contains__(self, item):
        return item in self.port_data

    def get(self, item, default=None):
        return self.port_data.get(item, default)

    def create_runtime_functions(self):
        return self.port_type.create_runtime_functions(self)

    def create_component_functions(self):
        return self.port_type.create_component_functions(self)
