import os
import yaml
import getpass

from framl.config import Config


class ConfigFraml(Config):
    user_config_path = os.environ['HOME'] + '/.framl'

    def __init__(self):

        self._skeleton_bucket: str = None
        self._skeleton_name: str = None
        self._skeleton_tag: str = None

        # if the user has no config file
        if not os.path.exists(ConfigFraml.user_config_path):
            self._create_user_config()

        self._fc = yaml.safe_load(open(ConfigFraml.user_config_path))

    def _create_user_config(self):
        default = {
            'skeleton':    {
                'bucket': 'framl-skeleton-artifact',
                'name':   'framl-skeleton-artifact',
                'tag':    'latest'
            },
            'environment': getpass.getuser()
        }
        with open(ConfigFraml.user_config_path, 'w') as outfile:
            yaml.dump(default, outfile, default_flow_style=False, sort_keys=False)

    def _load_lib_config(func) -> None:

        def wrapper(self):
            if self._skeleton_bucket is None:

                requirements = ['skeleton.bucket', 'skeleton.name', 'skeleton.tag']
                if not Config.keys_exist(requirements, self._fc):
                    raise Exception(f'Framl config is missing skeleton parameters. Check {ConfigFraml.user_config_path}')

                self._skeleton_bucket = Config.get_key('skeleton.bucket', self._fc)
                self._skeleton_name = Config.get_key('skeleton.name', self._fc)
                self._skeleton_tag = Config.get_key('skeleton.tag', self._fc)

            return func(self)

        return wrapper


    @_load_lib_config
    def get_skeleton_bucket(self):
        return self._skeleton_bucket

    @_load_lib_config
    def get_skeleton_name(self):
        return self._skeleton_name

    @_load_lib_config
    def get_skeleton_tag(self):
        return self._skeleton_tag

    @staticmethod
    def get_env() -> str:
        if 'FRAML_ENV' in os.environ and os.environ['FRAML_ENV'] is not None:
            return os.environ['FRAML_ENV']
        if os.path.exists(ConfigFraml.user_config_path):
            conf = yaml.safe_load(open(ConfigFraml.user_config_path))
            if 'environment' in conf.keys():
                return conf['environment']
        raise Exception(f"Can't determine Framl environment. "
                        f"Please specify it in {ConfigFraml.user_config_path} or as environment variable with 'FRAML_ENV'")

    @staticmethod
    def set_env(env):
        if os.path.exists(ConfigFraml.user_config_path):
            conf = yaml.safe_load(open(ConfigFraml.user_config_path))
            conf['environment'] = env
            with open(ConfigFraml.user_config_path, 'w') as outfile:
                yaml.dump(conf, outfile, default_flow_style=False, sort_keys=False)
        else:
            os.environ['FRAML_ENV'] = env
