"""Test the protocol.stacks module."""

# Builtins

# Packages

from phylline.links.loopback import TopLoopbackLink
from phylline.pipelines import PipelineBottomCoupler

from phyllo.protocol.application.stacks import make_minimal, make_pubsub
from phyllo.protocol.communication import AutomaticStack
from phyllo.protocol.stacks import make_stack
from phyllo.protocol.transport.stacks import (
    make_logical_minimal, make_logical_reduced
)
from phyllo.protocol.transport.stacks import make_stack as make_transport

import pytest

from tests.unit.protocol.transport.stacks import assert_loopback_below


@pytest.mark.parametrize('logical_substack_factory', [
    make_logical_minimal,
    make_logical_reduced
])
def test_minimal_loopback_coupler(logical_substack_factory):
    """Test for correct echo from send to receive."""
    print('Testing document loopback with PipelineBottomCoupler...')
    stack_one = make_stack(
        transport_stack=make_transport(logical_substack=logical_substack_factory()),
        application_stack=make_minimal(), name=' Protocol'
    )
    stack_two = AutomaticStack(
        make_stack(
            transport_stack=make_transport(logical_substack=logical_substack_factory()),
            application_stack=make_minimal()
        ),
        TopLoopbackLink()
    )
    coupler = PipelineBottomCoupler(stack_one, stack_two)
    print(coupler)
    assert_loopback_below(coupler.pipeline_one, (1, 2, 3))
    assert_loopback_below(coupler.pipeline_one, {'hello': 'world', 'foo': 'bar'})
    assert_loopback_below(
        coupler.pipeline_one, (0, 1, 2, True, None, (3, 4), {'foo': 'bar'})
    )
    assert_loopback_below(coupler.pipeline_one, 12345)


@pytest.mark.parametrize('logical_substack_factory', [
    make_logical_minimal,
    make_logical_reduced
])
def test_pubsub_loopback_coupler(logical_substack_factory):
    """Test for correct echo from send to receive."""
    print('Testing pub-sub loopback with PipelineBottomCoupler...')
    stack_one = make_stack(
        transport_stack=make_transport(logical_substack=logical_substack_factory()),
        application_stack=make_pubsub(), name=' Protocol'
    )
    stack_two = AutomaticStack(
        make_stack(
            transport_stack=make_transport(logical_substack=logical_substack_factory()),
            application_stack=make_pubsub()
        ),
        TopLoopbackLink()
    )
    coupler = PipelineBottomCoupler(stack_one, stack_two)
    print(coupler)
    assert_loopback_below(coupler.pipeline_one, (b'list', (1, 2, 3)))
    assert_loopback_below(coupler.pipeline_one, (b'dict', {'hello': 'world', 'foo': 'bar'}))
    assert_loopback_below(
        coupler.pipeline_one, (b'nested', (0, 1, 2, True, None, (3, 4), {'foo': 'bar'}))
    )
    assert_loopback_below(coupler.pipeline_one, (b'number', 12345))
