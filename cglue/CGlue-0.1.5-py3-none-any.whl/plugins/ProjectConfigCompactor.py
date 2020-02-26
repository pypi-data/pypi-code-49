from cglue.cglue import Plugin, CGlue


def process_runnable_ref_shorthand(runnable):
    """Parse shorthand form of runnable reference into a dictionary"""
    if type(runnable) is str:
        parts = runnable.split('/')
        runnable = {
            'short_name': runnable,
            'component':  parts[0],
            'runnable':   parts[1]
        }
    else:
        runnable['short_name'] = "{}/{}".format(runnable['component'], runnable['runnable'])

    return runnable


def process_port_ref_shorthand(port):
    """Parse shorthand form of port reference into a dictionary"""
    if type(port) is str:
        parts = port.split('/')
        port = {
            'short_name': port,
            'component':  parts[0],
            'port':       parts[1]
        }
    else:
        port['short_name'] = "{}/{}".format(port['component'], port['port'])

    return port


def expand_port_connection(port_connection):
    connection = {}

    attrs = {k: v for k, v in port_connection.items() if k not in ['provider', 'consumer', 'consumers']}

    if 'consumer' in port_connection:
        consumer = port_connection['consumer']
        if type(consumer) is list:
            consumer, attributes = consumer
        else:
            attributes = {}

        connection['consumers'] = [{
            **process_port_ref_shorthand(consumer),
            "attributes": attributes
        }]
    else:
        connection['consumers'] = []

        for consumer in port_connection['consumers']:
            if type(consumer) is not list:
                consumer = [consumer, {}]

            connection['consumers'].append({
                **process_port_ref_shorthand(consumer[0]),
                "attributes": consumer[1]
            })
    connection.update(attrs)

    connection['provider'] = process_port_ref_shorthand(port_connection['provider'])
    return connection


def expand_project_config(owner, project_config):
    """Expand shorthand forms in project configuration"""
    processed_runnables = {}
    raw_runnables = project_config['runtime'].get('runnables', {})
    raw_port_connections = project_config['runtime'].get('port_connections', [])

    for runnable_group, runnables in raw_runnables.items():
        processed_runnables[runnable_group] = []

        for runnable in runnables:
            if type(runnable) is not list:
                runnable = [runnable, {}]

            processed_runnables[runnable_group].append({
                **process_runnable_ref_shorthand(runnable[0]),
                'attributes': runnable[1]
            })

    processed_port_connections = []
    for port_connection in raw_port_connections:
        processed_port_connections.append(expand_port_connection(port_connection))

    project_config['runtime']['runnables'] = processed_runnables
    project_config['runtime']['port_connections'] = processed_port_connections


def _remove_empty_attribute_list(ref):
    if not ref['attributes']:
        del ref['attributes']


def _remove_empty_argument_list(ref):
    if 'arguments' in ref['attributes']:
        if not ref['attributes']['arguments']:
            del ref['attributes']['arguments']


def _ref_only_contains_default_keys(ref):
    return not set(ref.keys()).difference(['short_name', 'component', 'port', 'runnable', 'attributes'])


def _compact_ref(ref):
    if type(ref) is str:
        return ref

    if 'attributes' in ref:
        _remove_empty_argument_list(ref)
        _remove_empty_attribute_list(ref)

    if not _ref_only_contains_default_keys(ref):
        return {key: ref[key] for key in ref if key != 'short_name'}

    if 'attributes' in ref:
        return [ref['short_name'], ref['attributes']]
    else:
        return ref['short_name']


def compact_project_config(owner: CGlue, config):
    """Simplify parts that don't need to remain in their expanded forms"""
    types = {}

    for t in owner.types.export():
        project_type = t in config['types']
        for component_data in owner._components.values():
            if t in component_data.get('types', {}):
                project_type = False
                break

        if project_type:
            types[t] = config['types'][t]

    expanded_runtime = config['runtime'].copy()

    compacted_runtime = {
        'runnables':        {},
        'port_connections': []
    }

    for group, runnables in expanded_runtime['runnables'].items():
        compacted_runtime['runnables'][group] = list(map(_compact_ref, runnables))

    for connection in expanded_runtime['port_connections']:
        compacted_connection = {
            'provider': _compact_ref(connection['provider'])
        }

        consumers = list(map(_compact_ref, connection['consumers']))
        if len(consumers) == 1:
            compacted_connection['consumer'] = consumers[0]
        else:
            compacted_connection['consumers'] = consumers

        compacted_connection.update(
            {key: value for key, value in connection.items() if key not in ['provider', 'consumers']})

        compacted_runtime['port_connections'].append(compacted_connection)

    config['runtime'] = compacted_runtime
    config['types'] = types


def project_config_compactor():
    """Plugin that expands project configuration on load and compacts it on save"""
    handlers = {
        'load_project_config': expand_project_config,
        'save_project_config': compact_project_config
    }
    return Plugin("ProjectConfigCompactor", handlers)
