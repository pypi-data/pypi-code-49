import json


class Instance:
    def __init__(self, content):
        self.x = self._set_x(content)
        self.y = self._set_y()

    def _set_x(self, content):
        if isinstance(content, dict):
            content.pop('y', None)
            return content['x']
        else:
            x = []
            for i in range(len(content)):
                content[i].pop('_id', None)
                content[i].pop('y', None)
                # content[i]['x'].pop('data', None)
                x.append(content[i]['x'])
            return x

    def _set_y(self):
        return {
            "true": [],
            "pred": []
        }

    def pack(self):
        return json.dumps({
            "x": self.x,
            "y": self.y
        })
