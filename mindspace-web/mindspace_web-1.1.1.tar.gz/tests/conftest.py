from pytest import fixture

from mindspace_web import MindspaceFactory


@fixture(name='f')
def get_factory():
    return MindspaceFactory()
