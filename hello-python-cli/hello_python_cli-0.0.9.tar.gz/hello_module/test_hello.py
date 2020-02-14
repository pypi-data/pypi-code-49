from hello_module.hello import Hello


def test_hello_noname():
    h = Hello()
    assert h.hello() == 'Hello '


def test_hello_name():
    h = Hello('Mike')
    assert h.hello() == 'Hello Mike'


def test_hello_with_title():
    h = Hello('Mike')
    h.title = 'Mr.'
    assert h.hello() == 'Hello Mr. Mike'


def test_transform():
    h = Hello('Mike')
    h.title = 'Mr.'
    assert h.transform() == 'hello mr. mike'
