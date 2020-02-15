import abc
import enum
import typing

import aenum
from anji_orm import orm_register, extensions, core
from anji_orm.core.model import FIELD_CLASS_SELECTION_HOOK, Model
from anji_orm.core.fields.base import DICT_ORIGIN

from .data_model import FileRecord, FileDictProxy
from .fields import (
    FileField, FileDictField,
    FILE_FIELD_MARK, FILE_DICT_FIELD_MARK
)

__author__ = "Bogdan Gladyshev"
__copyright__ = "Copyright 2017, Bogdan Gladyshev"
__credits__ = ["Bogdan Gladyshev"]
__license__ = "MIT"
__version__ = "0.11.7"
__maintainer__ = "Bogdan Gladyshev"
__email__ = "siredvin.dark@gmail.com"
__status__ = "Production"
__all__ = ['FileExtensionProtocol', 'AbstractFileExtension']


def file_field_selection_listener(attr, attr_type) -> typing.Optional[typing.Tuple[FileField, int]]:
    if attr_type is FileRecord:
        return FileField(default=attr), 100
    return None


def file_dict_field_selection_listener(attr, attr_type) -> typing.Optional[typing.Tuple[FileDictField, int]]:  # pylint: disable=invalid-name
    if hasattr(attr_type, '__origin__') and attr_type.__origin__ is DICT_ORIGIN and attr_type.__args__[1] is FileRecord:
        return FileDictField(default=attr), 100
    return None


def file_field_predicate(record):
    return bool(record._field_marks.get(FILE_FIELD_MARK, False))


def file_dict_field_predicate(record):
    return bool(record._field_marks.get(FILE_DICT_FIELD_MARK, False))


def file_extensions_predicate(record):
    return 'file' in record._used_extensions


FIELD_CLASS_SELECTION_HOOK.add_callback(file_field_selection_listener)
FIELD_CLASS_SELECTION_HOOK.add_callback(file_dict_field_selection_listener)


class FileExtensionProtocol(aenum.Enum):

    couchdb = 'anji_orm.extensions.files.couchdb.CouchDBFileExtension'
    disk = 'anji_orm.extensions.files.disk.DiskFileExtension'
    minio = 'anji_orm.extensions.files.minio.MinioFileExtension'
    miniossl = 'anji_orm.extensions.files.minio.MinioFileExtension'


class FileActionEnum(enum.Enum):

    upload = 'upload'
    delete = 'delete'


class AbstractFileExtension(extensions.BaseExtension):

    __slots__ = ()

    @staticmethod
    def _unqlite_serialize_file_record(value: typing.Dict):
        if value is not None and 'name' in value and value['name'] is not None:
            value['name'] = value['name'].encode('utf-8')
        return value

    @staticmethod
    def _unqlite_deserialize_file_record(value: typing.Dict, _result_type):
        if value is not None and 'name' in value and value['name'] is not None:
            value['name'] = value['name'].decode('utf-8')
        return value

    @staticmethod
    def _unqlite_serialize_file_dict(value: typing.Dict):
        if value is not None:
            for key in value:
                value[key] = AbstractFileExtension._unqlite_serialize_file_record(value[key])
        return value

    @staticmethod
    def _unqlite_deserialize_file_dict(value: typing.Dict, _result_type):
        if value is not None:
            for key in value:
                value[key] = AbstractFileExtension._unqlite_deserialize_file_record(value[key], None)
        return value

    @staticmethod
    def update_adapter():
        if orm_register.selected_protocol == core.RegistryProtocol.unqlite:
            orm_register.backend_adapter.register_deserialization(
                FileRecord, AbstractFileExtension._unqlite_deserialize_file_record
            )
            orm_register.backend_adapter.register_serialization(
                FileRecord, AbstractFileExtension._unqlite_serialize_file_record
            )
            orm_register.backend_adapter.register_deserialization(
                typing.Dict[str, FileRecord], AbstractFileExtension._unqlite_deserialize_file_dict
            )
            orm_register.backend_adapter.register_serialization(
                typing.Dict[str, FileRecord], AbstractFileExtension._unqlite_serialize_file_dict
            )

    @staticmethod
    def update_listeners():
        Model.post_async_save.add_callback(
            AbstractFileExtension.async_process_file_field_logic,
            predicate=file_field_predicate
        )
        Model.post_async_save.add_callback(
            AbstractFileExtension.async_process_file_dict_field_logic,
            predicate=file_dict_field_predicate
        )
        Model.post_save.add_callback(
            AbstractFileExtension.process_file_field_logic,
            predicate=file_field_predicate
        )
        Model.post_save.add_callback(
            AbstractFileExtension.process_file_dict_field_logic,
            predicate=file_dict_field_predicate
        )
        Model.post_delete.add_callback(
            AbstractFileExtension.delete_record_handler,
            predicate=file_extensions_predicate
        )
        Model.post_async_delete.add_callback(
            AbstractFileExtension.async_delete_record_handler,
            predicate=file_extensions_predicate
        )

    async def async_load(self):
        self.update_adapter()
        self.update_listeners()

    def load(self):
        self.update_adapter()
        self.update_listeners()

    @abc.abstractmethod
    def upload_file(self, file_record: FileRecord) -> None:
        pass

    @abc.abstractmethod
    async def async_upload_file(self, file_record: FileRecord) -> None:
        pass

    @abc.abstractmethod
    def download_file(self, file_record: FileRecord) -> None:
        pass

    @abc.abstractmethod
    async def async_download_file(self, file_record: FileRecord) -> None:
        pass

    @abc.abstractmethod
    async def async_delete_file(self, file_record: FileRecord) -> None:
        pass

    @abc.abstractmethod
    def delete_file(self, file_record: FileRecord) -> None:
        pass

    @classmethod
    def collect_file_field_actions(cls, record: Model, record_python_id: int) -> typing.List[typing.Tuple[FileActionEnum, FileRecord]]:
        actions = []
        for field_name in record._field_marks.get(FILE_FIELD_MARK, []):
            field: FileField = record._fields.get(field_name)  # type: ignore
            actual_value: FileRecord = getattr(record, field_name)
            if field.value_changed.get(record_python_id, False):
                # cleanup old values
                if record_python_id in field.old_values:
                    for old_value in field.old_values[record_python_id]:
                        actions.append((FileActionEnum.delete, old_value))
                    del field.old_values[record_python_id]
                # upload new value
                if actual_value is not None:
                    actions.append((FileActionEnum.upload, actual_value))
                del field.value_changed[record_python_id]
            else:
                if actual_value is not None and actual_value.changed:
                    actions.append((FileActionEnum.upload, actual_value))
                    actual_value.reset()
        return actions

    @classmethod
    def collect_file_dict_field_actions(cls, record: Model, record_python_id: int) -> typing.List[typing.Tuple[FileActionEnum, FileRecord]]:  # pylint: disable=too-many-branches
        actions = []
        for field_name in record._field_marks.get(FILE_DICT_FIELD_MARK, []):
            field: FileDictField = record._fields.get(field_name)  # type: ignore
            actual_value: FileDictProxy = getattr(record, field_name)
            if field.value_changed.get(record_python_id, False):
                # cleanup old values
                if record_python_id in field.old_values:
                    for old_dict_value in field.old_values[record_python_id]:
                        for old_value in old_dict_value.values():
                            actions.append((FileActionEnum.delete, old_value))
                    del field.old_values[record_python_id]
                # upload new value
                if actual_value is not None:
                    for new_file in actual_value.values():
                        actions.append((FileActionEnum.upload, new_file))
                    actual_value.changed_keys.clear()
                del field.value_changed[record_python_id]
            else:
                if actual_value is not None and actual_value.changed:
                    for changed_key in actual_value.changed_keys:
                        if changed_key in actual_value:
                            file = actual_value[changed_key]
                            actions.append((FileActionEnum.upload, file))
                            file.reset()
                    for old_file in actual_value.old_values:
                        actions.append((FileActionEnum.delete, old_file))
                    for file_name, file in actual_value.items():
                        if file.changed and file_name not in actual_value.changed_keys:
                            actions.append((FileActionEnum.upload, file))
                            file.reset()
                    actual_value.changed_keys.clear()
                    actual_value.old_values.clear()
        return actions

    @classmethod
    async def async_process_file_field_logic(cls, record: Model) -> None:
        actions = cls.collect_file_field_actions(record, id(record))
        for action_enum, value in actions:
            if action_enum is FileActionEnum.upload:
                await orm_register.shared.file_extension.async_upload_file(value)
            elif action_enum is FileActionEnum.delete:
                await orm_register.shared.file_extension.async_delete_file(value)

    @classmethod
    async def async_process_file_dict_field_logic(cls, record: Model) -> None:  # pylint: disable=invalid-name,too-many-branches
        actions = cls.collect_file_dict_field_actions(record, id(record))
        for action_enum, value in actions:
            if action_enum is FileActionEnum.upload:
                await orm_register.shared.file_extension.async_upload_file(value)
            elif action_enum is FileActionEnum.delete:
                await orm_register.shared.file_extension.async_delete_file(value)

    @classmethod
    def process_file_field_logic(cls, record: Model) -> None:
        actions = cls.collect_file_field_actions(record, id(record))
        for action_enum, value in actions:
            if action_enum is FileActionEnum.upload:
                orm_register.shared.file_extension.upload_file(value)
            elif action_enum is FileActionEnum.delete:
                orm_register.shared.file_extension.delete_file(value)

    @classmethod
    def process_file_dict_field_logic(cls, record: Model) -> None:
        actions = cls.collect_file_dict_field_actions(record, id(record))
        for action_enum, value in actions:
            if action_enum is FileActionEnum.upload:
                orm_register.shared.file_extension.upload_file(value)
            elif action_enum is FileActionEnum.delete:
                orm_register.shared.file_extension.delete_file(value)

    @classmethod
    def delete_record_handler(cls, record: Model) -> None:
        for field_name in record._field_marks.get(FILE_FIELD_MARK, []):
            file_record = getattr(record, field_name)
            if file_record:
                orm_register.shared.file_extension.delete_file(file_record)
        for field_name in record._field_marks.get(FILE_DICT_FIELD_MARK, []):
            actual_value: FileDictProxy = getattr(record, field_name)
            if actual_value:
                for file_record in actual_value.values():
                    orm_register.shared.file_extension.delete_file(file_record)

    @classmethod
    async def async_delete_record_handler(cls, record: Model) -> None:
        for field_name in record._field_marks.get(FILE_FIELD_MARK, []):
            file_record = getattr(record, field_name)
            if file_record:
                await orm_register.shared.file_extension.async_delete_file(file_record)
        for field_name in record._field_marks.get(FILE_DICT_FIELD_MARK, []):
            actual_value: FileDictProxy = getattr(record, field_name)
            if actual_value:
                for file_record in actual_value.values():
                    await orm_register.shared.file_extension.async_delete_file(file_record)
