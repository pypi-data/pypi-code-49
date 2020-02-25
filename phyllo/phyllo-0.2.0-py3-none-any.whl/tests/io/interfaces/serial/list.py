"""List available serial ports."""

# Builtins

import json
import logging

# Packages

from phyllo.io.interfaces.serial import find_port, list_ports


logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())


def select_default_port():
    """Select the default port."""
    ports = list_ports()
    print(
        'Found {} port{}{}'
        .format(len(ports), '' if len(ports) == 1 else 's', ':' if ports else '!')
    )
    if not ports:
        return
    for (device, properties) in ports.items():
        print('{}: {}'.format(device, json.dumps(properties, indent=2)))
    return find_port(ports=ports)[0]


def main():
    """List the ports."""
    port = select_default_port()
    print('Default preferred port: {}'.format(port))


if __name__ == '__main__':
    main()
