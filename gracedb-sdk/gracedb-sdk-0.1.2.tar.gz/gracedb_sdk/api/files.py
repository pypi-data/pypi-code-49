from .base import Mapping, Resource


class File(Resource):

    def get(self):
        return self.session.get(self.url, stream=True).raw


class Files(Mapping, Resource):

    path = 'files/'
    mapped_class = File
