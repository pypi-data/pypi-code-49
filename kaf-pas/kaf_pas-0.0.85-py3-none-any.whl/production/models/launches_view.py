import datetime
import logging

from django.conf import settings
from django.db import transaction
from django.db.models import DateTimeField, PositiveIntegerField, F, BooleanField

from isc_common import getAttr
from isc_common.fields.related import ForeignKeyProtect
from isc_common.http.DSRequest import DSRequest
from isc_common.models.base_ref import BaseRefHierarcy, BaseRefManager, BaseRefQuerySet
from isc_common.number import DelProps
from isc_common.ws.progressStack import ProgressStack
from kaf_pas.production.models.launches import LaunchesManager
from kaf_pas.production.models.status_launch import Status_launch
from kaf_pas.sales.models.demand import Demand
from kaf_pas.sales.models.demand_view import Demand_view

logger = logging.getLogger(__name__)


class Launches_viewQuerySet(BaseRefQuerySet):
    def delete(self):
        return super().delete()

    def create(self, **kwargs):
        return super().create(**kwargs)

    def filter(self, *args, **kwargs):
        return super().filter(*args, **kwargs)


class Launches_viewManager(BaseRefManager):
    @staticmethod
    def make_launch(data):
        from isc_common.auth.models.user import User
        from kaf_pas.ckk.models.item_refs import Item_refs

        demand_id = getAttr(data, 'demand_id')
        qty = getAttr(data, 'qty')
        code = getAttr(data, 'code')
        date = getAttr(data, 'date')
        date = datetime.datetime.strptime(date, '%Y-%m-%d')
        user = User.objects.get(id=getAttr(data, 'user_id'))
        status, _ = Status_launch.objects.get_or_create(name='Формирование')

        with transaction.atomic():
            for demand in Demand.objects.select_for_update().filter(id=demand_id):
                tail_qty = Demand_view.objects.get(id=demand_id).tail_qty
                if tail_qty < qty:
                    raise Exception(f'Затребованное количестово для запуска ({qty}), превышает возможное к запуску ({tail_qty})')

                progress = ProgressStack(
                    host=settings.WS_HOST,
                    port=settings.WS_PORT,
                    channel=f'common_{user.username}',
                )

                id = f'demand_{demand.id}'
                demand_str = f'<h3>Формирование запуска: Заказ № {demand.code} от {demand.date}</h3>'

                progress.show(
                    title=f'<b>Обработано товарных позиций</b>',
                    label_contents=demand_str,
                    cntAll=Item_refs.objects.get_descendants_count(id=demand.precent_item.item.id),
                    id=id
                )

                cnt = 0
                Item_refs.objects.filter(child=F('parent')).delete()
                launch = Launches_view.objects.create(
                    code=code,
                    demand_id=demand_id,
                    qty=qty,
                    date=date,
                    status=status
                )
                for item_ref in Item_refs.objects.get_descendants(id=demand.precent_item.item.id):
                    print(item_ref)

        return data

    def createFromRequest(self, request):
        request = DSRequest(request=request)
        return Launches_viewManager.make_launch(request.get_data())

    @staticmethod
    def getRecord(record):
        res = {
            'id': record.id,
            'code': record.code,
            'name': record.name,
            'date': record.date,
            'description': record.description,
            'parent_id': record.parent.id if record.parent else None,

            'demand_id': record.demand.id,
            'demand__code': record.demand.code,
            'demand__date': record.demand.date,

            'status_id': record.status.id,
            'status__code': record.status.code,
            'status__name': record.status.name,

            'qty': record.qty,
            'routing_made': record.props.routing_made,
            'isFolder': record.isFolder,
            'props': record.props,

            'editing': record.editing,
            'deliting': record.deliting,
        }
        return DelProps(res)

    def get_queryset(self):
        return Launches_viewQuerySet(self.model, using=self._db)


class Launches_view(BaseRefHierarcy):
    date = DateTimeField()
    status = ForeignKeyProtect(Status_launch)
    demand = ForeignKeyProtect(Demand)
    qty = PositiveIntegerField()
    isFolder = BooleanField()
    props = LaunchesManager.props()

    objects = Launches_viewManager()

    def __str__(self):
        return f"ID:{self.id}, code: {self.code}, name: {self.name}, description: {self.description}"

    class Meta:
        verbose_name = 'Запуски'
        db_table = 'production_launches_view'
        managed = False
