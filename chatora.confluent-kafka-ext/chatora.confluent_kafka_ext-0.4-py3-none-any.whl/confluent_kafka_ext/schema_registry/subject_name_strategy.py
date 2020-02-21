__all__ = (
    'BaseSubjectNameStrategy',
    'TopicNameStrategy',
    'RecordNameStrategy',
    'TopicRecordNameStrategy',
    'TOPIC_NAME_STRATEGY',
    'RECORD_NAME_STRATEGY',
    'TOPIC_RECORD_NAME_STRATEGY',
)

import abc

from chatora.confluent_kafka_ext.exception import SubjectNameStrategyException
from chatora.confluent_kafka_ext.schema.base import BaseAvroSchema


class BaseSubjectNameStrategy(metaclass=abc.ABCMeta):

    __slots__ = ()

    def __reduce__(self):
        # when unpickled, refers to the marker (singleton)
        return self.__name__

    def __str__(self):
        return f'<{self.__module__}.{self.__name__}>'

    def __eq__(self, other):
        return type(self) is type(other)

    def __hash__(self):
        return hash(type(self))

    def __ne__(self, other):
        return type(self) is not type(other)

    def __bool__(self):
        return True

    @abc.abstractmethod
    def get_key_subject_name(
        self,
        topic: str,
        schema: BaseAvroSchema,
    ) -> str:
        raise NotImplementedError()

    @abc.abstractmethod
    def get_value_subject_name(
        self,
        topic: str,
        schema: BaseAvroSchema,
    ) -> str:
        raise NotImplementedError()

    def get_subject_name(
        self,
        topic: str,
        schema: BaseAvroSchema,
        is_key: bool,
    ):
        if is_key is True:
            return self.get_key_subject_name(topic=topic, schema=schema)
        else:
            return self.get_value_subject_name(topic=topic, schema=schema)


class TopicNameStrategy(BaseSubjectNameStrategy):

    __slots__ = ()
    __name__ = 'TOPIC_NAME_STRATEGY'

    def get_key_subject_name(
        self,
        topic: str,
        schema: BaseAvroSchema,
    ) -> str:
        if not topic:
            raise SubjectNameStrategyException('topic MUST be set.', topic=topic, schema=schema)
        return f'{topic}-key'

    def get_value_subject_name(
        self,
        topic: str,
        schema: BaseAvroSchema,
    ) -> str:
        if not topic:
            raise SubjectNameStrategyException('topic MUST be set.', topic=topic, schema=schema)
        return f'{topic}-value'


TOPIC_NAME_STRATEGY = TopicNameStrategy()


class RecordNameStrategy(BaseSubjectNameStrategy):

    __slots__ = ()
    __name__ = 'RECORD_NAME_STRATEGY'

    def get_key_subject_name(
        self,
        topic: str,
        schema: BaseAvroSchema,
    ) -> str:
        return schema.fullname

    get_value_subject_name = get_key_subject_name


RECORD_NAME_STRATEGY = RecordNameStrategy()


class TopicRecordNameStrategy(BaseSubjectNameStrategy):

    __slots__ = ()
    __name__ = 'TOPIC_RECORD_NAME_STRATEGY'

    def get_key_subject_name(
        self,
        topic: str,
        schema: BaseAvroSchema,
    ) -> str:
        if not topic:
            raise SubjectNameStrategyException('topic MUST be set.', topic=topic, schema=schema)
        return f'{topic}-{schema.fullname}'

    get_value_subject_name = get_key_subject_name


TOPIC_RECORD_NAME_STRATEGY = TopicRecordNameStrategy()
