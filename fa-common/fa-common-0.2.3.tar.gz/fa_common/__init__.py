from .config import get_settings, Settings, StorageType, DatabaseType
from .exception_handlers import setup_exception_handlers
from .exceptions import (
    DatabaseError,
    StorageError,
    HTTPException,
    NotImplementedError,
    UnknownError,
    BadRequestError,
    UnauthorizedError,
    ForbiddenError,
    NotFoundError,
)
from .utils import (
    force_async,
    force_sync,
    sizeof_fmt,
    resolve_dotted_path,
    get_logger,
    logger,
    get_current_app,
    get_remote_schema,
    get_now,
    get_timezone,
    async_get,
)
from .responses import UJSONResponse

from typing import Type
from starlette.middleware.cors import CORSMiddleware
from fastapi import FastAPI


import functools


def create_app(env_path=None) -> FastAPI:
    settings = get_settings(env_path)

    if settings.SENTRY_DSN is not None:
        import sentry_sdk

        sentry_sdk.init(settings.SENTRY_DSN)

    app = FastAPI(
        title=settings.PROJECT_NAME,
        openapi_url=f"{settings.API_PRE_PATH}/openapi.json",
    )
    # CORS
    origins = []

    # Set all CORS enabled origins
    if settings.BACKEND_CORS_ORIGINS:
        origins_raw = settings.BACKEND_CORS_ORIGINS
        for origin in origins_raw:
            use_origin = origin.strip()
            origins.append(use_origin)
        app.add_middleware(
            CORSMiddleware,
            allow_origins=origins,
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )

    setup_exception_handlers(app)

    @app.on_event("startup")
    async def on_start_app() -> None:
        await start_app(app)

    @app.on_event("shutdown")
    @logger.catch
    async def stop_app() -> None:
        logger.info("Stopping App")
        # await close_db_connection(app)

    return app


async def start_app(app: FastAPI):
    from fa_common.storage import setup_storage
    from fa_common.db import setup_db, create_indexes

    if get_settings().USE_FIREBASE:
        import firebase_admin

        if not len(firebase_admin._apps):
            firebase_admin.initialize_app()

    setup_db(app)
    setup_storage(app)

    await create_indexes()
