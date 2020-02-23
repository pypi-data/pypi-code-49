from PIL import Image
import os


class Numbers(object):
    asset_path = "/asset"

    def get(self, item):
        """get image reference"""
        if item not in self.loaded_resources:
            self.load_resource(item)

        return self.loaded_resources[item]

    def load_resource(self, number):
        """create reference to single number"""
        area = (self.offsets[number], 0, self.offsets[number] + self.size['width'], self.size['height'])
        self.loaded_resources[number] = self.resource.crop(area)

    def get_resource(self, file, path=None):
        if not path:
            path = os.path.dirname(__file__) + self.asset_path+"/"
        return Image.open(path + file)

    def get_transparency(self):
        """get font transparency"""
        return self.transparency
