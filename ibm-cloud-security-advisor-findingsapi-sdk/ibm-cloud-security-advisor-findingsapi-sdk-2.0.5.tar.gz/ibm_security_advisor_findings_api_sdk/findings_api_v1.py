# coding: utf-8

# (C) Copyright IBM Corp. 2020.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
The Findings API
"""

import json
from ibm_cloud_sdk_core.authenticators.authenticator import Authenticator
from ibm_security_advisor_findings_api_sdk.common import get_sdk_headers
from datetime import datetime
from enum import Enum
from ibm_cloud_sdk_core import BaseService
from ibm_cloud_sdk_core import datetime_to_string, string_to_datetime
from ibm_cloud_sdk_core import read_external_sources, DetailedResponse
from ibm_cloud_sdk_core.get_authenticator import get_authenticator_from_environment
from typing import Dict
from typing import List
import sys

##############################################################################
# Service
##############################################################################

class FindingsApiV1(BaseService):
    """The Findings API V1 service."""

    DEFAULT_SERVICE_URL = 'https://gateway.watsonplatform.net/findings'
    DEFAULT_SERVICE_NAME = 'findings_api'

    @classmethod
    def new_instance(cls, 
                     service_name: str = DEFAULT_SERVICE_NAME,
                    ) -> 'FindingsApiV1':
        authenticator = get_authenticator_from_environment(service_name)
        service = cls(
            authenticator,
            )
        service.configure_service(service_name)
        return service

    def __init__(self,
                 authenticator: Authenticator = None,
                 service_name: str = DEFAULT_SERVICE_NAME,
                ) -> None:
        """
        Construct a new client for the Findings API service.

        :param Authenticator authenticator: The authenticator specifies the authentication mechanism.
               Get up to date information from https://github.com/IBM/python-sdk-core/blob/master/README.md
               about initializing the authenticator of your choice.
        """
        BaseService.__init__(self,
            service_url=self.DEFAULT_SERVICE_URL,
            authenticator=authenticator,
            disable_ssl_verification=False)


    #########################
    # findingsGraph
    #########################


    def post_graph(self, account_id: str, body: str, *, content_type: str = None, **kwargs) -> 'DetailedResponse':
        """
        Query findings.

        :param str account_id: Account ID.
        :param str body: Body for query findings.
        :param str content_type: (optional) The type of the input.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if account_id is None:
            raise ValueError('account_id must be provided')
        if body is None:
            raise ValueError('body must be provided')

        headers = {
            'Content-Type': content_type
        }
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME, service_version='V1', operation_id='post_graph')
        headers.update(sdk_headers)

        if content_type == 'application/json' and isinstance(body, dict):
            data = json.dumps(body)
        else:
            data = body

        url = '/v1/{0}/graph'.format(*self._encode_path_vars(account_id))
        request = self.prepare_request(method='POST',
                                url=url,
                                headers=headers,
                                data=data)

        response = self.send(request)
        return response

    #########################
    # findingsNotes
    #########################


    def create_note(self, account_id: str, provider_id: str, short_description: str, long_description: str, kind: 'ApiNoteKind', id: str, reported_by: 'Reporter', *, name: str = None, related_url: List['ApiNoteRelatedUrl'] = None, expiration_time: datetime = None, create_time: datetime = None, update_time: datetime = None, shared: bool = None, finding: 'FindingType' = None, kpi: 'KpiType' = None, card: 'Card' = None, section: 'Section' = None, **kwargs) -> 'DetailedResponse':
        """
        Creates a new `Note`.

        :param str account_id: Account ID.
        :param str provider_id: Part of `parent`. This field contains the
               provider_id for example: providers/{provider_id}.
        :param str short_description: A one sentence description of this
               `Note`.
        :param str long_description: A detailed description of this `Note`.
        :param ApiNoteKind kind: Output only. This explicitly denotes which
               kind of note is specified. This
               field can be used as a filter in list requests.
                kind could be -
                    - FINDING
                    - KPI
                    - CARD
                    - CARD_CONFIGURED
                    - SECTION
                example:
                kind="FINDING"

        :param str id:
        :param Reporter reported_by: Details about the reporter of this `Note`.
                example-
                reported_by={'id':'1','title':'test1','url':'www.test.com'},
        :param str name: (optional)
        :param List[ApiNoteRelatedUrl] related_url: (optional)
        :param datetime expiration_time: (optional) Time of expiration for this
               note, null if note does not expire.
        :param datetime create_time: (optional) Output only. The time this note
               was created. This field can be used as a filter in list requests.
        :param datetime update_time: (optional) Output only. The time this note
               was last updated. This field can be used as a filter in list requests.
        :param bool shared: (optional) True if this `Note` can be shared by
               multiple accounts.
        :param FindingType finding: (optional) The finding details of the note.
                example -
                finding={
                    "severity": "LOW",
                    "next_steps": [
                        {
                            "title": "string",
                            "url": "string"
                        }
                    ]
                }
        :param KpiType kpi: (optional) The KPI details of the note.
                example -
                kpi={
                    "aggregation_type":"SUM",
                }
        :param Card card: (optional) The card details of the note.
                example -
                card={
                    "elements": [
                        {
                        "default_time_range": "1d",
                        "kind": "NUMERIC",
                        "text": "Count of findings reported by my security tool",
                        "value_type": {
                            "finding_note_names": [
                            "providers/sdktest/notes/sdk_note_name1"
                            ],
                            "kind": "FINDING_COUNT"
                        }
                        }
                    ],
                    "finding_note_names": [
                        "providers/sdktest/notes/sdk_note_name1"
                    ],
                    "section": "My Security Tools",
                    "order": 1,
                    "title": "My Security Tool Findings",
                    "subtitle": "My Security Tool",
                }
        :param Section section: (optional) The section details of the note.
                example - 
                section={
                    "title":"s1",
                    "image":"s1img"
                }
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if account_id is None:
            raise ValueError('account_id must be provided')
        if provider_id is None:
            raise ValueError('provider_id must be provided')
        if short_description is None:
            raise ValueError('short_description must be provided')
        if long_description is None:
            raise ValueError('long_description must be provided')
        if kind is None:
            raise ValueError('kind must be provided')
        if id is None:
            raise ValueError('id must be provided')
        if reported_by is None:
            raise ValueError('reported_by must be provided')
        #kind = self._convert_model(kind)
        reported_by = self._convert_model(reported_by)
        if related_url is not None:
            related_url = [ self._convert_model(x) for x in related_url ]
        if finding is not None:
            finding = self._convert_model(finding)
        if kpi is not None:
            kpi = self._convert_model(kpi)
        if card is not None:
            card = self._convert_model(card)
        if section is not None:
            section = self._convert_model(section)

        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME, service_version='V1', operation_id='create_note')
        headers.update(sdk_headers)

        data = {
            'short_description': short_description,
            'long_description': long_description,
            'kind': kind,
            'id': id,
            'reported_by': reported_by,
            'name': name,
            'related_url': related_url,
            'provider_id': provider_id,
            'shared': shared,
            'finding': finding,
            'kpi': kpi,
            'card': card,
            'section': section
        }
        if expiration_time != None :
            data.expiration_time = expiration_time.__str__()
        if create_time != None :
            data.create_time = create_time.__str__()   
        if update_time != None :
            data.update_time = update_time.__str__()


        url = '/v1/{0}/providers/{1}/notes'.format(*self._encode_path_vars(account_id, provider_id))
        request = self.prepare_request(method='POST',
                                url=url,
                                headers=headers,
                                data=data)

        response = self.send(request)
        return response


    def list_notes(self, account_id: str, provider_id: str, *, page_size: int = None, page_token: str = None, **kwargs) -> 'DetailedResponse':
        """
        Lists all `Notes` for a given provider.

        :param str account_id: Account ID.
        :param str provider_id: Part of `parent`. This field contains the
               provider_id for example: providers/{provider_id}.
        :param int page_size: (optional) Number of notes to return in the list.
        :param str page_token: (optional) Token to provide to skip to a particular
               spot in the list.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if account_id is None:
            raise ValueError('account_id must be provided')
        if provider_id is None:
            raise ValueError('provider_id must be provided')

        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME, service_version='V1', operation_id='list_notes')
        headers.update(sdk_headers)

        params = {
            'page_size': page_size,
            'page_token': page_token
        }

        url = '/v1/{0}/providers/{1}/notes'.format(*self._encode_path_vars(account_id, provider_id))
        request = self.prepare_request(method='GET',
                                url=url,
                                headers=headers,
                                params=params)

        response = self.send(request)
        return response


    def get_note(self, account_id: str, provider_id: str, note_id: str, **kwargs) -> 'DetailedResponse':
        """
        Returns the requested `Note`.

        :param str account_id: Account ID.
        :param str provider_id: First part of note `name`:
               providers/{provider_id}/notes/{note_id}.
        :param str note_id: Second part of note `name`:
               providers/{provider_id}/notes/{note_id}.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if account_id is None:
            raise ValueError('account_id must be provided')
        if provider_id is None:
            raise ValueError('provider_id must be provided')
        if note_id is None:
            raise ValueError('note_id must be provided')

        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME, service_version='V1', operation_id='get_note')
        headers.update(sdk_headers)

        url = '/v1/{0}/providers/{1}/notes/{2}'.format(*self._encode_path_vars(account_id, provider_id, note_id))
        request = self.prepare_request(method='GET',
                                url=url,
                                headers=headers)

        response = self.send(request)
        return response


    def update_note(self, account_id: str, provider_id: str, note_id: str, short_description: str, long_description: str, kind: 'ApiNoteKind', id: str, reported_by: 'Reporter', *, name: str = None, related_url: List['ApiNoteRelatedUrl'] = None, expiration_time: datetime = None, create_time: datetime = None, update_time: datetime = None, shared: bool = None, finding: 'FindingType' = None, kpi: 'KpiType' = None, card: 'Card' = None, section: 'Section' = None, **kwargs) -> 'DetailedResponse':
        """
        Updates an existing `Note`.

        :param str account_id: Account ID.
        :param str provider_id: First part of note `name`:
               providers/{provider_id}/notes/{note_id}.
        :param str note_id: Second part of note `name`:
               providers/{provider_id}/notes/{note_id}.
        :param str short_description: A one sentence description of this
               `Note`.
        :param str long_description: A detailed description of this `Note`.
        :param ApiNoteKind kind: Output only. This explicitly denotes which
               kind of note is specified. This
               field can be used as a filter in list requests.
               kind could be -
                    - FINDING
                    - KPI
                    - CARD
                    - CARD_CONFIGURED
                    - SECTION
                example:
                kind="FINDING"
        :param str id:
        :param Reporter reported_by: Details about the reporter of this `Note`.
                example-
                reported_by={'id':'1','title':'test1','url':'www.test.com'},
        :param str name: (optional)
        :param List[ApiNoteRelatedUrl] related_url: (optional)
        :param datetime expiration_time: (optional) Time of expiration for this
               note, null if note does not expire.
        :param datetime create_time: (optional) Output only. The time this note
               was created. This field can be used as a filter in list requests.
        :param datetime update_time: (optional) Output only. The time this note
               was last updated. This field can be used as a filter in list requests.
        :param bool shared: (optional) True if this `Note` can be shared by
               multiple accounts.
        :param FindingType finding: (optional) The finding details of the note.
                example -
                finding={
                    "severity": "LOW",
                    "next_steps": [
                        {
                            "title": "string",
                            "url": "string"
                        }
                    ]
                }
        :param KpiType kpi: (optional) The KPI details of the note.
                example -
                kpi={
                    "aggregation_type":"SUM",
                }
        :param Card card: (optional) The card details of the note.
                example -
                card={
                    "elements": [
                        {
                        "default_time_range": "1d",
                        "kind": "NUMERIC",
                        "text": "Count of findings reported by my security tool",
                        "value_type": {
                            "finding_note_names": [
                            "providers/sdktest/notes/sdk_note_name1"
                            ],
                            "kind": "FINDING_COUNT"
                        }
                        }
                    ],
                    "finding_note_names": [
                        "providers/sdktest/notes/sdk_note_name1"
                    ],
                    "section": "My Security Tools",
                    "order": 1,
                    "title": "My Security Tool Findings",
                    "subtitle": "My Security Tool",
                }
        :param Section section: (optional) The section details of the note.
                example - 
                section={
                    "title":"s1",
                    "image":"s1img"
                }
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if account_id is None:
            raise ValueError('account_id must be provided')
        if provider_id is None:
            raise ValueError('provider_id must be provided')
        if note_id is None:
            raise ValueError('note_id must be provided')
        if short_description is None:
            raise ValueError('short_description must be provided')
        if long_description is None:
            raise ValueError('long_description must be provided')
        if kind is None:
            raise ValueError('kind must be provided')
        if id is None:
            raise ValueError('id must be provided')
        if reported_by is None:
            raise ValueError('reported_by must be provided')
        #kind = self._convert_model(kind)
        reported_by = self._convert_model(reported_by)
        if related_url is not None:
            related_url = [ self._convert_model(x) for x in related_url ]
        if finding is not None:
            finding = self._convert_model(finding)
        if kpi is not None:
            kpi = self._convert_model(kpi)
        if card is not None:
            card = self._convert_model(card)
        if section is not None:
            section = self._convert_model(section)

        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME, service_version='V1', operation_id='update_note')
        headers.update(sdk_headers)

        data = {
            'short_description': short_description,
            'long_description': long_description,
            'kind': kind,
            'id': id,
            'reported_by': reported_by,
            'name': name,
            'related_url': related_url,
            'provider_id': provider_id,
            'shared': shared,
            'finding': finding,
            'kpi': kpi,
            'card': card,
            'section': section
        }

        if expiration_time != None :
            data.expiration_time = expiration_time.__str__()
        if create_time != None :
            data.create_time = create_time.__str__()   
        if update_time != None :
            data.update_time = update_time.__str__()

        url = '/v1/{0}/providers/{1}/notes/{2}'.format(*self._encode_path_vars(account_id, provider_id, note_id))
        request = self.prepare_request(method='PUT',
                                url=url,
                                headers=headers,
                                data=data)

        response = self.send(request)
        return response


    def delete_note(self, account_id: str, provider_id: str, note_id: str, **kwargs) -> 'DetailedResponse':
        """
        Deletes the given `Note` from the system.

        :param str account_id: Account ID.
        :param str provider_id: First part of note `name`:
               providers/{provider_id}/notes/{note_id}.
        :param str note_id: Second part of note `name`:
               providers/{provider_id}/notes/{note_id}.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if account_id is None:
            raise ValueError('account_id must be provided')
        if provider_id is None:
            raise ValueError('provider_id must be provided')
        if note_id is None:
            raise ValueError('note_id must be provided')

        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME, service_version='V1', operation_id='delete_note')
        headers.update(sdk_headers)

        url = '/v1/{0}/providers/{1}/notes/{2}'.format(*self._encode_path_vars(account_id, provider_id, note_id))
        request = self.prepare_request(method='DELETE',
                                url=url,
                                headers=headers)

        response = self.send(request)
        return response


    def get_occurrence_note(self, account_id: str, provider_id: str, occurrence_id: str, **kwargs) -> 'DetailedResponse':
        """
        Gets the `Note` attached to the given `Occurrence`.

        :param str account_id: Account ID.
        :param str provider_id: First part of occurrence `name`:
               providers/{provider_id}/occurrences/{occurrence_id}.
        :param str occurrence_id: Second part of occurrence `name`:
               providers/{provider_id}/occurrences/{occurrence_id}.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if account_id is None:
            raise ValueError('account_id must be provided')
        if provider_id is None:
            raise ValueError('provider_id must be provided')
        if occurrence_id is None:
            raise ValueError('occurrence_id must be provided')

        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME, service_version='V1', operation_id='get_occurrence_note')
        headers.update(sdk_headers)

        url = '/v1/{0}/providers/{1}/occurrences/{2}/note'.format(*self._encode_path_vars(account_id, provider_id, occurrence_id))
        request = self.prepare_request(method='GET',
                                url=url,
                                headers=headers)

        response = self.send(request)
        return response

    #########################
    # findingsOccurrences
    #########################


    def create_occurrence(self, account_id: str, provider_id: str, note_name: str, kind: 'ApiNoteKind', id: str, *, name: str = None, resource_url: str = None, remediation: str = None, create_time: datetime = None, update_time: datetime = None, context: 'Context' = None, finding: 'Finding' = None, kpi: 'Kpi' = None, replace_if_exists: bool = None, **kwargs) -> 'DetailedResponse':
        """
        Creates a new `Occurrence`. Use this method to create `Occurrences` for a resource.

        :param str account_id: Account ID.
        :param str provider_id: Part of `parent`. This contains the provider_id for
               example: providers/{provider_id}.
        :param str note_name: An analysis note associated with this image, in
               the form "{account_id}/providers/{provider_id}/notes/{note_id}" This field
               can be used as a filter in list requests.
        :param ApiNoteKind kind: Output only. This explicitly denotes which of
               the `Occurrence` details are specified.
               This field can be used as a filter in list requests.
                kind could be -
                        - FINDING
                        - KPI
                        - CARD
                        - CARD_CONFIGURED
                        - SECTION
                example:
                    kind="FINDING"
        :param str id:
        :param str name: (optional) Output only. The name of the `Occurrence`
               in the form
               "{account_id}/providers/{provider_id}/occurrences/{occuurence_id}".
        :param str resource_url: (optional) The unique URL of the resource,
               image or the container, for which the `Occurrence` applies. For example,
               https://gcr.io/provider/image@sha256:foo. This field can be used as a
               filter in list requests.
        :param str remediation: (optional)
        :param datetime create_time: (optional) Output only. The time this
               `Occurrence` was created.
        :param datetime update_time: (optional) Output only. The time this
               `Occurrence` was last updated.
        :param Context context: (optional) Details about the context of this
               `Occurrence`.
               example - 
               context = {
                    "region": "us-south",
                    "resource_type": "Cluster",
                    "service_name": "Kubernetes Cluster",
                    "account_id": "abc123"
                }
        :param Finding finding: (optional) Details of the occurrence of a
               finding.
                example - 
                    finding = {
                        "severity": "LOW",
                        "next_steps": [
                            {
                                "title": "string",
                                "url": "string"
                            }
                        ]
                    }
        :param Kpi kpi: (optional) Details of the occurrence of a KPI.
                example - 
                    kpi={
                        "value":1,
                        "total":1
                    }
        :param bool replace_if_exists: (optional) It allows replacing an existing
               occurrence when set to true.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if account_id is None:
            raise ValueError('account_id must be provided')
        if provider_id is None:
            raise ValueError('provider_id must be provided')
        if note_name is None:
            raise ValueError('note_name must be provided')
        if kind is None:
            raise ValueError('kind must be provided')
        if id is None:
            raise ValueError('id must be provided')
        #kind = self._convert_model(kind)
        if context is not None:
            context = self._convert_model(context)
        if finding is not None:
            finding = self._convert_model(finding)
        if kpi is not None:
            kpi = self._convert_model(kpi)

        headers = {
            'Replace-If-Exists': replace_if_exists
        }
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME, service_version='V1', operation_id='create_occurrence')
        headers.update(sdk_headers)

        data = {
            'note_name': note_name,
            'kind': kind,
            'id': id,
            'name': name,
            'resource_url': resource_url,
            'remediation': remediation,
            'provider_id': provider_id,
            'context': context,
            'finding': finding,
            'kpi': kpi
        }

        if create_time != None :
            data.create_time = create_time.__str__()   
        if update_time != None :
            data.update_time = update_time.__str__()
        
        url = '/v1/{0}/providers/{1}/occurrences'.format(*self._encode_path_vars(account_id, provider_id))
        request = self.prepare_request(method='POST',
                                url=url,
                                headers=headers,
                                data=data)

        response = self.send(request)
        return response


    def list_occurrences(self, account_id: str, provider_id: str, *, page_size: int = None, page_token: str = None, **kwargs) -> 'DetailedResponse':
        """
        Lists active `Occurrences` for a given provider matching the filters.

        :param str account_id: Account ID.
        :param str provider_id: Part of `parent`. This contains the provider_id for
               example: providers/{provider_id}.
        :param int page_size: (optional) Number of occurrences to return in the
               list.
        :param str page_token: (optional) Token to provide to skip to a particular
               spot in the list.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if account_id is None:
            raise ValueError('account_id must be provided')
        if provider_id is None:
            raise ValueError('provider_id must be provided')

        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME, service_version='V1', operation_id='list_occurrences')
        headers.update(sdk_headers)

        params = {
            'page_size': page_size,
            'page_token': page_token
        }

        url = '/v1/{0}/providers/{1}/occurrences'.format(*self._encode_path_vars(account_id, provider_id))
        request = self.prepare_request(method='GET',
                                url=url,
                                headers=headers,
                                params=params)

        response = self.send(request)
        return response


    def list_note_occurrences(self, account_id: str, provider_id: str, note_id: str, *, page_size: int = None, page_token: str = None, **kwargs) -> 'DetailedResponse':
        """
        Lists `Occurrences` referencing the specified `Note`. Use this method to get all occurrences referencing your `Note` across all your customer providers.

        :param str account_id: Account ID.
        :param str provider_id: First part of note `name`:
               providers/{provider_id}/notes/{note_id}.
        :param str note_id: Second part of note `name`:
               providers/{provider_id}/notes/{note_id}.
        :param int page_size: (optional) Number of notes to return in the list.
        :param str page_token: (optional) Token to provide to skip to a particular
               spot in the list.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if account_id is None:
            raise ValueError('account_id must be provided')
        if provider_id is None:
            raise ValueError('provider_id must be provided')
        if note_id is None:
            raise ValueError('note_id must be provided')

        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME, service_version='V1', operation_id='list_note_occurrences')
        headers.update(sdk_headers)

        params = {
            'page_size': page_size,
            'page_token': page_token
        }

        url = '/v1/{0}/providers/{1}/notes/{2}/occurrences'.format(*self._encode_path_vars(account_id, provider_id, note_id))
        request = self.prepare_request(method='GET',
                                url=url,
                                headers=headers,
                                params=params)

        response = self.send(request)
        return response


    def get_occurrence(self, account_id: str, provider_id: str, occurrence_id: str, **kwargs) -> 'DetailedResponse':
        """
        Returns the requested `Occurrence`.

        :param str account_id: Account ID.
        :param str provider_id: First part of occurrence `name`:
               providers/{provider_id}/occurrences/{occurrence_id}.
        :param str occurrence_id: Second part of occurrence `name`:
               providers/{provider_id}/occurrences/{occurrence_id}.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if account_id is None:
            raise ValueError('account_id must be provided')
        if provider_id is None:
            raise ValueError('provider_id must be provided')
        if occurrence_id is None:
            raise ValueError('occurrence_id must be provided')

        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME, service_version='V1', operation_id='get_occurrence')
        headers.update(sdk_headers)

        url = '/v1/{0}/providers/{1}/occurrences/{2}'.format(*self._encode_path_vars(account_id, provider_id, occurrence_id))
        request = self.prepare_request(method='GET',
                                url=url,
                                headers=headers)

        response = self.send(request)
        return response


    def update_occurrence(self, account_id: str, provider_id: str, occurrence_id: str, note_name: str, kind: 'ApiNoteKind', id: str, *, name: str = None, resource_url: str = None, remediation: str = None, create_time: datetime = None, update_time: datetime = None, context: 'Context' = None, finding: 'Finding' = None, kpi: 'Kpi' = None, **kwargs) -> 'DetailedResponse':
        """
        Updates an existing `Occurrence`.

        :param str account_id: Account ID.
        :param str provider_id: First part of occurrence `name`:
               providers/{provider_id}/occurrences/{occurrence_id}.
        :param str occurrence_id: Second part of occurrence `name`:
               providers/{provider_id}/occurrences/{occurrence_id}.
        :param str note_name: An analysis note associated with this image, in
               the form "{account_id}/providers/{provider_id}/notes/{note_id}" This field
               can be used as a filter in list requests.
        :param ApiNoteKind kind: Output only. This explicitly denotes which of
               the `Occurrence` details are specified.
               This field can be used as a filter in list requests.
               kind could be -
                        - FINDING
                        - KPI
                        - CARD
                        - CARD_CONFIGURED
                        - SECTION
                example:
                    kind="FINDING"
        :param str id:
        :param str name: (optional) Output only. The name of the `Occurrence`
               in the form
               "{account_id}/providers/{provider_id}/occurrences/{occuurence_id}".
        :param str resource_url: (optional) The unique URL of the resource,
               image or the container, for which the `Occurrence` applies. For example,
               https://gcr.io/provider/image@sha256:foo. This field can be used as a
               filter in list requests.
        :param str remediation: (optional)
        :param datetime create_time: (optional) Output only. The time this
               `Occurrence` was created.
        :param datetime update_time: (optional) Output only. The time this
               `Occurrence` was last updated.
        :param Context context: (optional) Details about the context of this
               `Occurrence`.
               example - 
               context = {
                    "region": "us-south",
                    "resource_type": "Cluster",
                    "service_name": "Kubernetes Cluster",
                    "account_id": "abc123"
                }
        :param Finding finding: (optional) Details of the occurrence of a
               finding.
               example - 
                    finding = {
                        "severity": "LOW",
                        "next_steps": [
                            {
                                "title": "string",
                                "url": "string"
                            }
                        ]
                    }
        :param Kpi kpi: (optional) Details of the occurrence of a KPI.
                example - 
                    kpi={
                        "value":1,
                        "total":1
                    }
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if account_id is None:
            raise ValueError('account_id must be provided')
        if provider_id is None:
            raise ValueError('provider_id must be provided')
        if occurrence_id is None:
            raise ValueError('occurrence_id must be provided')
        if note_name is None:
            raise ValueError('note_name must be provided')
        if kind is None:
            raise ValueError('kind must be provided')
        if id is None:
            raise ValueError('id must be provided')
        #kind = self._convert_model(kind)
        if context is not None:
            context = self._convert_model(context)
        if finding is not None:
            finding = self._convert_model(finding)
        if kpi is not None:
            kpi = self._convert_model(kpi)

        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME, service_version='V1', operation_id='update_occurrence')
        headers.update(sdk_headers)

        data = {
            'note_name': note_name,
            'kind': kind,
            'id': id,
            'name': name,
            'resource_url': resource_url,
            'remediation': remediation,
            'provider_id': provider_id,
            'context': context,
            'finding': finding,
            'kpi': kpi
        }

        if create_time != None :
            data.create_time = create_time.__str__()   
        if update_time != None :
            data.update_time = update_time.__str__()

        url = '/v1/{0}/providers/{1}/occurrences/{2}'.format(*self._encode_path_vars(account_id, provider_id, occurrence_id))
        request = self.prepare_request(method='PUT',
                                url=url,
                                headers=headers,
                                data=data)

        response = self.send(request)
        return response


    def delete_occurrence(self, account_id: str, provider_id: str, occurrence_id: str, **kwargs) -> 'DetailedResponse':
        """
        Deletes the given `Occurrence` from the system.

        :param str account_id: Account ID.
        :param str provider_id: First part of occurrence `name`:
               providers/{provider_id}/notes/{occurrence_id}.
        :param str occurrence_id: Second part of occurrence `name`:
               providers/{provider_id}/notes/{occurrence_id}.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if account_id is None:
            raise ValueError('account_id must be provided')
        if provider_id is None:
            raise ValueError('provider_id must be provided')
        if occurrence_id is None:
            raise ValueError('occurrence_id must be provided')

        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME, service_version='V1', operation_id='delete_occurrence')
        headers.update(sdk_headers)

        url = '/v1/{0}/providers/{1}/occurrences/{2}'.format(*self._encode_path_vars(account_id, provider_id, occurrence_id))
        request = self.prepare_request(method='DELETE',
                                url=url,
                                headers=headers)

        response = self.send(request)
        return response

    #########################
    # findingsProviders
    #########################


    def list_providers(self, account_id: str, *, page_size: int = None, page_token: str = None, **kwargs) -> 'DetailedResponse':
        """
        Lists all `Providers` for a given account id.

        :param str account_id: Account ID.
        :param int page_size: (optional) Number of providers to return in the list.
        :param str page_token: (optional) Token to provide to skip to a particular
               spot in the list.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if account_id is None:
            raise ValueError('account_id must be provided')

        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME, service_version='V1', operation_id='list_providers')
        headers.update(sdk_headers)

        params = {
            'page_size': page_size,
            'page_token': page_token
        }

        url = '/v1/{0}/providers'.format(*self._encode_path_vars(account_id))
        request = self.prepare_request(method='GET',
                                url=url,
                                headers=headers,
                                params=params)

        response = self.send(request)
        return response


class PostGraphEnums(object):
    class ContentType(Enum):
        """
        The type of the input.
        """
        APPLICATION_GRAPHQL = 'application/graphql'
        APPLICATION_JSON = 'application/json'


##############################################################################
# Models
##############################################################################


class Card():
    """
    Card provides details about a card kind of note.

    {
        "section": "string",
        "title": "string",
        "subtitle": "string",
        "order": 1,
        "finding_note_names": [
        "string"
        ],
        "requires_configuration": false,
        "badge_text": "string",
        "badge_image": "string",
        "elements": [
        {
            "kind": "NUMERIC",
            "default_time_range": "4d"
        }
        ]
    }
    :attr str section: The section this card belongs to.
    :attr str title: The title of this card.
    :attr str subtitle: The subtitle of this card.
    :attr int order: (optional) The order of the card in which it will appear on SA
          dashboard in the mentioned section.
    :attr List[str] finding_note_names: The finding note names associated to this
          card.
    :attr bool requires_configuration: (optional)
    :attr str badge_text: (optional) The text associated to the card's badge.
    :attr str badge_image: (optional) The base64 content of the image associated to
          the card's badge.
    :attr List[CardElement] elements: The elements of this card.
    """

    def __init__(self, section: str, title: str, subtitle: str, finding_note_names: List[str], elements: List['CardElement'], *, order: int = None, requires_configuration: bool = None, badge_text: str = None, badge_image: str = None) -> None:
        """
        Initialize a Card object.

        :param str section: The section this card belongs to.
        :param str title: The title of this card.
        :param str subtitle: The subtitle of this card.
        :param List[str] finding_note_names: The finding note names associated to
               this card.
        :param List[CardElement] elements: The elements of this card.
        :param int order: (optional) The order of the card in which it will appear
               on SA dashboard in the mentioned section.
        :param bool requires_configuration: (optional)
        :param str badge_text: (optional) The text associated to the card's badge.
        :param str badge_image: (optional) The base64 content of the image
               associated to the card's badge.
        """
        self.section = section
        self.title = title
        self.subtitle = subtitle
        self.order = order
        self.finding_note_names = finding_note_names
        self.requires_configuration = requires_configuration
        self.badge_text = badge_text
        self.badge_image = badge_image
        self.elements = elements

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Card':
        """Initialize a Card object from a json dictionary."""
        args = {}
        valid_keys = ['section', 'title', 'subtitle', 'order', 'finding_note_names', 'requires_configuration', 'badge_text', 'badge_image', 'elements']
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError('Unrecognized keys detected in dictionary for class Card: ' + ', '.join(bad_keys))
        if 'section' in _dict:
            args['section'] = _dict.get('section')
        else:
            raise ValueError('Required property \'section\' not present in Card JSON')
        if 'title' in _dict:
            args['title'] = _dict.get('title')
        else:
            raise ValueError('Required property \'title\' not present in Card JSON')
        if 'subtitle' in _dict:
            args['subtitle'] = _dict.get('subtitle')
        else:
            raise ValueError('Required property \'subtitle\' not present in Card JSON')
        if 'order' in _dict:
            args['order'] = _dict.get('order')
        if 'finding_note_names' in _dict:
            args['finding_note_names'] = _dict.get('finding_note_names')
        else:
            raise ValueError('Required property \'finding_note_names\' not present in Card JSON')
        if 'requires_configuration' in _dict:
            args['requires_configuration'] = _dict.get('requires_configuration')
        if 'badge_text' in _dict:
            args['badge_text'] = _dict.get('badge_text')
        if 'badge_image' in _dict:
            args['badge_image'] = _dict.get('badge_image')
        if 'elements' in _dict:
            args['elements'] = [CardElement._from_dict(x) for x in (_dict.get('elements') )]
        else:
            raise ValueError('Required property \'elements\' not present in Card JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Card object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'section') and self.section is not None:
            _dict['section'] = self.section
        if hasattr(self, 'title') and self.title is not None:
            _dict['title'] = self.title
        if hasattr(self, 'subtitle') and self.subtitle is not None:
            _dict['subtitle'] = self.subtitle
        if hasattr(self, 'order') and self.order is not None:
            _dict['order'] = self.order
        if hasattr(self, 'finding_note_names') and self.finding_note_names is not None:
            _dict['finding_note_names'] = self.finding_note_names
        if hasattr(self, 'requires_configuration') and self.requires_configuration is not None:
            _dict['requires_configuration'] = self.requires_configuration
        if hasattr(self, 'badge_text') and self.badge_text is not None:
            _dict['badge_text'] = self.badge_text
        if hasattr(self, 'badge_image') and self.badge_image is not None:
            _dict['badge_image'] = self.badge_image
        if hasattr(self, 'elements') and self.elements is not None:
            _dict['elements'] = [x._to_dict() for x in self.elements]
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this Card object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other: 'Card') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'Card') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class CardElement():
    """
    CardElement provides details about the elements of a Card.

    :attr str kind: Kind of element
          - NUMERIC&#58; Single numeric value
          - BREAKDOWN&#58; Breakdown of numeric values
          - TIME_SERIES&#58; Time-series of numeric values.
    :attr str default_time_range: (optional) The default time range of this card
          element.
    """

    def __init__(self, kind: str, *, default_time_range: str = None) -> None:
        """
        Initialize a CardElement object.

        :param str kind: Kind of element
               - NUMERIC&#58; Single numeric value
               - BREAKDOWN&#58; Breakdown of numeric values
               - TIME_SERIES&#58; Time-series of numeric values.
        :param str default_time_range: (optional) The default time range of this
               card element.
        """
        self.kind = kind
        self.default_time_range = default_time_range

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'CardElement':
        """Initialize a CardElement object from a json dictionary."""
        disc_class = cls._get_class_by_discriminator(_dict)
        if disc_class != cls:
            return disc_class.from_dict(_dict)
        args = {}
        valid_keys = ['kind', 'default_time_range']
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError('Unrecognized keys detected in dictionary for class CardElement: ' + ', '.join(bad_keys))
        if 'kind' in _dict:
            args['kind'] = _dict.get('kind')
        else:
            raise ValueError('Required property \'kind\' not present in CardElement JSON')
        if 'default_time_range' in _dict:
            args['default_time_range'] = _dict.get('default_time_range')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a CardElement object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'kind') and self.kind is not None:
            _dict['kind'] = self.kind
        if hasattr(self, 'default_time_range') and self.default_time_range is not None:
            _dict['default_time_range'] = self.default_time_range
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this CardElement object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other: 'CardElement') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'CardElement') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    @classmethod
    def _get_class_by_discriminator(cls, _dict: Dict) -> object:
        mapping = {}
        mapping['NumericCardElement'] = 'NumericCardElement'
        mapping['BreakdownCardElement'] = 'BreakdownCardElement'
        mapping['TimeSeriesCardElement'] = 'TimeSeriesCardElement'
        disc_value = _dict.get('kind')
        if disc_value is None:
            raise ValueError('Discriminator property \'kind\' not found in CardElement JSON')
        class_name = mapping.get(disc_value, disc_value)
        try:
            disc_class = getattr(sys.modules[__name__], class_name)
        except AttributeError:
            disc_class = cls
        if isinstance(disc_class, object):
            return disc_class
        raise TypeError('%s is not a discriminator class' % class_name)

    
    class KindEnum(Enum):
        """
        Kind of element
        - NUMERIC&#58; Single numeric value
        - BREAKDOWN&#58; Breakdown of numeric values
        - TIME_SERIES&#58; Time-series of numeric values.
        """
        NUMERIC = "NUMERIC"
        BREAKDOWN = "BREAKDOWN"
        TIME_SERIES = "TIME_SERIES"


class Certainty():
    """
    Note provider-assigned confidence on the validity of an occurrence
    - LOW&#58; Low Certainty
    - MEDIUM&#58; Medium Certainty
    - HIGH&#58; High Certainty.

    """

    def __init__(self) -> None:
        """
        Initialize a Certainty object.

        """

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Certainty':
        """Initialize a Certainty object from a json dictionary."""
        args = {}
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Certainty object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this Certainty object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other: 'Certainty') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'Certainty') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class Context():
    """
    Context.

    {
        "region": "string",
        "resource_crn": "string",
        "resource_id": "string",
        "resource_name": "string",
        "resource_type": "string",
        "service_crn": "string",
        "service_name": "string",
        "environment_name": "string",
        "component_name": "string",
        "toolchain_id": "string"
    }
    :attr str region: (optional) The IBM Cloud region.
    :attr str resource_crn: (optional) The resource CRN (e.g. certificate CRN, image
          CRN).
    :attr str resource_id: (optional) The resource ID, in case the CRN is not
          available.
    :attr str resource_name: (optional) The user-friendly resource name.
    :attr str resource_type: (optional) The resource type name (e.g. Pod, Cluster,
          Certificate, Image).
    :attr str service_crn: (optional) The service CRN (e.g. CertMgr Instance CRN).
    :attr str service_name: (optional) The service name (e.g. CertMgr).
    :attr str environment_name: (optional) The name of the environment the
          occurrence applies to.
    :attr str component_name: (optional) The name of the component the occurrence
          applies to.
    :attr str toolchain_id: (optional) The id of the toolchain the occurrence
          applies to.
    """

    def __init__(self, *, region: str = None, resource_crn: str = None, resource_id: str = None, resource_name: str = None, resource_type: str = None, service_crn: str = None, service_name: str = None, environment_name: str = None, component_name: str = None, toolchain_id: str = None) -> None:
        """
        Initialize a Context object.

        :param str region: (optional) The IBM Cloud region.
        :param str resource_crn: (optional) The resource CRN (e.g. certificate CRN,
               image CRN).
        :param str resource_id: (optional) The resource ID, in case the CRN is not
               available.
        :param str resource_name: (optional) The user-friendly resource name.
        :param str resource_type: (optional) The resource type name (e.g. Pod,
               Cluster, Certificate, Image).
        :param str service_crn: (optional) The service CRN (e.g. CertMgr Instance
               CRN).
        :param str service_name: (optional) The service name (e.g. CertMgr).
        :param str environment_name: (optional) The name of the environment the
               occurrence applies to.
        :param str component_name: (optional) The name of the component the
               occurrence applies to.
        :param str toolchain_id: (optional) The id of the toolchain the occurrence
               applies to.
        """
        self.region = region
        self.resource_crn = resource_crn
        self.resource_id = resource_id
        self.resource_name = resource_name
        self.resource_type = resource_type
        self.service_crn = service_crn
        self.service_name = service_name
        self.environment_name = environment_name
        self.component_name = component_name
        self.toolchain_id = toolchain_id

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Context':
        """Initialize a Context object from a json dictionary."""
        args = {}
        valid_keys = ['region', 'resource_crn', 'resource_id', 'resource_name', 'resource_type', 'service_crn', 'service_name', 'environment_name', 'component_name', 'toolchain_id']
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError('Unrecognized keys detected in dictionary for class Context: ' + ', '.join(bad_keys))
        if 'region' in _dict:
            args['region'] = _dict.get('region')
        if 'resource_crn' in _dict:
            args['resource_crn'] = _dict.get('resource_crn')
        if 'resource_id' in _dict:
            args['resource_id'] = _dict.get('resource_id')
        if 'resource_name' in _dict:
            args['resource_name'] = _dict.get('resource_name')
        if 'resource_type' in _dict:
            args['resource_type'] = _dict.get('resource_type')
        if 'service_crn' in _dict:
            args['service_crn'] = _dict.get('service_crn')
        if 'service_name' in _dict:
            args['service_name'] = _dict.get('service_name')
        if 'environment_name' in _dict:
            args['environment_name'] = _dict.get('environment_name')
        if 'component_name' in _dict:
            args['component_name'] = _dict.get('component_name')
        if 'toolchain_id' in _dict:
            args['toolchain_id'] = _dict.get('toolchain_id')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Context object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'region') and self.region is not None:
            _dict['region'] = self.region
        if hasattr(self, 'resource_crn') and self.resource_crn is not None:
            _dict['resource_crn'] = self.resource_crn
        if hasattr(self, 'resource_id') and self.resource_id is not None:
            _dict['resource_id'] = self.resource_id
        if hasattr(self, 'resource_name') and self.resource_name is not None:
            _dict['resource_name'] = self.resource_name
        if hasattr(self, 'resource_type') and self.resource_type is not None:
            _dict['resource_type'] = self.resource_type
        if hasattr(self, 'service_crn') and self.service_crn is not None:
            _dict['service_crn'] = self.service_crn
        if hasattr(self, 'service_name') and self.service_name is not None:
            _dict['service_name'] = self.service_name
        if hasattr(self, 'environment_name') and self.environment_name is not None:
            _dict['environment_name'] = self.environment_name
        if hasattr(self, 'component_name') and self.component_name is not None:
            _dict['component_name'] = self.component_name
        if hasattr(self, 'toolchain_id') and self.toolchain_id is not None:
            _dict['toolchain_id'] = self.toolchain_id
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this Context object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other: 'Context') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'Context') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class DataTransferred():
    """
    It provides details about data transferred between clients and servers.

    :attr int client_bytes: (optional) The number of client bytes transferred.
    :attr int server_bytes: (optional) The number of server bytes transferred.
    :attr int client_packets: (optional) The number of client packets transferred.
    :attr int server_packets: (optional) The number of server packets transferred.
    """

    def __init__(self, *, client_bytes: int = None, server_bytes: int = None, client_packets: int = None, server_packets: int = None) -> None:
        """
        Initialize a DataTransferred object.

        :param int client_bytes: (optional) The number of client bytes transferred.
        :param int server_bytes: (optional) The number of server bytes transferred.
        :param int client_packets: (optional) The number of client packets
               transferred.
        :param int server_packets: (optional) The number of server packets
               transferred.
        """
        self.client_bytes = client_bytes
        self.server_bytes = server_bytes
        self.client_packets = client_packets
        self.server_packets = server_packets

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'DataTransferred':
        """Initialize a DataTransferred object from a json dictionary."""
        args = {}
        valid_keys = ['client_bytes', 'server_bytes', 'client_packets', 'server_packets']
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError('Unrecognized keys detected in dictionary for class DataTransferred: ' + ', '.join(bad_keys))
        if 'client_bytes' in _dict:
            args['client_bytes'] = _dict.get('client_bytes')
        if 'server_bytes' in _dict:
            args['server_bytes'] = _dict.get('server_bytes')
        if 'client_packets' in _dict:
            args['client_packets'] = _dict.get('client_packets')
        if 'server_packets' in _dict:
            args['server_packets'] = _dict.get('server_packets')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a DataTransferred object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'client_bytes') and self.client_bytes is not None:
            _dict['client_bytes'] = self.client_bytes
        if hasattr(self, 'server_bytes') and self.server_bytes is not None:
            _dict['server_bytes'] = self.server_bytes
        if hasattr(self, 'client_packets') and self.client_packets is not None:
            _dict['client_packets'] = self.client_packets
        if hasattr(self, 'server_packets') and self.server_packets is not None:
            _dict['server_packets'] = self.server_packets
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this DataTransferred object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other: 'DataTransferred') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'DataTransferred') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class Finding():
    """
    Finding provides details about a finding occurrence.

    {
        "severity": "LOW",
        "certainty": "LOW",
        "next_steps": [
        {
            "title": "string",
            "url": "string"
        }
        ],
        "network_connection": {
        "direction": "string",
        "protocol": "string",
        "client": {
            "address": "string",
            "port": 0
        },
        "server": {
            "address": "string",
            "port": 0
        }
        },
        "data_transferred": {
        "client_bytes": 0,
        "server_bytes": 0,
        "client_packets": 0,
        "server_packets": 0
        }
    }
    :attr Severity severity: (optional) The common severity of this `Occurrence`.
    :attr Certainty certainty: (optional) The confidence level on this `Occurrence`.
    :attr List[RemediationStep] next_steps: (optional) Remediation steps for the
          issues reported in this finding. They override the note's next steps.
    :attr NetworkConnection network_connection: (optional) Network connection
          details of this finding.
    :attr DataTransferred data_transferred: (optional) Data transferred details of
          this finding.
    """

    def __init__(self, *, severity: 'Severity' = None, certainty: 'Certainty' = None, next_steps: List['RemediationStep'] = None, network_connection: 'NetworkConnection' = None, data_transferred: 'DataTransferred' = None) -> None:
        """
        Initialize a Finding object.

        :param Severity severity: (optional) The common severity of this
               `Occurrence`.
        :param Certainty certainty: (optional) The confidence level on this
               `Occurrence`.
        :param List[RemediationStep] next_steps: (optional) Remediation steps for
               the issues reported in this finding. They override the note's next steps.
        :param NetworkConnection network_connection: (optional) Network connection
               details of this finding.
        :param DataTransferred data_transferred: (optional) Data transferred
               details of this finding.
        """
        self.severity = severity
        self.certainty = certainty
        self.next_steps = next_steps
        self.network_connection = network_connection
        self.data_transferred = data_transferred

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Finding':
        """Initialize a Finding object from a json dictionary."""
        args = {}
        valid_keys = ['severity', 'certainty', 'next_steps', 'network_connection', 'data_transferred']
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError('Unrecognized keys detected in dictionary for class Finding: ' + ', '.join(bad_keys))
        if 'severity' in _dict:
            args['severity'] = Severity._from_dict(_dict.get('severity'))
        if 'certainty' in _dict:
            args['certainty'] = Certainty._from_dict(_dict.get('certainty'))
        if 'next_steps' in _dict:
            args['next_steps'] = [RemediationStep._from_dict(x) for x in (_dict.get('next_steps') )]
        if 'network_connection' in _dict:
            args['network_connection'] = NetworkConnection._from_dict(_dict.get('network_connection'))
        if 'data_transferred' in _dict:
            args['data_transferred'] = DataTransferred._from_dict(_dict.get('data_transferred'))
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Finding object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'severity') and self.severity is not None:
            _dict['severity'] = self.severity._to_dict()
        if hasattr(self, 'certainty') and self.certainty is not None:
            _dict['certainty'] = self.certainty._to_dict()
        if hasattr(self, 'next_steps') and self.next_steps is not None:
            _dict['next_steps'] = [x._to_dict() for x in self.next_steps]
        if hasattr(self, 'network_connection') and self.network_connection is not None:
            _dict['network_connection'] = self.network_connection._to_dict()
        if hasattr(self, 'data_transferred') and self.data_transferred is not None:
            _dict['data_transferred'] = self.data_transferred._to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this Finding object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other: 'Finding') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'Finding') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class FindingType():
    """
    FindingType provides details about a finding note.

    {
        "severity": "LOW",
        "next_steps": [
        {
            "title": "string",
            "url": "string"
        }
        ]
    }
    :attr Severity severity: The default severity of the findings related to this
          `Note`.
    :attr List[RemediationStep] next_steps: (optional) Common remediation steps for
          the finding of this type.
    """

    def __init__(self, severity: 'Severity', *, next_steps: List['RemediationStep'] = None) -> None:
        """
        Initialize a FindingType object.

        :param Severity severity: The default severity of the findings related to
               this `Note`.
        :param List[RemediationStep] next_steps: (optional) Common remediation
               steps for the finding of this type.
        """
        self.severity = severity
        self.next_steps = next_steps

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'FindingType':
        """Initialize a FindingType object from a json dictionary."""
        args = {}
        valid_keys = ['severity', 'next_steps']
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError('Unrecognized keys detected in dictionary for class FindingType: ' + ', '.join(bad_keys))
        if 'severity' in _dict:
            args['severity'] = Severity._from_dict(_dict.get('severity'))
        else:
            raise ValueError('Required property \'severity\' not present in FindingType JSON')
        if 'next_steps' in _dict:
            args['next_steps'] = [RemediationStep._from_dict(x) for x in (_dict.get('next_steps') )]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a FindingType object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'severity') and self.severity is not None:
            _dict['severity'] = self.severity._to_dict()
        if hasattr(self, 'next_steps') and self.next_steps is not None:
            _dict['next_steps'] = [x._to_dict() for x in self.next_steps]
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this FindingType object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other: 'FindingType') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'FindingType') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class Kpi():
    """
    Kpi provides details about a KPI occurrence.

    {
        "value": 0,
        "total": 0
    }
    :attr float value: The value of this KPI.
    :attr float total: (optional) The total value of this KPI.
    """

    def __init__(self, value: float, *, total: float = None) -> None:
        """
        Initialize a Kpi object.

        :param float value: The value of this KPI.
        :param float total: (optional) The total value of this KPI.
        """
        self.value = value
        self.total = total

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Kpi':
        """Initialize a Kpi object from a json dictionary."""
        args = {}
        valid_keys = ['value', 'total']
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError('Unrecognized keys detected in dictionary for class Kpi: ' + ', '.join(bad_keys))
        if 'value' in _dict:
            args['value'] = _dict.get('value')
        else:
            raise ValueError('Required property \'value\' not present in Kpi JSON')
        if 'total' in _dict:
            args['total'] = _dict.get('total')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Kpi object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'value') and self.value is not None:
            _dict['value'] = self.value
        if hasattr(self, 'total') and self.total is not None:
            _dict['total'] = self.total
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this Kpi object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other: 'Kpi') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'Kpi') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class KpiType():
    """
    KpiType provides details about a KPI note.

    {
        "aggregation_type": "SUM"
    }
    :attr str aggregation_type: The aggregation type of the KPI values.
          - SUM&#58; A single-value metrics aggregation type that sums up numeric values
            that are extracted from KPI occurrences.
    """

    def __init__(self, aggregation_type: str) -> None:
        """
        Initialize a KpiType object.

        :param str aggregation_type: The aggregation type of the KPI values.
               - SUM&#58; A single-value metrics aggregation type that sums up numeric
               values
                 that are extracted from KPI occurrences.
        """
        self.aggregation_type = aggregation_type

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'KpiType':
        """Initialize a KpiType object from a json dictionary."""
        args = {}
        valid_keys = ['aggregation_type']
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError('Unrecognized keys detected in dictionary for class KpiType: ' + ', '.join(bad_keys))
        if 'aggregation_type' in _dict:
            args['aggregation_type'] = _dict.get('aggregation_type')
        else:
            raise ValueError('Required property \'aggregation_type\' not present in KpiType JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a KpiType object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'aggregation_type') and self.aggregation_type is not None:
            _dict['aggregation_type'] = self.aggregation_type
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this KpiType object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other: 'KpiType') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'KpiType') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    
    class AggregationTypeEnum(Enum):
        """
        The aggregation type of the KPI values.
        - SUM&#58; A single-value metrics aggregation type that sums up numeric values
          that are extracted from KPI occurrences.
        """
        SUM = "SUM"


class NetworkConnection():
    """
    It provides details about a network connection.

    :attr str direction: (optional) The direction of this network connection.
    :attr str protocol: (optional) The protocol of this network connection.
    :attr SocketAddress client: (optional) The client socket address of this network
          connection.
    :attr SocketAddress server: (optional) The server socket address of this network
          connection.
    """

    def __init__(self, *, direction: str = None, protocol: str = None, client: 'SocketAddress' = None, server: 'SocketAddress' = None) -> None:
        """
        Initialize a NetworkConnection object.

        :param str direction: (optional) The direction of this network connection.
        :param str protocol: (optional) The protocol of this network connection.
        :param SocketAddress client: (optional) The client socket address of this
               network connection.
        :param SocketAddress server: (optional) The server socket address of this
               network connection.
        """
        self.direction = direction
        self.protocol = protocol
        self.client = client
        self.server = server

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'NetworkConnection':
        """Initialize a NetworkConnection object from a json dictionary."""
        args = {}
        valid_keys = ['direction', 'protocol', 'client', 'server']
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError('Unrecognized keys detected in dictionary for class NetworkConnection: ' + ', '.join(bad_keys))
        if 'direction' in _dict:
            args['direction'] = _dict.get('direction')
        if 'protocol' in _dict:
            args['protocol'] = _dict.get('protocol')
        if 'client' in _dict:
            args['client'] = SocketAddress._from_dict(_dict.get('client'))
        if 'server' in _dict:
            args['server'] = SocketAddress._from_dict(_dict.get('server'))
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a NetworkConnection object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'direction') and self.direction is not None:
            _dict['direction'] = self.direction
        if hasattr(self, 'protocol') and self.protocol is not None:
            _dict['protocol'] = self.protocol
        if hasattr(self, 'client') and self.client is not None:
            _dict['client'] = self.client._to_dict()
        if hasattr(self, 'server') and self.server is not None:
            _dict['server'] = self.server._to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this NetworkConnection object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other: 'NetworkConnection') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'NetworkConnection') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class RemediationStep():
    """
    A remediation step description and associated URL.

    :attr str title: (optional) Title of this next step.
    :attr str url: (optional) The URL associated to this next steps.
    """

    def __init__(self, *, title: str = None, url: str = None) -> None:
        """
        Initialize a RemediationStep object.

        :param str title: (optional) Title of this next step.
        :param str url: (optional) The URL associated to this next steps.
        """
        self.title = title
        self.url = url

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'RemediationStep':
        """Initialize a RemediationStep object from a json dictionary."""
        args = {}
        valid_keys = ['title', 'url']
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError('Unrecognized keys detected in dictionary for class RemediationStep: ' + ', '.join(bad_keys))
        if 'title' in _dict:
            args['title'] = _dict.get('title')
        if 'url' in _dict:
            args['url'] = _dict.get('url')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a RemediationStep object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'title') and self.title is not None:
            _dict['title'] = self.title
        if hasattr(self, 'url') and self.url is not None:
            _dict['url'] = self.url
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this RemediationStep object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other: 'RemediationStep') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'RemediationStep') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class Reporter():
    """
    The entity reporting a note.

    {
        "id": "string",
        "title": "string",
        "url": "string"
    }
    :attr str id: The id of this reporter.
    :attr str title: The title of this reporter.
    :attr str url: (optional) The url of this reporter.
    """

    def __init__(self, id: str, title: str, *, url: str = None) -> None:
        """
        Initialize a Reporter object.

        :param str id: The id of this reporter.
        :param str title: The title of this reporter.
        :param str url: (optional) The url of this reporter.
        """
        self.id = id
        self.title = title
        self.url = url

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Reporter':
        """Initialize a Reporter object from a json dictionary."""
        args = {}
        valid_keys = ['id', 'title', 'url']
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError('Unrecognized keys detected in dictionary for class Reporter: ' + ', '.join(bad_keys))
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        else:
            raise ValueError('Required property \'id\' not present in Reporter JSON')
        if 'title' in _dict:
            args['title'] = _dict.get('title')
        else:
            raise ValueError('Required property \'title\' not present in Reporter JSON')
        if 'url' in _dict:
            args['url'] = _dict.get('url')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Reporter object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'title') and self.title is not None:
            _dict['title'] = self.title
        if hasattr(self, 'url') and self.url is not None:
            _dict['url'] = self.url
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this Reporter object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other: 'Reporter') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'Reporter') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class Section():
    """
    Card provides details about a card kind of note.

    {
        "title": "string",
        "image": "string"
    }

    :attr str title: The title of this section.
    :attr str image: The image of this section.
    """

    def __init__(self, title: str, image: str) -> None:
        """
        Initialize a Section object.

        :param str title: The title of this section.
        :param str image: The image of this section.
        """
        self.title = title
        self.image = image

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Section':
        """Initialize a Section object from a json dictionary."""
        args = {}
        valid_keys = ['title', 'image']
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError('Unrecognized keys detected in dictionary for class Section: ' + ', '.join(bad_keys))
        if 'title' in _dict:
            args['title'] = _dict.get('title')
        else:
            raise ValueError('Required property \'title\' not present in Section JSON')
        if 'image' in _dict:
            args['image'] = _dict.get('image')
        else:
            raise ValueError('Required property \'image\' not present in Section JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Section object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'title') and self.title is not None:
            _dict['title'] = self.title
        if hasattr(self, 'image') and self.image is not None:
            _dict['image'] = self.image
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this Section object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other: 'Section') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'Section') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class Severity():
    """
    Note provider-assigned severity/impact ranking
    - LOW&#58; Low Impact
    - MEDIUM&#58; Medium Impact
    - HIGH&#58; High Impact.

    """

    def __init__(self) -> None:
        """
        Initialize a Severity object.

        """

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Severity':
        """Initialize a Severity object from a json dictionary."""
        args = {}
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Severity object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this Severity object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other: 'Severity') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'Severity') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class SocketAddress():
    """
    It provides details about a socket address.

    :attr str address: The IP address of this socket address.
    :attr int port: (optional) The port number of this socket address.
    """

    def __init__(self, address: str, *, port: int = None) -> None:
        """
        Initialize a SocketAddress object.

        :param str address: The IP address of this socket address.
        :param int port: (optional) The port number of this socket address.
        """
        self.address = address
        self.port = port

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'SocketAddress':
        """Initialize a SocketAddress object from a json dictionary."""
        args = {}
        valid_keys = ['address', 'port']
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError('Unrecognized keys detected in dictionary for class SocketAddress: ' + ', '.join(bad_keys))
        if 'address' in _dict:
            args['address'] = _dict.get('address')
        else:
            raise ValueError('Required property \'address\' not present in SocketAddress JSON')
        if 'port' in _dict:
            args['port'] = _dict.get('port')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a SocketAddress object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'address') and self.address is not None:
            _dict['address'] = self.address
        if hasattr(self, 'port') and self.port is not None:
            _dict['port'] = self.port
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this SocketAddress object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other: 'SocketAddress') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'SocketAddress') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ValueType():
    """
    the value type of a card element.

    :attr str kind: Kind of element
          - KPI&#58; Kind of value derived from a KPI occurrence
          - FINDING_COUNT&#58; Kind of value derived from a count of finding occurrences.
    :attr str text: The text of this element type.
    """

    def __init__(self, kind: str, text: str) -> None:
        """
        Initialize a ValueType object.

        :param str kind: Kind of element
               - KPI&#58; Kind of value derived from a KPI occurrence
               - FINDING_COUNT&#58; Kind of value derived from a count of finding
               occurrences.
        :param str text: The text of this element type.
        """
        self.kind = kind
        self.text = text

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ValueType':
        """Initialize a ValueType object from a json dictionary."""
        disc_class = cls._get_class_by_discriminator(_dict)
        if disc_class != cls:
            return disc_class.from_dict(_dict)
        args = {}
        valid_keys = ['kind', 'text']
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError('Unrecognized keys detected in dictionary for class ValueType: ' + ', '.join(bad_keys))
        if 'kind' in _dict:
            args['kind'] = _dict.get('kind')
        else:
            raise ValueError('Required property \'kind\' not present in ValueType JSON')
        if 'text' in _dict:
            args['text'] = _dict.get('text')
        else:
            raise ValueError('Required property \'text\' not present in ValueType JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ValueType object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'kind') and self.kind is not None:
            _dict['kind'] = self.kind
        if hasattr(self, 'text') and self.text is not None:
            _dict['text'] = self.text
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ValueType object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other: 'ValueType') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ValueType') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    @classmethod
    def _get_class_by_discriminator(cls, _dict: Dict) -> object:
        mapping = {}
        mapping['KpiValueType'] = 'KpiValueType'
        mapping['FindingCountValueType'] = 'FindingCountValueType'
        disc_value = _dict.get('kind')
        if disc_value is None:
            raise ValueError('Discriminator property \'kind\' not found in ValueType JSON')
        class_name = mapping.get(disc_value, disc_value)
        try:
            disc_class = getattr(sys.modules[__name__], class_name)
        except AttributeError:
            disc_class = cls
        if isinstance(disc_class, object):
            return disc_class
        raise TypeError('%s is not a discriminator class' % class_name)

    
    class KindEnum(Enum):
        """
        Kind of element
        - KPI&#58; Kind of value derived from a KPI occurrence
        - FINDING_COUNT&#58; Kind of value derived from a count of finding occurrences.
        """
        KPI = "KPI"
        FINDING = "FINDING"


class ApiListNoteOccurrencesResponse():
    """
    Response including listed occurrences for a note.

    :attr List[ApiOccurrence] occurrences: (optional) The occurrences attached to
          the specified note.
    :attr str next_page_token: (optional) Token to receive the next page of notes.
    """

    def __init__(self, *, occurrences: List['ApiOccurrence'] = None, next_page_token: str = None) -> None:
        """
        Initialize a ApiListNoteOccurrencesResponse object.

        :param List[ApiOccurrence] occurrences: (optional) The occurrences attached
               to the specified note.
        :param str next_page_token: (optional) Token to receive the next page of
               notes.
        """
        self.occurrences = occurrences
        self.next_page_token = next_page_token

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ApiListNoteOccurrencesResponse':
        """Initialize a ApiListNoteOccurrencesResponse object from a json dictionary."""
        args = {}
        valid_keys = ['occurrences', 'next_page_token']
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError('Unrecognized keys detected in dictionary for class ApiListNoteOccurrencesResponse: ' + ', '.join(bad_keys))
        if 'occurrences' in _dict:
            args['occurrences'] = [ApiOccurrence._from_dict(x) for x in (_dict.get('occurrences') )]
        if 'next_page_token' in _dict:
            args['next_page_token'] = _dict.get('next_page_token')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ApiListNoteOccurrencesResponse object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'occurrences') and self.occurrences is not None:
            _dict['occurrences'] = [x._to_dict() for x in self.occurrences]
        if hasattr(self, 'next_page_token') and self.next_page_token is not None:
            _dict['next_page_token'] = self.next_page_token
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ApiListNoteOccurrencesResponse object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other: 'ApiListNoteOccurrencesResponse') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ApiListNoteOccurrencesResponse') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ApiListNotesResponse():
    """
    Response including listed notes.

    :attr List[ApiNote] notes: (optional)
    :attr str next_page_token: (optional) The next pagination token in the list
          response. It should be used as page_token for the following request. An empty
          value means no more result.
    """

    def __init__(self, *, notes: List['ApiNote'] = None, next_page_token: str = None) -> None:
        """
        Initialize a ApiListNotesResponse object.

        :param List[ApiNote] notes: (optional)
        :param str next_page_token: (optional) The next pagination token in the
               list response. It should be used as page_token for the following request.
               An empty value means no more result.
        """
        self.notes = notes
        self.next_page_token = next_page_token

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ApiListNotesResponse':
        """Initialize a ApiListNotesResponse object from a json dictionary."""
        args = {}
        valid_keys = ['notes', 'next_page_token']
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError('Unrecognized keys detected in dictionary for class ApiListNotesResponse: ' + ', '.join(bad_keys))
        if 'notes' in _dict:
            args['notes'] = [ApiNote._from_dict(x) for x in (_dict.get('notes') )]
        if 'next_page_token' in _dict:
            args['next_page_token'] = _dict.get('next_page_token')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ApiListNotesResponse object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'notes') and self.notes is not None:
            _dict['notes'] = [x._to_dict() for x in self.notes]
        if hasattr(self, 'next_page_token') and self.next_page_token is not None:
            _dict['next_page_token'] = self.next_page_token
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ApiListNotesResponse object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other: 'ApiListNotesResponse') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ApiListNotesResponse') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ApiListOccurrencesResponse():
    """
    Response including listed active occurrences.

    :attr List[ApiOccurrence] occurrences: (optional) The occurrences requested.
    :attr str next_page_token: (optional) The next pagination token in the list
          response. It should be used as
          `page_token` for the following request. An empty value means no more results.
    """

    def __init__(self, *, occurrences: List['ApiOccurrence'] = None, next_page_token: str = None) -> None:
        """
        Initialize a ApiListOccurrencesResponse object.

        :param List[ApiOccurrence] occurrences: (optional) The occurrences
               requested.
        :param str next_page_token: (optional) The next pagination token in the
               list response. It should be used as
               `page_token` for the following request. An empty value means no more
               results.
        """
        self.occurrences = occurrences
        self.next_page_token = next_page_token

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ApiListOccurrencesResponse':
        """Initialize a ApiListOccurrencesResponse object from a json dictionary."""
        args = {}
        valid_keys = ['occurrences', 'next_page_token']
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError('Unrecognized keys detected in dictionary for class ApiListOccurrencesResponse: ' + ', '.join(bad_keys))
        if 'occurrences' in _dict:
            args['occurrences'] = [ApiOccurrence._from_dict(x) for x in (_dict.get('occurrences') )]
        if 'next_page_token' in _dict:
            args['next_page_token'] = _dict.get('next_page_token')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ApiListOccurrencesResponse object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'occurrences') and self.occurrences is not None:
            _dict['occurrences'] = [x._to_dict() for x in self.occurrences]
        if hasattr(self, 'next_page_token') and self.next_page_token is not None:
            _dict['next_page_token'] = self.next_page_token
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ApiListOccurrencesResponse object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other: 'ApiListOccurrencesResponse') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ApiListOccurrencesResponse') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ApiListProvidersResponse():
    """
    Response including listed providers.

    :attr List[ApiProvider] providers: (optional)
    """

    def __init__(self, *, providers: List['ApiProvider'] = None) -> None:
        """
        Initialize a ApiListProvidersResponse object.

        :param List[ApiProvider] providers: (optional)
        """
        self.providers = providers

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ApiListProvidersResponse':
        """Initialize a ApiListProvidersResponse object from a json dictionary."""
        args = {}
        valid_keys = ['providers']
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError('Unrecognized keys detected in dictionary for class ApiListProvidersResponse: ' + ', '.join(bad_keys))
        if 'providers' in _dict:
            args['providers'] = [ApiProvider._from_dict(x) for x in (_dict.get('providers') )]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ApiListProvidersResponse object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'providers') and self.providers is not None:
            _dict['providers'] = [x._to_dict() for x in self.providers]
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ApiListProvidersResponse object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other: 'ApiListProvidersResponse') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ApiListProvidersResponse') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ApiNote():
    """
    Provides a detailed description of a `Note`.

    :attr str name: (optional)
    :attr str short_description: A one sentence description of this `Note`.
    :attr str long_description: A detailed description of this `Note`.
    :attr ApiNoteKind kind: Output only. This explicitly denotes which kind of note
          is specified. This
          field can be used as a filter in list requests.
    :attr List[ApiNoteRelatedUrl] related_url: (optional)
    :attr datetime expiration_time: (optional) Time of expiration for this note,
          null if note does not expire.
    :attr datetime create_time: (optional) Output only. The time this note was
          created. This field can be used as a filter in list requests.
    :attr datetime update_time: (optional) Output only. The time this note was last
          updated. This field can be used as a filter in list requests.
    :attr str provider_id: (optional)
    :attr str id:
    :attr bool shared: (optional) True if this `Note` can be shared by multiple
          accounts.
    :attr Reporter reported_by: Details about the reporter of this `Note`.
    :attr FindingType finding: (optional) The finding details of the note.
    :attr KpiType kpi: (optional) The KPI details of the note.
    :attr Card card: (optional) The card details of the note.
    :attr Section section: (optional) The section details of the note.
    """

    def __init__(self, short_description: str, long_description: str, kind: 'ApiNoteKind', id: str, reported_by: 'Reporter', *, name: str = None, related_url: List['ApiNoteRelatedUrl'] = None, expiration_time: datetime = None, create_time: datetime = None, update_time: datetime = None, provider_id: str = None, shared: bool = None, finding: 'FindingType' = None, kpi: 'KpiType' = None, card: 'Card' = None, section: 'Section' = None) -> None:
        """
        Initialize a ApiNote object.

        :param str short_description: A one sentence description of this `Note`.
        :param str long_description: A detailed description of this `Note`.
        :param ApiNoteKind kind: Output only. This explicitly denotes which kind of
               note is specified. This
               field can be used as a filter in list requests.
        :param str id:
        :param Reporter reported_by: Details about the reporter of this `Note`.
        :param str name: (optional)
        :param List[ApiNoteRelatedUrl] related_url: (optional)
        :param datetime expiration_time: (optional) Time of expiration for this
               note, null if note does not expire.
        :param datetime create_time: (optional) Output only. The time this note was
               created. This field can be used as a filter in list requests.
        :param datetime update_time: (optional) Output only. The time this note was
               last updated. This field can be used as a filter in list requests.
        :param bool shared: (optional) True if this `Note` can be shared by
               multiple accounts.
        :param FindingType finding: (optional) The finding details of the note.
        :param KpiType kpi: (optional) The KPI details of the note.
        :param Card card: (optional) The card details of the note.
        :param Section section: (optional) The section details of the note.
        """
        self.name = name
        self.short_description = short_description
        self.long_description = long_description
        self.kind = kind
        self.related_url = related_url
        self.expiration_time = expiration_time
        self.create_time = create_time
        self.update_time = update_time
        self.provider_id = provider_id
        self.id = id
        self.shared = shared
        self.reported_by = reported_by
        self.finding = finding
        self.kpi = kpi
        self.card = card
        self.section = section

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ApiNote':
        """Initialize a ApiNote object from a json dictionary."""
        args = {}
        valid_keys = ['name', 'short_description', 'long_description', 'kind', 'related_url', 'expiration_time', 'create_time', 'update_time', 'provider_id', 'id', 'shared', 'reported_by', 'finding', 'kpi', 'card', 'section']
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError('Unrecognized keys detected in dictionary for class ApiNote: ' + ', '.join(bad_keys))
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        if 'short_description' in _dict:
            args['short_description'] = _dict.get('short_description')
        else:
            raise ValueError('Required property \'short_description\' not present in ApiNote JSON')
        if 'long_description' in _dict:
            args['long_description'] = _dict.get('long_description')
        else:
            raise ValueError('Required property \'long_description\' not present in ApiNote JSON')
        if 'kind' in _dict:
            args['kind'] = ApiNoteKind._from_dict(_dict.get('kind'))
        else:
            raise ValueError('Required property \'kind\' not present in ApiNote JSON')
        if 'related_url' in _dict:
            args['related_url'] = [ApiNoteRelatedUrl._from_dict(x) for x in (_dict.get('related_url') )]
        if 'expiration_time' in _dict:
            args['expiration_time'] = string_to_datetime(_dict.get('expiration_time'))
        if 'create_time' in _dict:
            args['create_time'] = string_to_datetime(_dict.get('create_time'))
        if 'update_time' in _dict:
            args['update_time'] = string_to_datetime(_dict.get('update_time'))
        if 'provider_id' in _dict:
            args['provider_id'] = _dict.get('provider_id')
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        else:
            raise ValueError('Required property \'id\' not present in ApiNote JSON')
        if 'shared' in _dict:
            args['shared'] = _dict.get('shared')
        if 'reported_by' in _dict:
            args['reported_by'] = Reporter._from_dict(_dict.get('reported_by'))
        else:
            raise ValueError('Required property \'reported_by\' not present in ApiNote JSON')
        if 'finding' in _dict:
            args['finding'] = FindingType._from_dict(_dict.get('finding'))
        if 'kpi' in _dict:
            args['kpi'] = KpiType._from_dict(_dict.get('kpi'))
        if 'card' in _dict:
            args['card'] = Card._from_dict(_dict.get('card'))
        if 'section' in _dict:
            args['section'] = Section._from_dict(_dict.get('section'))
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ApiNote object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'short_description') and self.short_description is not None:
            _dict['short_description'] = self.short_description
        if hasattr(self, 'long_description') and self.long_description is not None:
            _dict['long_description'] = self.long_description
        if hasattr(self, 'kind') and self.kind is not None:
            _dict['kind'] = self.kind._to_dict()
        if hasattr(self, 'related_url') and self.related_url is not None:
            _dict['related_url'] = [x._to_dict() for x in self.related_url]
        if hasattr(self, 'expiration_time') and self.expiration_time is not None:
            _dict['expiration_time'] = datetime_to_string(self.expiration_time)
        if hasattr(self, 'create_time') and self.create_time is not None:
            _dict['create_time'] = datetime_to_string(self.create_time)
        if hasattr(self, 'update_time') and self.update_time is not None:
            _dict['update_time'] = datetime_to_string(self.update_time)
        if hasattr(self, 'provider_id') and self.provider_id is not None:
            _dict['provider_id'] = self.provider_id
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'shared') and self.shared is not None:
            _dict['shared'] = self.shared
        if hasattr(self, 'reported_by') and self.reported_by is not None:
            _dict['reported_by'] = self.reported_by._to_dict()
        if hasattr(self, 'finding') and self.finding is not None:
            _dict['finding'] = self.finding._to_dict()
        if hasattr(self, 'kpi') and self.kpi is not None:
            _dict['kpi'] = self.kpi._to_dict()
        if hasattr(self, 'card') and self.card is not None:
            _dict['card'] = self.card._to_dict()
        if hasattr(self, 'section') and self.section is not None:
            _dict['section'] = self.section._to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ApiNote object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other: 'ApiNote') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ApiNote') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ApiNoteKind():
    """
    This must be 1&#58;1 with members of our oneofs, it can be used for filtering Note and
    Occurrence on their kind.
     - FINDING&#58; The note and occurrence represent a finding.
     - KPI&#58; The note and occurrence represent a KPI value.
     - CARD&#58; The note represents a card showing findings and related metric values.
     - CARD_CONFIGURED&#58; The note represents a card configured for a user account.
     - SECTION&#58; The note represents a section in a dashboard.

    """

    def __init__(self) -> None:
        """
        Initialize a ApiNoteKind object.

        """

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ApiNoteKind':
        """Initialize a ApiNoteKind object from a json dictionary."""
        args = {}
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ApiNoteKind object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ApiNoteKind object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other: 'ApiNoteKind') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ApiNoteKind') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ApiNoteRelatedUrl():
    """
    Metadata for any related URL information.

    :attr str label: (optional)
    :attr str url: (optional)
    """

    def __init__(self, *, label: str = None, url: str = None) -> None:
        """
        Initialize a ApiNoteRelatedUrl object.

        :param str label: (optional)
        :param str url: (optional)
        """
        self.label = label
        self.url = url

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ApiNoteRelatedUrl':
        """Initialize a ApiNoteRelatedUrl object from a json dictionary."""
        args = {}
        valid_keys = ['label', 'url']
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError('Unrecognized keys detected in dictionary for class ApiNoteRelatedUrl: ' + ', '.join(bad_keys))
        if 'label' in _dict:
            args['label'] = _dict.get('label')
        if 'url' in _dict:
            args['url'] = _dict.get('url')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ApiNoteRelatedUrl object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'label') and self.label is not None:
            _dict['label'] = self.label
        if hasattr(self, 'url') and self.url is not None:
            _dict['url'] = self.url
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ApiNoteRelatedUrl object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other: 'ApiNoteRelatedUrl') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ApiNoteRelatedUrl') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ApiOccurrence():
    """
    `Occurrence` includes information about analysis occurrences for an image.

    :attr str name: (optional) Output only. The name of the `Occurrence` in the form
          "{account_id}/providers/{provider_id}/occurrences/{occuurence_id}".
    :attr str resource_url: (optional) The unique URL of the resource, image or the
          container, for which the `Occurrence` applies. For example,
          https://gcr.io/provider/image@sha256:foo. This field can be used as a filter in
          list requests.
    :attr str note_name: An analysis note associated with this image, in the form
          "{account_id}/providers/{provider_id}/notes/{note_id}" This field can be used as
          a filter in list requests.
    :attr ApiNoteKind kind: Output only. This explicitly denotes which of the
          `Occurrence` details are specified.
          This field can be used as a filter in list requests.
    :attr str remediation: (optional)
    :attr datetime create_time: (optional) Output only. The time this `Occurrence`
          was created.
    :attr datetime update_time: (optional) Output only. The time this `Occurrence`
          was last updated.
    :attr str provider_id: (optional)
    :attr str id:
    :attr Context context: (optional) Details about the context of this
          `Occurrence`.
    :attr Finding finding: (optional) Details of the occurrence of a finding.
    :attr Kpi kpi: (optional) Details of the occurrence of a KPI.
    """

    def __init__(self, note_name: str, kind: 'ApiNoteKind', id: str, *, name: str = None, resource_url: str = None, remediation: str = None, create_time: datetime = None, update_time: datetime = None, provider_id: str = None, context: 'Context' = None, finding: 'Finding' = None, kpi: 'Kpi' = None) -> None:
        """
        Initialize a ApiOccurrence object.

        :param str note_name: An analysis note associated with this image, in the
               form "{account_id}/providers/{provider_id}/notes/{note_id}" This field can
               be used as a filter in list requests.
        :param ApiNoteKind kind: Output only. This explicitly denotes which of the
               `Occurrence` details are specified.
               This field can be used as a filter in list requests.
        :param str id:
        :param str name: (optional) Output only. The name of the `Occurrence` in
               the form
               "{account_id}/providers/{provider_id}/occurrences/{occuurence_id}".
        :param str resource_url: (optional) The unique URL of the resource, image
               or the container, for which the `Occurrence` applies. For example,
               https://gcr.io/provider/image@sha256:foo. This field can be used as a
               filter in list requests.
        :param str remediation: (optional)
        :param datetime create_time: (optional) Output only. The time this
               `Occurrence` was created.
        :param datetime update_time: (optional) Output only. The time this
               `Occurrence` was last updated.
        :param str provider_id: (optional)
        :param Context context: (optional) Details about the context of this
               `Occurrence`.
        :param Finding finding: (optional) Details of the occurrence of a finding.
        :param Kpi kpi: (optional) Details of the occurrence of a KPI.
        """
        self.name = name
        self.resource_url = resource_url
        self.note_name = note_name
        self.kind = kind
        self.remediation = remediation
        self.create_time = create_time
        self.update_time = update_time
        self.provider_id = provider_id
        self.id = id
        self.context = context
        self.finding = finding
        self.kpi = kpi

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ApiOccurrence':
        """Initialize a ApiOccurrence object from a json dictionary."""
        args = {}
        valid_keys = ['name', 'resource_url', 'note_name', 'kind', 'remediation', 'create_time', 'update_time', 'provider_id', 'id', 'context', 'finding', 'kpi']
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError('Unrecognized keys detected in dictionary for class ApiOccurrence: ' + ', '.join(bad_keys))
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        if 'resource_url' in _dict:
            args['resource_url'] = _dict.get('resource_url')
        if 'note_name' in _dict:
            args['note_name'] = _dict.get('note_name')
        else:
            raise ValueError('Required property \'note_name\' not present in ApiOccurrence JSON')
        if 'kind' in _dict:
            args['kind'] = ApiNoteKind._from_dict(_dict.get('kind'))
        else:
            raise ValueError('Required property \'kind\' not present in ApiOccurrence JSON')
        if 'remediation' in _dict:
            args['remediation'] = _dict.get('remediation')
        if 'create_time' in _dict:
            args['create_time'] = string_to_datetime(_dict.get('create_time'))
        if 'update_time' in _dict:
            args['update_time'] = string_to_datetime(_dict.get('update_time'))
        if 'provider_id' in _dict:
            args['provider_id'] = _dict.get('provider_id')
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        else:
            raise ValueError('Required property \'id\' not present in ApiOccurrence JSON')
        if 'context' in _dict:
            args['context'] = Context._from_dict(_dict.get('context'))
        if 'finding' in _dict:
            args['finding'] = Finding._from_dict(_dict.get('finding'))
        if 'kpi' in _dict:
            args['kpi'] = Kpi._from_dict(_dict.get('kpi'))
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ApiOccurrence object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'resource_url') and self.resource_url is not None:
            _dict['resource_url'] = self.resource_url
        if hasattr(self, 'note_name') and self.note_name is not None:
            _dict['note_name'] = self.note_name
        if hasattr(self, 'kind') and self.kind is not None:
            _dict['kind'] = self.kind._to_dict()
        if hasattr(self, 'remediation') and self.remediation is not None:
            _dict['remediation'] = self.remediation
        if hasattr(self, 'create_time') and self.create_time is not None:
            _dict['create_time'] = datetime_to_string(self.create_time)
        if hasattr(self, 'update_time') and self.update_time is not None:
            _dict['update_time'] = datetime_to_string(self.update_time)
        if hasattr(self, 'provider_id') and self.provider_id is not None:
            _dict['provider_id'] = self.provider_id
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'context') and self.context is not None:
            _dict['context'] = self.context._to_dict()
        if hasattr(self, 'finding') and self.finding is not None:
            _dict['finding'] = self.finding._to_dict()
        if hasattr(self, 'kpi') and self.kpi is not None:
            _dict['kpi'] = self.kpi._to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ApiOccurrence object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other: 'ApiOccurrence') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ApiOccurrence') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ApiProvider():
    """
    Provides a detailed description of a `Provider`.

    :attr str name:
    :attr str id:
    """

    def __init__(self, name: str, id: str) -> None:
        """
        Initialize a ApiProvider object.

        :param str name:
        :param str id:
        """
        self.name = name
        self.id = id

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ApiProvider':
        """Initialize a ApiProvider object from a json dictionary."""
        args = {}
        valid_keys = ['name', 'id']
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError('Unrecognized keys detected in dictionary for class ApiProvider: ' + ', '.join(bad_keys))
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        else:
            raise ValueError('Required property \'name\' not present in ApiProvider JSON')
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        else:
            raise ValueError('Required property \'id\' not present in ApiProvider JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ApiProvider object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ApiProvider object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other: 'ApiProvider') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ApiProvider') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class BreakdownCardElement(CardElement):
    """
    A card element with a breakdown of values.

    :attr str text: The text of this card element.
    :attr str direction: (optional) The direction of this breakdown card element.
    :attr List[ValueType] value_types: the value types associated to this card
          element.
    """

    def __init__(self, kind: str, text: str, value_types: List['ValueType'], *, default_time_range: str = None, direction: str = None) -> None:
        """
        Initialize a BreakdownCardElement object.

        :param str kind: Kind of element
               - NUMERIC&#58; Single numeric value
               - BREAKDOWN&#58; Breakdown of numeric values
               - TIME_SERIES&#58; Time-series of numeric values.
        :param str text: The text of this card element.
        :param List[ValueType] value_types: the value types associated to this card
               element.
        :param str default_time_range: (optional) The default time range of this
               card element.
        :param str direction: (optional) The direction of this breakdown card
               element.
        """
        self.kind = kind
        self.default_time_range = default_time_range
        self.text = text
        self.direction = direction
        self.value_types = value_types

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'BreakdownCardElement':
        """Initialize a BreakdownCardElement object from a json dictionary."""
        args = {}
        valid_keys = ['kind', 'default_time_range', 'text', 'direction', 'value_types']
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError('Unrecognized keys detected in dictionary for class BreakdownCardElement: ' + ', '.join(bad_keys))
        if 'kind' in _dict:
            args['kind'] = _dict.get('kind')
        else:
            raise ValueError('Required property \'kind\' not present in BreakdownCardElement JSON')
        if 'default_time_range' in _dict:
            args['default_time_range'] = _dict.get('default_time_range')
        if 'text' in _dict:
            args['text'] = _dict.get('text')
        else:
            raise ValueError('Required property \'text\' not present in BreakdownCardElement JSON')
        if 'direction' in _dict:
            args['direction'] = _dict.get('direction')
        if 'value_types' in _dict:
            args['value_types'] = [ValueType._from_dict(x) for x in (_dict.get('value_types') )]
        else:
            raise ValueError('Required property \'value_types\' not present in BreakdownCardElement JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a BreakdownCardElement object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'kind') and self.kind is not None:
            _dict['kind'] = self.kind
        if hasattr(self, 'default_time_range') and self.default_time_range is not None:
            _dict['default_time_range'] = self.default_time_range
        if hasattr(self, 'text') and self.text is not None:
            _dict['text'] = self.text
        if hasattr(self, 'direction') and self.direction is not None:
            _dict['direction'] = self.direction
        if hasattr(self, 'value_types') and self.value_types is not None:
            _dict['value_types'] = [x._to_dict() for x in self.value_types]
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this BreakdownCardElement object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other: 'BreakdownCardElement') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'BreakdownCardElement') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    
    class KindEnum(Enum):
        """
        Kind of element
        - NUMERIC&#58; Single numeric value
        - BREAKDOWN&#58; Breakdown of numeric values
        - TIME_SERIES&#58; Time-series of numeric values.
        """
        NUMERIC = "NUMERIC"
        BREAKDOWN = "BREAKDOWN"
        TIME_SERIES = "TIME_SERIES"


class FindingCountValueType(ValueType):
    """
    FindingCountValueType.

    :attr List[str] finding_note_names: the names of the finding note associated
          that act as filters for counting the occurrences.
    """

    def __init__(self, kind: str, text: str, finding_note_names: List[str]) -> None:
        """
        Initialize a FindingCountValueType object.

        :param str kind: Kind of element
               - KPI&#58; Kind of value derived from a KPI occurrence
               - FINDING_COUNT&#58; Kind of value derived from a count of finding
               occurrences.
        :param str text: The text of this element type.
        :param List[str] finding_note_names: the names of the finding note
               associated that act as filters for counting the occurrences.
        """
        self.kind = kind
        self.text = text
        self.finding_note_names = finding_note_names

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'FindingCountValueType':
        """Initialize a FindingCountValueType object from a json dictionary."""
        args = {}
        valid_keys = ['kind', 'text', 'finding_note_names']
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError('Unrecognized keys detected in dictionary for class FindingCountValueType: ' + ', '.join(bad_keys))
        if 'kind' in _dict:
            args['kind'] = _dict.get('kind')
        else:
            raise ValueError('Required property \'kind\' not present in FindingCountValueType JSON')
        if 'text' in _dict:
            args['text'] = _dict.get('text')
        else:
            raise ValueError('Required property \'text\' not present in FindingCountValueType JSON')
        if 'finding_note_names' in _dict:
            args['finding_note_names'] = _dict.get('finding_note_names')
        else:
            raise ValueError('Required property \'finding_note_names\' not present in FindingCountValueType JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a FindingCountValueType object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'kind') and self.kind is not None:
            _dict['kind'] = self.kind
        if hasattr(self, 'text') and self.text is not None:
            _dict['text'] = self.text
        if hasattr(self, 'finding_note_names') and self.finding_note_names is not None:
            _dict['finding_note_names'] = self.finding_note_names
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this FindingCountValueType object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other: 'FindingCountValueType') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'FindingCountValueType') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    
    class KindEnum(Enum):
        """
        Kind of element
        - KPI&#58; Kind of value derived from a KPI occurrence
        - FINDING_COUNT&#58; Kind of value derived from a count of finding occurrences.
        """
        KPI = "KPI"
        FINDING = "FINDING"


class KpiValueType(ValueType):
    """
    KpiValueType.

    :attr str kpi_note_name: The name of the kpi note associated to the occurrence
          with the value for this card element value type.
    """

    def __init__(self, kind: str, text: str, kpi_note_name: str) -> None:
        """
        Initialize a KpiValueType object.

        :param str kind: Kind of element
               - KPI&#58; Kind of value derived from a KPI occurrence
               - FINDING_COUNT&#58; Kind of value derived from a count of finding
               occurrences.
        :param str text: The text of this element type.
        :param str kpi_note_name: The name of the kpi note associated to the
               occurrence with the value for this card element value type.
        """
        self.kind = kind
        self.text = text
        self.kpi_note_name = kpi_note_name

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'KpiValueType':
        """Initialize a KpiValueType object from a json dictionary."""
        args = {}
        valid_keys = ['kind', 'text', 'kpi_note_name']
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError('Unrecognized keys detected in dictionary for class KpiValueType: ' + ', '.join(bad_keys))
        if 'kind' in _dict:
            args['kind'] = _dict.get('kind')
        else:
            raise ValueError('Required property \'kind\' not present in KpiValueType JSON')
        if 'text' in _dict:
            args['text'] = _dict.get('text')
        else:
            raise ValueError('Required property \'text\' not present in KpiValueType JSON')
        if 'kpi_note_name' in _dict:
            args['kpi_note_name'] = _dict.get('kpi_note_name')
        else:
            raise ValueError('Required property \'kpi_note_name\' not present in KpiValueType JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a KpiValueType object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'kind') and self.kind is not None:
            _dict['kind'] = self.kind
        if hasattr(self, 'text') and self.text is not None:
            _dict['text'] = self.text
        if hasattr(self, 'kpi_note_name') and self.kpi_note_name is not None:
            _dict['kpi_note_name'] = self.kpi_note_name
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this KpiValueType object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other: 'KpiValueType') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'KpiValueType') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    
    class KindEnum(Enum):
        """
        Kind of element
        - KPI&#58; Kind of value derived from a KPI occurrence
        - FINDING_COUNT&#58; Kind of value derived from a count of finding occurrences.
        """
        KPI = "KPI"
        FINDING = "FINDING"


class NumericCardElement(CardElement):
    """
    A card element with a single numeric value.

    :attr str text: The text of this card element.
    :attr object value_type:
    """

    def __init__(self, kind: str, text: str, value_type: object, *, default_time_range: str = None) -> None:
        """
        Initialize a NumericCardElement object.

        :param str kind: Kind of element
               - NUMERIC&#58; Single numeric value
               - BREAKDOWN&#58; Breakdown of numeric values
               - TIME_SERIES&#58; Time-series of numeric values.
        :param str text: The text of this card element.
        :param object value_type:
        :param str default_time_range: (optional) The default time range of this
               card element.
        """
        self.kind = kind
        self.default_time_range = default_time_range
        self.text = text
        self.value_type = value_type

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'NumericCardElement':
        """Initialize a NumericCardElement object from a json dictionary."""
        args = {}
        valid_keys = ['kind', 'default_time_range', 'text', 'value_type']
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError('Unrecognized keys detected in dictionary for class NumericCardElement: ' + ', '.join(bad_keys))
        if 'kind' in _dict:
            args['kind'] = _dict.get('kind')
        else:
            raise ValueError('Required property \'kind\' not present in NumericCardElement JSON')
        if 'default_time_range' in _dict:
            args['default_time_range'] = _dict.get('default_time_range')
        if 'text' in _dict:
            args['text'] = _dict.get('text')
        else:
            raise ValueError('Required property \'text\' not present in NumericCardElement JSON')
        if 'value_type' in _dict:
            args['value_type'] = _dict.get('value_type')
        else:
            raise ValueError('Required property \'value_type\' not present in NumericCardElement JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a NumericCardElement object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'kind') and self.kind is not None:
            _dict['kind'] = self.kind
        if hasattr(self, 'default_time_range') and self.default_time_range is not None:
            _dict['default_time_range'] = self.default_time_range
        if hasattr(self, 'text') and self.text is not None:
            _dict['text'] = self.text
        if hasattr(self, 'value_type') and self.value_type is not None:
            _dict['value_type'] = self.value_type
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this NumericCardElement object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other: 'NumericCardElement') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'NumericCardElement') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    
    class KindEnum(Enum):
        """
        Kind of element
        - NUMERIC&#58; Single numeric value
        - BREAKDOWN&#58; Breakdown of numeric values
        - TIME_SERIES&#58; Time-series of numeric values.
        """
        NUMERIC = "NUMERIC"
        BREAKDOWN = "BREAKDOWN"
        TIME_SERIES = "TIME_SERIES"


class TimeSeriesCardElement(CardElement):
    """
    A card element with a time series chart.

    :attr str text: The text of this card element.
    :attr str default_interval: (optional) The default interval of the time series.
    :attr List[ValueType] value_types: the value types associated to this card
          element.
    """

    def __init__(self, kind: str, text: str, value_types: List['ValueType'], *, default_time_range: str = None, default_interval: str = None) -> None:
        """
        Initialize a TimeSeriesCardElement object.

        :param str kind: Kind of element
               - NUMERIC&#58; Single numeric value
               - BREAKDOWN&#58; Breakdown of numeric values
               - TIME_SERIES&#58; Time-series of numeric values.
        :param str text: The text of this card element.
        :param List[ValueType] value_types: the value types associated to this card
               element.
        :param str default_time_range: (optional) The default time range of this
               card element.
        :param str default_interval: (optional) The default interval of the time
               series.
        """
        self.kind = kind
        self.default_time_range = default_time_range
        self.text = text
        self.default_interval = default_interval
        self.value_types = value_types

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'TimeSeriesCardElement':
        """Initialize a TimeSeriesCardElement object from a json dictionary."""
        args = {}
        valid_keys = ['kind', 'default_time_range', 'text', 'default_interval', 'value_types']
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError('Unrecognized keys detected in dictionary for class TimeSeriesCardElement: ' + ', '.join(bad_keys))
        if 'kind' in _dict:
            args['kind'] = _dict.get('kind')
        else:
            raise ValueError('Required property \'kind\' not present in TimeSeriesCardElement JSON')
        if 'default_time_range' in _dict:
            args['default_time_range'] = _dict.get('default_time_range')
        if 'text' in _dict:
            args['text'] = _dict.get('text')
        else:
            raise ValueError('Required property \'text\' not present in TimeSeriesCardElement JSON')
        if 'default_interval' in _dict:
            args['default_interval'] = _dict.get('default_interval')
        if 'value_types' in _dict:
            args['value_types'] = [ValueType._from_dict(x) for x in (_dict.get('value_types') )]
        else:
            raise ValueError('Required property \'value_types\' not present in TimeSeriesCardElement JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a TimeSeriesCardElement object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'kind') and self.kind is not None:
            _dict['kind'] = self.kind
        if hasattr(self, 'default_time_range') and self.default_time_range is not None:
            _dict['default_time_range'] = self.default_time_range
        if hasattr(self, 'text') and self.text is not None:
            _dict['text'] = self.text
        if hasattr(self, 'default_interval') and self.default_interval is not None:
            _dict['default_interval'] = self.default_interval
        if hasattr(self, 'value_types') and self.value_types is not None:
            _dict['value_types'] = [x._to_dict() for x in self.value_types]
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this TimeSeriesCardElement object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other: 'TimeSeriesCardElement') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'TimeSeriesCardElement') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    
    class KindEnum(Enum):
        """
        Kind of element
        - NUMERIC&#58; Single numeric value
        - BREAKDOWN&#58; Breakdown of numeric values
        - TIME_SERIES&#58; Time-series of numeric values.
        """
        NUMERIC = "NUMERIC"
        BREAKDOWN = "BREAKDOWN"
        TIME_SERIES = "TIME_SERIES"


