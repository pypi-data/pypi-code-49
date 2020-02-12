import logging
import os

from django.db import transaction, connection
from django.db.models import TextField, UniqueConstraint, Q

from crypto.models.crypto_file import CryptoManager, Crypto_file
from isc_common.fields.related import ForeignKeyProtect
from kaf_pas.kd.models.documents import Documents
from kaf_pas.kd.models.documents_thumb10 import Documents_thumb10
from kaf_pas.kd.models.lotsman_documents_hierarcy import Lotsman_documents_hierarcy

logger = logging.getLogger(__name__)


class Documents_thumbManager(CryptoManager):
    @staticmethod
    def refreshFromDbls(doc_type, table_name):
        with connection.cursor() as cursor:
            cursor.execute(f'''select
                                    count (*),
                                    {doc_type}_id,
                                    path
                                from
                                    kd_documents_{table_name}
                                where {doc_type}_id is not null        
                                group by
                                    {doc_type}_id,
                                    path
                                having
                                    count(*) >1
                                    ''')
            rows = cursor.fetchall()
            for row in rows:
                count, document, path = row
                cursor.execute(f'''select
                                        id
                                    from
                                        kd_documents_{table_name}
                                    where
                                        {doc_type}_id = %s
                                        and path = %s''', [document, path])
                rows1 = cursor.fetchall()
                first_step = True
                for row1 in rows1:
                    id, = row1
                    if not first_step:
                        cursor.execute(f'''delete from ckk_item_image_refs where {table_name}_id =%s''', [id])
                        cursor.execute(f'''delete
                                                from
                                                    kd_documents_{table_name}
                                                where
                                                    id = %s''', [id])
                        print(f'Deleted: {id}')
                    else:
                        first_step = False

    @staticmethod
    def getRecord(record):
        res = {
            "id": record.id,
            "path": record.file_name,
            "lastmodified": record.lastmodified,
            "editing": record.editing,
            "deliting": record.deliting,
            "file_document_thumb_url": f'/logic/DocumentsThumb/Download/{record.id}/',

        }
        return res

    def deleteFromRequest(self, request, removed=None, ):
        res = 0
        ids = request.GET.getlist('ids')

        with transaction.atomic():
            for i in range(0, len(ids), 2):
                id = ids[i]
                mode = ids[i + 1]

                if mode == 'hide':
                    for item in super().filter(id=id):
                        item.soft_delete()
                        Documents_thumb10.objects.filter(path=item.path).soft_delete()
                        res += 1
                else:
                    for item in super().filter(id=id):
                        item.delete()
                        Documents_thumb10.objects.filter(path=item.path).delete()
                        res += 1
        return res


class Documents_thumb(Crypto_file):
    # Менять на cascade нельзя, потому как не происходит удаленеи файлов изображений при удалении документа
    document = ForeignKeyProtect(Documents, verbose_name='КД', null=True, blank=True)
    lotsman_document = ForeignKeyProtect(Lotsman_documents_hierarcy, verbose_name='Лоцман', null=True, blank=True)
    path = TextField()

    @property
    def file_name(self):
        dir, filename = os.path.split(self.path)
        return filename

    objects = Documents_thumbManager()

    def __str__(self):
        return f"{self.id}"

    class Meta:
        verbose_name = 'JPEG варианты документов уменьшенная копия'
        constraints = [
            UniqueConstraint(fields=['path'], condition=Q(document=None) & Q(lotsman_document=None), name='Documents_thumb_unique_constraint_0'),
            UniqueConstraint(fields=['lotsman_document', 'path'], condition=Q(document=None), name='Documents_thumb_unique_constraint_1'),
            UniqueConstraint(fields=['document', 'path'], condition=Q(lotsman_document=None), name='Documents_thumb_unique_constraint_2'),
            UniqueConstraint(fields=['document', 'lotsman_document', 'path'], name='Documents_thumb_unique_constraint_3'),
        ]
