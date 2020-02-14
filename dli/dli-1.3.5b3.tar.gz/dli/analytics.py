from urllib.parse import urljoin

import dli
from dli.client.components.urls import consumption_urls


class AnalyticsHandler:
    __acceptable_properties = [
        'package_id', 'dataset_id', 'name', 'dataset_name', 'datafile_id',
        'dictionary_id', 'api_key'
    ]

    def __init__(self, dli_client):
        self._app_name = 'SDK'
        self._app_version = dli.__version__
        self._client = dli_client
        self._logger = dli_client.logger

    def create_event(
        self, user_id, organisation_id,
        entity=None, action=None, properties=None, result_status_code=None
    ):
        self._log_call_handling_exceptions(
            user_id, organisation_id, entity, action, properties,
            result_status_code
        )

    def _log_call_handling_exceptions(
        self, user_id, organisation_id, entity, action, properties, result
    ):
        try:
            body = self._prepare_body_to_send(
                user_id, organisation_id, entity, action, properties, result,
            )
            self._send_event_to_analytics(body)
        except Exception as e:
            self._logger.exception('Error while sending analytics: ', e)

    def _prepare_body_to_send(
        self, user_id, organisation_id, entity, action, properties, result
    ):
        properties_to_send = self._filter_out_properties(properties)
        properties_to_send = self._override_properties_for_dataset_functions(
            action, entity, properties, properties_to_send)
        if 'api_key' in properties:
            properties['api_key'] = properties['api_key'][:6]
        event = {
            'application_name': self._app_name,
            'application_version': self._app_version,
            'user_id': user_id,
            'entity': entity,
            'action': action,
            'organisation_id': organisation_id,
            'result': result,
            'properties': properties_to_send
        }
        body = {'data': [{'attributes': event}]}
        return body

    def _filter_out_properties(self, properties):
        return {
            k: v
            for k, v in properties.items() if k in self.__acceptable_properties
        }

    # This is ugly, but 1) register_dataset accepts builder,
    # so we need to extract data from it 2) some functions accept 'id'
    # instead of dataset_id. We either ovveride it like this or not make it
    # generic at all.
    def _override_properties_for_dataset_functions(
            self, action, entity, properties, props
    ):
        if entity == 'Dataset':
            if action == 'register_dataset':
                props = self._filter_out_properties(properties['builder']._data)
            elif 'id' in properties:
                props['dataset_id'] = properties['id']
        return props

    def _send_event_to_analytics(self, body):
        url = urljoin(
            self._client._environment.consumption,
            consumption_urls.consumption_analytics
        )
        if not self._client._session.has_expired:
            self._client._session.post(url, json=body)
