import importlib
import random
from pathlib import Path
from typing import List

from fastapi import FastAPI

from fa_common import logger, DatabaseType, get_settings


def default_id_generator(bit_size: int = 32) -> int:
    """
    Generator of IDs for newly created MongoDB rows.

    :return: `bit_size` long int
    """
    return random.getrandbits(bit_size)


def get_next_id() -> int:
    """
    Retrieves ID generator function from the path, specified in project's conf.
    :return: newly generated ID
    """
    return default_id_generator()


def setup_db(app: FastAPI) -> None:
    """
    Helper function to setup MongoDB connection & `motor` client during setup.
    Use during app startup as follows:

    .. code-block:: python

        app = FastAPI()

        @app.on_event('startup')
        async def startup():
            setup_mongodb(app)

    :param app: app object, instance of FastAPI
    :return: None
    """
    settings = get_settings()
    if settings.DATABASE_TYPE == DatabaseType.MONGODB:
        # Only import mongo deps if we are using mongo
        import motor.motor_asyncio

        client = motor.motor_asyncio.AsyncIOMotorClient(
            settings.MONGODB_DSN,
            minPoolSize=settings.mongodb_min_pool_size,
            maxPoolSize=settings.mongodb_max_pool_size,
        )
        app.mongodb = client[settings.MONGODB_DBNAME]  # type: ignore
        logger.info("Mongo Database has been set")

    elif settings.DATABASE_TYPE == DatabaseType.GCP_FIRESTORE:
        from firebase_admin import firestore

        app.firestore = firestore.client()  # type: ignore
        logger.info("Firestore client has been set")
    elif settings.DATABASE_TYPE == DatabaseType.NONE:
        logger.info("Database is set to NONE and cannot be used")
        return
    else:
        raise ValueError("DATABASE_TYPE Setting is not a valid database option.")


def get_db_client():
    """
    Gets instance of MongoDB client for you to make DB queries.
    :return: MongoDBClient
    """
    settings = get_settings()
    if settings.DATABASE_TYPE == DatabaseType.MONGODB:
        from .mongo_client import MongoDBClient

        client = MongoDBClient()
        return client
    elif settings.DATABASE_TYPE == DatabaseType.GCP_FIRESTORE:
        from .firestore_client import FirestoreClient

        client = FirestoreClient()
        return client

    raise ValueError("DATABASE_TYPE Setting is not a valid database option.")


def all_subclasses(cls):
    return set(cls.__subclasses__()).union(
        [s for c in cls.__subclasses__() for s in all_subclasses(c)]
    )


def get_models() -> list:
    """
    Scans `settings.APP_PATH`.
    Find `models` modules in each of them and get all attributes there.
    Last step is to filter attributes to return only those,
    subclassed from DocumentDBModel (or timestamped version).

    Used internally only by `create_indexes` function.

    :return: list of user-defined models (subclassed from DocumentDBModel) in apps
    """
    from .models import DocumentDBModel

    models = Path(get_settings().APP_PATH).glob("**/models.py")
    for m in models:
        mod_string = str(m).replace("/", ".").replace("\\", ".").replace(".py", "")
        importlib.import_module(mod_string)

    return list(all_subclasses(DocumentDBModel))


async def create_indexes() -> List[str]:
    """
    Gets all models in project and then creates indexes for each one of them.
    :return: list of indexes that has been invoked to create
             (could've been created earlier, it doesn't raise in this case)
    """
    models = get_models()
    indexes = []
    for model in models:
        indexes.append(await model.create_indexes())
    return list(filter(None, indexes))
