import logging

from django.core.management import BaseCommand

from kaf_pas.kd.models.lotsman_documents_hierarcy import Lotsman_documents_hierarcyManager

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    def handle(self, *args, **options):
        try:
            Lotsman_documents_hierarcyManager.make_mview()
        except Exception as ex:
            raise ex
