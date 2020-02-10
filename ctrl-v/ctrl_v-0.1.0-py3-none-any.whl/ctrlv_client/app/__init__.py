from flask import Flask
from ctrlv_client.config import config
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_mde import Mde
import os
login_manager = LoginManager()
login_manager.login_view = 'main.login'
db = SQLAlchemy()
mde = Mde()

SITE_CONFIG_FILE = os.path.join(
    os.path.dirname(os.path.dirname(__file__)),
    'site-config.json'
)


def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    db.init_app(app)
    login_manager.init_app(app)
    mde.init_app(app)

    # main Blueprint
    from .main.views import main as main_blueprint
    app.register_blueprint(main_blueprint)
    from .tag.views import tag as tag_blueprint
    app.register_blueprint(tag_blueprint)

    return app
