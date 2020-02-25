"""
Module that handles charts.\n
Charts are standard helm charts stored in a project.\n
They are created from templates.\n

Supports:\n
- Creating \n
- Using \n
- Getting \n
- Deleting
"""

import os
import shutil
import subprocess
import yaml
from cement import Controller, ex
from ..mpaas_exceptions import EmptyDirectoryError, ChartExistsError, NoContextError,\
    MissingTemplateError, MissingChartError, RequirementsFileError


class Chart(Controller):
    """
    Child class of the Controller class.
    Handles the 'chart' sub-commands.
    """
    class Meta:
        """
        Meta class attributes.
        'chart' is a nested sub-command of the base 'mpaas' command
        """
        label = 'chart'
        aliases = ['charts']
        stacked_type = 'nested'
        stacked_on = 'base'
        usage = 'kompaas [SUB-COMMANDS]'
        help = 'Handle charts.'

    @ex(
        help="""Add a chart from an available template to current project
                and give it a name""",
        arguments=[
            (
                ['-l', '--location'],
                {'action': 'store',
                 'dest': 'location',
                 'help': 'directory containing target chart'}
            ),
            (
                ['templateName'],
                {'action': 'store'}
            ),
            (
                ['name'],
                {'action': 'store'}
            ),
            (
                ['-u'],
                {'help': "Set new project as current context",
                 'action': 'store_false',
                 'dest': 'use'}
            )
        ]
    )
    def create(self):
        """
        Adds a helm chart from a template to the current project and names it.
        """
        projects_path = self.app.config.get('mpaas', 'projects_path')
        resource_name = self.app.pargs.name
        context = self.app.ch.get_context_project()
        project_path = projects_path + context + '/charts/' + resource_name
        templates_path = self.app.config.get('mpaas', 'templates_dir')

        #Delete preprocessed file so that plugins don't work with stale values
        self.app.ch.delete_preprocess(context, project_path+context)

        if self.app.pargs.location:
            template_path = self.app.pargs.location + '/' + self.app.pargs.templateName
        else:
            template_path = templates_path + self.app.pargs.templateName

        # If there is a project in the current context and
        # no chart with the same name, copy chart.
        if context != 'None':
            if os.path.isdir(template_path):
                try:
                    shutil.copytree(template_path, project_path)
                    with open(project_path + '/Chart.yaml', 'a+') as chart_yaml:
                        chart_yaml.write('#fromTemplate=%s' % self.app.pargs.templateName)
                    old_doc = yaml.safe_load(open(project_path + '/Chart.yaml'))
                    try:
                        old_doc['name'] = resource_name
                        with open(project_path + '/Chart.yaml', 'w') as chart_yaml:
                            chart_yaml.write(yaml.safe_dump(old_doc))
                        self.fill_dependancy(resource_name)
                    except IOError:
                        pass
                except FileExistsError:
                    raise ChartExistsError(context, resource_name)

                self.app.log.info('Successfully added chart %s' % (self.app.pargs.name))

                if self.app.pargs.use:
                    self.app.ch.set_context_chart(resource_name)
                    self.app.log.info('Changed chart context to %s' % resource_name)

            else:
                raise MissingTemplateError(self.app.pargs.templateName)
        else:
            raise NoContextError()


    def fill_dependancy(self, chart_name):
        """
        Organize dependancy flow
        """
        requirement_path = self.check_dependancy(chart_name)
        if requirement_path:
            chart_dict = self.parse_requirements(requirement_path)
            if chart_dict:
                self.define_helm_repo_add(chart_dict)
            self.update_dependency(chart_name)


    def update_dependency(self, chart_name):
        """
        Launch helm dependency command
        """
        projects_path = self.app.config.get('mpaas', 'projects_path')
        context = self.app.ch.get_context_project()
        resource_name = self.app.pargs.name
        project_path = projects_path + context + "/charts/" + resource_name
        subprocess.run(['helm', 'dep', 'update', project_path],
                       stdout=subprocess.DEVNULL)


    def define_helm_repo_add(self, chart_dict):
        """
        Loop to add repo in helm
        """
        from mpaas.main import mpaas
        uniquechartdict = []
        for chart in chart_dict:
            if chart['repository'] not in uniquechartdict:
                uniquechartdict.append(chart['repository'])

        for chart in uniquechartdict:
            with mpaas(argv=["museum", "add", chart]) as app:
                app.run()


    def parse_requirements(self, requirement_path):
        """
        Read requirements.yaml in a chart and parse it
        """
        try:
            document = yaml.safe_load(open(requirement_path))
            repositories = []
            if document['dependencies'] is not None:
                for dependency in document['dependencies']:
                    if not dependency["repository"].startswith("file://"):
                        repositories.append({"repository": dependency['repository'],
                                             "name": dependency['name'],
                                             "version": dependency['version']})
                if repositories:
                    return repositories
            return False
        except FileExistsError:
            raise RequirementsFileError(self.app.pargs.templateName)


    def check_dependancy(self, chart_name):
        """
        Check if a requirement.yaml is present in chart
        """
        project_path = self.app.config.get('mpaas', 'templates_dir')
        if os.path.exists(project_path + chart_name + "/requirements.yaml"):
            self.app.log.warning("External requirements detected")
            return project_path + chart_name + "/requirements.yaml"
        return False

    @ex(
        help='List all charts in current project',
    )
    def get(self):
        """
        Lists all charts from the current project.
        Renders output using a jinja2 template.
        """
        context = self.app.ch.get_context_project()
        if context != 'None':
            data = {}
            projects_path = self.app.config.get('mpaas', 'projects_path')
            charts_path = projects_path + self.app.ch.get_context_project() + '/charts'

            try:
                if os.listdir(charts_path):
                    charts = os.listdir(charts_path)
                else:
                    raise EmptyDirectoryError('Project ' + context + " charts")
            except FileNotFoundError:
                if self.app.ch.get_context_project() == 'None':
                    raise NoContextError()

            for chart in charts:
                data[chart] = {'version': self.app.ch.get_version(charts_path + '/' + chart),
                               'fromTemplate': self.app.ch.from_template(context, chart)}

            project = context
            resources = {'data': data, 'context': self.app.ch.get_context_all(), 'project': project}
            self.app.render(resources, '/list/charts.jinja2')

        else:
            raise NoContextError()

    @ex(
        help='Delete a chart from the current project',
        arguments=[
            (['chart_name'],
             {'help': 'Target chart name',
              'action': 'store'})
        ],
    )
    def delete(self):
        """
        Method that deletes target chart from current project.
        """
        chart_name = self.app.pargs.chart_name
        projects_path = self.app.config.get('mpaas', 'projects_path')
        context = self.app.ch.get_context_project()

        #Delete preprocessed file so that plugins don't work with stale values
        self.app.ch.delete_preprocess(context, projects_path+context)

        #Check if chart exists
        if os.path.isdir(projects_path + context + '/charts/' + chart_name):
            shutil.rmtree(projects_path + context + '/charts/' + chart_name)

            self.app.log.info('Successfully deleted chart %s from project %s.'
                              % (chart_name, context))

            if self.app.ch.get_context_chart() == chart_name:
                self.app.ch.set_context_chart('None')
                self.app.log.info('Changed chart context to None')

        else:
            raise MissingChartError(context, chart_name)

    @ex(
        help='Set chart context to target chart',
        arguments=[
            (['chart_name'],
             {'help': 'Target chart name',
              'action': 'store'})
        ],
    )
    def use(self):
        """
        Method that sets chart context to target chart
        """

        chart_name = self.app.pargs.chart_name

        if os.path.isdir(self.app.ch.getcontext_path() + '/charts/' + chart_name):
            self.app.ch.set_context_chart(chart_name)
            self.app.log.info("Changed chart context to %s" % chart_name)
        else:
            raise MissingChartError(self.app.ch.get_context_project(), chart_name)
