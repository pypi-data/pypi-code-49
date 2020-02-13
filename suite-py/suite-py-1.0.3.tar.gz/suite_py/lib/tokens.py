# -*- encoding: utf-8 -*-
import marshal
import os
import subprocess

from PyInquirer import prompt

from suite_py.lib.singleton import Singleton

TOKENS = ['github', 'youtrack', 'slack', 'drone']

class Tokens(metaclass=Singleton):
    _file_name = None
    _tokens = {}
    _changed = False

    def __init__(self, file_name=os.path.join(
            os.environ['HOME'], '.suite_py/tokens')):
        self._file_name = file_name
        try:
            self.load()
        except Exception:
            pass

        self.check()
        if self._changed:
            self.save()

    def load(self):
        with open(self._file_name, 'rb') as configfile:
            self._tokens = marshal.load(configfile)

    def check(self):
        for token in TOKENS:
            if not self._tokens.get(token):
                self._tokens[token] = prompt([{
                    'type': 'input',
                    'name': token,
                    'message': 'Insert your {} token:'.format(token.capitalize())
                }])[token]
                self._changed = True

    def save(self):
        with open(self._file_name, 'wb') as configfile:
            marshal.dump(self._tokens, configfile)

    @property
    def github(self):
        return self._tokens['github']

    @property
    def youtrack(self):
        return self._tokens['youtrack']

    @property
    def slack(self):
        return self._tokens['slack']

    @property
    def drone(self):
        return self._tokens['drone']
