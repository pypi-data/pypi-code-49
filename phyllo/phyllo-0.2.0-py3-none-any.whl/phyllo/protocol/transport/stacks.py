"""Transport protocol stacks for easy abstractions of communication links."""

# Builtins

# Packages

from phyllo.protocol.communication import AutomaticStack, PRESET_STACK_TYPES
from phyllo.protocol.transport.datagrams import DatagramLink, ValidatedDatagramLink
from phyllo.protocol.transport.frames import ChunkedStreamLink, FrameLink
from phyllo.protocol.transport.reliablebuffers import ReliableBufferLink


# Medium sub-stacks


def make_medium_stream(stack=AutomaticStack, name='Medium(Stream)'):
    """Make the Stream preset of the medium sub-stack."""
    return stack(ChunkedStreamLink(), FrameLink(), name=name)


# Logical sub-stacks


def make_logical_minimal(stack=AutomaticStack, name='Logical(Minimal)'):
    """Make the Minimal preset of the logical sub-stack."""
    return stack(DatagramLink(), name=name)


def make_logical_reduced(stack=AutomaticStack, name='Logical(Reduced)'):
    """Make the Reduced preset of the logical sub-stack."""
    return stack(make_logical_minimal(stack=stack), ValidatedDatagramLink(), name=name)


def make_logical_standard(stack=AutomaticStack, name='Logical(Standard)'):
    """Make the Reduced preset of the logical sub-stack."""
    return stack(make_logical_reduced(stack=stack), ReliableBufferLink(), name=name)


# Preset sub-stacks

PRESET_MEDIUM_SUBSTACK_FACTORIES = {
    'none': None,
    'stream': make_medium_stream
}

PRESET_LOGICAL_SUBSTACK_FACTORIES = {
    'none': None,
    'minimal': make_logical_minimal,
    'reduced': make_logical_reduced,
    'standard': make_logical_standard,
}


def make_preset_medium_substack(medium='stream', stack='automatic'):
    """Make a medium sub-stack specified by preset names."""
    factory = PRESET_MEDIUM_SUBSTACK_FACTORIES[medium]
    if factory is None:
        return None

    return factory(stack=PRESET_STACK_TYPES[stack])


def make_preset_logical_substack(logical='minimal', stack='automatic'):
    """Make a medium sub-stack specified by preset names."""
    factory = PRESET_LOGICAL_SUBSTACK_FACTORIES[logical]
    if factory is None:
        return None

    return factory(stack=PRESET_STACK_TYPES[stack])


# Transport stacks
def make_stack(
    medium_substack=make_medium_stream, logical_substack=make_logical_minimal,
    stack=AutomaticStack, name='Transport'
):
    """Make a transport stack."""
    substacks = []
    if medium_substack is not None:
        if callable(medium_substack):
            medium_substack = medium_substack()
        substacks.append(medium_substack)
    if logical_substack is not None:
        if callable(logical_substack):
            logical_substack = logical_substack()
        substacks.append(logical_substack)
    if not substacks:
        return None

    return stack(*substacks, name=name)


def make_preset_stack(medium='stream', logical='minimal', stack='automatic'):
    """Make a transport stack specified by preset names."""
    return make_stack(
        medium_substack=make_preset_medium_substack(medium=medium, stack=stack),
        logical_substack=make_preset_logical_substack(logical=logical, stack=stack),
        stack=PRESET_STACK_TYPES[stack]
    )
