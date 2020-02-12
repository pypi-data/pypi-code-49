import logging
import os

from django.core.exceptions import ObjectDoesNotExist
from django.db.models import TextField, CharField, UniqueConstraint, Q

from isc_common import delete_drive_leter, get_drive_leter
from isc_common.fields.related import ForeignKeyProtect
from isc_common.http.DSRequest import DSRequest
from isc_common.managers.common_managet_with_lookup_fields import CommonManagetWithLookUpFieldsManager, CommonManagetWithLookUpFieldsQuerySet
from isc_common.models.base_ref import Hierarcy
from kaf_pas.ckk.models.attr_type import Attr_type

logger = logging.getLogger(__name__)


class PathesQuerySet(CommonManagetWithLookUpFieldsQuerySet):
    def delete(self):
        from kaf_pas.kd.models.documents import Documents

        for item in self:
            Documents.objects.filter(path=item).delete()

        return super().delete()


class PathesManager(CommonManagetWithLookUpFieldsManager):
    def get_queryset(self):
        return PathesQuerySet(self.model, using=self._db)

    @staticmethod
    def getRecord(record):
        res = {
            "id": record.id,
            "path": record.path,
            "virt_path": record.virt_path,
            "parent_id": record.parent_id,
            "lastmodified": record.lastmodified,
            "editing": record.editing,
            "drive": record.drive,
            "deliting": record.deliting,
            "attr_type_id": record.attr_type.id if record.attr_type else None,
            "attr_type__code": record.attr_type.code if record.attr_type else None,
            "attr_type__name": record.attr_type.name if record.attr_type else None,
            # "isFolder": record.isFolder,
        }
        return res

    @property
    def sep(self):
        return os.altsep if os.altsep else os.sep

    def create_ex(self, **kwargs):
        path = kwargs.get('path')
        parent = kwargs.get('parent')
        with_out_last = kwargs.get('with_out_last')

        if not path:
            raise Exception(f'path {path} is not exists.')

        if path:
            drive = get_drive_leter(path)
            path = delete_drive_leter(path)

            if path != '':
                if with_out_last:
                    path = path.split(self.sep)[: - 1]
                else:
                    path = path.split(self.sep)

                for path_item in path:
                    if path_item:
                        alive_only = self.alive_only
                        try:
                            self.alive_only = False
                            if drive and path == '':
                                parent = super().get(drive=drive, path=path_item, parent=parent)
                            else:
                                parent = super().get(path=path_item, parent=parent)
                            self.alive_only = alive_only
                        except ObjectDoesNotExist:
                            self.alive_only = alive_only
                            if drive and path == '':
                                parent = super().create(drive=drive, path=path_item, parent=parent)
                            else:
                                parent = super().create(path=path_item, parent=parent)
            else:
                parent, _ = super().get_or_create(drive=drive, parent=parent)

        return parent

    def create_ex1(self, **kwargs):
        path = kwargs.get('path')
        parent = kwargs.get('parent')
        with_out_last = kwargs.get('with_out_last')

        if not path:
            raise Exception(f'path {path} is not exists.')

        if path:
            drive = get_drive_leter(path)
            path = delete_drive_leter(path)

            if path != '':
                if with_out_last:
                    path = path.split(self.sep)
                else:
                    path = path.split(self.sep)

                for path_item in path:
                    if path_item:
                        alive_only = self.alive_only
                        try:
                            self.alive_only = False
                            if drive and path == '':
                                parent = super().get(drive=drive, path=path_item, parent=parent)
                            else:
                                parent = super().get(path=path_item, parent=parent)
                            self.alive_only = alive_only
                        except ObjectDoesNotExist:
                            self.alive_only = alive_only
                            if drive and path == '':
                                parent = super().create(drive=drive, path=path_item, parent=parent)
                            else:
                                parent = super().create(path=path_item, parent=parent)
            else:
                parent, _ = super().get_or_create(drive=drive, parent=parent)

        return parent

    # Только для перенаправленных на виндовый сервак вызовов !!!!
    def deleteFromRequest(self, request, removed=None, ):
        from django.db import transaction
        from isc_common.management.commands.refresh_mat_views import refresh_mat_view
        from kaf_pas.kd.models.documents import DocumentManager
        from kaf_pas.kd.models.documents import Documents
        from kaf_pas.kd.models.uploades import Uploades
        from kaf_pas.kd.models.uploades_documents import Uploades_documents
        from kaf_pas.kd.models.uploades_log import Uploades_log
        from isc_common.auth.models.user import User

        ids = request.GET.getlist('ids')
        request = DSRequest(request=request)
        user_id = request.user_id

        res = 0
        with transaction.atomic():
            count = 0
            for i in range(0, len(ids), 2):
                if ids[i + 1] == 'hide':
                    res += super().filter(id=ids[i]).soft_delete()
                else:
                    for upload in Uploades.objects.filter(path=ids[i]):
                        Uploades_log.objects.filter(upload=upload).delete()
                        Uploades_documents.objects.filter(upload=upload).delete()
                        upload.delete()

                    for document in Documents.objects.filter(path_id=ids[i]):
                        count = DocumentManager.delete(document.id, User.objects.get(id=user_id))

                    res += super().filter(id=ids[i]).delete()[0]
            if count > 0:
                refresh_mat_view('kd_documents_mview')
                refresh_mat_view('kd_lotsman_documents_hierarcy_mview')
        return res

    def get_drive(self, id):
        try:
            path = self.get(id=id)
            if path.drive:
                return path.drive
            elif path.parent:
                return self.get_drive(path.parent.id)
            else:
                return path.drive
        except Pathes.DoesNotExist:
            return None

    def get_drive(self, id):
        try:
            path = self.get(id=id)
            if path.drive:
                return path.drive
            elif path.parent:
                return self.get_drive(path.parent.id)
            else:
                return path.drive
        except Pathes.DoesNotExist:
            return None


class Pathes(Hierarcy):
    drive = CharField(verbose_name='Диск', max_length=10, null=True, blank=True)
    path = TextField(verbose_name="Путь")
    virt_path = TextField(verbose_name="Мнимый путь", null=True, blank=True)
    attr_type = ForeignKeyProtect(Attr_type, verbose_name='Атрибут', null=True, blank=True)

    @property
    def sep(self):
        return os.altsep if os.altsep else os.sep

    def get_virt_path(self, id=None):
        try:
            path = Pathes.objects.get(id=id if id else self.id)
            if path.virt_path:
                return path.virt_path
            elif path.parent:
                return self.get_virt_path(path.parent.id)
            else:
                return path.virt_path
        except Pathes.DoesNotExist:
            return None

    @property
    def absolute_path(self):
        def get_parent(item_tuple):
            if item_tuple[0].parent:
                res = Pathes.objects.get(id=item_tuple[0].parent.id)
                res = (res, f"{res.path}/{item_tuple[1]}")
                return get_parent(res)
            else:
                return item_tuple

        if self.parent:
            res = get_parent((self, self.path))
            return f'{self.sep}{res[1]}'
        else:
            return f'{self.sep}{self.path}'

    def get_drive(self, id=None):
        try:
            path = Pathes.objects.get(id=id if id else self.id)
            if path.drive:
                return path.drive
            elif path.parent:
                return self.get_drive(path.parent.id)
            else:
                return path.drive
        except Pathes.DoesNotExist:
            return None

    @property
    def drived_absolute_path(self):
        drive = self.get_drive(self.id)
        if drive:
            return f'{drive}{self.absolute_path}'
        else:
            return self.absolute_path

    def __str__(self):
        return f"{self.absolute_path}"

    objects = PathesManager()

    class Meta:
        db_table = 'pathes'
        verbose_name = 'Пути нахождения документов'
        constraints = [
            UniqueConstraint(fields=['id'], condition=Q(parent=None), name='Pathes_unique_constraint_0'),
            UniqueConstraint(fields=['id', 'parent'], name='Pathes_unique_constraint_1'),
        ]


