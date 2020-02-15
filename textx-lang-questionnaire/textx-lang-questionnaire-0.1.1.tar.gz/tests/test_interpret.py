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
        '1', 'my_package', 'it is me', 'my@email.com', '2'
    ]

    monkeypatch.setattr('builtins.input', lambda _: inputs.pop(0))

    data = questionnaire_interpret(questionnaire)

    assert data['package'] == 'my_package'
    assert data[0] == 'lang'
    assert data[2] == 'it is me'

    # We can pass in default values by id
    inputs = [
        '1', '', '', 'my@email.com', '2'
    ]
    data = questionnaire_interpret(questionnaire,
                                   {'package': 'some_other_package',
                                    2: 'not me anymore'})

    assert data['package'] == 'some_other_package'
    assert data[0] == 'lang'
    assert data[2] == 'not me anymore'
