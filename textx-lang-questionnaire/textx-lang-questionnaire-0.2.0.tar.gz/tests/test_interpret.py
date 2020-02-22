from os.path import join, dirname
from textx import metamodel_for_language
from txquestionnaire import questionnaire_interpret


def test_interpret(monkeypatch):
    """
    Test Questionnaire interpreter
    """

    mm = metamodel_for_language('questionnaire')
    questionnaire = mm.model_from_file(join(dirname(__file__), 'example.que'))

    inputs = [
        '1', '*.test', 'my_package', 'it is me', 'my@email.com', '2'
    ]

    monkeypatch.setattr('builtins.input', lambda _: inputs.pop(0))

    data = questionnaire_interpret(questionnaire)

    assert data['package'] == 'my_package'
    assert data['type'] == 'lang'
    assert data[3] == 'it is me'

    # We can pass in default values by id
    inputs = [
        '1', '*.test', '', '', 'my@email.com', '2'
    ]
    data = questionnaire_interpret(questionnaire,
                                   {'package': 'some_other_package',
                                    3: 'not me anymore'})

    assert data['package'] == 'some_other_package'
    assert data['type'] == 'lang'
    assert data[3] == 'not me anymore'
    assert 'extension' in data

    # Test conditional, if project type is "gen" no extension will be asked for
    inputs = [
        '2', '', '', 'my@email.com', '2'
    ]
    data = questionnaire_interpret(questionnaire,
                                   {'package': 'some_other_package',
                                    3: 'not me anymore'})
    assert 'extension' not in data
