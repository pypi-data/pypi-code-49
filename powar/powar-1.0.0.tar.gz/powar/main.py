import argparse
import os
import logging
import time
import shutil

from powar.configuration import ModuleConfig, GlobalConfig, execute_command_fields
from powar.file_installer import FileInstaller
from powar.module_discoverer import ModuleDiscoverer
from powar.settings import AppSettings, AppMode, AppLogLevel
from powar.cache import CacheManager
from powar.util import realpath, UserError


LOGGING_FORMAT = "%(levelname)s: %(message)s"

def main():
    app_settings = AppSettings()

    parser = argparse.ArgumentParser()
    
    parser.add_argument("--dry-run", dest="dry_run",
                        help="don't modify any files, just show what would be done",
                        action="store_true")

    parser.add_argument("--template-dir", dest="template_dir",
                        help="use a custom directory for templates")

    parser.add_argument("--config-dir", dest="config_dir",
                        help="use a custom directory for configuration")

    group = parser.add_mutually_exclusive_group()
    group.add_argument("-q", "--quiet",
                       help="supress output",
                       action="store_const", dest="log_level", const=AppLogLevel.QUIET)
    group.add_argument("-v", "--verbose",
                       help="be verbose",
                       action="store_const", dest="log_level", const=AppLogLevel.VERBOSE)

    subparsers = parser.add_subparsers(help="mode to use", dest="mode command", required=True)

    # Install mode
    parser_install = subparsers.add_parser("install",
                                           help="install specified modules (empty argument installs all modules)")
    parser_install.set_defaults(mode=AppMode.INSTALL)
    parser_install.add_argument("modules_to_consider", nargs="*", metavar="MODULE",
                                help="module(s) to install (empty argument installs all modules)")
    parser_install.add_argument("--no-exec", dest="execute",
                                help="do not execute any exec-* fields in modules",
                                action="store_false")

    # Update mode
    parser_update = subparsers.add_parser("update",
                                          help="update modules as needed")
    parser_update.set_defaults(mode=AppMode.UPDATE)
    parser_update.add_argument("--no-exec", dest="execute",
                               help="do not execute any exec-* fields in modules",
                               action="store_false")

    # List-packages mode
    parser_list = subparsers.add_parser("list",
                                        help="list system packages required to install config files")
    parser_list.set_defaults(mode=AppMode.LIST_PACKAGES)
    parser_list.add_argument("modules_to_consider", nargs="*", metavar="MODULE",
                             help="module(s) to list packages for (empty argument lists for all modules)")

    # New module mode
    parser_new = subparsers.add_parser("new",
                                        help="create a new powar module")
    parser_new.set_defaults(mode=AppMode.NEW_MODULE)
    parser_new.add_argument("new_module_name", metavar="MODULE_NAME",
                             help="name of the new module to be created")
    parser_new.add_argument("--enable", dest="enable_new_module", action="store_true",
                                help="do not execute any exec-* fields in modules")

    # Init mode
    parser_init = subparsers.add_parser("init",
                                        help="create the folders required for powar")
    parser_init.set_defaults(mode=AppMode.INIT)

    parser.parse_args(namespace=app_settings)

    # set logging level from arguments
    logging.basicConfig(level=app_settings.log_level.into_logging_level(), format=LOGGING_FORMAT)
    logger: logging.Logger = logging.getLogger(__name__)

    # resolve $VARIABLES and ~, ensure absolute
    dirs_to_resolve = ["template_dir", "config_dir", "cache_dir"]
    for var in dirs_to_resolve:
        app_settings[var] = realpath(app_settings[var])
        if not os.path.isabs(app_settings[var]):
            parser.error(f"{var} needs to be absolute")

    try:
        if app_settings.mode == AppMode.INIT:
            os.makedirs(app_settings.config_dir, exist_ok=True)
            global_config_path = os.path.join(app_settings.config_dir, app_settings.global_config_filename)
            if not os.path.exists(global_config_path):
                shutil.copy(
                    os.path.join(
                        app_settings.data_path,
                        app_settings.global_config_template_filename
                    ),
                    global_config_path
                )
                print(f"{global_config_path} created.")
            else:
                logger.warn(f"{global_config_path} exists, skipping.")
            
            try:
                os.makedirs(app_settings.template_dir)
                print(f"{app_settings.template_dir}/ created.")
            except FileExistsError:
                logger.warn(f"{app_settings.template_dir} exists, skipping.")
            return


        if app_settings.mode == AppMode.NEW_MODULE:
            if not os.path.exists(app_settings.template_dir):
                raise UserError(f"{app_settings.template_dir} doesn't exist.")

            module_dir = os.path.join(app_settings.template_dir, app_settings.new_module_name)
            try:
                os.makedirs(module_dir)
            except FileExistsError:
                raise UserError(f"{module_dir} already exists.")

            module_config_path = os.path.join(module_dir, app_settings.module_config_filename)
            shutil.copy(
                os.path.join(
                    app_settings.data_path,
                    app_settings.module_config_template_filename
                ),
                module_config_path
            )
            print(f"{module_config_path} created.")
            return


        cache_man = CacheManager(app_settings.cache_dir)

        global_config = GlobalConfig.from_yaml_path(
            app_settings.config_dir, app_settings.global_config_filename)
        execute_command_fields(cwd=app_settings.config_dir, variables=global_config.variables, value=vars(global_config))

        module_discoverer = ModuleDiscoverer(app_settings, cache_man, global_config)

        directories = module_discoverer.get_all_dirs()

        if app_settings.mode == AppMode.LIST_PACKAGES:
            for directory in directories:
                config = ModuleConfig.from_yaml_path(directory, app_settings.module_config_filename)
                for package in config.system_packages:
                    print(package)
            return

        if app_settings.mode == AppMode.INSTALL or app_settings.mode == AppMode.UPDATE:

            if len(directories) == 0:
                logger.info("No new or modified files to install, exiting.")
                return

            # Main logic
            for directory in directories:
                config = ModuleConfig.from_yaml_path(directory, app_settings.module_config_filename)
                installer = FileInstaller(
                    config, global_config, directory, app_settings, module_discoverer)
                installer.install_and_exec()

            cache_man.set_last_run(time.time())
            return

    except UserError as error:
        for arg in error.args:
            logger.error(arg)
