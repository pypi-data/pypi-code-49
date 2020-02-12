def assert_eq(a, b, msg=None):
    assert a == b, '%s != %s: %s' % (a, b, msg)

def assert_neq(a, b, msg=None):
    assert a != b, '%s == %s: %s' % (a, b, msg)

def assert_gt(a, b, msg=None):
    assert a > b, '%s <= %s: %s' % (a, b, msg)

def assert_lt(a, b, msg=None):
    assert a < b, '%s >= %s: %s' % (a, b, msg)

def assert_ge(a, b, msg=None):
    assert a >= b, '%s < %s: %s' % (a, b, msg)

def assert_le(a, b, msg=None):
    assert a <= b, '%s > %s: %s' % (a, b, msg)

