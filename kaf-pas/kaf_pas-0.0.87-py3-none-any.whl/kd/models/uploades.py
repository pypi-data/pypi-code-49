import logging

from django.db import transaction

from isc_common.fields.related import ForeignKeyCascade
from isc_common.models.audit import AuditModel, AuditManager, AuditQuerySet
from isc_common.progress import managed_progress
from kaf_pas.kd.models.pathes import Pathes

logger = logging.getLogger(__name__)


class UploadesQuerySet(AuditQuerySet):
    def filter(self, *args, **kwargs):
        return super().filter(*args, **kwargs)


class UploadesManager(AuditManager):

    @staticmethod
    def getRecord(record):
        res = {
            'id': record.id,
            'lastmodified': record.lastmodified,
            'path_id': record.path.id,
            'absolute_path': record.path.absolute_path,
            'editing': record.editing,
            'deliting': record.deliting,
        }
        return res

    def get_queryset(self):
        return UploadesQuerySet(self.model, using=self._db)

    def deleteFromRequest(self, request):
        from isc_common.auth.models.user import User

        from isc_common.management.commands.refresh_mat_views import refresh_mat_view
        from kaf_pas.ckk.models.item import Item
        from kaf_pas.ckk.models.item import ItemManager
        from kaf_pas.ckk.models.item_image_refs import Item_image_refs
        from kaf_pas.kd.models.document_attr_cross import Document_attr_cross
        from kaf_pas.kd.models.documents import Documents
        from kaf_pas.kd.models.documents_history import Documents_history
        from kaf_pas.kd.models.documents_thumb import Documents_thumb
        from kaf_pas.kd.models.documents_thumb10 import Documents_thumb10
        from kaf_pas.kd.models.lotsman_documents_hierarcy import Lotsman_documents_hierarcy
        from kaf_pas.kd.models.lotsman_documents_hierarcy_files import Lotsman_documents_hierarcy_files
        from kaf_pas.kd.models.lotsman_documents_hierarcy_refs import Lotsman_documents_hierarcy_refs
        from kaf_pas.kd.models.uploades_documents import Uploades_documents
        from kaf_pas.kd.models.uploades_log import Uploades_log
        from kaf_pas.production.models.operations_item import Operations_item
        from kaf_pas.production.models.ready_2_launch_detail import Ready_2_launch_detail

        ids = request.GET.getlist('ids')
        user = User.objects.get(username=request.GET.get('ws_channel').split('_')[1])

        res = 0
        with transaction.atomic():
            for i in range(0, len(ids), 2):
                id = ids[i]
                visibleMode = ids[i + 1]

                if visibleMode != "none":
                    res += super().filter(id=id).soft_delete(visibleMode=visibleMode)
                else:
                    lotsman_cnt = 0

                    for upload_document in Uploades_documents.objects.filter(upload_id=id):
                        lotsman_cnt += Lotsman_documents_hierarcy.objects.filter(document=upload_document.document).count()

                    with managed_progress(
                            qty=Uploades_documents.objects.filter(upload_id=id).count() + lotsman_cnt,
                            id=id,
                            user=user,
                            message='Удаление закачек',
                            title='Выполнено'
                    ) as progress:
                        lotsman_cnt = 0
                        doc_cnt = 0

                        for upload_document in Uploades_documents.objects.filter(upload_id=id):

                            Document_attr_cross.objects.filter(document=upload_document.document).delete()

                            for item in Item.objects.filter(document=upload_document.document):
                                ItemManager.delete_recursive(item_id=item.id, delete_lines=True, user=user)

                                Operations_item.objects.filter(item=item).delete()

                                Ready_2_launch_detail.objects.filter(item=item).delete()
                                item.delete()

                            for documents_history in Documents_history.objects.filter(new_document=upload_document.document):
                                documents_history.old_document.props |= Documents.props.relevant
                                documents_history.old_document.save()
                                documents_history.delete()

                            for thumb in Documents_thumb.objects.filter(document=upload_document.document):
                                Item_image_refs.objects.filter(thumb=thumb).delete()
                                thumb.delete()

                            for thumb10 in Documents_thumb10.objects.filter(document=upload_document.document):
                                Item_image_refs.objects.filter(thumb10=thumb10).delete()
                                thumb10.delete()

                            for lotsman_document in Lotsman_documents_hierarcy.objects.filter(document=upload_document.document):
                                Lotsman_documents_hierarcy_refs.objects.filter(child=lotsman_document).delete()
                                Lotsman_documents_hierarcy_refs.objects.filter(parent=lotsman_document).delete()

                                for item in Item.objects.filter(lotsman_document=lotsman_document):
                                    ItemManager.delete_recursive(item_id=item.id, delete_lines=True, user=user)

                                    Operations_item.objects.filter(item=item).delete()

                                    Ready_2_launch_detail.objects.filter(item=item).delete()
                                    item.delete()

                                for thumb in Documents_thumb.objects.filter(lotsman_document=lotsman_document):
                                    Item_image_refs.objects.filter(thumb=thumb).delete()
                                    thumb.delete()

                                for thumb10 in Documents_thumb10.objects.filter(lotsman_document=lotsman_document):
                                    Item_image_refs.objects.filter(thumb10=thumb10).delete()
                                    thumb10.delete()

                                Lotsman_documents_hierarcy_files.objects.filter(lotsman_document=lotsman_document).delete()
                                lotsman_document.delete()
                                lotsman_cnt += 1
                                progress.step()

                            logger.debug(f'Deliting: {upload_document.document}')
                            upload_document.document.delete()
                            doc_cnt += 1
                            logger.debug('Done.')
                            progress.step()
                        Uploades_log.objects.filter(upload_id=id).delete()

                        if doc_cnt > 0:
                            progress.setContentsLabel('<h3>Refresh kd_documents_mview</h3>')
                            refresh_mat_view('kd_documents_mview')

                        if lotsman_cnt > 0:
                            progress.setContentsLabel('<h3>Refresh kd_lotsman_documents_hierarcy_mview</h3>')
                            refresh_mat_view('kd_lotsman_documents_hierarcy_mview')

                    res += super().filter(id=id).delete()[0]
        return res


class Uploades(AuditModel):
    path = ForeignKeyCascade(Pathes)
    objects = UploadesManager()

    def __str__(self):
        return f"{self.id}"

    class Meta:
        verbose_name = 'Загрузки внешних данных'
