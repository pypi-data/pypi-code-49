"""Communication protocol stacks for easy abstractions of communication links."""

# Builtins

# Packages

from phyllo.protocol.application.stacks import make_preset_stack as make_preset_application
from phyllo.protocol.application.stacks import make_pubsub
from phyllo.protocol.communication import AutomaticStack, PRESET_STACK_TYPES
from phyllo.protocol.transport.stacks import make_preset_stack as make_preset_transport
from phyllo.protocol.transport.stacks import make_stack as make_transport


# Protocol stacks

def make_stack(
    transport_stack=make_transport, application_stack=make_pubsub,
    stack=AutomaticStack, name='Protocol'
):
    """Make a protocol stack."""
    stacks = []
    if transport_stack is not None:
        if callable(transport_stack):
            transport_stack = transport_stack()
        stacks.append(transport_stack)
    if application_stack is not None:
        if callable(application_stack):
            application_stack = application_stack()
        stacks.append(application_stack)
    if not stacks:
        raise ValueError('Cannot make an empty protocol stack!')

    return stack(*stacks, name=name)


# Preset stacks

def make_preset_stack(
    transport_medium='stream', transport_logical='minimal', application='pubsub',
    stack='automatic', name='Protocol'
):
    """Make a protocol stack specified by preset names."""
    transport = make_preset_transport(
        medium=transport_medium, logical=transport_logical, stack=stack
    )
    application = make_preset_application(application=application, stack=stack)
    return make_stack(
        transport_stack=transport, application_stack=application,
        stack=PRESET_STACK_TYPES[stack], name=name
    )
