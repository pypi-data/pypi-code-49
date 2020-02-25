"""
Contains mpaas class, handles initialization and lauch of the application.
"""

import os
from pathlib import Path
import yaml
from cement import App, TestApp, init_defaults
from cement.ext.ext_plugin import CementPluginHandler
from cement.core.exc import CaughtSignal
from .core.exc import mpaasError
from .controllers.base import Base
from .controllers.project import Project
from .controllers.template import Template
from .controllers.chart import Chart
from .controllers.value import Value
from .controllers.config import Config
from .controllers.museum import Museum
from .charter import Charter
from .value_parser import ValueParser
from .config_handler import ConfigHandler
from pprint import pprint

from .mpaas_exceptions import \
    NoValidTemplateError, MissingResourceError, ResourceExistsError, NoContextError,\
    TemplateFetchError, EmptyDirectoryError, EmptyLinksError, DeployError, RenderError,\
    MissingChartError, NoConfigError, EmptyConfigDirectoryError, ConfigExistsError, \
    MissingConfigError, MissingValueError

# configuration defaults
CONFIG = init_defaults('mpaas')
# Variable d'environement
MPAASDIR = os.getenv('HOME') + '/.kompaas/'
CONFIG['mpaas']['install_dir'] = MPAASDIR
CONFIG['mpaas']['templates_dir'] = MPAASDIR + 'templates/'
CONFIG['mpaas']['tempfile'] = MPAASDIR + 'temp'
CONFIG['mpaas']['projects_path'] = MPAASDIR + 'projects/'
CONFIG['mpaas']['context_path'] = MPAASDIR + 'context'
CONFIG['mpaas']['temp_file'] = MPAASDIR + 'temp'
CONFIG['mpaas']['repo_file'] = MPAASDIR + 'repo'
CONFIG['mpaas']['kubeconfigs_path'] = MPAASDIR + 'kubeconfigs/'
CONFIG['mpaas']['plugin_dir'] = MPAASDIR + 'plugins/'
CONFIG['mpaas']['active_plugins'] = []



def extend_value_parser(app):
    """
    Function that extends a ValueParser instance to the whole application.
    """
    app.extend('vp', ValueParser())


def extend_charter(app):
    """
    Function that extends a Charter instance to the whole application.
    """
    app.extend('ch',
               Charter(app.config.get('mpaas', 'context_path'),
                       app.config.get('mpaas', 'projects_path'),
                       app.config.get('mpaas', 'kubeconfigs_path')))


def extend_config_handler(app):
    """
    Function that extends a ConfigHandler instance to the whole application.
    """

    app.extend('config_handler',
               ConfigHandler(app.config.get('mpaas', 'kubeconfigs_path'),
                             app.config.get('mpaas', 'context_path'),
                             app.config.get('mpaas', 'projects_path'))
               )


def setup_install_dir(app):
    """
    Function that sets up the file structure for the mpaas app
    """

    install_dir = app.config.get('mpaas', 'install_dir')

    if not os.path.isdir(install_dir):
        os.makedirs(install_dir)
        os.mkdir(app.config.get('mpaas', 'templates_dir'))
        os.mkdir(app.config.get('mpaas', 'projects_path'))
        os.mkdir(app.config.get('mpaas', 'kubeconfigs_path'))

    if not os.path.isdir(app.config.get('mpaas', 'plugin_dir')):
        os.mkdir(app.config.get('mpaas', 'plugin_dir'))

    if not os.path.isfile(app.config.get('mpaas', 'repo_file')):
        Path(app.config.get('mpaas', 'repo_file')).touch()
        open(app.config.get('mpaas', 'repo_file'), 'w+')


def setup_context(app):
    """
    Function that sets up the context file.
    """

    context_path = app.config.get('mpaas', 'context_path')
    context_dict = {'project': 'None', 'config': 'None', 'chart': 'None'}

    if not os.path.isfile(context_path):
        with open(context_path, 'w+') as context:
            context.write(yaml.safe_dump(context_dict))
        app.config_handler.check_config()

    if not os.path.isfile(os.getenv('HOME')+'/.kube/config.old'):
        if os.path.isfile(os.getenv('HOME')+'/.kube/config'):
            if app.ch.get_context_config() == 'None':
                app.config_handler.check_config()
        else:
            app.ch.set_context_config('None')
            app.log.warning("No kubeconfig file was found. " +
                            "\nSee https://docs.kompaas.io/#configs")


def setup_plugins(app):
    cph = CementPluginHandler()
    cph._setup(app)
    plugin_dir = app.config.get('mpaas', 'plugin_dir')
    for plugin_name in os.listdir(plugin_dir):
        if os.path.isdir(plugin_dir + plugin_name) and plugin_name[0] != '_':
            try:
                cph.load_plugin(plugin_name)
            except ImportError:
                app.log.warning('Plugin %s could not be loaded' % plugin_name)
    app.extend('mpaas_plugin_handler', cph)


class mpaas(App):
    """Mpaas-CLI primary application."""

    class Meta:
        """
        Meta class arguments.
        """
        label = 'mpaas'

        # configuration defaults
        config_defaults = CONFIG
        # call sys.exit() on close
        exit_on_close = False

        # load additional framework extensions
        extensions = [
            'yaml',
            'colorlog',
            'jinja2',
        ]

        # configuration handler
        config_handler = 'yaml'

        # configuration file suffix
        config_file_suffix = '.yml'

        # set the log handler
        log_handler = 'colorlog'

        # set the output handler
        output_handler = 'jinja2'
        # template_dirs = [CONFIG['mpaas']]

        # register handlers
        handlers = [
            Base,
            Project,
            Template,
            Chart,
            Value,
            Config,
            Museum
        ]

        hooks = [
            ('post_setup', setup_install_dir),
            ('post_setup', extend_value_parser),
            ('post_setup', extend_charter),
            ('post_setup', extend_config_handler),
            ('post_setup', setup_context),
            ('post_setup', setup_plugins)
        ]


class mpaasTest(TestApp, mpaas):
    """A sub-class of mpaas that is better suited for testing."""

    class Meta:
        """
        Meta class arguments
        """
        label = 'kompaas'

        # configuration defaults
        config_defaults = CONFIG
        
        # load additional framework extensions
        extensions = [
            'yaml',
            'colorlog',
            'jinja2',
        ]

        # configuration handler
        config_handler = 'yaml'

        # configuration file suffix
        config_file_suffix = '.yml'

        # set the log handler
        log_handler = 'colorlog'

        # set the output handler
        output_handler = 'jinja2'

        # register handlers
        handlers = [
            Base,
            Project,
            Template,
            Chart,
            Value,
            Config,
            Museum
        ]

        hooks = [
            ('post_setup', setup_install_dir),
            ('post_setup', extend_value_parser),
            ('post_setup', extend_charter),
            ('post_setup', extend_config_handler),
            ('post_setup', setup_context),
            ('post_setup', setup_plugins)
        ]


def main():
    """
    Main init function
    """
    with mpaas() as app:
        try:
            app.run()

        except AssertionError as error:
            print('AssertionError > %s' % error.args[0])
            app.exit_code = 1

            if app.debug is True:
                import traceback
                traceback.print_exc()

        except mpaasError as error:
            print('mpaasError > %s' % error.args[0])
            app.exit_code = 1

            if app.debug is True:
                import traceback
                traceback.print_exc()

        except CaughtSignal as error:
            # Default Cement signals are SIGINT and SIGTERM, exit 0 (non-error)
            print('\n%s' % error)
            app.exit_code = 0

        except MissingChartError as error:
            app.log.error('MissingChartError > %s' % error.message)

        except ConfigExistsError as error:
            app.log.error('ConfigExistsError > %s' % error.message)

        except MissingValueError as error:
            app.log.error('MissingValueError > %s' % error.message)

        except MissingConfigError as error:
            app.log.error('MissingConfigError > %s' % error.message)

        except NoContextError as error:
            app.log.error('NoContextError > %s' % error.message)

        except TemplateFetchError as error:
            app.log.error('TemplateFetchError > %s' % error.message)

        except EmptyDirectoryError as error:
            app.log.error('EmptyDirectoryError > %s' % error.message)

        except EmptyLinksError as error:
            app.log.error('EmptyLinksError > %s' % error.message)

        except DeployError as error:
            app.log.error('DeployError > %s' % error.message)
            raise DeployError

        except RenderError as error:
            app.log.error('RenderError > %s' % error.message)

        except NoValidTemplateError as error:
            app.log.error('NoValidTemplateError > %s' % error.message)

        except NoConfigError as error:
            app.log.error('NoConfigError > %s' % error.message)

        except EmptyConfigDirectoryError as error:
            app.log.error('EmptyConfigDirectoryError > %s' % error.message)

        except MissingResourceError as error:
            app.log.error('MissingResourceError > %s' % error.message)

        except ResourceExistsError as error:
            app.log.error('ResourceExistsError > %s' % error.message)

        except Exception as error:
            app.log.error('Exception > %s' % error.message)

if __name__ == '__main__':
    main()
