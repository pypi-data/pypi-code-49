"""Test the protocol.transport.stacks module."""

# Builtins

# Packages

from phylline.links.loopback import BottomLoopbackLink, TopLoopbackLink
from phylline.pipelines import PipelineBottomCoupler

from phyllo.protocol.communication import AutomaticStack
from phyllo.protocol.transport.stacks import (
    make_logical_minimal, make_logical_reduced, make_logical_standard,
    make_medium_stream, make_stack
)

import pytest


def assert_loopback_below(stack, payload):
    """Asset that the stack has correct below-loopback behavior."""
    stack.send(payload)
    assert stack.has_receive()
    result = stack.receive()
    print('Loopback received: {}'.format(result))
    assert result.data == payload


@pytest.mark.parametrize('logical_substack_factory', [
    make_logical_minimal,
    make_logical_reduced,
    make_logical_standard
])
def test_transport_loopback_below(logical_substack_factory):
    """Test for correct echo from send to receive."""
    print('Testing transport loopback with BottomLoopbackLink...')
    stack = AutomaticStack(
        BottomLoopbackLink(),
        make_stack(make_medium_stream(), logical_substack_factory()),
        name='LoopbackBelow'
    )
    print(stack)
    assert_loopback_below(stack, b'\0\0\0\0\1\2\3\4\0\0\0\0')


@pytest.mark.parametrize('logical_substack_factory', [
    make_logical_minimal,
    make_logical_reduced
])
def test_loopback_coupler(logical_substack_factory):
    """Test for correct echo from send to receive."""
    print('Testing byte buffer loopback with PipelineBottomCoupler...')
    stack_one = make_stack(
        logical_substack=logical_substack_factory(), name=' Transport'
    )
    stack_two = AutomaticStack(
        make_stack(logical_substack=logical_substack_factory()),
        TopLoopbackLink()
    )
    coupler = PipelineBottomCoupler(stack_one, stack_two)
    print(coupler)
    assert_loopback_below(coupler.pipeline_one, b'\1\2\3\4\0')
