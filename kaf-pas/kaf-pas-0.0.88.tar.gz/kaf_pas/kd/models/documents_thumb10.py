import logging

from django.db.models import TextField, UniqueConstraint, Q

from crypto.models.crypto_file import Crypto_file, CryptoManager
from isc_common.fields.related import ForeignKeyProtect
from kaf_pas.kd.models.documents import Documents
from kaf_pas.kd.models.lotsman_documents_hierarcy import Lotsman_documents_hierarcy

logger = logging.getLogger(__name__)


class Documents_thumb10(Crypto_file):
    # Менять на cascade нельзя, потому как не происходит удаленеи файлов изображений при удалении документа
    document = ForeignKeyProtect(Documents, verbose_name='КД', null=True, blank=True)
    lotsman_document = ForeignKeyProtect(Lotsman_documents_hierarcy, verbose_name='Лоцман', null=True, blank=True)
    path = TextField()

    objects = CryptoManager()

    def __str__(self):
        return f"{self.id}"

    class Meta:
        verbose_name = 'JPEG варианты документов'
        constraints = [
            UniqueConstraint(fields=['path'], condition=Q(document=None) & Q(lotsman_document=None), name='Documents_thumb10_unique_constraint_0'),
            UniqueConstraint(fields=['lotsman_document', 'path'], condition=Q(document=None), name='Documents_thumb10_unique_constraint_1'),
            UniqueConstraint(fields=['document', 'path'], condition=Q(lotsman_document=None), name='Documents_thumb10_unique_constraint_2'),
            UniqueConstraint(fields=['document', 'lotsman_document', 'path'], name='Documents_thumb10_unique_constraint_3'),
        ]
