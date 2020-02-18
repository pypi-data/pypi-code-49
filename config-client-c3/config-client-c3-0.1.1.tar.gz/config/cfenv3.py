import json
import os
from typing import Any

import attr

from config.cloudfoundry import (
    default_vcap_application,
    default_vcap_services3
)

from glom import glom


@attr.s(slots=True)
class CFenv3:
    vcap_service_prefix = attr.ib(
        type=str,
        default=os.getenv('VCAP_SERVICE_PREFIX', 'p.config-server'),
        validator=attr.validators.instance_of(str)
    )
    vcap_application = attr.ib(
        type=dict,
        default=json.loads(
            os.getenv('VCAP_APPLICATION', default_vcap_application)
        ),
        validator=attr.validators.instance_of(dict)
    )
    vcap_services = attr.ib(
        type=dict,
        default=json.loads(
            os.getenv('VCAP_SERVICES', default_vcap_services3)
        ),
        validator=attr.validators.instance_of(dict)
    )

    def __attrs_post_init__(self) -> None:
        if self.vcap_service_prefix not in self.vcap_services.keys():
            vcap_services_copy = self.vcap_services.copy()
            vcap_services_copy[self.vcap_service_prefix] = vcap_services_copy.pop('p.config-server')
            self.vcap_services = vcap_services_copy

    @property
    def space_name(self) -> Any:
        return glom(self.vcap_application, 'space_name', default='')

    @property
    def organization_name(self) -> Any:
        return glom(self.vcap_application, 'organization_name', default='')

    @property
    def application_name(self) -> Any:
        return glom(self.vcap_application, 'application_name', default='')

    @property
    def uris(self) -> Any:
        return glom(self.vcap_application, 'uris', default=[])

    def credhub_uri(self, vcap_path: str = '.0.credentials.credhub-ref') -> Any:
        path = self._format_vcap_path(vcap_path)
        return glom(self.vcap_services, path, default='')

    def configserver_access_token_uri(self, vcap_path: str = '.0.credentials.uri') -> Any:
        path = self._format_vcap_path(vcap_path)
        return glom(self.vcap_services, path, default='')

    def configserver_client_id(self, vcap_path: str = '.0.credentials.username') -> Any:
        path = self._format_vcap_path(vcap_path)
        return glom(self.vcap_services, path, default='')

    def configserver_client_secret(self, vcap_path: str = '.0.credentials.password') -> Any:
        path = self._format_vcap_path(vcap_path)
        return glom(self.vcap_services, path, default='')

    def _format_vcap_path(self, path) -> str:
        return f"{self.vcap_service_prefix}{path}"
