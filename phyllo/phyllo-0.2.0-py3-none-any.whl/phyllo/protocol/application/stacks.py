"""Application protocol stacks for easy abstractions of communication links."""

# Builtins

# Packages

from phyllo.protocol.application.pubsub import DocumentLink as PubSubDocumentLink
from phyllo.protocol.application.pubsub import MessageLink
from phyllo.protocol.communication import AutomaticStack, PRESET_STACK_TYPES
from phyllo.protocol.presentation.documents import DocumentLink


# Application stacks


def make_minimal(stack=AutomaticStack, name='Minimal'):
    """Make the Minimal preset of the application stack."""
    return stack(DocumentLink(), name=name)


def make_pubsub(stack=AutomaticStack, name='PubSub'):
    """Make the PubSub preset of the application stack."""
    return stack(MessageLink(), PubSubDocumentLink(), name=name)


# Preset stacks

PRESET_STACK_FACTORIES = {
    'none': None,
    'minimal': make_minimal,
    'pubsub': make_pubsub,
}


def make_preset_stack(application='pubsub', stack='automatic'):
    """Make an application stack specified by preset names."""
    factory = PRESET_STACK_FACTORIES[application]
    if factory is None:
        return None

    return factory(stack=PRESET_STACK_TYPES[stack])
