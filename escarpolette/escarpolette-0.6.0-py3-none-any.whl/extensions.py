from fastapi import FastAPI

from escarpolette.player import Player
from escarpolette.settings import Config


def init_app(app: FastAPI, config: Config):
    # CORS(app)
    # Migrate(app, db)
    pass
