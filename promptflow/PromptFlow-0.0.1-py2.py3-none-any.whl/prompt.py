from collections import Mapping

from questionary import Choice
from questionary import prompt

import custom


class Prompt(object):
    def __init__(self, name, config):
        self.config = config
        self.name = name
        self.q_config = {
            k: v
            for k, v in config.items()
            if k in ('type', 'title', 'message')
        }
        self.q_config['name'] = self.name
        self.check_for_function_choices(config.get('choices'))
        if not self.choice_function:
            self.choices = self.set_choices(config.get('choices', []))

        self.reply_config = config.get('reply', {})

    def check_for_function_choices(self, choices):
        if isinstance(choices, Mapping) and choices.get('function'):
            self.choice_function = choices['function']
            self.choices = []
        else:
            self.choice_function = None

    @staticmethod
    def set_choices(choices):
        out = []
        for choice in choices:
            if isinstance(choice, Mapping):
                out.append(Choice(**choice))
            else:
                out.append(Choice(choice))

        return out

    def ask(self):
        if self.choice_function:
            func = getattr(custom, self.choice_function)
            self.choices = self.set_choices(func())

        if self.choices:
            self.q_config['choices'] = self.choices

        self.answer = prompt(self.q_config).get(self.name)

    def reply(self):
        if self.reply_config:
            print(self.reply_config.get('text', ''))
