from requests import Session
from datetime import datetime
from typing import Optional, Union
from urllib.parse import urlencode

from .helpers import generate_list_get_param, convert
from .exceptions import K50APIException


class K50Client(object):
    API_URL = 'https://api.tracker.k50.ru/api/v2'

    def __init__(self, access_token: str) -> None:
        self.access_token = access_token
        self._session = Session()
        self._session.headers['apiKey'] = self.access_token

    def _send_api_request(self, http_method: str, url: str, params: Optional[dict] = None,
                          csv=False) -> Union[dict, str]:
        response = self._session.__getattribute__(http_method)(url, json=params)
        if response.status_code > 204:
            raise K50APIException(response.json()['error'])
        return response.json() if not csv else response.content.decode('utf-8')

    def get_projects(self) -> dict:
        """
        doc - https://help.k50.ru/tracker-api/api-requests/get-counters-list/
        :return: dict
        """
        url = 'https://api.tracker.k50.ru/api/me'
        return self._send_api_request('get', url=url)

    def get_pool_list(self, counter: int, page: int = 1, items_per_page: int = 1000) -> dict:
        """
        doc - https://help.k50.ru/tracker-api/api-requests/get-pool/
        :param counter: int (counter for project)
        :param page: int default - 1
        :param items_per_page: int default 1000
        :return: dict
        """
        params = {'counter': counter, 'page': page, 'itemsPerPage': items_per_page}
        url = f'{self.API_URL}/pool/list/?{urlencode(params)}'
        return self._send_api_request('get', url)

    def get_call_stats(self, counter: int, dimensions: list, filter_: Optional[str] = None,
                       page: int = 1, items_per_page: int = 1000, csv: bool = False) -> Union[dict, str]:
        """
        doc - https://help.k50.ru/tracker-api/api-requests/get-calls-stat-v2/
        :param counter: counter: int (counter for project)
        :param dimensions: list (list of dimensions)
        :param filter_: optional str
        :param page: int default - 1
        :param items_per_page: int default 1000
        :param csv: bool default False
        :return: dict
        """
        return self._get_stats('call', counter, dimensions, filter_, page, items_per_page, csv)

    def _get_stats(self, entity: str, counter: int, dimensions: list, filter_: Optional[str] = None,
                   page: int = 1, items_per_page: int = 1000, csv: bool = False) -> Union[dict, str]:
        """
        :param entity: counter: str
        :param counter: counter: int (counter for project)
        :param dimensions: list (list of dimensions)
        :param filter_: optional str
        :param page: int default - 1
        :param items_per_page: int default 1000
        :param csv: bool default False
        :return: dict
        """
        params = {'counter': counter, 'dimensions': dimensions, 'page': page, 'itemsPerPage': items_per_page}
        if filter_:
            params['filter'] = filter_
        url = f'{self.API_URL}/{entity}/list/' if not csv else f'{self.API_URL}/{entity}/list/csv'
        return self._send_api_request('post', url, params=params, csv=csv)

    def get_order_stats(self, counter: int, dimensions: list, filter_: Optional[str] = None,
                        page: int = 1, items_per_page: int = 1000, csv: bool = False) -> Union[dict, str]:
        """
        doc - https://help.k50.ru/tracker-api/api-requests/get-orders-stat-v2/
        :param counter: counter: int (counter for project)
        :param dimensions: list (list of dimensions)
        :param filter_: optional str
        :param page: int default - 1
        :param items_per_page: int default 1000
        :param csv: bool default False
        :return: dict
        """
        return self._get_stats('order', counter, dimensions, filter_, page, items_per_page, csv)

    def get_tags(self, counter: int, page: int = 1, items_per_page: int = 1000, csv: bool = False) -> Union[dict, str]:
        """
        doc -https://help.k50.ru/tracker-api/api-requests/get-tags/
        :param counter: counter: int (counter for project)
        :param page: int default - 1
        :param items_per_page: int default 1000
        :param csv: bool default False
        :return: dict
        """
        params = {'counter': counter, 'page': page, 'itemsPerPage': items_per_page}
        url = f'{self.API_URL}/tag/list/?{urlencode(params)}' if not csv else f'{self.API_URL}/tag/list/csv' \
                                                                              f'?{urlencode(params)}'
        return self._send_api_request('get', url, csv=csv)

    def get_leads(self, counter: int, dimensions: list, is_show_inter_action_chain: bool = False,
                  filter_: Optional[str] = None, page: int = 1, items_per_page: int = 10000,
                  csv: bool = False) -> Union[dict, str]:
        """
        doc - https://help.k50.ru/tracker-api/api-requests/get-leads/
        :param counter: int
        :param dimensions: list
        :param is_show_inter_action_chain: bool
        :param filter_: str
        :param page: int
        :param items_per_page: int
        :param csv: bool
        :return:
        """
        params = {'counter': counter, 'dimensions': dimensions, 'page': page, 'itemsPerPage': items_per_page}
        if is_show_inter_action_chain:
            params['isShowInterActionChain'] = is_show_inter_action_chain
        if filter_:
            params['filter'] = filter_
        url = f'{self.API_URL}/leads/list/' if not csv else f'{self.API_URL}/leads/list/csv'
        return self._send_api_request('post', url, params=params, csv=csv)

    def get_reports(self, counter: int, dimensions: list, metrics: list, date_from: datetime,
                    date_to: datetime, limit: int = 1000, offset: int = 1000, order_by: Optional[dict] = None,
                    csv: bool = False) -> Union[dict, str]:
        """
        doc - https://help.k50.ru/tracker-api/api-requests/get-reports/
        :param counter: int
        :param dimensions: list
        :param metrics: list
        :param date_from: datetime
        :param date_to: datetime
        :param limit: int
        :param offset: int
        :param order_by: dict
        :param csv: bool
        :return: Union(dict or string)
        """
        endpoint_url = f'https://api.tracker.k50.ru/api/counter/reports?' if not csv else \
            f'https://api.tracker.k50.ru/api/counter/reports/csv?'
        default_params = urlencode({'counterId': counter, 'limit': limit, 'offset': offset})
        dimensions_param = generate_list_get_param('dimensions', dimensions)
        metrics_param = generate_list_get_param('metrics', metrics)
        period = f'&period[from]={date_from}&period[to]={date_to}'
        endpoint_url += default_params + dimensions_param + metrics_param + period
        if order_by:
            order_by_param = ''
            for k, v in order_by.items():
                order_by_param += f'&orderBy[{key}]={v}'
            endpoint_url += order_by_param
        return self._send_api_request('get', endpoint_url, csv=csv)

    def _add_or_update_call(self, method: str, counter: int, call_id: str, start_time: datetime, caller_phone: str,
                            called_phone: str, **kwargs) -> dict:
        params = {
            'counter': counter,
            'callId': call_id,
            'startTime': start_time.strftime('%Y-%m-%d %H:%M:%S'),
            'callerPhone': caller_phone,
            'calledPhone': called_phone,
        }
        if kwargs:
            kwargs = {convert(key): value for key, value in kwargs.items()}
            params.update(**kwargs)
        url = f'{self.API_URL}/call/{method}/'
        return self._send_api_request('post', url, params=params)

    def add_call(self, counter: int, call_id: str, start_time: datetime, caller_phone: str, called_phone: str,
                 **kwargs) -> dict:
        """
        doc - https://help.k50.ru/tracker-api/api-requests/add-calls/
        :param counter: int
        :param call_id: str
        :param start_time: datetime
        :param caller_phone: str
        :param called_phone: str
        :param kwargs: dict
        :return: dict
        """
        return self._add_or_update_call('add', counter, call_id, start_time, caller_phone, called_phone, **kwargs)

    def update_call(self, counter: int, call_id: str, start_time: datetime, caller_phone: str, called_phone: str,
                    **kwargs) -> dict:
        """
        doc - https://help.k50.ru/tracker-api/api-requests/update-calls/
        :param counter: int
        :param call_id: str
        :param start_time: datetime
        :param caller_phone: str
        :param called_phone: str
        :param kwargs: dict
        :return: dict
        """
        return self._add_or_update_call('update', counter, call_id, start_time, caller_phone, called_phone, **kwargs)

    def _add_or_update_order(self, method: str, counter: int, order_id: str, date_time: datetime,
                             sid: Optional[str] = None, uuid_: Optional[str] = None,
                             caller_phone: Optional[str] = None, margin: Optional[float] = None,
                             revenue: Optional[float] = None, contact_person: Optional[dict] = None,
                             email: Optional[str] = None, comment: Optional[str] = None,
                             tags: Optional[list] = None) -> dict:
        """
        :param method: str
        :param counter: int
        :param order_id: str
        :param date_time: datetime
        :param sid: str
        :param uuid_: str
        :param caller_phone: str
        :param margin: float
        :param revenue: float
        :param contact_person: dict
        :param email: str
        :param comment: str
        :param tags: list
        :return: dict
        """
        params = {
            "counter": counter,
            "orderId": order_id,
            "dateTime": date_time,
        }
        if sid is not None:
            params['sid'] = sid
        if uuid_ is not None:
            params['uuid'] = uuid_
        if caller_phone is not None:
            params['callerPhone'] = caller_phone
        if margin is not None:
            params['margin'] = margin
        if revenue is not None:
            params['revenue'] = revenue
        if contact_person is not None:
            params['contactPerson'] = contact_person
        if email is not None:
            params['email'] = email
        if comment is not None:
            params['comment'] = comment
        if tags is not None:
            params['tags'] = tags
        url = f'{self.API_URL}/order/{method}/'
        return self._send_api_request('post', url, params=params)

    def add_order(self, counter: int, order_id: str, date_time: datetime,
                  sid: Optional[str] = None, uuid_: Optional[str] = None,
                  caller_phone: Optional[str] = None, margin: Optional[float] = None,
                  revenue: Optional[float] = None, contact_person: Optional[dict] = None,
                  email: Optional[str] = None, comment: Optional[str] = None,
                  tags: Optional[list] = None) -> dict:
        """
        doc - https://help.k50.ru/tracker-api/api-requests/add-orders-stat-v2/
        :param counter: int
        :param order_id: str
        :param date_time: datetime
        :param sid: str
        :param uuid_: str
        :param caller_phone: str
        :param margin: float
        :param revenue: float
        :param contact_person: dict
        :param email: str
        :param comment: str
        :param tags: list
        :return: dic
        """
        return self._add_or_update_order('add', **locals())

    def update_order(self, counter: int, order_id: str, date_time: datetime,
                     sid: Optional[str] = None, uuid_: Optional[str] = None,
                     caller_phone: Optional[str] = None, margin: Optional[float] = None,
                     revenue: Optional[float] = None, contact_person: Optional[dict] = None,
                     email: Optional[str] = None, comment: Optional[str] = None,
                     tags: Optional[list] = None) -> dict:
        """
        doc - https://help.k50.ru/tracker-api/api-requests/update-orders-stat-v2/
        :param counter: int
        :param order_id: str
        :param date_time: datetime
        :param sid: str
        :param uuid_: str
        :param caller_phone: str
        :param margin: float
        :param revenue: float
        :param contact_person: dict
        :param email: str
        :param comment: str
        :param tags: list
        :return: dic
        """
        return self._add_or_update_order('update', **locals())

    def _add_or_remove_tags_to_calls(self, operation: str, counter: int, call_ids: list, tags: list) -> dict:
        """
        :param operation: str
        :param counter: int
        :param call_ids: list
        :param tags: list
        :return: dict
        """
        params = {'counter': counter, 'callIds': call_ids, 'tags': tags}
        url = f'{self.API_URL}/calls/{operation}/'
        return self._send_api_request('post', url, params=params)

    def add_tags_to_calls(self, counter: int, call_ids: list, tags: list) -> dict:
        """
        doc - https://help.k50.ru/tracker-api/api-requests/add-call-tags/
        :param counter: int
        :param call_ids: list
        :param tags: list
        :return: dict
        """
        return self._add_or_remove_tags_to_calls('addTags', counter, call_ids, tags)

    def remove_tags_from_calls(self, counter: int, call_ids: list, tags: list) -> dict:
        """
        doc - https://help.k50.ru/tracker-api/api-requests/add-call-tags/
        :param counter: int
        :param call_ids: list
        :param tags: list
        :return: dict
        """
        return self._add_or_remove_tags_to_calls('removeTags', counter, call_ids, tags)

