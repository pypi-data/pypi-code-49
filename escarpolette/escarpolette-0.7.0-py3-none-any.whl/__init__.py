import logging

from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from starlette.requests import Request
from sqlalchemy.orm import Session

from escarpolette import db, routers
from escarpolette.models import Playlist
from escarpolette.settings import Config
from escarpolette.player import get_player

request_logger = logging.getLogger("escarpolette")


def create_new_playlist(db: Session):
    playlist = Playlist()
    db.add(playlist)
    db.commit()


def create_app(config: Config):
    app = FastAPI(
        title="Escarpolette",
        version="0.1",
        description="Manage your party's playlist without friction",
    )

    routers.init_app(app)

    app.add_middleware(
        CORSMiddleware, allow_credentials=True, allow_methods=["*"], allow_origins=["*"]
    )

    @app.middleware("http")
    async def log_request(request: Request, call_next):
        request_logger.info("%s %s", request.method, request.url.path)
        response = await call_next(request)
        return response

    @app.on_event("shutdown")
    def shutdown() -> None:
        get_player().shutdown()

    @app.on_event("startup")
    async def start() -> None:
        db.init_app(config)

        with db.get_db() as db_session:
            create_new_playlist(db_session)

        await get_player().init_app(config)

    return app
