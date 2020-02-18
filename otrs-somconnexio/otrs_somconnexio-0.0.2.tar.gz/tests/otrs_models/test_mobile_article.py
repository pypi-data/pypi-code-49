# coding: utf-8
import unittest
from mock import Mock, patch

from otrs_somconnexio.otrs_models.mobile_article import MobileArticle


class MobileArticleTestCase(unittest.TestCase):

    @patch('otrs_somconnexio.otrs_models.mobile_article.Article')
    def test_call(self, MockArticle):
        service_type = 'mobile'
        eticom_contract = Mock(spec=['id'])
        eticom_contract.id = 123

        expected_article_arguments = {
            "Subject": "Sol·licitud mobile 123",
            "Body": "",
            "ContentType": "text/plain; charset=utf8"
        }

        MobileArticle(service_type, eticom_contract).call()
        MockArticle.assert_called_with(expected_article_arguments)
