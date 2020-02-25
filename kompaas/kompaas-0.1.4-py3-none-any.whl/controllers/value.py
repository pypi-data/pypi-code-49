"""
Module that handles values.\n
Values are reprensentations of yaml key/value pairs.\n

Supports:\n
- Updating\n
- Replacing\n
- Getting\n
- Deleting
"""

import os
import sys
from cement import Controller, ex
from ..mpaas_exceptions import NoContextError, MissingChartError,\
     MissingValueError, MissingResourceError


class Value(Controller):
    """
    Child class of the Controller class.
    Handles the 'create' sub-commands.
    """
    class Meta:
        """
        Meta class attributes.
        'create' is a nested sub-command of the base 'mpaas' command
        """
        label = 'value'
        aliases = ['values']
        stacked_type = 'nested'
        stacked_on = 'base'
        usage = 'kompaas [SUB-COMMANDS]'
        help = 'Handle values.'

    @ex(
        help='List all values in selected chart',
        arguments=[
            (
                ['-c', '--chart'],
                {'action': 'store',
                 'dest': 'chart'}
            ),
            (
                ['--all'],
                {'action': 'store_true',
                 'help': 'Lists values from all charts in current project'}
            ),
        ]
    )
    def get(self):
        """
        Lists all values from current chart in current project.
        Renders output using jinja2 template.
        """
        context = self.app.ch.get_context_project()
        projects_path = self.app.config.get('mpaas', 'projects_path')
        charts_path = projects_path + context + '/charts'

        if context != 'None':
            if not self.app.pargs.all:
                if self.app.pargs.chart:
                    chart = self.app.pargs.chart
                else:
                    chart = self.app.ch.get_context_chart()

                values_path = charts_path + '/' + chart + '/values.yaml'

                if chart in os.listdir(charts_path):
                    values = self.app.vp.parse_with_JSON(values_path)
                else:
                    raise MissingChartError(context, chart)

                data = {'objectname': chart,
                        'data': values,
                        'project': context,
                        'version': self.app.ch.get_version(charts_path + '/' + chart)}

                self.app.render({'context': self.app.ch.get_context_all()}, 'list/context.jinja2')
                self.app.render(data, '/list/values.jinja2')

            else:
                self.app.render({'context': self.app.ch.get_context_all()}, 'list/context.jinja2')
                for chart in os.listdir(charts_path):
                    values_path = charts_path + '/' + chart + '/values.yaml'
                    values = self.app.vp.parse(values_path)

                    data = {'objectname': chart,
                            'data': values,
                            'context': self.app.ch.get_context_all(),
                            'project': context,
                            'version': self.app.ch.get_version(charts_path + '/' + chart)}

                    self.app.render(data, '/list/values.jinja2')
        else:
            raise NoContextError

    @ex(
        help='Set values in an object',
        arguments=[

            (['-p', '--project'],
             {'help': 'target resource name',
              'action': 'store',
              'dest': 'project_name'}),

            (['-c', '--chart'],
             {'action': 'store',
              'dest': 'chart'}),

            (['value_name'],
             {'help': 'target value to change',
              'action': 'store'}),

            (['new_value'],
             {'help': 'new value of target key',
              'action': 'store'})
            ]
        )

    def replace(self):
        """
        Method that replaces a value in a chart in target project.
        """

        if self.app.pargs.chart:
            chart = self.app.pargs.chart
        else:
            chart = self.app.ch.get_context_chart()

        if self.app.pargs.project_name:
            context = self.app.pargs.project_name
        else:
            context = self.app.ch.get_context_project()

        project_path = self.app.config.get('mpaas', 'projects_path')
        value_name = self.app.pargs.value_name
        new_value = self.app.pargs.new_value

        #Delete preprocessed file so that plugins don't work with stale values
        self.app.ch.delete_preprocess(context, project_path+context)

        values_yaml_path = self.app.ch.get_values_path(context, chart)

        if os.path.isdir(self.app.ch.get_chart_path(context, chart)):
            if not self.app.ch.value_exists(values_yaml_path, value_name):
                self.app.log.warning('Value %s did not exist in default chart, creating anyway.'
                                     % value_name)
                self.app.ch.create_value(values_yaml_path, value_name, new_value)

            else:
                document, value_type = self.app.ch.delete_value(values_yaml_path, value_name)
                self.app.ch.replace_value(values_yaml_path, document)
                self.app.ch.update_value(values_yaml_path, value_name, new_value,
                                         value_type=value_type)
                self.app.log.info('Successfully replaced value %s to %s' % (value_name, new_value))
        else:
            raise MissingChartError(context, chart)

    @ex(
        help='Add a value to a list or dictionary in target chart',
        arguments=[

            (['-p', '--project'],
             {'help': 'target resource name',
              'action': 'store',
              'dest': 'project_name'}),

            (['-c', '--chart'],
             {'action': 'store',
              'dest': 'chart'}),

            (['-f', '--file'],
             {'action': 'store_true',
              'help': 'Set a value to the content of a file',
              'dest': 'sourcefile'}),

            (['value_name'],
             {'help': 'target value to change',
              'action': 'store'}),

            (['new_value'],
             {'help': 'new value of target key',
              'nargs': '?',
              'action': 'store'})
        ]
    )
    def update(self):
        """
        Adds a value to a list or dictionary inside target values.yaml file
        """

        if self.app.pargs.chart:
            chart = self.app.pargs.chart
        else:
            chart = self.app.ch.get_context_chart()

        if self.app.pargs.project_name:
            context = self.app.pargs.project_name
        else:
            context = self.app.ch.get_context_project()

        project_path = self.app.config.get('mpaas', 'projects_path')
        value_name = self.app.pargs.value_name

        #Delete preprocessed file so that plugins don't work with stale values
        self.app.ch.delete_preprocess(context, project_path+context)

        if self.app.pargs.sourcefile:
            try:
                new_value = sys.stdin.read()
                # new_value = new_value.strip("'")
                # new_value = "'" + new_value + "'"
            except FileNotFoundError:
                raise MissingResourceError('File', self.app.pargs.new_value)
        else:
            new_value = self.app.pargs.new_value

        values_yaml_path = project_path + context + '/charts/' + chart + '/values.yaml'
        if not os.path.isfile(values_yaml_path):
            raise MissingChartError(context, chart)

        if not self.app.ch.value_exists(values_yaml_path, value_name):
            self.app.log.warning('Value %s did not exist in default chart, creating anyway.'
                                 % value_name)
            self.app.ch.create_value(values_yaml_path, value_name, new_value)
        else:
            self.app.ch.update_value(values_yaml_path, value_name, new_value)

        self.app.log.info('Successfully set %s to %s' % (value_name, new_value))

    @ex(
        help='Add a value to a list or dictionary in target chart',
        arguments=[

            (['-p', '--project'],
             {'help': 'target resource name',
              'action': 'store',
              'dest': 'project_name'}),

            (['-c', '--chart'],
             {'action': 'store',
              'dest': 'chart'}),

            (['value_name'],
             {'help': 'target value to change',
              'action': 'store'})
        ]
    )
    def delete(self):
        """
        Deletes a value from target values.yaml file
        """

        if self.app.pargs.chart:
            chart = self.app.pargs.chart
        else:
            chart = self.app.ch.get_context_chart()

        if self.app.pargs.project_name:
            context = self.app.pargs.project_name
        else:
            context = self.app.ch.get_context_project()

        project_path = self.app.config.get('mpaas', 'projects_path')
        value_name = self.app.pargs.value_name

        #Delete preprocessed file so that plugins don't work with stale values
        self.app.ch.delete_preprocess(context, project_path+context)

        values_yaml_path = project_path + context + '/charts/' + chart + '/values.yaml'
        if not os.path.isfile(values_yaml_path):
            raise MissingChartError(context, chart)

        if self.app.ch.value_exists(values_yaml_path, value_name):

            document, value_type = self.app.ch.delete_value(values_yaml_path, value_name)
            self.app.ch.replace_value(values_yaml_path, document)
            self.app.ch.update_value(values_yaml_path, value_name, '', value_type=value_type)
            self.app.log.info('Successfully deleted value %s.' % (value_name))
        else:
            raise MissingValueError(value_name, chart)

    @ex(
        help="test"
    )
    def test(self):
        self.app.vp.parse_with_JSON("/home/paolo/tests/bla.yaml")
