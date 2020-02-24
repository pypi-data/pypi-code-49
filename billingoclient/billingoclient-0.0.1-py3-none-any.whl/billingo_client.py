from typing import Dict, Any, Union, List

import requests

from dto.invoice import Invoice
from jwt_header import JwtHeader


class BillingoClient:
    api_url = 'https://www.billingo.hu/api'

    def __init__(self, public_key: str, private_key: str, leeway: int = 60):
        self.jwt_header = JwtHeader(public_key, private_key, leeway)

    def list_invoices(self, page: int = 1, max_per_page: int = 20) -> Dict[int, Invoice]:
        assert 0 < max_per_page <= 50
        j_list = self._request('get', f'/invoices?page={page}&max_per_page={max_per_page}')
        return {i['id']: Invoice.parse_obj(i['attributes']) for i in j_list}

    def get_invoice(self, id: int) -> Invoice:
        response_json = self._request('get', f'/invoices/{id}')
        if not response_json: raise Exception(f'Invoice not found with id {id}')
        invoice_json = response_json[0]['attributes']
        return Invoice.parse_obj(invoice_json)

    def get_currency(self, value: float, *, change_from: str, change_to: str) -> float:
        """https://billingo.readthedocs.io/en/latest/currency/"""
        response_json = self._request('get', f'/currency?from={change_from}&to={change_to}&value={value}')
        if not response_json: raise Exception(f'Could not change currency from {change_from} to {change_to}. Value: {value}')
        return response_json['value']

    def _request(self, method: str, endpoint: str) -> Union[Dict[str, Any], List[Dict[str, Any]]]:
        response = requests.request(method, BillingoClient.api_url + endpoint, headers=self.jwt_header.generate())
        return self._handle_response(response)

    @staticmethod
    def _handle_response(response: requests.Response) -> Union[Dict[str, Any], List[Dict[str, Any]]]:
        response_json = response.json()
        if response.status_code == 200 and response_json and response_json.get('success'):
            return response_json.get('data')
        if response_json and response_json.get('error'):
            raise Exception(f'API error. Status code: {response.status_code}, error: {response_json.get("error")}')
        raise Exception(f'Unknown API error. Status code: {response.status_code}')
