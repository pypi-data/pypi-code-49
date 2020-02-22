import json
import os
import yaml


class Config:
    def __init__(self):
        self.global_config = dict({})
        self.user_config = dict({})

    def add_global_config(self, item):
        assert self.global_config.get(item.config_code) is None, "config code {} already in".format(item.config_code)
        self.global_config[item.config_code] = item

    def add_user_config(self, item):
        assert self.user_config.get(item.config_code) is None, "config code {} already in".format(item.config_code)
        self.user_config[item.config_code] = item

    def export(self):
        return {
            'global_config': {item: self.global_config[item].export() for item in self.global_config},
            'user_config': {item: self.user_config[item].export() for item in self.user_config},
        }

    @staticmethod
    def load_from_object(json_object):
        object_config = Config()
        if json_object.get('global_config'):
            object_config.global_config = {item: ConfigItem.load_from_object(json_object.get('global_config')[item]) for
                                           item in json_object.get('global_config').keys()}
        if json_object.get('user_config'):
            object_config.user_config = {item: ConfigItem.load_from_object(json_object.get('user_config')[item]) for
                                         item in json_object.get('user_config').keys()}
        return object_config

    @staticmethod
    def load_from_yaml_file(yaml_file_path):
        try:
            with open(yaml_file_path, 'r', encoding='utf-8') as file_config:
                json_config = yaml.load(file_config.read(), Loader=yaml.FullLoader)
                if json_config:
                    if json_config.get('global_config'):
                        json_config['global_config'] = {item['config_code']: item for item in
                                                        json_config['global_config']}
                    if json_config.get('user_config'):
                        json_config['user_config'] = {item['config_code']: item for item in
                                                      json_config['user_config']}
                    return Config.load_from_object(json_config)
                else:
                    return None
        except:
            return None

    def __str__(self):
        return json.dumps(self.export(), sort_keys=True, indent=4)


class ConfigItem:
    def __init__(self):
        self.config_code = None
        self.title = None
        self.description = None
        self.view_type = None
        self.data = None

    @staticmethod
    def load_from_object(json_object):
        object_config = ConfigItem()
        object_config.config_code = json_object.get('config_code')
        object_config.title = json_object.get('title')
        object_config.description = json_object.get('description')
        object_config.view_type = json_object.get('view_type')
        object_config.data = json_object.get('data')
        return object_config

    def export(self):
        return {
            'title': self.title,
            'config_code': self.config_code,
            'description': self.description,
            'view_type': self.view_type,
            'data': self.data,
        }

    def __str__(self):
        return json.dumps(self.export(), sort_keys=True, indent=4)


class EditText(ConfigItem):
    def __init__(self, config_code, title, description=None, content=""):
        super().__init__()
        self.config_code = config_code
        self.title = title
        self.description = description
        self.view_type = "EditText"
        self.data = {
            'text': content
        }

#
# print(str(EditText('0', 'a', 'b', 'c')))
# print(str(ConfigItem.load_from_object(EditText('0', 'a', 'b', 'c').export())))
#
# m_config = Config()
# m_config.add_global_config(EditText('1', 'a', 'b', 'c'))
# m_config.add_global_config(EditText('2', 'd', 'e', 'f'))
# m_config.add_user_config(EditText('3', 'g', 'h', 'i'))
# m_config.add_user_config(EditText('4', 'j', 'k', 'l'))
# import yaml
# print(m_config)
# print(Config.load_from_object(m_config.export()))
