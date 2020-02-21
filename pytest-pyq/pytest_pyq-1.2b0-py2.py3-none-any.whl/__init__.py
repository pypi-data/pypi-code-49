import pytest


def q_impl():
    from pyq import q as _q
    cmds = 'Pc'
    vals = {}
    for c in cmds:
        vals[c] = _q('\\' + c)

    # Reset default values
    _q(r'\c 25 80')
    _q(r'\P 7')

    ns = _q.value('.')
    _q("delete from `.")

    yield _q

    _q.set('.', ns)
    for c in cmds:
        _q('\\%s %s' % (c, vals[c]))


@pytest.fixture
def q():
    """clean and restore q's global namespace"""
    for i in q_impl():
        yield i


@pytest.fixture(scope="module")
def q_module():
    """clean and restore q's global namespace (once per test module)"""
    for i in q_impl():
        yield i


@pytest.fixture(scope="session")
def q_session():
    """clean and restore q's global namespace (once per test session)"""
    for i in q_impl():
        yield i
