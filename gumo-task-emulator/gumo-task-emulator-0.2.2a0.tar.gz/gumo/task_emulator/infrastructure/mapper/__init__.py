import json
from injector import inject

from gumo.datastore.infrastructure import DatastoreEntity
from gumo.datastore.infrastructure import EntityKeyMapper
from gumo.task_emulator.domain import GumoTaskProcess
from gumo.task_emulator.domain import ProcessHistory
from gumo.task_emulator.domain import TaskState


class DatastoreGumoProcessHistoryMapper:
    def to_datastore_entity(self, process_history: ProcessHistory) -> DatastoreEntity:
        doc = DatastoreEntity(exclude_from_indexes=[
            "data", "request_headers", "request_body", "response_headers", "response_body", "error_message"
        ])
        doc.update({
            'started_at': process_history.started_at,
            'duration_seconds': process_history.duration_seconds,
            'method': process_history.method,
            'url': process_history.url,
            'data': json.dumps(process_history.data),
            'status_code': process_history.status_code,
            'request_headers': json.dumps(process_history.request_headers),
            'request_body': process_history.request_body,
            'response_headers': json.dumps(process_history.response_headers),
            'response_body': process_history.response_body,
            'error_message': process_history.error_message,
        })
        return doc

    def to_entity(self, doc: dict) -> ProcessHistory:
        return ProcessHistory(
            started_at=doc.get('started_at'),
            duration_seconds=doc.get('duration_seconds'),
            method=doc.get('method'),
            url=doc.get('url'),
            data=json.loads(doc.get('data')),
            status_code=doc.get('status_code'),
            request_headers=json.loads(doc.get('request_headers')),
            request_body=doc.get('request_body'),
            response_headers=json.loads(doc.get('response_headers')),
            response_body=doc.get('response_body'),
            error_message=doc.get('error_message'),
        )


class DatastoreGumoTaskProcessMapper:
    @inject
    def __init__(
            self,
            entity_key_mapper: EntityKeyMapper,
            process_history_mapper: DatastoreGumoProcessHistoryMapper,
    ):
        self._entity_key_mapper = entity_key_mapper
        self._process_history_mapper = process_history_mapper

    def to_datastore_entity(self, task_process: GumoTaskProcess) -> DatastoreEntity:
        entity = DatastoreEntity(
            key=self._entity_key_mapper.to_datastore_key(entity_key=task_process.key),
            exclude_from_indexes=["payload"]
        )
        entity.update({
            'relative_uri': task_process.relative_uri,
            'method': task_process.method,
            'payload': task_process.payload,
            'headers': task_process.headers,
            'schedule_time': task_process.schedule_time,
            'created_at': task_process.created_at,
            'updated_at': task_process.updated_at,
            'queue_name': task_process.queue_name,
            'state': task_process.state.value,
            'attempts': task_process.attempts,
            'last_run_at': task_process.last_run_at,
            'run_at': task_process.run_at,
            'locked_at': task_process.locked_at,
            'succeeded_at': task_process.succeeded_at,
            'failed_at': task_process.failed_at,
            'histories': [
                self._process_history_mapper.to_datastore_entity(history) for history in task_process.histories
            ],
        })
        return entity

    def to_entity(self, datastore_entity: DatastoreEntity) -> GumoTaskProcess:
        key = self._entity_key_mapper.to_entity_key(datastore_entity.key)
        return GumoTaskProcess(
            key=key,
            relative_uri=datastore_entity.get('relative_uri'),
            method=datastore_entity.get('method'),
            payload=datastore_entity.get('payload'),
            headers=datastore_entity.get('headers'),
            schedule_time=datastore_entity.get('schedule_time'),
            created_at=datastore_entity.get('created_at'),
            updated_at=datastore_entity.get('updated_at'),
            queue_name=datastore_entity.get('queue_name'),
            state=TaskState.get(datastore_entity.get('state')),
            attempts=datastore_entity.get('attempts'),
            last_run_at=datastore_entity.get('last_run_at'),
            run_at=datastore_entity.get('run_at'),
            locked_at=datastore_entity.get('locked_at'),
            succeeded_at=datastore_entity.get('succeeded_at'),
            failed_at=datastore_entity.get('failed_at'),
            histories=[
                self._process_history_mapper.to_entity(history) for history in datastore_entity.get('histories')
            ],
        )
