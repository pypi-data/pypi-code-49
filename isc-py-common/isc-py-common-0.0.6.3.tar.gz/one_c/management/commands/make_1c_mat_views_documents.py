import configparser
import logging
from tkinter import *

from django.core.management import BaseCommand
from django.db import connection
from transliterate import translit
from transliterate.exceptions import LanguageDetectionError

from one_c.models.entity_1c import Entity_1c
from one_c.models.one_c_params_entity_view import One_c_params_entity_view

logger = logging.getLogger(__name__)


class ExceptionOnDocLoading(Exception):
    pass


class Command(BaseCommand):
    config = configparser.ConfigParser()
    config['DEFAULT'] = {}

    config.sections()
    config.read('config.ini')

    help = "Создание мат вьюшек для документов из 1С"
    root = Tk()

    def dbl_qutes_str(self, str):
        return f'"{str}"'

    def qutes_str(self, str):
        return f"'{str}'"

    def handle(self, *args, **options):

        try:
            param_field = []
            for entity in Entity_1c.objects.filter():
                entity_code = translit(entity.code, reversed=True).replace("'",'')
                m_view_name = f'{self.dbl_qutes_str(entity_code + "_mview")}'
                param_field.append(f'DROP MATERIALIZED VIEW IF EXISTS {m_view_name};')
                param_field.append(f'CREATE MATERIALIZED VIEW {m_view_name} AS SELECT d.ref, d.entity_id,')
                cnt = One_c_params_entity_view.objects.filter(entity=entity).count()
                for param in One_c_params_entity_view.objects.filter(entity=entity):
                    cnt -= 1
                    try:
                        param_code = translit(param.code, reversed=True).replace("'",'')
                    except LanguageDetectionError:
                        param_code = param.code

                    item = f'(SELECT dp.value FROM one_c_documents_param_1c dp JOIN one_c_param_type pt ON pt.id = dp.type_id WHERE dp.document_id = d.ref AND pt.code::text = {self.qutes_str(param.code)}::text) AS {self.dbl_qutes_str(param_code)}'
                    if cnt > 0:
                        item += ','
                    param_field.append(item)

                param_field.append(f'FROM one_c_document_1c d WHERE d.entity_id = {entity.id} WITH DATA;')
                param_field.append(f'REFRESH MATERIALIZED VIEW {m_view_name};')

                sql_str = '\n'.join(param_field)

                with connection.cursor() as cursor:
                    # logger.debug(f'Creating: {m_view_name}')
                    print(f'Creating: {m_view_name}')
                    cursor.execute(sql_str)
                    # logger.debug(f'Created')
                    print(f'Created')

        except ExceptionOnDocLoading as ex:
            self.root.withdraw()
            logger.error('\n !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n')

            for msg_item in ex.args:
                logger.error(msg_item)

            logger.error('\n !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
