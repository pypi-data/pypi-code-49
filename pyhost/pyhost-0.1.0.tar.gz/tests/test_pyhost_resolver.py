from pyhost.resolver import Resolver

def test_pyhost_resolver_default_executable():
    resolver = Resolver()
    assert resolver.executable == 'dig'

def test_pyhost_resolver_custom_executable():
    resolver = Resolver(executable='ipsum')
    assert resolver.executable == 'ipsum'

def test_pyhost_resolver_default_nameservers():
    resolver = Resolver()
    assert resolver.nameservers == []

def test_pyhost_resolver_custom_nameservers():
    resolver = Resolver(nameservers=['localhost'])
    assert resolver.nameservers == ['localhost']

def test_pyhost_resolver_default_additional_args():
    resolver = Resolver()
    assert resolver.additional_args == ['+short']

def test_pyhost_resolver_custom_additional_args():
    resolver = Resolver(additional_args=['+noall', '+nocmd', '+answer'])
    assert resolver.additional_args == ['+noall', '+nocmd', '+answer']

def test_pyhost_resolver_default_encoding():
    resolver = Resolver()
    assert resolver.encoding == 'utf-8'

def test_pyhost_resolver_custom_encoding():
    resolver = Resolver(encoding='iso-8859-1')
    assert resolver.encoding == 'iso-8859-1'
