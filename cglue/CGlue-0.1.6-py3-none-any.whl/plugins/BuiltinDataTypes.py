import chevron

from cglue.function import FunctionPrototype, FunctionImplementation
from cglue.utils.common import chevron_list_mark_last, dict_to_chevron_list
from cglue.ports import PortType
from cglue.data_types import TypeCollection, TypeCategory
from cglue.cglue import Plugin, CGlue
from cglue.signal import SignalConnection, SignalType
from cglue.component import Component


class StructType(TypeCategory):

    def __init__(self, type_collection):
        attributes = {
            'required': ['fields'],
            'optional': {
                'pass_semantic': TypeCollection.PASS_BY_POINTER,
                'default_value': {}
            },
            'static':   {
                'type': TypeCollection.STRUCT
            }
        }
        super().__init__(type_collection, 'struct', attributes)

    def render_typedef(self, type_name, type_data):
        context = {
            'template': "\n"
                        "typedef struct {\n"
                        "    {{# fields }}\n"
                        "    {{ type }} {{ name }};\n"
                        "    {{/ fields }}\n"
                        "} {{ type_name }};",

            'data':     {
                'type_name': type_name,
                'fields':    dict_to_chevron_list(type_data['fields'], key_name='name', value_name='type')
            }
        }

        return chevron.render(**context)

    def render_value(self, type_name, type_data, value, context='assignment'):
        if type(value) is str:
            return value

        types = self._type_collection
        field_types = type_data['fields']
        field_values = {field_name: value.get(field_name) for field_name in field_types}

        def render(field_name, field_value):
            """Render field values"""
            return types.get(field_types[field_name]).render_value(field_value, 'initialization')

        rendered_values = {name: render(name, value) for name, value in field_values.items()}

        rendered_field_values = (f'.{name} = {rendered}' for name, rendered in rendered_values.items())

        fields_str = ', '.join(rendered_field_values)
        if context == 'initialization':
            return f'{{ {fields_str} }}'
        else:
            return f'({type_name}) {{ {fields_str} }}'

    def attribute(self, type_name, type_data, name):
        if name == 'default_value':
            # if a struct member does not have default value, look for it recursively
            default = type_data['default_value']
            struct_fields = type_data['fields']

            def default_value(field_name):
                # use 'or' so we only look up the default for the field if it is not given in the struct data
                return default.get(field_name) or self._type_collection.get(struct_fields[field_name]).default_value()

            return {name: default_value(name) for name in struct_fields}
        else:
            return super().attribute(type_name, type_data, name)


class EnumType(TypeCategory):

    def __init__(self, type_collection):
        attributes = {
            'required': ['values', 'default_value'],
            'optional': {'pass_semantic': TypeCollection.PASS_BY_VALUE},
            'static':   {
                'type': TypeCollection.ENUM
            }
        }
        super().__init__(type_collection, 'enum', attributes)

    def render_typedef(self, type_name, type_data):
        context = {
            'template': "\n"
                        "typedef enum {\n"
                        "    {{# values }}\n"
                        "    {{ value }}{{^ last }},{{/ last }}\n"
                        "    {{/ values }}\n"
                        "} {{ type_name }};",

            'data':     {
                'type_name': type_name,
                'values':    chevron_list_mark_last([{'value': value} for value in type_data['values']])
            }
        }

        return chevron.render(**context)


class UnionType(TypeCategory):

    def __init__(self, type_collection):
        attributes = {
            'required': ['members', 'default_value'],
            'optional': {'pass_semantic': TypeCollection.PASS_BY_POINTER},
            'static':   {
                'type': TypeCollection.UNION
            }
        }
        super().__init__(type_collection, 'union', attributes)

    def render_typedef(self, type_name, type_data):
        context = {
            'template': "\n"
                        "typedef union {\n"
                        "    {{# members }}\n"
                        "    {{ type }} {{ name }};\n"
                        "    {{/ members }}\n"
                        "} {{ type_name }};",

            'data':     {
                'type_name': type_name,
                'members':   dict_to_chevron_list(type_data['members'], key_name='name', value_name='type')
            }
        }

        return chevron.render(**context)

    def render_value(self, type_name, type_data, value, context='assignment'):
        if type(value) is str:
            return value

        if len(value) != 1:
            raise Exception('Only a single union member can be assigned')

        members = {name: self._type_collection.get(member_type) for name, member_type in type_data['members'].items()}
        values = [f'.{name} = {members[name].render_value(value, "initialization")}'
                  for name, value in value.items()]

        values_str = ', '.join(values)
        if context == 'initialization':
            return f'{{ {values_str} }}'
        else:
            return f'({type_name}) {{ {values_str} }}'


def lookup_member(types: TypeCollection, data_type, member_list):
    if not member_list:
        return data_type

    type_data = types.get(data_type)

    keys = {
        TypeCollection.STRUCT: 'fields',
        TypeCollection.UNION: 'members'
    }

    try:
        member_key = keys[type_data['type']]
        members = type_data[member_key]
    except KeyError:
        raise Exception(f'Trying to access member of non-struct type {data_type}')

    return lookup_member(types, members[member_list[0]], member_list[1:])


def create_member_accessor(member):
    return '.' + member


class VariableSignal(SignalType):
    def __init__(self):
        super().__init__(consumers='multiple')

    def create(self, context, connection: SignalConnection):
        runtime = context['runtime']
        provider_port_data = runtime.get_port(connection.provider)
        data_type_name = provider_port_data['data_type']
        data_type = runtime.types.get(data_type_name)
        init_value = connection.attributes.get('init_value', data_type.default_value())
        rendered_init_value = data_type.render_value(init_value, 'initialization')
        context['declarations'].append(
            f'static {data_type_name} {connection.name} = {rendered_init_value};'
        )

    def generate_provider(self, context, connection: SignalConnection, provider_name):
        runtime = context['runtime']
        provider_port_data = runtime.get_port(provider_name)
        data_type = provider_port_data['data_type']

        function = runtime.functions[provider_name]['write']
        argument_names = list(function.arguments.keys())

        if runtime.types.get(data_type).passed_by() == TypeCollection.PASS_BY_VALUE:
            assignment = f'{connection.name} = {argument_names[0]};'
        else:
            assignment = f'{connection.name} = *{argument_names[0]};'

        return {
            provider_name: {
                'write': {
                    'used_arguments': argument_names,
                    'body':           assignment
                }
            }
        }

    def generate_consumer(self, context, connection: SignalConnection, consumer_name, attributes):
        runtime = context['runtime']
        provider_port_data = runtime.get_port(connection.provider)
        source_data_type = provider_port_data['data_type']

        consumer_port_data = runtime.get_port(consumer_name)
        data_type = consumer_port_data['data_type']

        if 'member' in attributes:
            member_list = attributes['member'].split('.')
            source_data_type = lookup_member(runtime.types, source_data_type, member_list)
            member_accessor = create_member_accessor(attributes['member'])
        else:
            member_accessor = ''

        if data_type != source_data_type:
            raise Exception(
                f'Port data types don\'t match (Provider: {source_data_type} Consumer: {data_type})')

        function = runtime.functions[consumer_name]['read']
        argument_names = list(function.arguments.keys())
        mods = {
            consumer_name: {'read': {}}
        }
        if runtime.types.get(data_type).passed_by() == TypeCollection.PASS_BY_VALUE:
            return_value = f'{data_type} return_value = {connection.name}{member_accessor};'
            mods[consumer_name]['read']['body'] = return_value
            mods[consumer_name]['read']['return_statement'] = 'return_value'
        else:
            out_name = argument_names[0]
            out_assignment = f'*{out_name} = {connection.name}{member_accessor};'
            mods[consumer_name]['read']['used_arguments'] = [out_name]
            mods[consumer_name]['read']['body'] = out_assignment

        return mods


class ArraySignal(SignalType):
    def __init__(self):
        super().__init__(consumers='multiple')

    def create(self, context, connection: SignalConnection):
        runtime = context['runtime']
        provider_port_data = runtime.get_port(connection.provider)
        data_type_name = provider_port_data['data_type']
        count = provider_port_data['count']

        try:
            # either all init values are specified
            init_values = connection.attributes['init_values']
        except KeyError:
            # ... or a single one is
            data_type = runtime.types.get(data_type_name)
            default_value = data_type.default_value()
            init_value = connection.attributes.get('init_value', default_value)
            init_values = [data_type.render_value(init_value, 'initialization')] * count

        if type(init_values) is list:
            if len(init_values) != count:
                raise Exception(f'Array initializer count ({len(init_values)}) does not '
                                f'match size ({count}) - signal provided by {connection.provider}')

            init_values = ', '.join(init_values)

        context['declarations'].append(f'static {data_type_name} {connection.name}[{count}] = {{ {init_values} }};')

    def generate_provider(self, context, connection: SignalConnection, provider_name):
        runtime = context['runtime']
        provider_port_data = runtime.get_port(provider_name)
        data_type = provider_port_data['data_type']

        function = runtime.functions[provider_name]['write']
        argument_names = list(function.arguments.keys())

        index = argument_names[0]
        value = argument_names[1]

        if runtime.types.get(data_type).passed_by() == TypeCollection.PASS_BY_VALUE:
            body = f'{connection.name}[{index}] = {value};'
        else:
            body = f'{connection.name}[{index}] = *{value};'

        return {
            provider_name: {
                'write': {
                    'used_arguments': [index, value],
                    'body':           body
                }
            }
        }

    def generate_consumer(self, context, connection: SignalConnection, consumer_name, attributes):
        runtime = context['runtime']
        provider_port_data = runtime.get_port(connection.provider)
        source_data_type = provider_port_data['data_type']

        consumer_port_data = runtime.get_port(consumer_name)
        data_type = consumer_port_data['data_type']

        if 'member' in attributes:
            member_list = attributes['member'].split('.')
            source_data_type = lookup_member(runtime.types, source_data_type, member_list)
            member_accessor = create_member_accessor(attributes['member'])
        else:
            member_accessor = ''

        if data_type != source_data_type:
            raise Exception('Port data types don\'t match')

        function = runtime.functions[consumer_name]['read']
        argument_names = list(function.arguments.keys())

        if runtime.types.get(data_type).passed_by() == TypeCollection.PASS_BY_VALUE:

            if 'count' not in consumer_port_data:
                # single read, index should be next to consumer name
                index = attributes['index']
                used_arguments = []
            else:
                if consumer_port_data['count'] > provider_port_data['count']:
                    raise Exception(
                        f'{consumer_name} signal count ({consumer_port_data["count"]}) '
                        f'is incompatible with {connection.provider} ({provider_port_data["count"]})')
                index = argument_names[0]
                used_arguments = [index]

            mods = {
                consumer_name: {
                    'read': {
                        'used_arguments': used_arguments,
                        'body': f'{data_type} return_value = {connection.name}[{index}]{member_accessor};',
                        'return_statement': 'return_value'
                    }
                }
            }
        else:
            if 'count' not in consumer_port_data:
                # single read, index should be next to consumer name in attributes
                index = connection.attributes['index']
                out_name = argument_names[0]
                used_arguments = []
            else:
                if consumer_port_data['count'] > provider_port_data['count']:
                    raise Exception(
                        f'{consumer_name} signal count ({consumer_port_data["count"]}) '
                        f'is incompatible with {connection.provider} ({provider_port_data["count"]})')
                index = argument_names[0]
                out_name = argument_names[1]
                used_arguments = [index, out_name]

            mods = {
                consumer_name: {
                    'read': {
                        'used_arguments': used_arguments,
                        'body': f'*{out_name} = {connection.name}[{index}]{member_accessor};'
                    }
                }
            }

        return mods


class QueueSignal(SignalType):
    def __init__(self):
        super().__init__(consumers='multiple_signals', required_attributes=['queue_length'])

    def create(self, context, connection: SignalConnection):
        if connection.attributes['queue_length'] == 1:
            template = \
                "static {{ data_type }} {{ signal_name }};\n" \
                "static bool {{ signal_name }}_overflow = false;\n" \
                "static bool {{ signal_name }}_data_valid = false;"
        else:
            template = \
                "static {{ data_type }} {{ signal_name }}[{{ queue_length }}u];\n" \
                "static size_t {{ signal_name}}_count = 0u;\n" \
                "static size_t {{ signal_name}}_write_index = 0u;\n" \
                "static bool {{ signal_name }}_overflow = false;"

        runtime = context['runtime']
        provider_port_data = runtime.get_port(connection.provider)
        data_type = provider_port_data['data_type']

        data = {
            'data_type':    data_type,
            'signal_name':  connection.name,
            'queue_length': connection.attributes['queue_length']
        }
        context['declarations'].append(chevron.render(template, data))

    def generate_provider(self, context, connection: SignalConnection, provider_name):
        runtime = context['runtime']
        provider_port_data = runtime.get_port(provider_name)
        data_type = provider_port_data['data_type']

        if connection.attributes['queue_length'] == 1:
            template = \
                "{{ signal_name }}_overflow = {{ signal_name }}_data_valid;\n" \
                "{{ signal_name }} = {{ value }};\n" \
                "{{ signal_name }}_data_valid = true;"
        else:
            template = \
                "{\n" \
                "    if ({{ signal_name }}_count < {{ queue_length }}u)\n" \
                "    {\n" \
                "        ++{{ signal_name }}_count;\n" \
                "    }\n" \
                "    else\n" \
                "    {\n" \
                "        {{ signal_name }}_overflow = true;\n" \
                "    }\n" \
                "    size_t idx = {{ signal_name }}_write_index;\n" \
                "    {{ signal_name }}_write_index = ({{ signal_name }}_write_index + 1u) % {{ queue_length }}u;\n" \
                "    {{ signal_name }}[idx] = {{ value }};\n" \
                "}"

        function = runtime.functions[provider_name]['write']
        argument_names = list(function.arguments.keys())
        passed_by_value = runtime.types.get(data_type).passed_by() == TypeCollection.PASS_BY_VALUE
        return {
            connection.provider: {
                'write': {
                    'used_arguments': [argument_names[0]],
                    'body':           chevron.render(template, {
                        'queue_length': connection.attributes['queue_length'],
                        'signal_name':  connection.name,
                        'value':        argument_names[0] if passed_by_value else '*' + argument_names[0]
                    })
                }
            }
        }

    def generate_consumer(self, context, connection: SignalConnection, consumer_name, attributes):
        runtime = context['runtime']
        provider_port_data = runtime.get_port(connection.provider)
        source_data_type = provider_port_data['data_type']

        if 'member' in attributes:
            member_list = attributes['member'].split('.')
            source_data_type = lookup_member(runtime.types, source_data_type, member_list)
            member_accessor = create_member_accessor(attributes['member'])
        else:
            member_accessor = ''

        if connection.attributes['queue_length'] == 1:
            template = \
                "QueueStatus_t return_value = QueueStatus_Empty;\n" \
                "bool was_overflow = {{ signal_name }}_overflow;\n" \
                "if ({{ signal_name }}_data_valid)\n" \
                "{\n" \
                "    {{ signal_name }}_overflow = false;\n" \
                "    {{ out_name }} = {{ signal_name }}{{ member_accessor }};\n" \
                "    {{ signal_name }}_data_valid = false;\n" \
                "    if (was_overflow)\n" \
                "    {\n" \
                "        return_value = QueueStatus_Overflow;\n" \
                "    }\n" \
                "    else\n" \
                "    {\n" \
                "        return_value = QueueStatus_Ok;\n" \
                "    }\n" \
                "}"
        else:
            template = \
                "QueueStatus_t return_value = QueueStatus_Empty;\n" \
                "if ({{ signal_name }}_count > 0u)\n" \
                "{\n" \
                "    size_t idx = ({{ signal_name }}_write_index - {{ signal_name }}_count) % {{ queue_length }}u;\n" \
                "    --{{ signal_name }}_count;\n" \
                "    {{ out_name }} = {{ signal_name }}[idx]{{ member_accessor }};\n" \
                "    \n" \
                "    if ({{ signal_name }}_overflow)\n" \
                "    {\n" \
                "        {{ signal_name }}_overflow = false;\n" \
                "        return_value = QueueStatus_Overflow;\n" \
                "    }\n" \
                "    else\n" \
                "    {\n" \
                "        return_value = QueueStatus_Ok;\n" \
                "    }\n" \
                "}"

        function = runtime.functions[consumer_name]['read']
        argument_names = list(function.arguments.keys())
        passed_by_value = runtime.types.get(source_data_type).passed_by() == TypeCollection.PASS_BY_VALUE
        data = {
            'queue_length':    connection.attributes['queue_length'],
            'signal_name':     connection.name,
            'out_name':        argument_names[0] if passed_by_value else '*' + argument_names[0],
            'member_accessor': member_accessor
        }

        return {
            consumer_name: {
                'read': {
                    'used_arguments':   [argument_names[0]],
                    'body':             chevron.render(template, data),
                    'return_statement': 'return_value'
                }
            }
        }


class ConstantSignal(SignalType):
    def __init__(self):
        super().__init__(consumers='multiple')

    def create(self, context, connection: SignalConnection):
        pass

    def generate_provider(self, context, connection: SignalConnection, provider_name):
        pass

    def generate_consumer(self, context, connection: SignalConnection, consumer_name, attributes):
        runtime = context['runtime']
        provider_port_data = runtime.get_port(connection.provider)
        source_data_type = provider_port_data['data_type']

        consumer_port_data = runtime.get_port(consumer_name)
        data_type = consumer_port_data['data_type']

        if 'member' in attributes:
            member_list = attributes['member'].split('.')
            source_data_type = lookup_member(runtime.types, source_data_type, member_list)
            member_accessor = create_member_accessor(attributes['member'])
        else:
            member_accessor = ''

        if data_type != source_data_type:
            raise Exception('Port data types don\'t match')

        function = context['functions'][consumer_name]['read']
        argument_names = list(function.arguments.keys())

        constant_provider = runtime.get_port(connection.provider).functions['constant']
        mods = {
            consumer_name: {'read': {}}
        }

        if runtime.types.get(data_type).passed_by() == TypeCollection.PASS_BY_VALUE:
            mods[consumer_name]['read']['return_statement'] = constant_provider.generate_call({}) + member_accessor
        else:
            if member_accessor:
                body = f"{provider_port_data['data_type']} tmp;\n" \
                       f"{constant_provider.generate_call({'value': '&tmp'})};\n" \
                       f"{argument_names[0]} = tmp{member_accessor};"
            else:
                body = constant_provider.generate_call({"value": argument_names[0]}) + ';'

            mods[consumer_name]['read']['used_arguments'] = [argument_names[0]]
            mods[consumer_name]['read']['body'] = body

        return mods


class ConstantArraySignal(SignalType):
    def __init__(self):
        super().__init__(consumers='multiple')

    def create(self, context, connection: SignalConnection):
        pass

    def generate_provider(self, context, connection: SignalConnection, provider_name):
        pass

    def generate_consumer(self, context, connection: SignalConnection, consumer_name, attributes):
        runtime = context['runtime']
        provider_port_data = runtime.get_port(connection.provider)
        source_data_type = provider_port_data['data_type']

        consumer_port_data = runtime.get_port(consumer_name)
        data_type = consumer_port_data['data_type']

        if 'member' in attributes:
            member_list = attributes['member'].split('.')
            source_data_type = lookup_member(runtime.types, source_data_type, member_list)
            member_accessor = create_member_accessor(attributes['member'])
        else:
            member_accessor = ''

        if data_type != source_data_type:
            raise Exception('Port data types don\'t match')

        function = context['functions'][consumer_name]['read']
        argument_names = list(function.arguments.keys())

        constant_provider = runtime.get_port(connection.provider).functions['constant']

        mods = {
            consumer_name: {'read': {}}
        }

        if runtime.types.get(data_type).passed_by() == TypeCollection.PASS_BY_VALUE:

            if 'count' not in consumer_port_data:
                # single read, index should be next to consumer name
                index = attributes['index']
            else:
                if consumer_port_data['count'] > provider_port_data['count']:
                    raise Exception(
                        f'{consumer_name} signal count ({consumer_port_data["count"]}) '
                        f'is incompatible with {connection.provider} ({provider_port_data["count"]})')
                index = argument_names[0]
                mods[consumer_name]['read']['used_arguments'] = [argument_names[0]]

            ctx = {
                'template': '{{ data_type}} return_value = {{ constant_provider }}{{ member_accessor }};',
                'data':     {
                    'data_type':         data_type,
                    'constant_provider': constant_provider.generate_call({'index': index}),
                    'member_accessor':   member_accessor
                }
            }
            mods[consumer_name]['read']['body'] = chevron.render(**ctx)
            mods[consumer_name]['read']['return_statement'] = 'return_value'
        else:

            if 'count' not in consumer_port_data:
                # single read, index should be next to consumer name
                index = connection.attributes['index']
                out_name = argument_names[0]
            else:
                if consumer_port_data['count'] > provider_port_data['count']:
                    raise Exception(
                        f'{consumer_name} signal count ({consumer_port_data["count"]}) '
                        f'is incompatible with {connection.provider} ({provider_port_data["count"]})')
                index = argument_names[0]
                out_name = argument_names[1]
                mods[consumer_name]['read']['used_arguments'] = [argument_names[0], argument_names[1]]

            if member_accessor:
                ctx = {
                    'template': '{{ data_type }} tmp;\n'
                                '{{ constant_provider }};\n'
                                '{{ out_name }} = tmp{{ member_accessor }};',
                    'data':     {
                        'constant_provider': constant_provider.generate_call({'index': index, 'value': '&tmp'}),
                        'out_name':          out_name,
                        'member_accessor':   member_accessor,
                        'data_type':         provider_port_data['data_type']
                    }
                }
                mods[consumer_name]['read']['body'] = chevron.render(**ctx)
            else:
                mods[consumer_name]['read']['body'] = constant_provider.function_call({"index": index,
                                                                                       "value": out_name}) + ';'

        return mods


def process_type_def(types: TypeCollection, type_name, type_def):
    type_data = type_def.copy()
    # determine type of definition
    if 'type' in type_data:
        type_category = type_data['type']
        del type_data['type']
    else:
        if 'defined_in' in type_data:
            type_category = TypeCollection.EXTERNAL_DEF
        elif 'aliases' in type_data:
            type_category = TypeCollection.ALIAS
        elif 'fields' in type_data:
            type_category = TypeCollection.STRUCT
        elif 'members' in type_data:
            type_category = TypeCollection.UNION
        else:
            raise Exception(f'Invalid type definition for {type_name}')

    try:
        return types.category(type_category).process_type(type_data)
    except KeyError:
        print(f'Unknown type category {type_category} set for {type_name}')
        raise
    except Exception as e:
        raise Exception(f'Type {type_name} ({type_category}) definition is not valid: {e}')


class ReadValuePortType(PortType):
    def __init__(self, types):
        super().__init__(types, {
            'order':          3,
            'consumes':       {
                'array':            'single',
                'variable':         'single',
                'constant':         'single',
                'constant_array':   'single'
            },
            'def_attributes': {
                'required': ['data_type'],
                'optional': {'default_value': None},
                'static':   {}
            }
        })

    def declare_functions(self, port):
        data_type = self._types.get(port['data_type'])

        fn_name = f'{port.component_name}_Read_{port.port_name}'

        if data_type.passed_by() == 'value':
            function = FunctionPrototype(fn_name, data_type.name)
        else:
            function = FunctionPrototype(fn_name, 'void', {
                'value': {'direction': 'out', 'data_type': data_type}
            })

        return {'read': function}

    def create_component_functions(self, port):
        prototype = port.functions['read']
        data_type = self._types.get(port['data_type'])

        function = FunctionImplementation(prototype)
        function.attributes.add('weak')

        default_value = data_type.render_value(port['default_value'])
        if data_type.passed_by() == 'value':
            function.set_return_statement(default_value)
        else:
            function.add_input_assert('value != NULL')
            function.mark_argument_used('value')
            function.add_body('*value = {};'.format(default_value))

        return {'read': function}

    def create_runtime_functions(self, port):
        prototype = port.functions['read']
        data_type = self._types.get(port['data_type'])

        function = FunctionImplementation(prototype)
        if data_type.passed_by() == 'pointer':
            function.add_input_assert('value != NULL')

        return {'read': function}


class ReadQueuedValuePortType(PortType):
    def __init__(self, types):
        super().__init__(types, {
            'order':          3,
            'consumes':       {'queue': 'single'},
            'def_attributes': {
                'required': ['data_type'],
                'optional': {'default_value': None},
                'static':   {}
            }
        })

    def declare_functions(self, port):
        data_type = self._types.get(port['data_type'])

        fn_name = f'{port.component_name}_Read_{port.port_name}'

        function = FunctionPrototype(fn_name, 'QueueStatus_t', {
            'value': {'direction': 'out', 'data_type': data_type}
        })

        return {'read': function}

    def create_component_functions(self, port):
        prototype = port.functions['read']

        queue_status_type = self._types.get('QueueStatus_t')

        function = FunctionImplementation(prototype)
        function.attributes.add('weak')
        function.add_input_assert('value != NULL')
        function.mark_argument_used('value')

        function.set_return_statement(queue_status_type.render_value(None))

        return {'read': function}

    def create_runtime_functions(self, port):
        prototype = port.functions['read']

        function = FunctionImplementation(prototype)
        function.add_input_assert('value != NULL')
        function.mark_argument_used('value')

        return {'read': function}


class ReadIndexedValuePortType(PortType):
    def __init__(self, types):
        super().__init__(types, {
            'order':          3,
            'consumes':       {
                'array':          'multiple',
                'constant_array': 'multiple'
            },
            'def_attributes': {
                'required': ['data_type', 'count'],
                'optional': {'default_value': None},
                'static':   {}
            }
        })

    def declare_functions(self, port):
        data_type = self._types.get(port['data_type'])

        fn_name = f'{port.component_name}_Read_{port.port_name}'

        if data_type.passed_by() == 'value':
            function = FunctionPrototype(fn_name, data_type.name, {
                'index': {'direction': 'in', 'data_type': self._types.get('uint32_t')}
            })
        else:
            function = FunctionPrototype(fn_name, 'void', {
                'index': {'direction': 'in', 'data_type': self._types.get('uint32_t')},
                'value': {'direction': 'out', 'data_type': data_type}
            })

        return {'read': function}

    def create_component_functions(self, port):
        prototype = port.functions['read']
        data_type = self._types.get(port['data_type'])

        function = FunctionImplementation(prototype)
        function.attributes.add('weak')
        function.add_input_assert('index < {}'.format(port['count']))
        function.mark_argument_used('index')

        default_value = data_type.render_value(port['default_value'])
        if data_type.passed_by() == 'value':
            function.set_return_statement(default_value)
        else:
            function.add_input_assert('value != NULL')
            function.mark_argument_used('value')
            function.add_body('*value = {};'.format(default_value))

        return {'read': function}

    def create_runtime_functions(self, port):
        prototype = port.functions['read']
        data_type = self._types.get(port['data_type'])

        function = FunctionImplementation(prototype)
        function.add_input_assert(f'index < {port["count"]}')
        function.mark_argument_used('index')

        if data_type.passed_by() == 'pointer':
            function.add_input_assert('value != NULL')
            function.mark_argument_used('value')

        return {'read': function}


class WriteDataPortType(PortType):
    def __init__(self, types):
        super().__init__(types, {
            'order':          2,
            'provides':       {'variable', 'queue'},
            'def_attributes': {
                'required': ['data_type'],
                'optional': {},
                'static':   {}
            }
        })

    def declare_functions(self, port):
        data_type = self._types.get(port['data_type'])

        fn_name = f'{port.component_name}_Write_{port.port_name}'

        function = FunctionPrototype(fn_name, 'void', {
            'value': {'direction': 'in', 'data_type': data_type}
        })

        return {'write': function}

    def create_component_functions(self, port):
        prototype = port.functions['write']
        data_type = self._types.get(port['data_type'])

        function = FunctionImplementation(prototype)
        function.attributes.add('weak')

        if data_type.passed_by() == 'pointer':
            function.add_input_assert('value != NULL')
            function.mark_argument_used('value')

        return {'write': function}

    def create_runtime_functions(self, port):
        prototype = port.functions['write']
        data_type = self._types.get(port['data_type'])

        function = FunctionImplementation(prototype)

        if data_type.passed_by() == 'pointer':
            function.add_input_assert('value != NULL')
            function.mark_argument_used('value')

        return {'write': function}


class WriteIndexedDataPortType(PortType):
    def __init__(self, types):
        super().__init__(types, {
            'order':          2,
            'provides':       {'array'},
            'def_attributes': {
                'required': ['data_type', 'count'],
                'optional': {},
                'static':   {}
            }
        })

    def declare_functions(self, port):
        data_type = self._types.get(port['data_type'])

        fn_name = f'{port.component_name}_Write_{port.port_name}'

        function = FunctionPrototype(fn_name, 'void', {
            'index': {'direction': 'in', 'data_type': self._types.get('uint32_t')},
            'value': {'direction': 'in', 'data_type': data_type}
        })

        return {'write': function}

    def create_component_functions(self, port):
        prototype = port.functions['write']
        data_type = self._types.get(port['data_type'])

        function = FunctionImplementation(prototype)
        function.attributes.add('weak')
        function.add_input_assert(f'index < {port["count"]}')
        function.mark_argument_used('index')

        if data_type.passed_by() == 'pointer':
            function.add_input_assert('value != NULL')
            function.mark_argument_used('value')

        return {'write': function}

    def create_runtime_functions(self, port):
        prototype = port.functions['write']
        data_type = self._types.get(port['data_type'])

        function = FunctionImplementation(prototype)
        function.add_input_assert(f'index < {port["count"]}')
        function.mark_argument_used('index')

        if data_type.passed_by() == 'pointer':
            function.add_input_assert('value != NULL')
            function.mark_argument_used('value')

        return {'write': function}


class ConstantPortType(PortType):
    def __init__(self, types):
        super().__init__(types, {
            'order':          1,
            'provides':       {'constant'},
            'def_attributes': {
                'required': ['data_type', 'value'],
                'optional': {},
                'static':   {}
            }
        })

    def declare_functions(self, port):
        data_type = self._types.get(port['data_type'])

        fn_name = f'{port.component_name}_Constant_{port.port_name}'

        if data_type.passed_by() == 'value':
            function = FunctionPrototype(fn_name, data_type.name)
        else:
            function = FunctionPrototype(fn_name, 'void', {
                'value': {'direction': 'out', 'data_type': data_type}
            })

        return {'constant': function}

    def create_component_functions(self, port):
        prototype = port.functions['constant']
        data_type = self._types.get(port['data_type'])

        function = FunctionImplementation(prototype)

        constant_value = data_type.render_value(port['value'])
        if data_type.passed_by() == 'value':
            function.set_return_statement(constant_value)
        else:
            function.add_input_assert('value != NULL')
            function.mark_argument_used('value')
            function.add_body(f'*value = {constant_value};')

        return {'constant': function}

    def create_runtime_functions(self, port):
        return {}


class ConstantArrayPortType(PortType):
    def __init__(self, types):
        super().__init__(types, {
            'order':          1,
            'provides':       {'constant_array'},
            'def_attributes': {
                'required': ['data_type', 'value', 'count'],
                'optional': {},
                'static':   {}
            }
        })

    def declare_functions(self, port):
        data_type = self._types.get(port['data_type'])

        fn_name = f'{port.component_name}_Constant_{port.port_name}'

        if data_type.passed_by() == 'value':
            function = FunctionPrototype(fn_name, data_type.name, {
                'index': {'direction': 'in', 'data_type': self._types.get('uint32_t')}
            })
        else:
            function = FunctionPrototype(fn_name, 'void', {
                'index': {'direction': 'in', 'data_type': self._types.get('uint32_t')},
                'value': {'direction': 'out', 'data_type': data_type}
            })

        return {'constant': function}

    def create_component_functions(self, port):
        prototype = port.functions['constant']
        data_type = self._types.get(port['data_type'])

        function = FunctionImplementation(prototype)
        function.add_input_assert(f'index < {port["count"]}')
        function.mark_argument_used('index')

        constant_value = ', '.join(port['value'])
        function.add_body(f'static const {data_type.name} constant[{port["count"]}] = {{ {constant_value} }};')
        if data_type.passed_by() == 'value':
            function.set_return_statement('constant[index]')
        else:
            function.add_input_assert('value != NULL')
            function.mark_argument_used('value')
            function.add_body('*value = constant[index];')

        return {'constant': function}

    def create_runtime_functions(self, port):
        return {}


known_port_types = {
    'ReadValue': ReadValuePortType,
    'ReadIndexedValue': ReadIndexedValuePortType,
    'ReadQueuedValue': ReadQueuedValuePortType,
    'WriteData': WriteDataPortType,
    'WriteIndexedData': WriteIndexedDataPortType,
    'Constant': ConstantPortType,
    'ConstantArray': ConstantArrayPortType
}


def init(owner: CGlue):
    owner.types.add_category(StructType(owner.types))
    owner.types.add_category(EnumType(owner.types))
    owner.types.add_category(UnionType(owner.types))

    owner.add_signal_type('variable', VariableSignal())
    owner.add_signal_type('array', ArraySignal())
    owner.add_signal_type('constant', ConstantSignal())
    owner.add_signal_type('constant_array', ConstantArraySignal())
    owner.add_signal_type('queue', QueueSignal())

    for port_type_name, port_type_class in known_port_types.items():
        owner.add_port_type(port_type_name, port_type_class(owner.types))


def add_type_def(owner: CGlue, type_name, type_data):
    processed_type_data = process_type_def(owner.types, type_name, type_data)
    owner.types.add(type_name, processed_type_data)


def process_project_types(owner: CGlue, project_config):
    for type_name, type_data in project_config.get('types', {}).items():
        add_type_def(owner, type_name, type_data)


def process_component_ports_and_types(owner: CGlue, component: Component):
    print(f"Processing component: {component.name}")

    try:
        for type_name, type_data in component.config['types'].items():
            add_type_def(owner, type_name, type_data)
    except Exception:
        print(f"Failed to add type definitions for {component.name}")
        raise


def sort_functions(owner: CGlue, context):
    def sort_by_name(fn):
        # only sort functions of known port types
        port = owner.get_port(fn)
        if port['port_type'] in known_port_types:
            return fn
        else:
            return '0'

    def sort_by_port_type(fn):
        return owner.get_port(fn).port_type.config.get('order', 0)

    by_name = sorted(context['functions'], key=sort_by_name)
    by_port_type = sorted(by_name, key=sort_by_port_type)
    context['functions'] = {fn: context['functions'][fn] for fn in by_port_type}


def cleanup_component(owner: CGlue, _, ctx):
    sort_functions(owner, ctx)


def builtin_data_types():
    return Plugin("BuiltinDataTypes", {
        'init':                        init,
        'load_project_config':         process_project_types,
        'load_component_config':       process_component_ports_and_types,
        'before_generating_component': cleanup_component,
        'before_generating_runtime':   sort_functions
    })
