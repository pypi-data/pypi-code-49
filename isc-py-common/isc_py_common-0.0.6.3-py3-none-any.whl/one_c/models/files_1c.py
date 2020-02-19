import logging

from bitfield import BitField
from django.db.models import DateTimeField

from crypto.models.crypto_file import Crypto_file
from isc_common.models.audit import AuditQuerySet, AuditManager

logger = logging.getLogger(__name__)


class Files_1cQuerySet(AuditQuerySet):
    def filter(self, *args, **kwargs):
        return super().filter(*args, **kwargs)


class Files_1cManager(AuditManager):

    @staticmethod
    def getRecord(record):
        res = {}
        return res

    def get_queryset(self):
        return Files_1cQuerySet(self.model, using=self._db)


class Files_1c(Crypto_file):
    file_modification_time = DateTimeField(verbose_name='Дата время поcледнего модификации документа')
    props = BitField(flags=(('imp', 'Импорт'), ('exp', 'Экспорт')), db_index=True)

    objects = Files_1cManager()

    def __str__(self):
        return f"id: {self.id}, real_name: {self.real_name}"

    class Meta:
        verbose_name = 'Файлы 1С'
