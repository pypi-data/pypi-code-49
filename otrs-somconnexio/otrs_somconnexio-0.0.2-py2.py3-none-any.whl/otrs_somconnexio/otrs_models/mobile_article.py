# coding: utf-8
from pyotrs.lib import Article


class MobileArticle():
    def __init__(self, service_type, eticom_contract):
        self.service_type = service_type
        self.eticom_contract = eticom_contract

    def call(self):
        return Article({
            "Subject": "Sol·licitud {} {}".format(
                self.service_type,
                self.eticom_contract.id
            ),
            "Body": "",
            "ContentType": "text/plain; charset=utf8"
        })
