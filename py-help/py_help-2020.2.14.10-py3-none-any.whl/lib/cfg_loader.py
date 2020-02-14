# coding=utf-8
import yaml
import os
import codecs
from .CommonLogger import debug, info
from .path_helper import PathHelper


class CfgLoader:
    """
    加载配置文件的方法集合
    这里会被日志用到,不能打日志
    """

    project_cfg_dict = {}

    @classmethod
    def load_yml(cls, config_path, loader=yaml.Loader):
        # info("try to load {config_path}".format(config_path=config_path))
        if config_path is None:
            return {}
        if not os.path.exists(config_path):
            # info("config.yml not found in {config_path}".format(config_path=config_path))
            return False
        with codecs.open(config_path, encoding="utf-8") as stream:
            config = yaml.load(stream, loader)
        return config

    @classmethod
    def get_project_cfg(cls, cfg_name):
        if cls.project_cfg_dict.get(cfg_name) is not None:
            # debug("已经加载了 {}".format(cfg_name))
            pass
        else:
            cls.project_cfg_dict[cfg_name] = cls.load_yml(os.path.join(PathHelper.get_project_cfg(), cfg_name))
        return cls.project_cfg_dict.get(cfg_name)
