import logging

from django.core.management import BaseCommand

from isc_common.logger.Logger import Logger

logger = logging.getLogger(__name__)
logger.__class__ = Logger


class Command(BaseCommand):
    help = 'Создание товаоных позиций после импорта из Лоцмана'

    def handle(self, *args, **options):
        try:
            from kaf_pas.kd.models.lotsman_documents_hierarcy import Lotsman_documents_hierarcyManager
            from isc_common.management.commands.refresh_mat_views import refresh_mat_view

            Lotsman_documents_hierarcyManager.make_items(logger=logger)
            refresh_mat_view('kd_lotsman_documents_hierarcy_mview')
        except Exception as ex:
            raise ex
