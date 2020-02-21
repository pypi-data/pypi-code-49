__all__ = (
    'BaseKafkaException',
    'BaseKafkaTransientException',
    'SubjectNameStrategyException',
    'SchemaRegistryClientError',
    'SchemaRegistryRequestException',
    'SchemaRegistryUnknownException',
    'SchemaRegistryUnknownServerException',
    'SchemaRegistryUnknownClientException',
    'SchemaRegistryIncompatibleAvroSchemaException',
    'SchemaRegistrySubjectNotFoundException',
    'SchemaRegistryVersionNotFoundException',
    'SchemaRegistrySchemaNotFoundException',
    'SchemaRegistryInvalidAvroSchemaException',
    'SchemaRegistryInvalidVersionException',
    'SchemaRegistryInvalidCompatibilityLevelException',
    'SchemaRegistryBackendStoreException',
    'SchemaRegistryOperationTimeoutException',
    'SchemaRegistryRequestForwardException',
    'SchemaRegistryUnknownMasterException',
    'AvroCodecException',
    'AvroEncodeException',
    'AvroRecordEncodeException',
    'AvroDecodeException',
    'AvroRecordDecodeException',
)

import typing

import structlog

if typing.TYPE_CHECKING:
    from chatora.confluent_kafka_ext.schema.base import BaseAvroSchema


logger = structlog.get_logger(__name__)


class BaseKafkaException(Exception):

    def __init__(
        self,
        description: str,
        *args
    ) -> None:
        self.description = description
        super().__init__(description, *args)
        return

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}(' \
               f'description={self.description},' \
               f')'


class BaseKafkaTransientException(BaseKafkaException):
    pass


class SubjectNameStrategyException(BaseKafkaException, ValueError):

    def __init__(
        self,
        description: str,
        topic: str,
        schema: 'BaseAvroSchema',
        *args,
    ) -> None:
        self.topic = topic
        self.schema = schema
        super().__init__(description=description, *args)
        return


class SchemaRegistryClientError:
    """ Error thrown by Schema Registry clients """

    @classmethod
    def init(
        cls,
        description: str,
        url: str,
        http_method: str,
        http_status_code: typing.Optional[int] = None,
        schema_registry_error_code: typing.Optional[int] = None,
        schema_registry_message: typing.Optional[str] = None,
    ) -> 'SchemaRegistryClientError':
        if http_status_code is None:
            klass = SchemaRegistryRequestException
        elif http_status_code == 409:
            klass = SchemaRegistryIncompatibleAvroSchemaException
        else:
            try:
                klass = _SCHEMA_REGISTRY_EXC_MAP[http_status_code][schema_registry_error_code]
            except KeyError:
                if 400 <= http_status_code < 500:
                    klass = SchemaRegistryUnknownClientException
                elif 500 <= http_status_code < 600:
                    klass = SchemaRegistryUnknownServerException
                else:
                    klass = SchemaRegistryUnknownException
        return klass(
            description=description,
            url=url,
            http_method=http_method,
            http_status_code=http_status_code,
            schema_registry_error_code=schema_registry_error_code,
            schema_registry_message=schema_registry_message,
        )

    def __init__(
        self,
        description: str,
        url: str,
        http_method: str,
        http_status_code: typing.Optional[int] = None,
        schema_registry_error_code: typing.Optional[int] = None,
        schema_registry_message: typing.Optional[str] = None,
    ) -> None:
        self.url = url
        self.http_method = http_method
        self.http_status_code = http_status_code
        self.schema_registry_error_code = schema_registry_error_code
        self.schema_registry_message = schema_registry_message
        super().__init__(description)
        return

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}(' \
               f'description={self.description},' \
               f'url={self.url},' \
               f'http_method={self.http_method},' \
               f'http_status_code={self.http_status_code}' \
               f'schema_registry_error_code={self.schema_registry_error_code}' \
               f'schema_registry_message={self.schema_registry_message}' \
               f')'


class SchemaRegistryRequestException(
    SchemaRegistryClientError,
    BaseKafkaTransientException,
):
    pass


class SchemaRegistryUnknownException(
    SchemaRegistryClientError,
    BaseKafkaException,
):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        if self.schema_registry_error_code is not None:
            logger.warning(
                f'unknown schema_registry_error_code ({self.schema_registry_error_code}) found',
                exc=self,
            )
        return


class SchemaRegistryUnknownServerException(
    SchemaRegistryUnknownException,
):
    pass


class SchemaRegistryUnknownClientException(
    SchemaRegistryUnknownException,
):
    pass


class SchemaRegistryIncompatibleAvroSchemaException(
    SchemaRegistryClientError,
    BaseKafkaException,
):
    pass


class SchemaRegistrySubjectNotFoundException(
    SchemaRegistryClientError,
    BaseKafkaException,
):
    pass


class SchemaRegistryVersionNotFoundException(
    SchemaRegistryClientError,
    BaseKafkaException,
):
    pass


class SchemaRegistrySchemaNotFoundException(
    SchemaRegistryClientError,
    BaseKafkaException,
):
    pass


class SchemaRegistryInvalidAvroSchemaException(
    SchemaRegistryClientError,
    BaseKafkaException,
):
    pass


class SchemaRegistryInvalidVersionException(
    SchemaRegistryClientError,
    BaseKafkaException,
):
    pass


class SchemaRegistryInvalidCompatibilityLevelException(
    SchemaRegistryClientError,
    BaseKafkaException,
):
    pass


class SchemaRegistryBackendStoreException(
    SchemaRegistryClientError,
    BaseKafkaTransientException,
):
    pass


class SchemaRegistryOperationTimeoutException(
    SchemaRegistryClientError,
    BaseKafkaTransientException,
):
    pass


class SchemaRegistryRequestForwardException(
    SchemaRegistryClientError,
    BaseKafkaTransientException,
):
    pass


class SchemaRegistryUnknownMasterException(
    SchemaRegistryClientError,
    BaseKafkaTransientException,
):
    pass


_SCHEMA_REGISTRY_EXC_MAP: typing.Mapping[int, typing.Mapping[int, typing.Type[SchemaRegistryClientError]]] = {
    404: {
        40401: SchemaRegistrySubjectNotFoundException,
        40402: SchemaRegistryVersionNotFoundException,
        40403: SchemaRegistrySchemaNotFoundException,
    },
    422: {
        42201: SchemaRegistryInvalidAvroSchemaException,
        42202: SchemaRegistryInvalidVersionException,
        42203: SchemaRegistryInvalidCompatibilityLevelException,
    },
    500: {
        50001: SchemaRegistryBackendStoreException,
        50002: SchemaRegistryOperationTimeoutException,
        50003: SchemaRegistryRequestForwardException,
        50004: SchemaRegistryUnknownMasterException,
    }
}


class AvroCodecException(BaseKafkaException):

    def __init__(
        self,
        description: str,
        *args
    ) -> None:
        self.description = description
        super().__init__(description, *args)
        return


class AvroEncodeException(AvroCodecException):

    def __init__(
        self,
        description: str,
        value: typing.Any,
        schema: typing.Optional['BaseAvroSchema'],
    ):
        self.schema = schema
        self.value = value
        super().__init__(description)
        return


class AvroRecordEncodeException(AvroCodecException):

    def __init__(
        self,
        description: str,
        key: typing.Any,
        value: typing.Any,
        key_schema: typing.Optional['BaseAvroSchema'],
        value_schema: typing.Optional['BaseAvroSchema'],
    ):
        self.key = key
        self.value = value
        self.key_schema = key_schema
        self.value_schema = value_schema
        super().__init__(description)
        return


class AvroDecodeException(AvroCodecException):

    def __init__(
        self,
        description: str,
        value: typing.Optional[bytes],
        schema: typing.Optional['BaseAvroSchema'],
    ):
        self.schema = schema
        self.value = value
        super().__init__(description)
        return


class AvroRecordDecodeException(AvroCodecException):

    def __init__(
        self,
        description: str,
        key: typing.Optional[bytes],
        value: typing.Optional[bytes],
        key_schema: typing.Optional['BaseAvroSchema'],
        value_schema: typing.Optional['BaseAvroSchema'],
    ):
        self.key = key
        self.value = value
        self.key_schema = key_schema
        self.value_schema = value_schema
        super().__init__(description)
        return
