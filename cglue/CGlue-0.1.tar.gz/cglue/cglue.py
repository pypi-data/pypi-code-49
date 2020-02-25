import json
import os

import chevron

from .utils.common import to_underscore, list_to_chevron_list
from .signal import SignalType
from .data_types import TypeCollection

runtime_header_template = """#ifndef GENERATED_RUNTIME_H_
#define GENERATED_RUNTIME_H_

{{# type_includes }}
#include {{{ header }}}
{{/ type_includes }}

{{# types }}
{{{ . }}}
{{/ types }}

{{# components }}
#define COMPONENT_TYPES_{{ guard_def }}_H_
{{/ components }}

{{# components }}
#include "components/{{ name }}/{{ name }}.h"
{{/ components }}

{{# function_declarations }}
{{{ . }}};
{{/ function_declarations }}

#endif /* GENERATED_RUNTIME_H */
"""

component_header_template = '''#ifndef COMPONENT_{{ guard_def }}_H_
#define COMPONENT_{{ guard_def }}_H_

#ifndef COMPONENT_TYPES_{{ guard_def }}_H_
#define COMPONENT_TYPES_{{ guard_def }}_H_

{{# type_includes }}
#include {{{ header }}}
{{/ type_includes }}

{{# types }}
{{{ . }}}
{{/ types }}

#endif /* COMPONENT_TYPES_{{ guard_def }}_H_ */

{{# function_headers }}
{{{ . }}};
{{/ function_headers }}

#endif /* COMPONENT_{{ guard_def }}_H_ */
'''

source_template = '''{{# includes }}
#include {{{ header }}}
{{/ includes }}

{{# variables }}
{{{ . }}}
{{/ variables }}
{{# functions }}

{{{ . }}}{{/ functions }}'''


class Plugin:
    def __init__(self, name, handlers: dict, requires: list = None):
        self.name = name
        self._event_handlers = handlers
        self._owner = None
        self._requires = requires or []

    def bind(self, owner):
        for plugin in self._requires:
            if plugin not in owner._plugins:
                raise Exception(f'{self.name} requires unloaded plugin {plugin}')
        self._owner = owner

    def handle(self, event_name, args):
        try:
            handler = self._event_handlers[event_name]
        except KeyError:
            return

        print(f'Running {self.name}::{event_name}')
        handler(self._owner, *args)


class CGlue:
    def __init__(self, project_config_file):
        self._project_config_file = project_config_file
        self._basedir = os.path.dirname(project_config_file)
        self._plugins = {}
        self._defined_types = {}
        self._project_config = {}
        self._components = {}
        self._types = TypeCollection()
        self._port_types = {}
        self._signal_types = {}
        self._functions = {}

        self._ports = {}

        self._print_warnings = ['unconnected_signals']

    def add_plugin(self, plugin: Plugin):
        self._plugins[plugin.name] = plugin
        plugin.bind(self)

    def load(self):
        self.raise_event('init')

        with open(self._project_config_file, "r") as file:
            project_config = json.load(file)

        self.raise_event('load_project_config', project_config)

        if 'settings' not in project_config:
            project_config['settings'] = {
                'name': 'Project Name',
                'components_folder': 'components',
                'required_plugins': []
            }

        print(f"Loaded configuration for {project_config['settings']['name']}")

        self._project_config = project_config

        for plugin_name in self.settings['required_plugins']:
            if plugin_name not in self._plugins:
                raise Exception('Project requires {} plugin, which is not loaded'.format(plugin_name))

        for component_name in project_config['components']:
            self._load_component_config(component_name)

        self.raise_event('project_config_loaded', project_config)

    def add_port_type(self, port_type_name, port_type):
        self._port_types[port_type_name] = port_type

    def _load_component_config(self, component_name):
        component_config_file = '/'.join([self._basedir, self.settings['components_folder'], component_name, 'config.json'])
        with open(component_config_file, "r") as file:
            component_config = json.load(file)
            self.add_component(component_name, component_config)

    def add_component(self, component_name, component_config):
        self.raise_event('load_component_config', component_name, component_config)
        self._components[component_name] = component_config

        if not component_config['ports']:
            print(f'Warning: {component_name} has no ports')

        for port_name, port_data in component_config['ports'].items():
            processed_port = self._port_types[port_data['port_type']].process_port(component_name, port_name, port_data)

            self._ports[processed_port.full_name] = processed_port

    def _normalize_type_name(self, type_name):

        try:
            self._types.get(type_name)
        except KeyError:
            type_name = type_name.replace('const ', '').replace('*', '').replace(' ', '')

        return type_name

    def _get_type_includes(self, type_name) -> set:
        if type(type_name) is list:
            includes = set()
            for tn in type_name:
                inc = self._get_type_includes(tn)
                if type(inc) is set:
                    includes.update(inc)

            return includes

        else:
            type_name = self._normalize_type_name(type_name)

            try:
                return {self._types.get(type_name).get_attribute('defined_in')}
            except KeyError:
                return set()

    def _collect_type_dependencies(self, type_name):
        defs = []

        type_name = self._normalize_type_name(type_name)
        type_data = self._types.get(type_name)

        if type_data['type'] == TypeCollection.ALIAS:
            defs += self._collect_type_dependencies(type_data['aliases'])

        elif type_data['type'] == TypeCollection.EXTERNAL_DEF:
            pass

        elif type_data['type'] == TypeCollection.STRUCT:
            for field in type_data['fields'].values():
                defs += self._collect_type_dependencies(field)

        elif type_data['type'] == TypeCollection.UNION:
            for member in type_data['members'].values():
                defs += self._collect_type_dependencies(member)

        defs.append(type_name)

        return defs

    def _sort_types_by_dependency(self, type_names, visited_types=None):
        if visited_types is None:
            visited_types = []

        if type(type_names) is not list:
            type_names = [type_names]

        types = []

        for t in type_names:
            if t not in visited_types:
                visited_types.append(t)

                deps = self._collect_type_dependencies(t)

                for d in deps:
                    types += self._sort_types_by_dependency(d, visited_types)

                types.append(t)

        return types

    def update_component(self, component_name):

        component_folder = os.path.join(self._basedir, self.settings['components_folder'], component_name)
        source_file = os.path.join(component_folder, component_name + '.c')
        header_file = os.path.join(component_folder, component_name + '.h')
        config_file = os.path.join(component_folder, 'config.json')

        context = {
            'runtime': self,
            'component_folder': component_folder,
            'functions': {},
            'declarations': [],
            'files': {
                config_file: '',
                source_file: '',
                header_file: ''
            },
            'folders': [component_name]
        }

        for port_name, port_data in self._components[component_name]['ports'].items():
            short_name = f'{component_name}/{port_name}'
            context['functions'][short_name] = self._ports[short_name].create_component_functions()

        self.raise_event('before_generating_component', component_name, context)

        function_headers = []
        function_implementations = []
        used_types = []
        includes = {
            f'"{component_name}.h"',
            '"utils.h"'
        }

        for functions in context['functions'].values():
            for func in functions.values():
                function_headers.append(func.get_header())
                function_implementations.append(func.get_function())
                used_types += func.referenced_types
                includes.update(func.includes)

        defined_type_names = list(self._components[component_name].get('types', {}).keys())

        sorted_types = self._sort_types_by_dependency(defined_type_names + used_types)

        type_includes = self._get_type_includes(sorted_types)
        typedefs = [self._types.get(t).render_typedef() for t in sorted_types]

        ctx = {
            'includes': list_to_chevron_list(sorted(includes), 'header'),
            'component_name': component_name,
            'guard_def': to_underscore(component_name).upper(),
            'variables': context['declarations'],
            'types': typedefs,
            'type_includes': list_to_chevron_list(sorted(type_includes), 'header'),
            'functions': function_implementations,
            'function_headers': function_headers
        }

        context['files'][config_file] = self.dump_component_config(component_name)
        context['files'][source_file] = chevron.render(source_template, ctx)
        context['files'][header_file] = chevron.render(component_header_template, ctx)

        self.raise_event('generating_component', component_name, context)

        return context['files']

    def add_signal_type(self, name, signal_type: SignalType):
        self._signal_types[name] = signal_type

    def get_port(self, short_name):
        return self._ports[short_name]

    def generate_runtime(self, filename, context=None):
        source_file_name = filename + '.c'
        header_file_name = filename + '.h'

        default_context = {
            'runtime':                        self,
            'files':                          {source_file_name: '', header_file_name: ''},
            'functions':                      {},
            'declarations':                   [],
            'exported_function_declarations': [],
            'runtime_includes':               {'"utils.h"'},
            'signals':                        {},
            'used_types':                     []
        }

        if context is None:
            context = default_context
        else:
            context.update({**default_context, **context})

        for short_name, port in self._ports.items():
            self._functions[short_name] = port.create_runtime_functions()

        for connection in self._project_config['runtime']['port_connections']:
            provider_ref = connection['provider']
            provider_short_name = provider_ref['short_name']
            provider_port = self.get_port(provider_short_name)

            if provider_port.full_name not in context['functions']:
                context['functions'][provider_port.full_name] = provider_port.create_runtime_functions()

            provider_attributes = {key: connection[key] for key in connection if
                                   key not in ['provider', 'consumer', 'consumers']}

            # create a dict to store providers signals
            if provider_port.full_name not in context['signals']:
                context['signals'][provider_port.full_name] = {}
            provider_signals = context['signals'][provider_port.full_name]

            for consumer_ref in connection['consumers']:
                consumer_short_name = consumer_ref['short_name']
                consumer_port = self.get_port(consumer_short_name)

                # infer signal type
                consumed_signal_types = consumer_port.port_type['consumes']
                inferred_signal_type = provider_port.port_type['provides'].intersection(consumed_signal_types)

                if len(inferred_signal_type) == 0:
                    raise Exception(f'Incompatible ports: {provider_port.full_name} and {consumer_port.full_name}')
                elif len(inferred_signal_type) > 1:
                    raise Exception('Connection type can not be inferred for'
                                    f'{provider_port.full_name} and {consumer_port.full_name}')

                signal_type_name = inferred_signal_type.pop()
                signal_type = self._signal_types[signal_type_name]

                # create consumer function
                if consumer_port.full_name not in context['functions']:
                    context['functions'][consumer_port.full_name] = consumer_port.create_runtime_functions()
                else:
                    # this port already is the consumer of some signal
                    # some ports can consume multiple signals, this is set in the port data
                    # (e.g. a runnable can be called by multiple events or calls)

                    if consumed_signal_types[signal_type_name] == 'single':
                        raise Exception(f'{consumer_port.full_name} cannot consume multiple signals')

                # create signal connection
                signal_name = f'{provider_port.full_name}_{signal_type_name}'.replace('/', '_')

                consumer_attributes = consumer_ref.get('attributes', {})

                try:
                    signals_of_current_type = provider_signals[signal_type_name]
                    if type(signals_of_current_type) is list:
                        if signal_type.consumers == 'multiple_signals':
                            # create new signal in all cases
                            signal_name += str(len(signals_of_current_type))

                            new_signal = signal_type.create_connection(context, signal_name, provider_port.full_name, provider_attributes)
                            new_signal.add_consumer(consumer_short_name, consumer_attributes)

                            signals_of_current_type.append(new_signal)
                        else:
                            signals_of_current_type.add_consumer(consumer_port.full_name, consumer_attributes)
                    elif signal_type.consumers == 'multiple':
                        signals_of_current_type.add_consumer(consumer_port.full_name, consumer_attributes)
                    else:
                        raise Exception('Multiple consumers not allowed for {} signal (provided by {})'
                                        .format(signal_type_name, provider_port.full_name))
                except KeyError:
                    new_signal = signal_type.create_connection(context, signal_name, provider_port.full_name, provider_attributes)
                    new_signal.add_consumer(consumer_short_name, consumer_attributes)

                    if signal_type.consumers == 'multiple_signals':
                        provider_signals[signal_type_name] = [new_signal]
                    else:
                        provider_signals[signal_type_name] = new_signal

        for signals in context['signals'].values():
            for signal in signals.values():
                if type(signal) is list:
                    for s in signal:
                        s.generate()
                else:
                    signal.generate()

        if 'unconnected_signals' in self._print_warnings:
            all_unconnected = set(self._ports.keys()) - context['functions'].keys()
            for unconnected in sorted(all_unconnected):
                if self.get_port(unconnected).is_consumer:
                    print(f'Warning: {unconnected} port is not connected')

        self.raise_event('before_generating_runtime', context)

        type_names = context['used_types']
        for c in self._components.values():
            type_names += c.get('types', {}).keys()

        output_filename = filename[filename.rfind('/') + 1:]
        includes = context['runtime_includes']
        includes.add(f'"{output_filename}.h"')

        function_headers = []
        function_implementations = []
        for port_name, funcs in context['functions'].items():
            for f in funcs.values():
                if port_name in context['exported_function_declarations']:
                    function_headers.append(f.get_header())
                function_implementations.append(f.get_function())
                type_names += f.referenced_types
                includes.update(f.includes)

        sorted_types = self._sort_types_by_dependency(type_names)

        type_includes = self._get_type_includes(sorted_types)
        typedefs = [self._types.get(t).render_typedef() for t in sorted_types]

        template_data = {
            'output_filename': output_filename,
            'includes': list_to_chevron_list(sorted(includes), 'header'),
            'components': [
                {
                    'name': name,
                    'guard_def': to_underscore(name).upper()
                } for name in self._components if name != 'Runtime'],  # TODO
            'types': typedefs,
            'type_includes': list_to_chevron_list(sorted(type_includes), 'header'),
            'function_declarations': function_headers,
            'functions':             function_implementations,
            'variables':             context['declarations']
        }

        context['files'][source_file_name] = chevron.render(source_template, template_data)
        context['files'][header_file_name] = chevron.render(runtime_header_template, template_data)

        self.raise_event('after_generating_runtime', context)

        return context['files']

    def raise_event(self, event_name, *args):
        for plugin in self._plugins:
            try:
                self._plugins[plugin].handle(event_name, args)
            except Exception:
                print(f'Error while processing {plugin}/{event_name}')
                raise

    @property
    def functions(self):
        return self._functions

    @property
    def types(self):
        return self._types

    @property
    def port_types(self):
        return self._port_types

    @property
    def settings(self):
        return self._project_config['settings']

    def dump_component_config(self, component_name):
        config = self._components[component_name].copy()
        self.raise_event('save_component_config', config)
        return json.dumps(config, indent=4)

    def dump_project_config(self):
        config = self._project_config.copy()
        self.raise_event('save_project_config', config)
        return json.dumps(config, indent=4)
