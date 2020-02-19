import os
from yapf.yapflib.yapf_api import FormatFile

class Writer(object):
    def __init__(self, path_output=None, template_path=None):
        self.path_output = path_output
        self.template_path = template_path

        if not os.path.exists(self.template_path):
            raise Exception(f'Path: {self.template_path} not exists.')

    def write_entity(self, replace_map=None):
        o = open(self.path_output, "w+")  # open for append
        for line in open(self.template_path):
            if isinstance(replace_map, dict):
                for key, value in replace_map.items():
                    if isinstance(value, list):
                        value = '\n'.join(value)
                    line = line.replace('${' + key + '}', value)
            o.write(f'{line}')
        o.close()
        # FormatFile(self.path_output, in_place=True)
