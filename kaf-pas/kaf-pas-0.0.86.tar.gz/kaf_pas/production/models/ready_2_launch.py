import logging

from bitfield import BitField, BitHandler
from django.conf import settings
from django.db import transaction
from django.db.models import TextField, F
from django.forms import model_to_dict

from isc_common import delAttr, setAttr, getAttr
from isc_common.auth.models.user import User
from isc_common.bit import IsBitOn, TurnBitOn
from isc_common.common import getOrElse
from isc_common.datetime import DateToStr
from isc_common.fields.related import ForeignKeyCascade
from isc_common.http.DSRequest import DSRequest
from isc_common.models.audit import AuditModel, AuditManager, AuditQuerySet
from isc_common.number import DelProps
from isc_common.ws.progressStack import ProgressStack
from kaf_pas.ckk.models.item_line import Item_line
from kaf_pas.ckk.models.item_refs import Item_refs
from kaf_pas.production.models.operation_material import Operation_material
from kaf_pas.production.models.operation_resources import Operation_resources
from kaf_pas.production.models.operations_item import Operations_item
from kaf_pas.sales.models.demand import Demand

logger = logging.getLogger(__name__)


class Ready_2_launchQuerySet(AuditQuerySet):
    def delete(self):
        return super().delete()

    def create(self, **kwargs):
        return super().create(**kwargs)

    def filter(self, *args, **kwargs):
        return super().filter(*args, **kwargs)

    def get_info(self, request, *args):
        request = DSRequest(request=request)
        request = Ready_2_launchManager._del_options(request)
        criteria = self.get_criteria(json=request.json)
        cnt = super().filter(*args, criteria).count()
        cnt_all = super().filter().count()
        return dict(qty_rows=cnt, all_rows=cnt_all)

    def get_range_rows1(self, request, function=None, distinct_field_names=None):
        request = DSRequest(request=request)
        request = Ready_2_launchManager._del_options(request)
        self.alive_only = request.alive_only
        self.enabledAll = request.enabledAll
        res = self.get_range_rows(start=request.startRow, end=request.endRow, function=function, distinct_field_names=distinct_field_names, json=request.json)
        return res


class Ready_2_launchManager(AuditManager):

    @staticmethod
    def _del_options(request):
        delAttr(request.json.get('data'), 'full_name')
        delAttr(request.json.get('data'), 'check_qty')
        delAttr(request.json.get('data'), 'check_material')
        delAttr(request.json.get('data'), 'check_resources')
        delAttr(request.json.get('data'), 'check_edizm')
        delAttr(request.json.get('data'), 'check_operation')
        return request

    @staticmethod
    def make(demand, user, ready_2_launch=None, props=32):
        from kaf_pas.production.models.ready_2_launch_detail import Ready_2_launch_detail

        if isinstance(demand, int):
            demand = Demand.objects.get(id=demand)
        elif not isinstance(demand, Demand):
            raise Exception(f'demand must be a Demand instance or int')

        if isinstance(user, int):
            user = User.objects.get(id=user)
        elif not isinstance(user, User):
            raise Exception(f'user must be a User instance or int')

        cnt = 0
        cnt_not = 0

        all_notes = []
        options = []

        if IsBitOn(props, 0):
            options.append('Включена опция проверки наличия у операции длительности выполнения.')

        if IsBitOn(props, 1):
            options.append('Включена опция проверки наличия у операции № п/п.')

        if IsBitOn(props, 2):
            options.append('Включена опция проверки наличия у операции материалов или стандартных изделий.')

        if IsBitOn(props, 3):
            options.append('Включена опция проверки наличия у операции ресурса либо места выполнения.')

        if IsBitOn(props, 4):
            options.append('Включена опция проверки наличия у операции единицы измерения.')

        if IsBitOn(props, 5):
            options.append('Включена опция проверки наличия операций.')

        progress = ProgressStack(
            host=settings.WS_HOST,
            port=settings.WS_PORT,
            channel=f'common_{user.username}',
            user_id=user.id,
        )

        id = f'demand_{demand.id}_{ready_2_launch.props}_{user.id}'
        try:
            demand_str = f'<h3>Оценка готовности к запуску: Заказ № {demand.code} от {DateToStr(demand.date)}</h3>'
            deleted, _ = Item_refs.objects.filter(child=F('parent')).delete()

            cntAll = Item_refs.objects.get_descendants_count(id=demand.precent_item.item.id)
            progress.show(
                title=f'<b>Обработано товарных позиций</b>',
                label_contents=demand_str,
                cntAll=cntAll,
                id=id
            )

            if not ready_2_launch:
                ready_2_launch, _ = Ready_2_launch.objects.get_or_create(demand=demand)

            Item_refs.objects.filter(child=F('parent')).delete()
            for item_ref in Item_refs.objects.get_descendants(id=demand.precent_item.item.id):
                notes = []
                operations_cnt = Operations_item.objects.filter(item=item_ref.child).count()
                STMP_1 = item_ref.child.STMP_1.value_str if item_ref.child.STMP_1 else None
                STMP_2 = item_ref.child.STMP_2.value_str if item_ref.child.STMP_2 else None
                section = None
                try:
                    section = Item_line.objects.get(parent=item_ref.parent, child=item_ref.child).section
                except Item_line.DoesNotExist:
                    # cnt_not += 1
                    # notes.append(f'Наименование: {getOrElse("", STMP_1)}, Обозначение: {getOrElse("", STMP_2)} ID={item_ref.child.id}, PARENT_ID={item_ref.parent.id} не входит в детализацию.')
                    pass

                cnt_not1 = 0
                if section and section != 'Документация':
                    if operations_cnt == 0:
                        if IsBitOn(props, 5):
                            cnt_not += 1
                            notes.append(f'Наименование: {getOrElse("", STMP_1)}, Обозначение: {getOrElse("", STMP_2)} ID={item_ref.child.id}, PARENT_ID={item_ref.parent.id} не указаны операции.')
                    else:
                        for operation in Operations_item.objects.filter(item=item_ref.child):
                            if IsBitOn(props, 0) and not operation.qty:
                                cnt_not1 = 1
                                notes.append(f'Операция: {operation.operation.full_name} не указана длительность.')

                            if IsBitOn(props, 1) and not operation.num:
                                cnt_not1 = 1
                                notes.append(f'Операция: {operation.operation.full_name} не указан № п/п.')

                            if IsBitOn(props, 2):
                                operation_material_cnt = Operation_material.objects.filter(operationitem=operation).count()
                                if operation_material_cnt == 0:
                                    cnt_not1 = 1
                                    notes.append(f'Операция: {operation.operation.full_name} не указаны материалы или стандартные изделия.')

                            if IsBitOn(props, 3):
                                operation_resources_cnt = Operation_resources.objects.filter(operationitem=operation).count()
                                if operation_resources_cnt == 0:
                                    cnt_not1 = 1
                                    notes.append(f'Операция: {operation.operation.full_name} не указан ресурс либо место выполнения.')

                            if IsBitOn(props, 4) and not operation.ed_izm:
                                cnt_not1 = 1
                                notes.append(f'Операция: {operation.operation.full_name} не указана единица измерения.')

                if len(notes) > 0:
                    notes_str = "\n".join(notes)
                    Ready_2_launch_detail.objects.get_or_create(
                        item=item_ref.child,
                        ready=ready_2_launch,
                        notes=notes_str
                        # notes=f'<pre>{notes_str}</pre>'
                    )
                cnt_not += cnt_not1
                progress.setCntDone(cnt, id)
                cnt += 1

            ready = round(100 - cnt_not / cnt * 100, 2)
            all_notes.append(f'Готовность: {ready}%')
            notes_str = "\n".join(all_notes)
            ready_2_launch.notes = f'<pre>{notes_str}</pre>'
            ready_2_launch.save()
            progress.close(id=id)

            options_str = "\n" + "\n".join(options)
            settings.EVENT_STACK.EVENTS_PRODUCTION_READY_2_LAUNCH.send_message(f'Выполнена {demand_str} <h3>готовность: {ready} </h3>{options_str}<p/>')

        except Exception as ex:
            progress.close(id=id)
            raise ex

    def createFromRequest(self, request):
        request = DSRequest(request=request)
        data = request.get_data()
        _data = data.copy()

        demand_id = _data.get('demand_id')
        delAttr(_data, 'demand__date')
        delAttr(_data, 'demand__code')
        delAttr(_data, 'demand__description')
        delAttr(_data, 'demand__precent_item__STMP_1__value_str')
        delAttr(_data, 'demand__precent_item__STMP_2__value_str')

        props = 0
        if _data.get('check_qty'):
            props = TurnBitOn(props, 0)
        delAttr(_data, 'check_qty')

        if _data.get('check_num'):
            props = TurnBitOn(props, 1)
        delAttr(_data, 'check_num')

        if _data.get('check_material'):
            props = TurnBitOn(props, 2)
        delAttr(_data, 'check_material')

        if _data.get('check_resources'):
            props = TurnBitOn(props, 3)
        delAttr(_data, 'check_resources')

        if _data.get('check_edizm'):
            props = TurnBitOn(props, 4)
        delAttr(_data, 'check_edizm')

        if _data.get('check_operation'):
            props = TurnBitOn(props, 5)
        delAttr(_data, 'check_operation')

        setAttr(_data, 'props', props)

        with transaction.atomic():
            # date = StrToDate(_data.get('date'))
            # setAttr(_data, 'lastmodified', date)
            delAttr(_data, 'date')
            res = super().create(**_data)
            Ready_2_launchManager.make(
                demand=demand_id,
                user=request.user_id,
                ready_2_launch=res,
                props=props
            )

            res = Ready_2_launchManager.getRecord(res)
            data.update(DelProps(res))
        return data

    def updateFromRequest(self, request, removed=None, function=None):
        if not isinstance(request, DSRequest):
            request = DSRequest(request=request)
        data = request.get_data()
        return data

    @staticmethod
    def getRecord(record):
        res = {
            'id': record.id,
            'date': record.lastmodified,
            'demand_id': record.demand.id,
            'demand__date': record.demand.date,
            'demand__code': record.demand.code,
            'demand__name': record.demand.name,
            'check_qty': IsBitOn(record.props, 0),
            'check_num': IsBitOn(record.props, 1),
            'check_material': IsBitOn(record.props, 2),
            'check_resources': IsBitOn(record.props, 3),
            'check_edizm': IsBitOn(record.props, 4),
            'check_operation': IsBitOn(record.props, 5),
            'demand__description': record.demand.description,
            'demand__precent_item_id': record.demand.precent_item.id,
            'demand__precent_item__STMP_1_id': record.demand.precent_item.item.STMP_1.id if record.demand.precent_item.item.STMP_1 else None,
            'demand__precent_item__STMP_1__value_str': record.demand.precent_item.item.STMP_1.value_str if record.demand.precent_item.item.STMP_1 else None,
            'demand__precent_item__STMP_2_id': record.demand.precent_item.item.STMP_2.id if record.demand.precent_item.item.STMP_2 else None,
            'demand__precent_item__STMP_2__value_str': record.demand.precent_item.item.STMP_2.value_str if record.demand.precent_item.item.STMP_2 else None,
            'notes': record.notes,
            'editing': record.editing,
            'deliting': record.deliting,
        }
        return DelProps(res)

    def get_queryset(self):
        return Ready_2_launchQuerySet(self.model, using=self._db)


class Ready_2_launch(AuditModel):
    demand = ForeignKeyCascade(Demand)
    notes = TextField(null=True, blank=True)
    props = BitField(flags=(
        ('check_qty', 'Проверять длительность'),  # 1
        ('check_num', 'Проверять № п/п'),  # 2
        ('check_material', 'Проверять материалы'),  # 4
        ('check_resources', 'Проверять ресурсы'),  # 8
        ('check_edizm', 'Проверять еденицу измерения'),  # 16
        ('check_operation', 'Проверять операцию'),  # 32
    ), default=0, db_index=True)

    objects = Ready_2_launchManager()

    def __str__(self):
        return f"ID:{self.id}, code: {self.code}, name: {self.name}, description: {self.description}"

    class Meta:
        verbose_name = 'Готовность к запуску'
