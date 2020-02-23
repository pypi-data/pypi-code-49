#!/usr/bin/env python3

# Libraries
import colored
import json
import os
import oyaml as yaml
from pathlib import Path
import PyInquirer
import sys

# Components
from .main import NAME
from .patcher import InquirerControl
from .runner import launcher
from .utils import dictGet

# Selector theme
SelectorTheme = PyInquirer.style_from_dict({
    PyInquirer.Token.Separator: '#FFFF00 bold',
    PyInquirer.Token.QuestionMark: '#FFFF00 bold',
    PyInquirer.Token.Selected: '#00FF00 bold',
    PyInquirer.Token.Instruction: '#00FFFF bold',
    PyInquirer.Token.Pointer: '#FFFF00 bold',
    PyInquirer.Token.Answer: '#00FFFF bold',
    PyInquirer.Token.Question: '#00FF00 bold',
})

# Configurations theme
ConfigurationsTheme = PyInquirer.style_from_dict({
    PyInquirer.Token.Selected: '#00FF00 bold',
    PyInquirer.Token.Instruction: '#00FFFF bold',
    PyInquirer.Token.Pointer: '#FFFF00 bold',
    PyInquirer.Token.Answer: '#00FFFF bold',
    PyInquirer.Token.Question: '#FFFF00 bold',
})

# Selector
def selector(options, jobs):

    # Variables
    default_check = options.all
    jobs_available = False
    jobs_choices = []
    jobs_index = 0
    result = True
    stage = ''

    # Stages groups
    for job in jobs:

        # Filter names
        if options.names:

            # Filter jobs list
            if not options.pipeline and job not in options.names:
                continue

            # Filter stages list
            if options.pipeline and jobs[job]['stage'] not in options.names:
                continue

        # Stages separator
        if stage != jobs[job]['stage']:
            stage = jobs[job]['stage']
            jobs_choices += PyInquirer.Separator('\n Stage %s:' % (stage)),

        # Disabled jobs
        disabled = False
        when = ''
        if jobs[job]['when'] in ['manual'] and not options.manual:
            disabled = 'Manual'
        else:
            if jobs[job]['when'] == 'manual':
                when = ' (Manual)'
            elif jobs[job]['when'] == 'on_failure':
                when = ' (On failure)'
            jobs_available = True

        # Register job tags
        tags = ''
        if jobs[job]['tags']:
            tags = ' [%s]' % (','.join(jobs[job]['tags']))

        # Job choices
        jobs_index += 1
        jobs_choices += [{
            # 'key': str(jobs_index),
            'name': '%s%s%s' % (jobs[job]['name'], tags, when),
            'value': job,
            'checked': default_check,
            'disabled': disabled
        }]

    # Prepare jobs selection
    selection_type = 'list' if options.list else 'checkbox'
    selection_prompt = [{
        'type': selection_type,
        'qmark': '',
        'message': '===[ Jobs selector ]===',
        'name': 'jobs',
        'choices': jobs_choices
    }]

    # Request jobs selection
    if jobs_choices and jobs_available:
        answers = PyInquirer.prompt(selection_prompt, style=SelectorTheme)
    else:
        print(
            ' %s%s: %sERROR: %sNo jobs found for selection%s' %
            (colored.fg('green') + colored.attr('bold'), NAME,
             colored.fg('red') + colored.attr('bold'),
             colored.attr('reset') + colored.attr('bold'), colored.attr('reset')),
            flush=True)
        answers = None

    # Parse jobs selection
    if answers and 'jobs' in answers:
        options.names = answers['jobs']
    else:
        options.names = []

    # Drop pipeline mode for jobs
    options.pipeline = False

    # Footer
    print(' ')
    print(' ', flush=True)

    # Launch jobs
    if options.names:
        result = launcher(options, jobs)

    # Result
    return result

# Configurator
def configurator(options, configurations):

    # Variables
    result = dict()

    # Header
    print(' ')
    print(' %s===[ %sConfigurations menu %s]===%s' %
          (colored.fg('green') + colored.attr('bold'),
           colored.fg('yellow') + colored.attr('bold'),
           colored.fg('green') + colored.attr('bold'), colored.attr('reset')))
    print(' ', flush=True)

    # Walk through configurations
    for variable in configurations:

        # Variables
        variable_choices = []
        variable_default = ''
        variable_index = 0
        variable_set = False
        variable_values = []

        # Extract configuration fields
        variable_node = configurations[variable]
        variable_help = variable_node['help']
        variable_type = variable_node['type']

        # Prepare configuration selection
        configuration_prompt = [{
            'name': variable,
            'qmark': '',
            'message': 'Variable %s: %s:' % (variable, variable_help),
        }]

        # Extract environment variable
        if variable in os.environ:
            variable_default = os.environ[variable]
            variable_set = True

        # Parse configuration types: boolean
        if variable_type == 'boolean':
            if 'default' in variable_node and variable_node['default'] in [
                    False, 'false'
            ]:
                variable_values = ['false', 'true']
            else:
                variable_values = ['true', 'false']
            if not variable_set:
                variable_default = variable_values[0]
            for choice in variable_values:
                variable_index += 1
                variable_choices += [{
                    # 'key': str(variable_index),
                    'name': '%s' % (choice),
                    'value': choice
                }]
            configuration_prompt[0]['type'] = 'list'
            configuration_prompt[0]['choices'] = variable_choices

        # Parse configuration types: choice
        elif variable_type == 'choice':
            variable_values = variable_node['values']
            if not variable_set:
                variable_default = variable_values[0]
            for choice in variable_values:
                variable_index += 1
                variable_choices += [{
                    'key': str(variable_index),
                    'name': '%s' % (choice),
                    'value': choice
                }]
            configuration_prompt[0]['type'] = 'list'
            configuration_prompt[0]['choices'] = variable_choices

        # Parse configuration types: input
        elif variable_type == 'input':
            configuration_prompt[0]['type'] = 'input'
            if 'default' in variable_node and variable_node[
                    'default'] and not variable_set:
                variable_default = variable_node['default']
                configuration_prompt[0]['default'] = variable_default

        # Parse configuration types: json
        elif variable_type == 'json':
            if not variable_set:
                configuration_path = str(Path(options.path) / variable_node['path'])
                configuration_key = variable_node['key']
                with open(configuration_path, 'r') as configuration_data:
                    variable_values = dictGet(json.load(configuration_data),
                                              configuration_key)
                    if not variable_values:
                        raise ValueError(
                            'Unknown "%s" key in %s for "%s"' %
                            (configuration_key, configuration_path, variable))
                    for choice in variable_values:
                        variable_index += 1
                        variable_choices += [{
                            'key': str(variable_index),
                            'name': '%s' % (choice),
                            'value': choice
                        }]
                    configuration_prompt[0]['type'] = 'list'
                    configuration_prompt[0]['choices'] = variable_values

        # Parse configuration types: yaml
        elif variable_type == 'yaml':
            if not variable_set:
                configuration_path = str(Path(options.path) / variable_node['path'])
                configuration_key = variable_node['key']
                with open(configuration_path, 'r') as configuration_data:
                    variable_values = dictGet(yaml.safe_load(configuration_data),
                                              configuration_key)
                    if not variable_values:
                        raise ValueError(
                            'Unknown "%s" key in %s for "%s"' %
                            (configuration_key, configuration_path, variable))
                    for choice in variable_values:
                        variable_index += 1
                        variable_choices += [{
                            'key': str(variable_index),
                            'name': '%s' % (choice),
                            'value': choice
                        }]
                    configuration_prompt[0]['type'] = 'list'
                    configuration_prompt[0]['choices'] = variable_values

        # Parse configuration types: unknown
        else:
            print(' ')
            print(' %s%s: %sERROR: %sUnsupported configuration type "%s"...%s' %
                  (colored.fg('green') + colored.attr('bold'), NAME, colored.fg('red') +
                   colored.attr('bold'), colored.attr('reset') + colored.attr('bold'),
                   variable_type, colored.attr('reset')))
            print(' ', flush=True)

        # Extract environment variable
        if variable in os.environ:
            variable_default = os.environ[variable]
            variable_set = True

        # Request configuration selection
        if not sys.stdin.isatty() or variable_set or options.defaults:
            result[variable] = str(variable_default)
            print(' %s%s  %s%s%s' %
                  (colored.fg('yellow') + colored.attr('bold'),
                   configuration_prompt[0]['message'], colored.fg('cyan') +
                   colored.attr('bold'), result[variable], colored.attr('reset')))
        else:
            answers = PyInquirer.prompt(configuration_prompt, style=ConfigurationsTheme)
            if not answers:
                raise KeyboardInterrupt
            result[variable] = str(answers[variable])

    # Footer
    print(' ', flush=True)

    # Result
    return result
