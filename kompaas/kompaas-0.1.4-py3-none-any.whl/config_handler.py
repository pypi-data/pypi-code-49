"""
Module that handles kubeconfigs
"""

import shutil
import os
from mpaas.charter import Charter
from mpaas.mpaas_exceptions import ConfigExistsError, MissingConfigError, \
    MissingResourceError


class ConfigHandler:
    """
    Class that handles the creation and storage of kubeconfigs.
    """

    def __init__(self, path, context_path, projects_path):
        """
        Init method for ConfigHandler class
        :param path: path to the default mpaas config location
        :type path: String
        :param context_path: path to the default mpaas context path locationde
        :type projects_path: String
        """
        self.path = path
        self.charter = Charter(context_path, projects_path, path)

    def create_config(self, config_name, base_config_path):
        """
        Method that creates a config from an existing config file.
        :param config_name: Name of config file to create
        :type config_name: String
        :param base_config_path: Path to the original kubeconfig file
        :type base_config_path: String
        """

        #Check that config file with same name doesn't already exist
        if os.path.isfile(self.path + config_name):
            raise ConfigExistsError(config_name)
        else:
            #copy base config file to new config file
            shutil.copy(base_config_path, self.path + config_name)

    def check_config(self):
        """
        Function that checks the config's status.
        Returns true if a default config file has been found, False otherwise.
        Makes a backup of the default config if it exists, to restore later.
        :rtype: Boolean
        """

        res = False

        if os.path.isfile(os.getenv('HOME')+'/.kube/config'):
            self.charter.set_context_config('Default')
            res = True

        elif os.getenv('KUBECONFIG') is not None:
            self.charter.set_context_config('Default')
            res = True

        elif os.getenv('KUBE_CONFIG_DATA') is not None:
            if not os.path.isdir(os.getenv('HOME')+'/.kube'):
                os.makedirs(os.getenv('HOME')+'/.kube')
            with open(os.getenv('HOME')+'/.kube/config', 'w+') as kubeconfig:
                kubeconfig.write(os.getenv('KUBE_CONFIG_DATA'))
            self.charter.set_context_config('Default')
            res = True

        else:
            self.charter.set_context_config('None')

        #making a backup of original kubeconfig file
        if not os.path.isfile(os.getenv('HOME')+'/.kube/config.old'):
            if os.path.isfile(os.getenv('HOME')+'/.kube/config'):
                shutil.copyfile(os.getenv('HOME')+'/.kube/config',
                                os.getenv('HOME')+'/.kube/config.old')

                if not os.path.isdir(os.getenv("HOME") + '/.mpaas/kubeconfigs'):
                    os.makedirs(os.getenv("HOME") + '/.mpaas/kubeconfigs')

                shutil.copyfile(os.getenv('HOME')+'/.kube/config',
                                os.getenv('HOME')+'/.mpaas/kubeconfigs/Default')

        return res

    def set_config(self, config_name):
        """
        Function that writes to the default kubeconfig location from a
        mpaas config file.
        """

        if os.path.isfile(self.path + config_name):
            target_config = open(self.path + config_name).read()
        else:
            raise MissingConfigError(config_name)

        with open(os.getenv('HOME')+'/.kube/config', 'w+') as kubeconfig:
            kubeconfig.write(target_config)

    def delete_config(self, config_name):
        """
        Method that deletes a mpaas config file.
        :param config_name: Name of target config to delete
        :type config_name: String
        """

        if not os.path.isfile(self.path + config_name):
            raise MissingConfigError(config_name)

        os.remove(self.path + config_name)

    def set_default_config(self):
        """
        Method that sets the current config from a backup of the
        original host's kubeconfig file
        """

        if os.path.isfile(os.getenv('HOME')+'/.kube/config.old'):
            shutil.copyfile(os.getenv('HOME')+'/.kube/config.old',
                            os.getenv('HOME')+'/.kube/config')
            self.charter.set_context_config('Default')
        else:
            raise MissingResourceError('config ', 'Default')
