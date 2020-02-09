import pytest
from labelsync.logic import ConflictResolver

@pytest.fixture
def resolver():
    return ConflictResolver()

def test_simple_init(resolver):
    existing_online = ["foo", "bar"]
    local_state = []
    changed_state = ["baz", "roo"]

    to_add, to_update, to_remove = resolver.resolve(existing_online, local_state, changed_state, "override")

    assert(to_add == set(["baz", "roo"]))
    assert(to_update == set())
    assert(to_remove == set())

def test_init_collision_preexisting_override(resolver):
    existing_online = ["baz", "bar"]
    local_state = []
    changed_state = ["baz", "roo"]

    to_add, to_update, to_remove = resolver.resolve(existing_online, local_state, changed_state, "override")

    assert(to_add == set(["roo"]))
    assert(to_update == set(["baz"]))
    assert(to_remove == set())

def test_init_collision_preexisting_ignore(resolver):
    existing_unmanaged = ["baz", "bar"]
    local_state = []
    changed_state = ["baz", "roo"]

    to_add, to_update, to_remove = resolver.resolve(existing_unmanaged, local_state, changed_state, "ignore")

    assert(to_add == set(["roo"]))
    assert(to_update == set())
    assert(to_remove == set())

def test_change_override(resolver):
    existing_online = ["baz", "bar"]
    local_state = ["baz"]
    changed_state = ["baz", "roo", "bar"]

    to_add, to_update, to_remove = resolver.resolve(existing_online, local_state, changed_state, "override")

    assert(to_add == set(["roo"]))
    assert(to_update == set(["baz", "bar"]))
    assert(to_remove == set())

def test_change_ignore(resolver):
    existing_online = ["baz", "bar"]
    local_state = ["baz"]
    changed_state = ["baz", "roo", "bar"]

    to_add, to_update, to_remove = resolver.resolve(existing_online, local_state, changed_state, "ignore")

    assert(to_add == set(["roo"]))
    assert(to_update == set(["baz"]))
    assert(to_remove == set())

@pytest.mark.parametrize('strat', ('override', 'ignore'))
def test_remove(resolver, strat):
    existing_online = ["baz", "bar"]
    local_state = ["baz"]
    changed_state = []

    to_add, to_update, to_remove = resolver.resolve(existing_online, local_state, changed_state, strat)

    assert(to_add == set())
    assert(to_update == set())
    assert(to_remove == set(["baz"]))

def test_no_update(resolver):
    existing_online = ["baz", "bar"]
    local_state = ["baz"]
    changed_state = []

    to_add, to_update, to_remove = resolver.resolve(existing_online, local_state, changed_state, "ignore")

    assert(to_add == set())
    assert(to_update == set())
    assert(to_remove == set(["baz"]))
