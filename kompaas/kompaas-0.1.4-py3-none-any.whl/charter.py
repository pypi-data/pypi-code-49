"""
Contains helper class Charter that deals with
the file structure of the program.
Getter and setter methods for context,
paths to certain resources.
"""

import os
import subprocess
import yaml
from mpaas.mpaas_exceptions import MissingConfigError, \
    MissingResourceError, RenderError, NoContextError


class Charter:
    """
    Helper class to deal with Charts and current Context
    """

    def __init__(self, context_path, projects_path, configs_path):
        """
        Initialises using the paths to context file and projects directory

        :param context_path: Path to the  the default context file
        :type context_path: String
        :param projects_path: Path to the default mpaas projects directory
        :type projects_path: String

        """
        self.context_path = context_path
        self.projects_path = projects_path
        self.configs_path = configs_path

    def set_context_project(self, context):
        """
        Method that sets current project context.

        :param context: Name of context to be set
        :type context:  String

        """
        if not os.path.isfile(self.context_path):
            self.init_context()

        context_dict = yaml.safe_load(open(self.context_path))
        context_dict['project'] = context

        with open(self.context_path, 'w+') as context_file:
            context_file.write(yaml.safe_dump(context_dict))

    def set_context_config(self, config):
        """
        Method thats sets the current config context.

        :param config: Name of config to be set
        :type config: String

        """
        if not os.path.isfile(self.context_path):
            self.init_context()

        context_dict = yaml.safe_load(open(self.context_path))
        context_dict['config'] = config

        with open(self.context_path, 'w+') as context_file:
            context_file.write(yaml.safe_dump(context_dict))

    def set_context_chart(self, chart):
        """
        Method that sets the current chart context

        :param chart: Name of chart to be set
        :type chart: String

        """

        if not os.path.isfile(self.context_path):
            self.init_context()

        context_dict = yaml.safe_load(open(self.context_path))
        context_dict['chart'] = chart

        with open(self.context_path, 'w+') as context_file:
            context_file.write(yaml.safe_dump(context_dict))

    def get_context_project(self):
        """
        Method that returns current project in context

        :rtype: String

        """
        try:
            with open(self.context_path, 'r') as context_file:
                context_dict = yaml.safe_load(context_file)
                return str(context_dict['project'])
        except FileNotFoundError:
            self.init_context()

    def get_context_config(self):
        """
        Method that returns current config file in context

        :rtype: String

        """
        try:
            with open(self.context_path, 'r') as context_file:
                context_dict = yaml.safe_load(context_file)
                return str(context_dict['config'])
        except IOError:
            self.init_context()

    def get_context_chart(self):
        """
        Method that returns current chart in context

        :rtype: String

        """
        try:
            with open(self.context_path, 'r') as context_file:
                context_dict = yaml.safe_load(context_file)
                return str(context_dict['chart'])
        except IOError:
            self.init_context()

    def get_context_all(self):
        """
        Method that returns a dict of all the current context objects

        :rtype: Dict

        """

        try:
            with open(self.context_path, 'r') as context_file:
                context_dict = yaml.safe_load(context_file)
                return {'config': context_dict['config'],
                        'project': context_dict['project'],
                        'chart': context_dict['chart']}
        except IOError:
            self.init_context()

    def init_context(self):
        """
        Method that initializes the context file

        :rtype: None

        """

        context_dict = {
            'project': 'None',
            'chart': 'None',
            'config': 'None'
        }

        with open(self.context_path, 'w+') as context_file:
            context_file.write(yaml.safe_dump(context_dict))

    def getcontext_path(self):
        """
        Method that returns the path to current Project

        :rtype: String

        """

        if self.get_context_project() != 'None':
            return self.projects_path + self.get_context_project()

    def get_version(self, chart_path):
        """
        Method that returns the version of target template or Chart

        :param chart_path: Path to target chart directory
        :type chart_path: String

        """

        if os.path.isfile(chart_path+'/Chart.yaml'):
            chart = yaml.safe_load(open(chart_path+'/Chart.yaml'))
            return chart['version']
        else:
            return None

    def describe_config(self, config_name):
        """
        Method that returns the contents of target config

        :param config_name: Name of target config
        :type config_name: String
        :rtype: Dictionary

        """

        if os.path.isfile(self.configs_path + config_name):
            return yaml.safe_load(open(self.configs_path + config_name))
        else:
            raise MissingConfigError(config_name)

    def replace_value(self, values_yaml_path, document):
        """
        Method that overwrites target yaml file with the contents of a python Dict.

        :param values_yaml_path: Path to values.yaml file you wish to replace.
        :type values_yaml_path: String
        :param document: Variable that contains the new values
        :type document: Dictionary
        :rtype: Boolean

        """

        try:
            with open(values_yaml_path, 'w') as yaml_values:
                # Merging the dict from current values with the new dict containing the new value
                yaml_values.write(yaml.safe_dump(document))
        except IOError:
            raise MissingResourceError('File', values_yaml_path)

        return True

    def update_value(self, values_yaml_path, value_name, new_value, value_type=None):
        """
        Generates a new yaml document with an updated value.

        :param values_yaml_path: Path to values.yaml file you wish to replace a value in.
        :type values_yaml_path: String
        :param value_name: Name of the value you wish to change,
        each level of depth separated by a '.' (Same syntax as 'mpaas list values' output)
        :type value_name: String
        :param new_value: New value to be taken by [value_name]
        :type new_value: String, List or Dict

        """

        # Load old version of the yaml file to update
        document = yaml.safe_load(open(values_yaml_path))

        # If target value exists in the yaml file,
        # Format the new value to its correct type
        if self.value_exists(values_yaml_path, value_name):

            value = str(new_value)

            if value in ('True', 'False'):
                value_type = bool

            # If no type for the new value was provided, search in the old
            # yaml file to find the type of the value
            if not value_type:
                value_type = self.get_value_type(values_yaml_path, value_name)


        # If a value type was provided :

            # If the new value is a list,
            # Add it to the existing list
            # or create a new one
            if value_type is list:
                old_value = self.get_target_value(values_yaml_path, value_name)
                if not old_value:
                    old_value = []
                if new_value:
                    old_value.append(new_value)
                value = old_value

            # If the new value is a dict,
            # Add it to the existing dict
            # or create a new one
            elif value_type is dict:
                old_value = self.get_target_value(values_yaml_path, value_name)
                if not old_value:
                    old_value = {}
                if new_value:
                    new_value_key = str(new_value.split(':')[0])
                    new_value_value = str(new_value.split(':')[-1])
                    old_value[new_value_key] = new_value_value
                value = old_value

            elif value_type is bool:
                if value in ('True', 'true'):
                    value = True
                elif value in ('False', 'false'):
                    value = False
                else:
                    value = str(value)

            elif value_type is str:
                value = new_value


        # Generating the new document
            key = value_name

            # Parse the path
            keys = key.split('.')
            # Create reference to the top most item
            element = document

            # Process up to the last key item
            for key in keys[:-1]:
                # Find the old value
                element = element[key]

            # Replace the old value
            try:
                element[keys[-1]] = value
            except TypeError:
                element[0][keys[-1]] = value

            return self.replace_value(values_yaml_path, document)


    def create_value(self, values_yaml_path, value_name, new_value):
        """
        Creates a value in a values.yaml file
        """

        # Load the old yaml file
        document = yaml.safe_load(open(values_yaml_path))

        # Parse the path
        steps = value_name.split('.')

        # Reverse the steps so that the path is in
        # ascending order
        steps.reverse()
        step_count = len(steps)

        # Format the new value
        if new_value == '{}':
            new_doc = {}
        elif new_value == '[]':
            new_doc = []
        else:
            new_doc = new_value

        # Create the structure for the new value
        for i in range(step_count):
            new_doc = {steps.pop(0):new_doc}

        # Merge the old and new values
        new_doc = {**document, **new_doc}

        # Update the yaml file with the new document
        with open(values_yaml_path, 'w+') as file:
            file.write(yaml.safe_dump(new_doc))

        return True

    def delete_value(self, values_yaml_path, value_name):
        """
        Returns a dictionary of a yaml file with target value removed.

        :param values_yaml_path: Path to values.yaml file you wish to replace a value of.
        :type values_yaml_path: String
        :param value_name: Name of the value you wish to change,
        each level of depth separated by a '.' (Same syntax as 'mpaas list values' output)
        :type value_name: String
        :rtype: Dictionary

        """

        value_type = self.get_value_type(values_yaml_path, value_name)

        value = ''
        subdocs = []

        # Load the old document
        document = yaml.safe_load(open(values_yaml_path))

        # Parse the path
        steps = value_name.split('.')


        if len(steps) > 1:
            # Find value to delete
            for index, step in enumerate(steps):
                if index == len(steps)-1:
                    try:
                        document[step] = value
                        subdocs.append(document)
                    except TypeError:
                        for index, entry in enumerate(document):
                            if step in entry:
                                document[index][step] = value
                                subdocs.append(document)

                else:
                    subdocs.append(document)
                    document = document[step]
        else:
            document[steps[0]] = value

        if subdocs:
            return (subdocs[0], value_type)
        else:
            return (document, value_type)


    def get_value(self, document_path, value_path):
        """
        Method that returns a value in a target yaml document.
        If the value does not exist, returns None

        :param document_path: Path to target document
        :type document_path: String
        :param value_path: Name of the value you wish to get,
        each level of depth separated by a '.' (Same syntax as 'mpaas list values' output)
        :type value_path: String
        :rtype: String, List, Dict or None

        """

        document = yaml.safe_load(open(document_path))
        element = document
        keys = value_path.split('.')

        for key in keys[:-1]:
            # Try to find the old value
            try:
                element = element[key]
            except KeyError:
                return None

        # Return the old value
        try:
            return element[keys[-1]]
        except TypeError:
            try:
                return element[0][keys[-1]]
            except KeyError:
                return None
        except KeyError:
            return None


    def value_exists(self, document_path, value_path):
        """
        Method that checks if a value exists in target yaml document.

        :param document_path: Path to target document
        :type document_path: String
        :param value_path: Name of the value you wish to check,
        each level of depth separated by a '.' (Same syntax as 'mpaas list values' output)
        :type value_path: String
        :rtype: Boolean

        """
        return self.get_value(document_path, value_path) is not None


    def get_value_type(self, document_path, value_path):
        """
        Method that returns the type of a value in a target yaml document

        :param document_path: Path to target document
        :type document_path: String
        :param value_path: Name of the value you wish to get type,
        each level of depth separated by a '.' (Same syntax as 'mpaas list values' output)
        :type value_path: String
        :rtype: type

        """

        return type(self.get_target_value(document_path, value_path))

    def get_target_value(self, document_path, value_path):
        """
        Method that returns the value of target key in a yaml document

        :param document_path: Path to target document
        :type document_path: String
        :param value_path: Name of the value you wish to get type,
        each level of depth separated by a '.' (Same syntax as 'mpaas list values' output)
        :type value_path: String
        :rtype: dict, list or string

        """

        if self.value_exists(document_path, value_path):
            document = yaml.safe_load(open(document_path))
            steps = value_path.split('.')
            if len(steps) > 1:
                for step in steps:
                    try:
                        document = document[step]
                    except TypeError:
                        document = document[0][step]
                    except KeyError:
                        return None
            else:
                document = document[steps[0]]
            return document
        return None

    def is_simple_value(self, document_path, value_path):
        """
        Method that return True if target value is not a dict or a list

        :param document_path: Path to target document
        :type document_path: String
        :param value_path: Name of the value you wish to check,
        each level of depth separated by a '.' (Same syntax as 'mpaas list values' output)
        :type value_path: String
        :rtype: Boolean

        """
        return self.get_value_type(document_path, value_path) is not (dict or list)

    def get_chart_path(self, project, chart):
        """
        Returns path to target chart in target project.

        :param project: Name of target project
        :type project: String
        :param chart: Name of target chart
        :type chart: String
        :rtype: String

        """
        return self.projects_path + project + '/charts/' + chart

    def get_values_path(self, project, chart):
        """
        Returns the path to the values.yaml file in target chart in target project.
        Returns path to target chart in target project.

        :param project: Name of target project
        :type project: String
        :param chart: Name of target chart
        :type chart: String
        :rtype: String

        """
        return self.get_chart_path(project, chart) + '/values.yaml'

    def lint_chart(self, chart_path):
        """
        Returns true if target path is a valid helm chart,
        false otherwise.

        :param chart_path: Path to target chart
        :type chart_path: String
        :rtype: Boolean

        """
        try:
            res = subprocess.check_output(['helm', 'lint', chart_path],
                                          stderr=open('/dev/null', 'w'))
        except subprocess.CalledProcessError:
            return False

        if 'no failures' in str(res).split(',')[-1]:
            return True
        else:
            return False

    def from_template(self, project, chart_name):
        """
        Returns the name of the template a chart was created from.

        :param project: Name of target project
        :type project: String
        :param chart_name: Name of target chart
        :type chart_name: String
        :rtype: String

        """
        try:
            with open(self.get_chart_path(project, chart_name) + '/Chart.yaml') as chart_yaml:
                for line in chart_yaml.readlines():
                    if '#fromTemplate' in line:
                        return line.split('=')[-1]
        except FileNotFoundError:
            pass

        return 'Unknown'

    def preprocess(self, project_name, project_location, namespace):
        """
        Renders a complete template of target project.
        """

        if project_name != 'None':
            try:
                for chart in os.listdir(project_location+'/charts'):
                    output = subprocess.check_output(['helm', 'template',
                                                        project_location+'/charts/'+chart,
                                                        '--namespace', namespace, '--name',
                                                        project_name]).decode('utf-8')
            except:
                raise RenderError(project_name)
        else:
            raise NoContextError()

        return output

    def write_preprocess(self, project_name, project_location, namespace):
        """
        Writes the preprocessed template to the default location in the template
        """

        with open(project_location+'/output/templates/'+project_name, 'w+') as file:
            file.write(self.preprocess(project_name, project_location, namespace))

    def has_preprocessed(self, project_name, project_location):
        """
        Returns False if no preprocessed template has been found, True otherwise.
        """
        
        return os.path.isfile(project_location+'/output/templates/'+project_name)

    def delete_preprocess(self, project_name, project_location):
        """
        Deletes the preprocesses file. Useful when some values change or new plugins are loaded.
        Ensures every plugin gets to work with the latests values.
        """

        if self.has_preprocessed(project_name, project_location):
            try:
                os.remove(project_location+'/output/templates/'+project_name)
            except:
                pass
