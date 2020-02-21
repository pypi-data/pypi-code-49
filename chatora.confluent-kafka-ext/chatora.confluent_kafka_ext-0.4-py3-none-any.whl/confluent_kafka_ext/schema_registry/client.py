__all__ = (
    'SchemaRegistryClient',
)

from collections.abc import Mapping
import typing

import requests
from requests.adapters import (
    DEFAULT_POOLBLOCK,
    DEFAULT_POOLSIZE,
    HTTPAdapter,
)
from simplejson import dumps as simplejson_dumps
import structlog
from urllib3.util.retry import Retry

from chatora.confluent_kafka_ext.exception import SchemaRegistryClientError
from chatora.confluent_kafka_ext.schema.base import (
    BaseAvroSchema,
    avro_loads
)


logger = structlog.get_logger(__name__)

DEFAULT_HTTP_HEADER: typing.Dict[str, str] = {
    # 'Accept': 'application/vnd.schemaregistry.v1+json, application/vnd.schemaregistry+json, application/json',
    'Accept': 'application/vnd.schemaregistry.v1+json',
}

DEFAULT_HTTP_HEADER_WITH_BODY: typing.Dict[str, str] = {
    'Accept': 'application/vnd.schemaregistry.v1+json',
    'Content-Type': 'application/vnd.schemaregistry.v1+json',
}


class SchemaRegistryClient:

    def __init__(
        self,
        url: str,
        requests_session: typing.Optional[requests.Session] = None,
        requests_pool_connections: int = DEFAULT_POOLSIZE,
        requests_pool_maxsize: int = DEFAULT_POOLSIZE,
        requests_max_retries: Retry = Retry(
            total=100,
            method_whitelist=frozenset(['HEAD', 'TRACE', 'GET', 'PUT', 'OPTIONS', 'DELETE', 'POST']),
            status_forcelist=(500, 502, 503, 504, 509),
            backoff_factor=0.7,
            raise_on_redirect=True,
        ),
        requests_pool_block: bool = DEFAULT_POOLBLOCK,
        ca_location: typing.Union[bool, str] = None,
        cert_location: typing.Optional[str] = None,
        key_location: typing.Optional[str] = None,
    ) -> None:
        self.url = url.rstrip('/')
        if requests_session:
            self.requests_session = requests.Session()
        else:
            self.requests_session = s = requests.Session()
            s.mount(
                prefix=f'{self.url.split(":", 1)[0]}://',
                adapter=HTTPAdapter(
                    pool_connections=requests_pool_connections,
                    pool_maxsize=requests_pool_maxsize,
                    max_retries=requests_max_retries,
                    pool_block=requests_pool_block,
                ),
            )
            if ca_location is not None:
                s.verify = ca_location
            if cert_location is not None and key_location is not None:
                s.cert = (cert_location, key_location)
            elif any((cert_location, key_location)):
                raise ValueError(
                    "Both cert_location and key_location must be set"
                )
        logger.info('[init]', callee=self.__class__, url=url)
        return

    def __del__(self) -> None:
        self.close()
        return

    def __enter__(self) -> 'SchemaRegistryClient':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()
        return

    def close(self) -> None:
        self.requests_session.close()
        logger.info('[close]', callee=self.__class__.close)
        return

    def send_request(
        self,
        url: str,
        method: str = 'GET',
        body: typing.Any = None,
        headers: typing.Optional[str] = None,
    ) -> typing.Any:
        blogger = logger.bind(callee=self.__class__.send_request, url=url, method=method, headers=headers, body=body)
        blogger.debug('[start]')
        try:
            response = self.requests_session.request(
                method=method, url=url, json=body, headers={
                    **(DEFAULT_HTTP_HEADER_WITH_BODY if body else DEFAULT_HTTP_HEADER),
                    **(headers or {})
                },
            )
            http_status_code = response.status_code
        except Exception as _exc:
            exc = SchemaRegistryClientError.init(
                description='http error',
                url=url,
                http_method=method,
            )
            exc.__cause__ = _exc
            blogger.exception('[error]', exc_info=exc)
            raise exc

        try:
            response_obj = response.json()
            _exc_json_decode = None
        except Exception as _exc_json_decode:
            response_obj = {'error_code': None, 'message': None}

        if not 200 <= http_status_code < 300 or (isinstance(response, Mapping) and 'error_code' in response_obj):
            exc = SchemaRegistryClientError.init(
                description='http error',
                url=url,
                http_method=method,
                http_status_code=http_status_code,
                schema_registry_error_code=response_obj.get('error_code'),
                schema_registry_message=response_obj.get('message'),
            )
            exc.__cause__ =_exc_json_decode
            blogger.error('[error]', exc_info=exc)
            raise exc

        blogger.debug('[end]', response_obj=response_obj)
        return response_obj

    def get_schema(
        self,
        schema_id: int,
    ) -> BaseAvroSchema:
        return avro_loads(self.send_request(
            url=f'{self.url}/schemas/ids/{schema_id}',
            method='GET',
        )['schema'])

    def get_subjects(self) -> typing.Tuple[str]:
        return tuple(self.send_request(
            url=f'{self.url}/subjects',
            method='GET',
        ))

    def get_versions_under_subject(
        self,
        subject_name: str,
    ) -> typing.Tuple[int]:
        return tuple(self.send_request(
            url=f'{self.url}/subjects/{subject_name}/versions',
            method='GET',
        ))

    def delete_subject(
        self,
        subject_name: str,
    ) -> typing.Tuple[int]:
        return tuple(self.send_request(
            url=f'{self.url}/subjects/{subject_name}',
            method='DELETE',
        ))

    def get_version_info_under_subject(
        self,
        subject_name: str,
        version: typing.Union[int, str] = 'latest',
    ) -> typing.Dict[str, typing.Any]:
        info = self.send_request(
            url=f'{self.url}/subjects/{subject_name}/versions/{version}',
            method='GET',
        )
        info['schema'] = avro_loads(simplejson_dumps(
            info['schema'],
            ensure_ascii=False,
            separators=(',',':'),
        ))
        return info

    def get_version_schema_under_subject(
        self,
        subject_name: str,
        version: typing.Union[int, str] = 'latest',
    ) -> BaseAvroSchema:
        return avro_loads(simplejson_dumps(
            self.send_request(
                url=f'{self.url}/subjects/{subject_name}/versions/{version}/schema',
                method='GET',
            ),
            ensure_ascii=False,
            separators=(',',':'),
        ))

    def put_schema_under_subject(
        self,
        subject_name: str,
        schema: BaseAvroSchema,
    ) -> typing.Dict[str, int]:
        return self.send_request(
            url=f'{self.url}/subjects/{subject_name}/versions',
            method='POST',
            body={'schema': schema.x_json_str},
        )

    def get_schema_info_under_subject(
        self,
        subject_name: str,
        schema: BaseAvroSchema,
    ) -> typing.Dict[str, typing.Any]:
        info = self.send_request(
            url=f'{self.url}/subjects/{subject_name}',
            method='POST',
            body={'schema': schema.x_json_str},
        )
        info['schema'] = schema
        return info

    def delete_schema_under_subject(
        self,
        subject_name: str,
        version: typing.Union[int, str],
    ) -> int:
        return self.send_request(
            url=f'{self.url}/subjects/{subject_name}/versions/{version}',
            method='DELETE',
        )

    def check_schema_compatibility_under_subject(
        self,
        subject_name: str,
        schema: BaseAvroSchema,
        version: typing.Union[int, str] = 'latest'
    ) -> typing.Dict[str, bool]:
        return self.send_request(
            url=f'{self.url}/compatibility/subjects/{subject_name}/versions/{version}',
            method='POST',
            body={'schema': schema.x_json_str},
        )

    def put_global_config(
        self,
        compatibility: str,
    ) -> typing.Dict[str, typing.Any]:
        return self.send_request(
            url=f'{self.url}/config',
            method='PUT',
            body={'compatibility': compatibility},
        )

    def get_global_config(self) -> typing.Dict[str, typing.Any]:
        return self.send_request(
            url=f'{self.url}/config',
            method='GET',
        )

    def put_subject_config(
        self,
        subject_name: str,
        compatibility: str,
    ) -> typing.Dict[str, typing.Any]:
        return self.send_request(
            url=f'{self.url}/config/{subject_name}',
            method='PUT',
            body={'compatibility': compatibility},
        )

    def get_subject_config(
        self,
        subject_name: str,
    ) -> typing.Dict[str, typing.Any]:
        return self.send_request(
            url=f'{self.url}/config/{subject_name}',
            method='GET',
        )
