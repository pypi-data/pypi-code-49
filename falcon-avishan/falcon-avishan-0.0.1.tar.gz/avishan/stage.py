import falcon

from avishan.middlewares import JSONTranslator
from avishan.utils import all_subclasses
from avishan.views import AvishanView


class AvishanFalconStage:
    def __init__(self, middlewares: list = ()):
        self.app = self.create_app(middlewares=middlewares)
        for view in all_subclasses(AvishanView):
            url: str = view.url
            if not url.startswith('/'):
                url = '/' + url
            self.app.add_route(url, view())

    @staticmethod
    def create_app(middlewares: list = ()):
        return falcon.API(middleware=[JSONTranslator()] + list(middlewares))
