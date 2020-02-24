from .view import (
    View,
    UtilsView
)

import os
from pony.orm import Database
from flask import (
    Flask,
    Blueprint,

)
from typing import Dict

base_path = os.path.dirname(os.path.abspath(__file__))


class PonyManager:
    def __init__(self, app: Flask = None, db: Database = None):
        self.app = None

        if app is not None:
            self.init_app(app)

        self.db = db
        self.blueprint = Blueprint(
            name=self.__name__.lower(),
            import_name=__name__,

            static_url_path='/',
            static_folder=os.path.join(base_path, 'static'),
            template_folder=os.path.join(base_path, 'templates'),

            url_prefix='/manage'
        )
        self.views: Dict[str, View] = dict()
        self.add_view(UtilsView(self))

    def init_app(self, app: Flask):
        """
        It's a weird Flask way to do this.
        """
        self.app = app
        self.app.context_processor(lambda: dict(manager=self))

    def add_view(self, view: View) -> None:
        """
        Add View to manager.
        """
        self.views[view.name] = view
        if not view.registered:
            view.register()

    def register(self):
        """
        Register manager blueprint.
        """
        self.app.register_blueprint(self.blueprint)


