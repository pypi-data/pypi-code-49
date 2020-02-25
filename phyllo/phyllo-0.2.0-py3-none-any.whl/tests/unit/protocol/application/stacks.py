"""Test the protocol.application.stacks module."""

# Builtins

# Packages

from phylline.links.loopback import BottomLoopbackLink, TopLoopbackLink
from phylline.pipelines import PipelineBottomCoupler

from phyllo.protocol.application.stacks import make_minimal, make_pubsub
from phyllo.protocol.communication import AutomaticStack

from tests.unit.protocol.transport.stacks import assert_loopback_below


def test_minimal_loopback_below():
    """Test for correct echo from send to receive with minimal stack."""
    print('Testing minimal application loopback with BottomLoopbackLink...')
    stack = AutomaticStack(BottomLoopbackLink(), make_minimal(), name='LoopbackBelow')
    print(stack)
    assert_loopback_below(stack, (1, 2, (3, {'foo': 'bar'})))


def test_pubsub_loopback_below():
    """Test for correct echo from send to receive with pub-sub stack."""
    print('Testing pub-sub application loopback with BottomLoopbackLink...')
    stack = AutomaticStack(BottomLoopbackLink(), make_pubsub(), name='LoopbackBelow')
    print(stack)
    topic = b'test'
    assert_loopback_below(stack, (topic, (1, 2, (3, {'foo': 'bar'}))))


def test_minimal_loopback_coupler():
    """Test for correct echo from send to receive."""
    print('Testing byte buffer loopback with PipelineBottomCoupler...')
    stack_one = make_minimal()
    stack_two = AutomaticStack(make_minimal(), TopLoopbackLink())
    coupler = PipelineBottomCoupler(stack_one, stack_two)
    print(coupler)
    assert_loopback_below(coupler.pipeline_one, (1, 2, 3))
    assert_loopback_below(coupler.pipeline_one, {'hello': 'world', 'foo': 'bar'})
    assert_loopback_below(
        coupler.pipeline_one, (0, 1, 2, True, None, (3, 4), {'foo': 'bar'})
    )
    assert_loopback_below(coupler.pipeline_one, 12345)


def test_pubsub_loopback_coupler():
    """Test for correct echo from send to receive."""
    print('Testing byte buffer loopback with PipelineBottomCoupler...')
    stack_one = make_pubsub()
    stack_two = AutomaticStack(make_pubsub(), TopLoopbackLink())
    coupler = PipelineBottomCoupler(stack_one, stack_two)
    print(coupler)
    assert_loopback_below(coupler.pipeline_one, (b'list', (1, 2, 3)))
    assert_loopback_below(coupler.pipeline_one, (b'dict', {'hello': 'world', 'foo': 'bar'}))
    assert_loopback_below(
        coupler.pipeline_one, (b'nested', (0, 1, 2, True, None, (3, 4), {'foo': 'bar'}))
    )
    assert_loopback_below(coupler.pipeline_one, (b'number', 12345))
