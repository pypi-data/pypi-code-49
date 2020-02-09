import logging

from bitfield import BitField
from django.db import transaction

from isc_common import setAttr
from isc_common.auth.models.user import User
from isc_common.fields.related import ForeignKeyCascade
from isc_common.http.DSRequest import DSRequest
from isc_common.models.audit import AuditModel, AuditManager, AuditQuerySet
from isc_common.number import DelProps
from kaf_pas.planing.models.operation_types import Operation_types
from kaf_pas.planing.models.operations import Operations

logger = logging.getLogger(__name__)


class Operation_types_usersQuerySet(AuditQuerySet):
    def delete(self):
        return super().delete()

    def create(self, **kwargs):
        return super().create(**kwargs)

    def filter(self, *args, **kwargs):
        return super().filter(*args, **kwargs)


class Operation_types_usersManager(AuditManager):

    def createFromRequest(self, request, removed=None):
        request = DSRequest(request=request)
        data = request.get_data()
        user_ids = data.get('user_ids', None)
        context_ids = data.get('context_ids', None)
        _data = []

        with transaction.atomic():
            if user_ids and context_ids:
                if not isinstance(user_ids, list):
                    user_ids = [user_ids]

                if not isinstance(context_ids, list):
                    context_ids = [context_ids]

                for user_id in user_ids:
                    for context_id in context_ids:
                        res = super().create(user_id=user_id, operation_type_id=context_id)

            return data

    def updateFromRequest(self, request, removed=None, function=None):
        if not isinstance(request, DSRequest):
            request = DSRequest(request=request)
        data = request.get_data()

        with transaction.atomic():
            props = data.get('props', 0)
            if data.get('compulsory_reading') == True:
                props |= Operation_types_users.props.compulsory_reading
            else:
                props &= ~Operation_types_users.props.compulsory_reading

            _data = dict()
            setAttr(_data, 'props', props)

            super().filter(id=data.get('id')).update(**_data)

            return data

    def deleteFromRequest(self, request, removed=None, ):
        request = DSRequest(request=request)
        res = 0
        tuple_ids = request.get_tuple_ids()
        with transaction.atomic():
            for id, mode in tuple_ids:
                if mode == 'hide':
                    super().filter(id=id).soft_delete()
                else:
                    res = super().get(id=id)
                    res.delete()
                    qty = 1
                res += qty

            return res

    @staticmethod
    def getRecord(record):
        res = {
            'id': record.id,
            'user_id': record.user.id,
            'user__username': record.user.username,
            'user__first_name': record.user.first_name,
            'user__last_name': record.user.last_name,
            'user__email': record.user.email,
            'user__middle_name': record.user.middle_name,
            'compulsory_reading': Operation_types_users.props.compulsory_reading,
            'props': record.props,
            'editing': record.editing,
            'deliting': record.deliting,
        }
        return DelProps(res)

    def get_queryset(self):
        return Operation_types_usersQuerySet(self.model, using=self._db)


class Operation_types_users(AuditModel):
    operation_type = ForeignKeyCascade(Operation_types)
    user = ForeignKeyCascade(User)
    props = BitField(flags=(
        ('compulsory_reading', 'Обязательное прочтение'),  # 1
    ), default=1, db_index=True)

    objects = Operation_types_usersManager()

    def __str__(self):
        return f"ID:{self.id}"

    def __repr__(self):
        return self.__str__()

    class Meta:
        verbose_name = 'Ответстветственные по операциям планирования'
