import logging

from bitfield import BitField
from django.db import transaction
from django.db.models import UniqueConstraint, Q

from isc_common import setAttr
from isc_common.auth.models.user import User
from isc_common.fields.related import ForeignKeyCascade
from isc_common.http.DSRequest import DSRequest
from isc_common.models.audit import AuditManager, AuditQuerySet
from isc_common.models.base_ref import Hierarcy
from isc_common.number import DelProps
from kaf_pas.ckk.models.locations import Locations

logger = logging.getLogger(__name__)


class Locations_usersQuerySet(AuditQuerySet):
    def delete(self):
        return super().delete()

    def create(self, **kwargs):
        return super().create(**kwargs)

    def filter(self, *args, **kwargs):
        return super().filter(*args, **kwargs)


class Locations_usersManager(AuditManager):

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
                        res = super().get_or_create(user_id=user_id, location_id=context_id)

            return data

    def updateFromRequest(self, request, removed=None, function=None):
        if not isinstance(request, DSRequest):
            request = DSRequest(request=request)
        data = request.get_data()
        parent_id = data.get('parent_id')

        with transaction.atomic():
            props = data.get('props', 0)
            if data.get('compulsory_reading') == True:
                props |= Locations_users.props.compulsory_reading
            else:
                props &= ~Locations_users.props.compulsory_reading

            _data = dict()
            setAttr(_data, 'props', props)
            setAttr(_data, 'parent_id', parent_id)

            super().filter(id=data.get('id')).update(**_data)

            return data

    def copyUsersFromRequest(self, request, removed=None, function=None):
        if not isinstance(request, DSRequest):
            request = DSRequest(request=request)
        data = request.get_data()
        source = data.get('source')
        destination = data.get('destination')

        res = 0
        with transaction.atomic():
            for s in source:
                Locations_users.objects.get_or_create(user_id=s.get('user_id'), location_id=s.get('context_id'), parent_id=destination.get('user_id'))
                res += 1
            return res

    def deleteFromRequest(self, request, removed=None, ):
        request = DSRequest(request=request)
        res = 0
        tuple_ids = request.get_tuple_ids()
        with transaction.atomic():
            for id, mode in tuple_ids:
                if mode == 'hide':
                    super().filter(id=id).soft_delete()
                else:
                    super().filter(id=id).delete()
                    res += 1

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
            'compulsory_reading': Locations_users.props.compulsory_reading,
            'props': record.props,
            'editing': record.editing,
            'deliting': record.deliting,
            'location_id': record.location.id,
            'location_position': record.location_position,
            'parent_id': record.parent.id if record.parent else None,
        }
        return DelProps(res)

    def get_queryset(self):
        return Locations_usersQuerySet(self.model, using=self._db)


class Locations_users(Hierarcy):
    location = ForeignKeyCascade(Locations)
    user = ForeignKeyCascade(User)
    props = BitField(flags=(
        ('compulsory_reading', 'Обязательное прочтение'),  # 1
    ), default=1, db_index=True)

    @property
    def location_position(self):
        from kaf_pas.input.models.user_add_info import User_add_info
        res = []
        for item in User_add_info.objects.filter(user=self.user):
            res.append(f'{item.location.full_name} : {item.position.name}')
        return ', '.join(res)

    objects = Locations_usersManager()

    def __str__(self):
        return f"ID:{self.id}"

    class Meta:
        constraints = [
            UniqueConstraint(fields=['location', 'user'], condition=Q(parent=None), name='Locations_users_unique_constraint_0'),
            UniqueConstraint(fields=['location', 'parent', 'user'], name='Locations_users_unique_constraint_1'),
        ]
        verbose_name = 'Ответственные пользователи ресурсов'
