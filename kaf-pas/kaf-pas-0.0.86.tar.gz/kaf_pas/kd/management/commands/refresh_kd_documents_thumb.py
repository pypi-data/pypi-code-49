import logging

from django.core.management import BaseCommand
from django.db import transaction

from isc_common.logger.Logger import Logger

logger = logging.getLogger(__name__)
logger.__class__ = Logger


class Command(BaseCommand):
    help = 'Создание товаоных позиций после импорта из Лоцмана'

    def handle(self, *args, **options):
        try:
            from kaf_pas.kd.models.documents_thumb import Documents_thumbManager
            with transaction.atomic():
                Documents_thumbManager.refreshFromDbls(doc_type='lotsman_document', table_name='thumb')
                Documents_thumbManager.refreshFromDbls(doc_type='lotsman_document', table_name='thumb10')

                Documents_thumbManager.refreshFromDbls(doc_type='document', table_name='thumb')
                Documents_thumbManager.refreshFromDbls(doc_type='document', table_name='thumb10')
        except Exception as ex:
            raise ex
