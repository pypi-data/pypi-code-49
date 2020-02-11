import os

from jmespath import search

from . import plugins
from .helpers import load_file
from .helpers import validate_config
from .prompt import Prompt


class Flow(object):
    def __init__(self, path):
        self.check_path(path)
        self.config = self.load_config(path)
        self.load_prompts()
        self.flows = self.config.get('flows', {})
        self.vars = {}

    @staticmethod
    def check_path(path):
        if not os.path.isfile(path):
            path = os.path.join(
                os.path.abspath(os.path.dirname(__file__)), path)
            if not os.path.isfile(path):
                raise Exception('Invalid config path provided.')

    @staticmethod
    def load_config(path):
        conf = load_file(path)
        validate_config(conf)
        return conf

    def load_prompts(self):
        self.prompts = {}
        for name, config in self.config.get('prompts', {}).items():
            self.prompts[name] = Prompt(name, config)

    def get_var_value(self, name):
        name = name.replace('$', '')
        return search(name, self.vars)

    def save_answer(self, prompt, flow_name):
        if flow_name not in self.vars:
            self.vars[flow_name] = {}

        var_type = prompt.config.get('varType', 'str')
        var_name = prompt.config.get('var')
        answer = prompt.answer
        out = None

        if var_type == 'str':
            out = str(answer)
        elif var_type == 'list':
            out = list(answer)
        elif var_type == 'str_to_list':
            out = [a.strip() for a in answer.split(',')]

        if self.vars[flow_name].get(var_name):
            if not isinstance(self.vars[flow_name][var_name], list):
                self.vars[flow_name][var_name] = [
                    self.vars[flow_name][var_name]]

            self.vars[flow_name][var_name].append(out)
        else:
            self.vars[flow_name][var_name] = out

    def execute_prompt(self, prompt_name, flow_name):
        prompt = self.prompts.get(prompt_name)
        if not prompt:
            raise Exception(f'Invalid prompt called: {prompt_name}.')

        prompt.ask()
        self.save_answer(prompt, flow_name)

    def execute_function(self, func_name, flow):
        try:
            func = getattr(plugins, func_name)
            inputs = self.get_var_value(flow.get('inputs', '*'))
            if flow.get('return'):
                out = func(inputs)
            else:
                func(inputs)
        except Exception as e:
            raise(e)

    def execute_flow(self, flow_name):
        flow = self.flows.get(flow_name)
        if not flow:
            raise Exception(f'Invalid flow called: {flow_name}.')

        for f in flow:
            item = f.get('item')
            if item.startswith('$'):
                item = self.get_var_value(item)

            if not isinstance(item, list):
                item = [item]

            for val in item:
                if f.get('type', '') == 'prompt':
                    self.execute_prompt(val, flow_name)
                elif f.get('type', '') == 'flow':
                    self.execute_flow(val)
                elif f.get('type', '') == 'function':
                    self.execute_function(val, f)

    def execute(self):
        name = self.config['first'] if 'first' in self.config else 'main'
        self.execute_flow(name)
