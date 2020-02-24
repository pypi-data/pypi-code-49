import pytest
from colltools import NameRegistry


@pytest.fixture(autouse=True)
def clean_registry():
    NameRegistry.__items__ = {}


def test_name_registry_has_no_instances():
    assert NameRegistry.__members__ == {}


def test_validates_name():
    with pytest.raises(KeyError):
        NameRegistry('doesnt_exist')


def test_raises_error_when_name_doesnt_exist():
    class Registry(NameRegistry):
        __values__ = ['xxx']

    with pytest.raises(KeyError):
        Registry('doesnt_exist')


def test_gets_instance():
    class Registry(NameRegistry):
        __values__ = ['xxx']

    assert isinstance(Registry.get('xxx'), Registry)


def test_gets_instance_from_superclass():
    class Registry(NameRegistry):
        __values__ = ['xxx']

    assert isinstance(NameRegistry.get('xxx'), Registry)


def test_singleton_instances():
    class Registry(NameRegistry):
        __values__ = ['xxx']

    val1 = Registry.get('xxx')
    val2 = Registry.get('xxx')
    assert val1 is val2


def test_cascade():
    class Registry1(NameRegistry):
        __values__ = ['xxx']

    class Registry2(Registry1):
        __values__ = ['yyy']

    class Registry3(Registry2):
        __values__ = ['zzz']

    assert set(NameRegistry.__members__.keys()) == set(['xxx', 'yyy', 'zzz'])
    assert set(Registry1.__members__.keys()) == set(['xxx', 'yyy', 'zzz'])
    assert set(Registry2.__members__.keys()) == set(['yyy', 'zzz'])
    assert set(Registry3.__members__.keys()) == set(['zzz'])


def test_name_attribute():
    class Registry(NameRegistry):
        __values__ = ['xxx']

    assert Registry.get('xxx').name == 'xxx'


def test_to_string():
    class Registry(NameRegistry):
        __values__ = ['xxx']

    assert str(Registry.get('xxx')) == 'xxx'


def test_repre():
    class Registry(NameRegistry):
        __values__ = ['xxx']

    assert repr(Registry.get('xxx')) == '<Registry:xxx>'
