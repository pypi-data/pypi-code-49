from typing import Any, List, Optional, Tuple, Type

from google.cloud.exceptions import NotFound
from google.cloud.firestore import Client, CollectionReference, Query

from .base_client import BaseClient
from .models import (
    DBIndex,
    DeleteResult,
    DocumentDBModel,
    FireOffset,
    SortOrder,
    WhereCondition,
    WriteResult,
)
from fa_common import force_async, get_current_app, logger as LOG, DatabaseError


class FirestoreClient(BaseClient):
    """
    Singleton client for interacting with Firestore.
    Operates mostly using models, specified when making DB queries.

    Implements only part of internal `motor` methods, but can be populated more.

    Please don't use it directly, use `scidra.core.db.utils.get_db_client`.
    """

    __instance = None
    firestore: Client = None

    def __new__(cls) -> "FirestoreClient":
        if cls.__instance is None:
            cls.__instance = object.__new__(cls)
            app = get_current_app()
            cls.__instance.firestore = app.firestore  # type: ignore
        return cls.__instance

    def get_collection(self, collection_name: str) -> CollectionReference:
        return self.firestore.collection(collection_name)

    def generate_id(self, collection_name: str) -> str:
        collection = self.get_collection(collection_name)
        return collection.document().id

    async def insert(
        self, model: DocumentDBModel, include=None, exclude=None, session: Any = None,
    ) -> WriteResult:
        data = model.dict(include=include, exclude=exclude)
        _id: str = data["id"]
        collection_name = model.get_db_collection()
        collection = self.get_collection(collection_name)

        try:
            result = await force_async(collection.add)(data, _id)
        except Exception:
            raise DatabaseError("Document with id: {} already exists", _id)

        LOG.info("Insert Result: {}", result[1].id)

        return WriteResult(transform_results=[result[1].id])

    async def count(self, model: Type[DocumentDBModel], session: Any = None) -> int:

        collection_name = model.get_db_collection()
        collection = self.get_collection(collection_name)
        docs = await force_async(collection.list_documents)()

        return len(docs)

    async def delete(
        self, model: Type[DocumentDBModel], _id: str, session: Any = None
    ) -> DeleteResult:

        collection_name = model.get_db_collection()
        collection = self.get_collection(collection_name)
        doc_ref = collection.document(_id)
        try:
            timestamp = await force_async(doc_ref.delete)()
            LOG.info(f"User deleted at {timestamp}")
            return DeleteResult()
        except NotFound as exc:
            LOG.warning(f"Error deleting user {_id} from firestore, user not found")
            raise exc

    async def update_one(
        self, model: Type[DocumentDBModel], _id: str, data: dict, session: Any = None
    ) -> WriteResult:

        collection_name = model.get_db_collection()
        collection = self.get_collection(collection_name)
        await force_async(collection.document(_id).update)(data)
        return WriteResult()

    async def update_many(
        self, model: Type[DocumentDBModel], data: List[Tuple[str, dict]]
    ) -> WriteResult:

        collection_name = model.get_db_collection()
        collection = self.get_collection(collection_name)

        batch = self.firestore.batch()
        for _id, _data in data:
            doc_ref = collection.document(_id)

            batch.update(doc_ref, field_updates=_data)
        await force_async(batch.commit)()

        return WriteResult()

    async def get(
        self, model: Type[DocumentDBModel], _id: str, session: Any = None
    ) -> Optional[DocumentDBModel]:

        collection_name = model.get_db_collection()
        collection = self.get_collection(collection_name)

        result = await force_async(collection.document(_id).get)()

        if not result.exists:
            return None

        return model(**result.to_dict())

    async def find_one(
        self,
        model: Type[DocumentDBModel],
        where: List[WhereCondition] = [],
        session: Any = None,
    ) -> Optional[DocumentDBModel]:

        collection_name = model.get_db_collection()
        collection = self.get_collection(collection_name)
        query_ref = collection
        for wc in where:
            query_ref = query_ref.where(wc.field, wc.operator, wc.value)
        query_ref.limit(1)

        result = await force_async(query_ref.stream)()

        for res in result:
            LOG.debug("Find One Result: {}", res.to_dict())
            item = model(**res.to_dict())
            item.id = res.id
            return item

        return None

    async def list(
        self,
        model: Type[DocumentDBModel],
        where: List[WhereCondition] = [],
        _limit: int = 0,
        _sort: List[Tuple[str, SortOrder]] = None,
        mongo_offset: int = 0,
        fire_offset: FireOffset = None,
        session: Any = None,
    ) -> List[DocumentDBModel]:

        collection_name = model.get_db_collection()
        collection = self.get_collection(collection_name)
        offset_value = None
        if fire_offset is not None:
            if fire_offset.start_id is not None:
                offset_value = await force_async(
                    collection.document(fire_offset.start_id).get
                )()
            else:
                offset_value = fire_offset.start_fields
        query_ref = collection
        for wc in where:
            query_ref = query_ref.where(wc.field, wc.operator, wc.value)
        if _sort is not None:
            for s in _sort:
                direction = (
                    Query.DESCENDING if s is SortOrder.DESCENDING else Query.ASCENDING
                )
                query_ref = query_ref.order_by(s[0], direction=direction)
        if offset_value is not None:
            if fire_offset.start_at:  # type: ignore
                query_ref = query_ref.start_at(offset_value)
            else:
                query_ref = query_ref.start_after(offset_value)
        if _limit > 0:
            query_ref = query_ref.limit(_limit)

        results = await force_async(collection.stream)()

        models: List[DocumentDBModel] = []
        for res in results:

            models.append(model(**res.to_dict()))
        return models

    async def create_indexes(self, index=List[DBIndex]) -> Optional[List[str]]:
        return None
