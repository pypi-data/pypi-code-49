"""
Module that handles configs.
A config is nothing more than a kubeconfig file.
Multiple configs can be created to easily switch between
clusters for example.

Supports:\n
- Creating\n
- Using\n
- Getting\n
- Deleting
"""

import os
from cement import Controller, ex
from mpaas.mpaas_exceptions import MissingResourceError, EmptyConfigDirectoryError


class Config(Controller):
    """
    Child class of the Controller class.
    Handles the 'configs' sub-commands.
    """
    class Meta:
        """
        Meta class attributes.
        'config' is a nested sub-command of the base 'mpaas' command
        """
        label = 'config'
        aliases = ['configs']
        stacked_type = 'nested'
        stacked_on = 'base'
        usage = 'kompaas [SUB-COMMANDS]'
        help = 'Handle configs.'

    @ex(
        help="Create a config object and give it a name",
        arguments=[
            (
                ['name'],
                {'action': 'store'}
            ),
            (
                ['config_path'],
                {'action': 'store'}
            ),
            (
                ['-u'],
                {'action': 'store_false',
                 'dest': 'use'}
            )
        ]
    )
    def create(self):
        """
        Handles creating configs
        """

        config_name = self.app.pargs.name
        config_path = self.app.pargs.config_path

        if os.path.isfile(config_path):
            self.app.config_handler.create_config(config_name, config_path)
            self.app.log.info('Successfully created config file %s from %s' %
                              (config_name, config_path))
        else:
            raise MissingResourceError('File', config_path)

        if self.app.pargs.use:
            self.app.config_handler.set_config(config_name)
            self.app.ch.set_context_config(config_name)
            self.app.log.info('Now using config %s' % config_name)



    @ex(
        help="Get a list of all configs.",
    )
    def get(self):
        """
        Method that returns a list of all current configs
        """

        configs_path = self.app.config.get('mpaas', 'kubeconfigs_path')
        configs = os.listdir(configs_path)

        if configs:
            data = {'names': configs, 'context': self.app.ch.get_context_all()}
        else:
            raise EmptyConfigDirectoryError()

        self.app.render(data, 'list/configs.jinja2')

    @ex(
        help="Describe a config",
        arguments=[
            (
                ['name'],
                {'action': 'store'}
            ),
        ]
    )
    def describe(self):
        """
        Method that renders a list of target config's attributes
        """

        config_name = self.app.pargs.name

        describe = self.app.ch.describe_config(config_name)

        data = {'contexts': describe['contexts'],
                'current_context': describe['current-context'],
                'context': self.app.ch.get_context_all(),
                'config_name': config_name}

        self.app.render(data, 'describe_config.jinja2')

    @ex(
        help="Use a target config.",
        arguments=[
            (['config_name'],
             {'action': 'store'})
        ]
    )
    def use(self):
        """
        Method that sets the current config.
        """

        config_name = self.app.pargs.config_name

        self.app.config_handler.set_config(config_name)
        self.app.ch.set_context_config(config_name)
        self.app.log.info('Now using config %s' % config_name)

    @ex(
        help="Delete a target config.",
        arguments=[
            (['config_name'],
             {'action': 'store'})
        ]
    )
    def delete(self):
        """
        Method that sets the current config.
        """

        config_name = self.app.pargs.config_name

        self.app.config_handler.delete_config(config_name)
        self.app.config_handler.check_config()
        self.app.log.info('Successfully deleted %s' % config_name)

    @ex(
        help="Restore default config."
    )
    def default(self):
        """
        Method that restores the default kube config.
        """

        self.app.config_handler.set_default_config()
        self.app.log.info("Successfully set config back to default.")
