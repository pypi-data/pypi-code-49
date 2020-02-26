import datetime
import logging

from django.db.models import TextField
from django.forms import model_to_dict
from django.utils import timezone

from isc_common import setAttr
from isc_common.auth.models.user import User
from isc_common.datetime import StrToDate
from isc_common.fields.related import ForeignKeyCascade
from isc_common.http.DSRequest import DSRequest
from isc_common.models.audit import AuditModel, AuditQuerySet, AuditManager

logger = logging.getLogger(__name__)


class ParamsQuerySet(AuditQuerySet):
    def get_params(self, request, *args):
        request = DSRequest(request=request)
        data = request.get_data()
        app_id = data.get('app_id')

        periodEraseHistory = int(super().get_or_create(user=request.user, key=f'periodEraseHistory{app_id}', defaults=dict(value=1))[0].value)

        lastEraseHistory = super().get_or_create(user=request.user, key=f'lastEraseHistory{app_id}', defaults=dict(value=timezone.now()))[0].value
        lastEraseHistory = StrToDate(lastEraseHistory, '%Y-%m-%d %H:%M:%S')
        delta = timezone.now() - lastEraseHistory

        if not delta or delta.days > periodEraseHistory:
            super().filter(user=request.user, key__icontains='_ComboBoxItemSS').delete()
            if not lastEraseHistory:
                super().create(user=request.user, key=f'lastEraseHistory{app_id}', value=datetime.datetime.now())
            else:
                super().filter(user=request.user, key=f'lastEraseHistory{app_id}', value=lastEraseHistory).update(value=timezone.now())

        queryResult = super().filter(user_id=data.get('user_id'))
        res = [model_to_dict(record) for record in queryResult]
        return res

    def get_params_key(self, request, *args):
        request = DSRequest(request=request)
        data = request.get_data()
        key = data.get('key')

        try:
            return Params.objects.get(user=request.user, key=key).value
        except Params.DoesNotExist:
            return dict()


class ParamsManager(AuditManager):
    def get_queryset(self):
        return ParamsQuerySet(self.model, using=self._db)

    @staticmethod
    def getRecord(record):
        res = {
            'id': record.id,
            'key': record.key[1:len(record.key) - 1] if record.key[0:1] == "'" else record.key,
            'value': record.value,
            'lastmodified': record.lastmodified,
        }
        return res

    def deleteFromRequest(self, request):
        request = DSRequest(request=request)
        data = request.get_data()
        ids = []
        if data:
            ids = [param.id for param in Params.objects.filter(user=data.get('user_id'), key=data.get('key'))]

        if len(ids) == 0:
            ids = request.get_ids()
        res = super().filter(id__in=ids).delete()
        return res[0]

    def update1FromRequest(self, request):
        request = DSRequest(request=request)
        data = request.get_data()
        key = data.get('key')
        value = data.get('value')
        user_id = data.get('user_id')

        res = data
        if key != None and user_id != None:
            if key[0:1] == "'":
                key = key[1:len(key) - 1]
            setAttr(data, 'key', key)

            if value == None or value == '':
                res = super().filter(
                    user_id=user_id,
                    key=key
                ).delete()
            else:
                res, _ = super().update_or_create(
                    user_id=user_id,
                    key=key,
                    defaults=dict(value=value)
                )
                res = model_to_dict(res)
        return res


class Params(AuditModel):
    user = ForeignKeyCascade(User)
    key = TextField()
    value = TextField(null=True, blank=True)

    objects = ParamsManager()

    def __str__(self):
        return f"{self.key}: {self.value}"

    class Meta:
        verbose_name = 'Сохраненные параметры'
        unique_together = (('user', 'key'),)
