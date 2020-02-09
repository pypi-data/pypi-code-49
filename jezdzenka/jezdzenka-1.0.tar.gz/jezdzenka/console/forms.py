from datetime import datetime

import PyInquirer

from jezdzenka.classes.Type import Type
from jezdzenka.translation import _


type_prompt_question = {
            'type': 'list',
            'name': 'type',
            'message': _('new_prompt.type.message'),
            'choices': [Type.TRANSIT.value, Type.COUPON.value, Type.EVENT.value, Type.CARD.value, Type.OTHER.value],
            'filter': lambda x: Type(x)
        }


def generate_form(elements):
    questions = []
    for key, element in elements.items():
        if isinstance(element, datetime):
            questions.append({'type': 'input', 'name': key, 'default': element.strftime("%Y-%m-%d %H:%M:%S"),
                              'validate': DateTimeValidator, 'filter': lambda val: datetime.fromisoformat(val),
                              'message': _('new_prompt.' + key + '.message')})
        elif isinstance(element, list):
            strg = ""
            questions.append(
                {'type': 'input', 'name': key, 'default': strg.join(" ").join(element),
                 'filter': lambda val: list(val.split(" ")), 'message': _('new_prompt.' + key + '.message')})
        elif isinstance(element, Type):
            questions.append(type_prompt_question)
        else:
            questions.append(
                {'type': 'input', 'name': key, 'default': element, 'message': _('new_prompt.' + key + '.message')})
    return questions


def type_prompt():
    questions = [
        type_prompt_question
    ]
    return PyInquirer.prompt(questions)


def new_empty_prompt(elements):
    questions = generate_form(elements)
    return PyInquirer.prompt(questions)


class DateTimeValidator(PyInquirer.Validator):
    def validate(self, document):
        try:
            datetime.strptime(document.text, "%Y-%m-%d %H:%M:%S")
            return True
        except ValueError:
            raise PyInquirer.ValidationError(
                message=_('datetime.validator.error'),
                cursor_position=len(document.text),
            )