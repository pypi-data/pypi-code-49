import configparser
import os
from logzero import logger


class ConfigParserUtil:
    @staticmethod
    def get_instance(folder_path, file_name):
        return ConfigParserUtil(folder_path, file_name)

    def __init__(self, folder_path:str, file_name:str):
        self._folder_path = folder_path
        self._file_name = file_name
        self._config_file_path = os.path.join(self._folder_path, self._file_name)
        logger.info("配置文件地址:{}".format(self._config_file_path))

    def read_value(self, group_name:str, key_name:str):
        """
        指定group，key读取值
        :param group_name: 
        :param key_name: 
        :return: 
        """
        if not os.path.exists(self._config_file_path):
            logger.error("配置文件不存在:{}".format(self._config_file_path))
            return None

        conf = configparser.ConfigParser()
        conf.read(self._config_file_path, encoding='utf-8')
        return conf.get(group_name, key_name)
