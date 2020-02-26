import chevron

from cglue.function import FunctionPrototype, FunctionImplementation
from cglue.ports import PortType
from cglue.cglue import Plugin, CGlue
from cglue.signal import SignalType, SignalConnection


# FIXME clean up implementation
# FIXME see what can be done about duplicated pass-by-pointer logic
# TODO: multiple callers to the same server
class AsyncServerCallSignal(SignalType):
    def __init__(self):
        super().__init__('single', {'update_on'})

    def create(self, context, connection: SignalConnection):
        port = context['runtime'].get_port(connection.provider)

        update_function = FunctionImplementation(FunctionPrototype(connection.name + '_Update', 'void'))

        context['functions'][connection.provider]['update'] = update_function

        stored_arguments = []
        callee_arguments = {}

        for name, arg_data in port.get('arguments', {}).items():
            if type(arg_data) is str:
                arg_dir = 'in'
                arg_type = context['runtime'].types.get(arg_data)
            else:
                arg_dir = arg_data['direction']
                arg_type = context['runtime'].types.get(arg_data['data_type'])

            stored_arguments.append({'name': name, 'type': arg_type.name})

            indent = ' ' * 12
            if arg_dir == 'out' or arg_type.passed_by() == 'pointer':
                callee_arguments[name] = f'\n{indent}&{connection.name}_argument_{name}'
            else:
                callee_arguments[name] = f'\n{indent}{connection.name}_argument_{name}'

        context['declarations'].append(chevron.render(**{
            'template':
                '\n/* {{ signal_name }} */\n'
                'static AsyncOperationState_t {{ signal_name }}_state = AsyncState_Idle;\n'
                'static AsyncCommand_t {{ signal_name }}_command = AsyncCommand_None;\n'
                '{{# arguments }}'
                'static {{ type }} {{ signal_name }}_argument_{{ name }};\n'
                '{{/ arguments }}'
                'static {{ updater_header }};',
            'data': {
                'signal_name': connection.name,
                'arguments': stored_arguments,
                'updater_header': update_function.get_header()
            }
        }))
        context['used_types'].append('AsyncOperationState_t')
        context['used_types'].append('AsyncCommand_t')

        # generate the updater function
        if 'run' in port.functions:
            self._generate_sync_updater_impl(callee_arguments, connection, port, update_function)

        elif 'async_run' in port.functions:
            self._generate_async_updater_impl(callee_arguments, connection, port, update_function)
        else:
            raise NotImplementedError

    def _generate_async_updater_impl(self, callee_arguments, connection, port, update_function):
        lock, unlock = self._get_lock_impl(connection)

        # long running handler function
        update_function.add_body(chevron.render(**{
            'template': '''{{ lock }}
AsyncCommand_t command = {{ signal_name }}_command;
{{ signal_name }}_command = AsyncCommand_None;

switch (command)
{
    case AsyncCommand_Start:
        {{ signal_name }}_state = AsyncOperationState_Busy;
        {{ unlock }}

        AsyncResult_t result = {{ run_call }};
        switch (result)
        {
            case AsyncResult_Ok:
                {{ signal_name }}_state = AsyncOperationState_Done;
                break;

            case AsyncResult_Pending:
                break;

            default:
                ASSERT(0);
                break;
        }
        break;

    case AsyncCommand_None:
        if ({{ signal_name }}_state == AsyncOperationState_Busy)
        {
            {{ unlock }}

            AsyncResult_t result = {{ run_call }};
            switch (result)
            {
                case AsyncResult_Ok:
                    {{ signal_name }}_state = AsyncOperationState_Done;
                    break;

                case AsyncResult_Pending:
                    break;

                default:
                    ASSERT(0);
                    break;
            }
        }
        else
        {
            {{ unlock }}
        }
        break;

    case AsyncCommand_Cancel:
        if ({{ signal_name }}_state == AsyncOperationState_Busy)
        {
            {{ unlock }}
            (void) {{ cancel_call }};
        }
        else
        {
            {{ unlock }}
        }
        {{ signal_name }}_state = AsyncState_Idle;
        break;

    default:
        {{ unlock }}
        ASSERT(0);
        break;
}
''',
            'data': {
                'lock': lock,
                'unlock': unlock,
                'run_call': port.functions['async_run'].generate_call(
                    {'asyncCommand': 'command', **callee_arguments}),
                'cancel_call': port.functions['async_run'].generate_call(
                    {'asyncCommand': 'AsyncCommand_Cancel', **callee_arguments}),
                'signal_name': connection.name
            }
        }))

    def _generate_sync_updater_impl(self, callee_arguments, connection, port, update_function):
        lock, unlock = self._get_lock_impl(connection)

        # simple handler function to wrap synchronous runnables
        update_function.add_body(chevron.render(**{
            'template': '''{{ lock }}
AsyncCommand_t command = {{ signal_name }}_command;
{{ signal_name }}_command = AsyncCommand_None;

switch (command)
{
    case AsyncCommand_Start:
        {{ signal_name }}_state = AsyncState_Busy;
        {{ unlock }}

        {{{ call }}};

        {{ signal_name }}_state = AsyncState_Done;
        break;

    case AsyncCommand_Cancel:
        {{ unlock }}
        {{ signal_name }}_state = AsyncState_Idle;
        break;

    default:
        {{ unlock }}
        break;
}''',
            'data': {
                'lock': lock,
                'unlock': unlock,
                'call': port.functions['run'].generate_call(callee_arguments),
                'signal_name': connection.name
            }
        }))

    def generate_provider(self, context, connection: SignalConnection, provider_name):
        pass

    def generate_consumer(self, context, connection: SignalConnection, consumer_name, attributes):
        runtime = context['runtime']
        provider_port = runtime.get_port(connection.provider)
        port_functions = context['functions'][consumer_name]

        call_function = port_functions['async_call']
        cancel_function = port_functions['cancel']
        result_function = port_functions['get_result']
        update_function = context['functions'][connection.provider]['update']

        lock, unlock = self._get_lock_impl(connection)

        # generate the caller functions
        for arg in attributes.get('arguments', {}):
            if arg not in provider_port['arguments']:
                print(f'Warning: extra argument "{arg}" on signal {connection.provider}, consumed by {consumer_name}')

        call_arguments, missing_arguments = self._get_consumer_call_args(attributes, call_function.prototype,
                                                                         provider_port, runtime)

        if missing_arguments:
            raise Exception(f'{consumer_name} does not provide {connection.provider} with'
                            f' the following in-arguments: {", ".join(missing_arguments)}')

        call_function.add_body(chevron.render(**{
            'template': '''AsyncOperationState_t returned_state = AsyncState_Busy;
{{ signal_name }}_command = AsyncCommand_None;
{{ lock }}
if ({{ signal_name}}_state == AsyncState_Idle || {{ signal_name}}_state == AsyncState_Done)
{
    {{ signal_name}}_state = AsyncState_Started;
    {{ unlock }}

{{# arguments }}
    {{ signal_name }}_argument_{{ name }} = {{# by_pointer }}*{{/ by_pointer }}{{ value }};
{{/ arguments }}

    returned_state = AsyncState_Started;
    {{ signal_name }}_command = AsyncCommand_Start;
}
else
{
    {{ unlock }}
}''',
            'data': {
                'signal_name': connection.name,
                'lock': lock,
                'unlock': unlock,
                'arguments': call_arguments
            }
        }))

        for arg in call_function.prototype.arguments:
            call_function.mark_argument_used(arg)
        call_function.set_return_statement('returned_state')

        # canceller
        cancel_function.add_body(f'{connection.name}_command = AsyncCommand_Cancel;')

        # update event
        # FIXME: add a proper event maybe?
        update_call = update_function.prototype.generate_call({})
        update_event_function = context['functions'][connection.attributes['update_on']]['run']
        update_event_function.add_body(f'{update_call};')

        # get result
        # if the provider doesn't have an out arg, the default value for the type is passed back
        result_arguments = []
        for arg in result_function.arguments:
            if arg not in call_function.arguments:
                value = f'{connection.name}_argument_{arg}'
            else:
                value = result_function.arguments[arg]['data_type'].render_value(None)

            result_arguments.append({'name': arg, 'value': value})

        result_function.add_body(chevron.render(**{
            'template': '''AsyncOperationState_t returned_state;
{{ lock }}
switch ({{ signal_name }}_state)
{
    case AsyncState_Done:
{{# arguments }}
        if ({{ name }})
        {
            *{{ name }} = {{{ value }}};
        }
{{/ arguments }}
        {{ signal_name }}_state = AsyncState_Idle;
        {{ unlock }}
        returned_state = AsyncState_Done;
        break;

    case AsyncState_Started:
        {{ unlock }}
        returned_state = AsyncState_Busy;
        break;

    default:
        {{ unlock }}
        returned_state = {{ signal_name }}_state;
        break;
}''',
            'data': {
                'signal_name': connection.name,
                'lock': lock,
                'unlock': unlock,
                'arguments': result_arguments
            }
        }))
        result_function.set_return_statement('returned_state')

        for arg in result_function.prototype.arguments:
            result_function.mark_argument_used(arg)

    def _get_consumer_call_args(self, attributes, function_prototype, provider_port, runtime):
        call_arguments = []
        missing_arguments = set()
        for arg, data in provider_port['arguments'].items():
            arg_type = runtime.types.get(data['data_type'])

            if data['direction'] == 'in':
                if arg in attributes.get('arguments', {}):
                    # there is a config entry in the runtime config for this argument
                    config_value = attributes['arguments'][arg]
                    if config_value in function_prototype.arguments:
                        # argument remapping (different names, same types)
                        if arg_type != function_prototype.arguments[config_value]['data_type']:
                            raise Exception('Incompatible port types')

                        call_arguments.append({
                            'name': arg,
                            'value': config_value,
                            'by_pointer': arg_type.passed_by() == 'pointer'
                        })
                    else:
                        # constant value
                        call_arguments.append({
                            'name': arg,
                            'value': arg_type.render_value(config_value),
                            'by_pointer': False
                        })
                elif arg in function_prototype.arguments:
                    # connect arguments by name
                    call_arguments.append({
                        'name': arg,
                        'value': arg,
                        'by_pointer': arg_type.passed_by() == 'pointer'
                    })
                else:
                    missing_arguments.add(arg)

        return call_arguments, missing_arguments

    def _get_lock_impl(self, connection):
        if 'no_locks' not in connection.attributes or not connection.attributes['no_locks']:
            lock = '__disable_irq();'
            unlock = '__enable_irq();'
        else:
            lock = ''
            unlock = ''
        return lock, unlock


class AsyncCallPortType(PortType):
    def __init__(self, types):
        super().__init__(types, {
            'order':          1,
            'consumes':       {'async_call': 'multiple'},
            'def_attributes': {
                'required': [],
                'optional': {"arguments": {}},
                'static':   {}
            }
        })

    def declare_functions(self, port):
        call_fn_name = f'{port.component_name}_Async_{port.port_name}_Call'
        result_fn_name = f'{port.component_name}_Async_{port.port_name}_GetResult'
        cancel_fn_name = f'{port.component_name}_Async_{port.port_name}_Cancel'

        call_function = FunctionPrototype(call_fn_name, 'AsyncOperationState_t')
        result_function = FunctionPrototype(result_fn_name, 'AsyncOperationState_t')
        cancel_function = FunctionPrototype(cancel_fn_name, 'void')

        for name, arg_data in port.get('arguments', {}).items():
            if type(arg_data) is str:
                call_function.arguments.add(name, 'in', self._types.get(arg_data))
            elif arg_data['direction'] == 'in':
                call_function.arguments.add(name, 'in', self._types.get(arg_data['data_type']))
            else:
                result_function.arguments.add(name, 'out', self._types.get(arg_data['data_type']))

        return {
            'async_call': call_function,
            'get_result': result_function,
            'cancel': cancel_function
        }

    def create_component_functions(self, port):
        declared_functions = port.functions

        call_fn = FunctionImplementation(declared_functions['async_call'])
        call_fn.attributes.add('weak')
        call_fn.set_return_statement('AsyncState_Busy')

        result_fn = FunctionImplementation(declared_functions['get_result'])
        result_fn.attributes.add('weak')
        result_fn.set_return_statement('AsyncState_Busy')

        cancel_fn = FunctionImplementation(declared_functions['cancel'])
        cancel_fn.attributes.add('weak')

        return {'async_call': call_fn, 'get_result': result_fn, 'cancel': cancel_fn}

    def create_runtime_functions(self, port):
        declared_functions = port.functions

        call_fn = FunctionImplementation(declared_functions['async_call'])
        result_fn = FunctionImplementation(declared_functions['get_result'])
        cancel_fn = FunctionImplementation(declared_functions['cancel'])

        return {'async_call': call_fn, 'get_result': result_fn, 'cancel': cancel_fn}


class AsyncRunnablePortType(PortType):
    def __init__(self, types):
        super().__init__(types, {
            'order':          1,
            'provides':       {'async_call'},
            'def_attributes': {
                'required': [],
                'optional': {"arguments": {}},
                'static':   {}
            }
        })

    def declare_functions(self, port):
        fn_name = '{}_AsyncRunnable_{}'.format(port.component_name, port.port_name)

        function = FunctionPrototype(fn_name, 'AsyncResult_t')

        function.arguments.add('asyncCommand', 'in', self._types.get('AsyncCommand_t'))

        for name, arg_data in port.get('arguments', {}).items():
            if type(arg_data) is str:
                data_type = arg_data
                direction = 'in'
            else:
                data_type = arg_data['data_type']
                direction = arg_data['direction']

            function.arguments.add(name, direction, self._types.get(data_type))

        return {
            'async_run': function
        }

    def create_component_functions(self, port):
        function = FunctionImplementation(port.functions['async_run'])

        return {'async_run': function}

    def create_runtime_functions(self, port):
        return {}


def init(owner: CGlue):
    types = owner.types

    types.add(
        'AsyncOperationState_t',
        types.category('enum').process_type({
            'values': [
                'AsyncState_Idle',
                'AsyncState_Started',
                'AsyncState_Busy',
                'AsyncState_Done'
            ],
            'default_value': 'AsyncState_Idle'
        })
    )
    types.add(
        'AsyncCommand_t',
        types.category('enum').process_type({
            'values': [
                'AsyncCommand_None',
                'AsyncCommand_Start',
                'AsyncCommand_Continue',
                'AsyncCommand_Cancel'
            ],
            'default_value': 'AsyncCommand_None'
        })
    )
    types.add(
        'AsyncResult_t',
        types.category('enum').process_type({
            'values': [
                'AsyncResult_Pending',
                'AsyncResult_Ok'
            ],
            'default_value': 'AsyncResult_Pending'
        })
    )

    add_event_to = ['Runnable']
    for port_type, known_port_type in owner.port_types.items():
        if port_type in add_event_to:
            known_port_type['provides'].add('async_call')

    owner.add_signal_type('async_call', AsyncServerCallSignal())
    owner.add_port_type('AsyncServerCall', AsyncCallPortType(types))
    owner.add_port_type('AsyncRunnable', AsyncRunnablePortType(types))


def async_server_calls():
    return Plugin("AsyncServerCalls", {
        'init': init,
    }, requires=['BuiltinDataTypes', 'RuntimeEvents'])
