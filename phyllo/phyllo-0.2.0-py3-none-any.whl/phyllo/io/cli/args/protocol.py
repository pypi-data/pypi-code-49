"""Print all data received on the serial port."""

# Builtins

# Packages

from phyllo.protocol.application.stacks import (
    PRESET_STACK_FACTORIES as PRESET_APPLICATION_STACK_FACTORIES
)
from phyllo.protocol.transport.stacks import (
    PRESET_LOGICAL_SUBSTACK_FACTORIES,
    PRESET_MEDIUM_SUBSTACK_FACTORIES
)


# Preset protocol stacks

def args_transport_medium_substack(parser):
    """Add command-line args for building the transport medium sub-stack."""
    parser.add_argument(
        '--medium', default='stream',
        choices=PRESET_MEDIUM_SUBSTACK_FACTORIES.keys(),
        help='Preset name for transport medium sub-stack.'
    )


def args_transport_logical_substack(parser):
    """Add command-line args for building the transport logical sub-stack."""
    parser.add_argument(
        '--logical', default='minimal',
        choices=PRESET_LOGICAL_SUBSTACK_FACTORIES.keys(),
        help='Preset name for transport logical sub-stack.'
    )


def args_transport_stack(parser):
    """Add command-line args for building the transport stack."""
    args_transport_medium_substack(parser)
    args_transport_logical_substack(parser)


def args_application_stack(parser):
    """Add command-line args for building the application stack."""
    parser.add_argument(
        '--application', default='pubsub',
        choices=PRESET_APPLICATION_STACK_FACTORIES.keys(),
        help='Preset name for application stack.'
    )


def group_protocol_stack(parser):
    """Start command-line args group for specifying the protocol stack."""
    return parser.add_argument_group(
        'Protocol Stack', 'Specify how to build the communication protocol stack.'
    )


def args_protocol_stack(parser):
    """Add command-line args for building the protocol stack."""
    group_protocol_stack(parser)
    args_transport_stack(parser)
    args_application_stack(parser)
