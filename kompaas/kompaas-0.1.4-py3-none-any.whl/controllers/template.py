"""
Module that handles templates.\n
Templates are nothing more than helm charts.\n
They are required to create a chart object in a project.\n

Supports:\n
- Creating\n
- Getting\n
- Deleting
"""

import os
import shutil
from cement import Controller, ex
from ..mpaas_exceptions import EmptyDirectoryError, MissingDirectoryError, NoValidTemplateError,\
    MissingTemplateError


class Template(Controller):
    """
    Child class of the Controller class.
    Handles the 'create' sub-commands.
    """
    class Meta:
        """
        Meta class attributes.
        'template' is a nested sub-command of the base 'mpaas' command
        """
        label = 'template'
        aliases = ['templates']
        stacked_type = 'nested'
        stacked_on = 'base'
        usage = 'kompaas [SUB-COMMANDS]'
        help = 'Handle templates.'

    @ex(
        help='List all available templates',
        arguments=[
            (['-l', '-- location'],
             {'action': 'store',
              'dest': 'location'})
        ]
    )
    def get(self):
        """
        Lists all templates currently in the mpaas template directory,
        or in target location if -l is specified.
        """
        data = {}
        if self.app.pargs.location is not None:
            templates_path = self.app.pargs.location
        else:
            templates_path = self.app.config.get('mpaas', 'templates_dir')

        if os.path.isdir(templates_path):
            templates = os.listdir(templates_path)
        else:
            raise MissingDirectoryError(templates_path)

        if not templates:
            raise EmptyDirectoryError(templates_path)

        for template in templates:
            template_path = os.path.join(templates_path, template)
            if self.app.ch.lint_chart(template_path):
                data[template] = self.app.ch.get_version(template_path)

        if not data:
            raise NoValidTemplateError(templates_path)

        data = {'data': data, 'context': self.app.ch.get_context_all()}
        self.app.render(data, '/list/templates.jinja2')

    @ex(
        help='Delete target template in default location.',
        arguments=[
            (['template_name'],
             {'action': 'store'})
        ]
    )
    def delete(self):
        """
        Method to delete target template
        """

        template_name = self.app.pargs.template_name
        templates_path = self.app.config.get('mpaas', 'templates_dir')

        if os.path.isdir(templates_path):
            templates = os.listdir(templates_path)
        else:
            raise MissingDirectoryError(templates_path)

        if not templates:
            raise EmptyDirectoryError(templates_path)

        try:
            shutil.rmtree(templates_path + template_name)
        except IOError:
            raise MissingTemplateError(template_name)

        self.app.log.info('Successfully deleted template %s' % template_name)
