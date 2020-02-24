import logging

from bitfield import BitField
from django.conf import settings
from django.db import transaction
from django.db.models import TextField, F

from isc_common import delAttr, setAttr, Stack
from isc_common.auth.models.user import User
from isc_common.bit import IsBitOn, TurnBitOn
from isc_common.common.mat_views import create_tmp_mat_view
from isc_common.datetime import DateToStr
from isc_common.fields.related import ForeignKeyCascade
from isc_common.http.DSRequest import DSRequest
from isc_common.models.audit import AuditModel, AuditManager, AuditQuerySet
from isc_common.number import DelProps
from isc_common.progress import managed_progress, ProgressDroped
from kaf_pas.ckk.models.item_line import Item_line
from kaf_pas.ckk.models.item_refs import Item_refs
from kaf_pas.production.models import progress_deleted, p_id
from kaf_pas.production.models.operation_material import Operation_material
from kaf_pas.production.models.operation_resources import Operation_resources
from kaf_pas.production.models.operations_item import Operations_item
from kaf_pas.sales.models.demand import Demand

logger = logging.getLogger(__name__)


class Ready_2_launchQuerySet(AuditQuerySet):
    pass

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


class Item_refs_Stack(Stack):
    def add_parents(self, id):

        for item_ref in Item_refs.objects.raw(f'''WITH RECURSIVE r AS (
                                                    SELECT *, 1 AS level
                                                    FROM ckk_item_refs
                                                    WHERE child_id IN (%s)
                                                    and parent_id != %s

                                                    union all

                                                    SELECT ckk_item_refs.*, r.level + 1 AS level
                                                    FROM ckk_item_refs
                                                             JOIN r
                                                                  ON ckk_item_refs.child_id = r.parent_id)

                                                select  *
                                                from r
                                                where child_id != %s order by level desc''', [
            id,
            p_id,
            p_id
        ]):
            self.push(item_ref)

    @property
    def _get_full_path_obj(self):
        arr = []
        last = self.top()
        if last:
            arr.append(last)
        while True:
            if last.parent != None:
                last = [item for item in self.stack if item.child.id == last.parent.id]
                if len(last) > 0:
                    last = last[0]
                    arr.append(last)
                else:
                    break
            else:
                # arr.append(last)
                break

        arr = [item for item in reversed(arr)]
        return arr

    @property
    def get_full_path_obj(self):
        from kaf_pas.ckk.models.item_operations_view import Item_operations_view
        from kaf_pas.ckk.models.item_operations_view import Item_operations_viewManager
        arr = [Item_operations_viewManager.getRecord(Item_operations_view.objects.get(refs_id=item.id)) for item in self._get_full_path_obj]
        return arr

    @property
    def get_full_path(self):
        arr = self._get_full_path_obj
        # arr = [item for item in arr if arr.parent != None]
        res = ' / '.join([item.child.item_name for item in arr])
        return '/ ' + res


class Ready_2_launchManager(AuditManager):

    @staticmethod
    def _del_options(request):
        delAttr(request.json.get('data'), 'full_name')
        delAttr(request.json.get('data'), 'check_qty')
        delAttr(request.json.get('data'), 'check_material')
        delAttr(request.json.get('data'), 'check_resources')
        delAttr(request.json.get('data'), 'check_edizm')
        delAttr(request.json.get('data'), 'check_operation')
        delAttr(request.json.get('data'), 'check_colvo')
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
        step_res = 0

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

        if IsBitOn(props, 6):
            options.append('Включена опция проверки количества.')

        demand_str = f'<h3>Оценка готовности к запуску: Заказ № {demand.code} от {DateToStr(demand.date)}</h3>'

        with managed_progress(
                id=f'demand_{demand.id}_{ready_2_launch.props}_{user.id}',
                qty=Item_refs.objects.get_descendants_count(
                    id=demand.precent_item.item.id,
                    # distinct='distinct',
                    where_clause=f'''where parent_id != {p_id}'''
                ),
                user=user,
                message=demand_str,
                title='Выполнено',
                props=TurnBitOn(0, 0)

        ) as progress:
            deleted, _ = Item_refs.objects.filter(child=F('parent')).delete()

            if not ready_2_launch:
                ready_2_launch, _ = Ready_2_launch.objects.get_or_create(demand=demand)

            items_refs_stack = Item_refs_Stack()
            items_refs_stack.add_parents(demand.precent_item.item.id)

            for item_ref in Item_refs.objects.get_descendants(
                    id=demand.precent_item.item.id,
                    where_clause=f'''where parent_id != {p_id}''',
                    # distinct='distinct'
            ):
                notes = []

                # items_refs_stack.push(item_ref, lambda stack, item: len([it for it in stack if it.id != item_ref.id]) == 0)
                items_refs_stack.push(item_ref)

                operations_cnt = Operations_item.objects.filter(item=item_ref.child).count()
                section = None
                item_full_name = None
                item_full_name_obj = None
                cnt_not1 = 0

                try:
                    item_line = Item_line.objects.get(parent=item_ref.parent, child=item_ref.child)
                    section = item_line.section

                    if section and section != 'Документация':
                        if IsBitOn(props, 6) and not item_line.qty:
                            cnt_not1 += 1
                            notes.append(f'Не указано количество.')
                            if not item_full_name:
                                item_full_name_obj = items_refs_stack.get_full_path_obj
                                item_full_name = items_refs_stack.get_full_path

                except Item_line.DoesNotExist:
                    cnt_not += 1
                    notes.append(f'Не входит в детализацию.')
                    if not item_full_name:
                        item_full_name_obj = items_refs_stack.get_full_path_obj
                        item_full_name = items_refs_stack.get_full_path

                if section and section != 'Документация':
                    if operations_cnt == 0:
                        if IsBitOn(props, 5):
                            cnt_not += 1
                            notes.append(f'Не указаны операции.')
                            item_full_name_obj = items_refs_stack.get_full_path_obj
                            item_full_name = items_refs_stack.get_full_path
                    else:
                        for operation in Operations_item.objects.filter(item=item_ref.child):
                            if IsBitOn(props, 0) and not operation.qty:
                                cnt_not1 = 1
                                notes.append(f'Операция: {operation.operation.full_name} не указана длительность.')
                                if not item_full_name:
                                    item_full_name_obj = items_refs_stack.get_full_path_obj
                                    item_full_name = items_refs_stack.get_full_path

                            if IsBitOn(props, 1) and not operation.num:
                                cnt_not1 = 1
                                notes.append(f'Операция: {operation.operation.full_name} не указан № п/п.')
                                if not item_full_name:
                                    item_full_name_obj = items_refs_stack.get_full_path_obj
                                    item_full_name = items_refs_stack.get_full_path

                            if IsBitOn(props, 2):
                                operation_material_cnt = Operation_material.objects.filter(operationitem=operation).count()
                                if operation_material_cnt == 0:
                                    cnt_not1 = 1
                                    notes.append(f'Операция: {operation.operation.full_name} не указаны материалы или стандартные изделия.')
                                    if not item_full_name:
                                        item_full_name_obj = items_refs_stack.get_full_path_obj
                                        item_full_name = items_refs_stack.get_full_path

                            if IsBitOn(props, 3):
                                operation_resources_cnt = Operation_resources.objects.filter(operationitem=operation).count()
                                if operation_resources_cnt == 0:
                                    cnt_not1 = 1
                                    notes.append(f'Операция: {operation.operation.full_name} не указан ресурс либо место выполнения.')
                                    if not item_full_name:
                                        item_full_name_obj = items_refs_stack.get_full_path_obj
                                        item_full_name = items_refs_stack.get_full_path

                            if IsBitOn(props, 4) and not operation.ed_izm:
                                cnt_not1 = 1
                                notes.append(f'Операция: {operation.operation.full_name} не указана единица измерения.')
                                if not item_full_name:
                                    item_full_name_obj = items_refs_stack.get_full_path_obj
                                    item_full_name = items_refs_stack.get_full_path


                if len(notes) > 0:
                    notes_str = "\n".join(notes)
                    Ready_2_launch_detail.objects.get_or_create(
                        ready=ready_2_launch,
                        notes=notes_str,
                        item_full_name=item_full_name,
                        item_full_name_obj=item_full_name_obj,
                    )
                cnt_not += cnt_not1
                step_res = progress.step()
                cnt += 1
                if step_res != 0:
                    break

            if step_res == 0:
                ready = round(100 - cnt_not / cnt * 100, 2)
                all_notes.append(f'{ready}%')
                notes_str = "\n".join(all_notes)
                ready_2_launch.notes = f'<pre>{notes_str}</pre>'
                ready_2_launch.save()

                options_str = "\n" + "\n".join(options)
                settings.EVENT_STACK.EVENTS_PRODUCTION_READY_2_LAUNCH.send_message(f'Выполнена {demand_str} <h3>готовность: {ready} </h3>{options_str}<p/>')
            else:
                raise ProgressDroped(progress_deleted)

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

        if _data.get('check_colvo'):
            props = TurnBitOn(props, 6)
        delAttr(_data, 'check_colvo')

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

    def makeTmpMatViewFromRequest(self, request):
        from kaf_pas.production.models.ready_2_launch_detail import Ready_2_launch_detail
        from isc_common.models.mat_view import Mat_view

        if not isinstance(request, DSRequest):
            request = DSRequest(request=request)
        data = request.get_data()

        ready_2_launch_detail = Ready_2_launch_detail.objects.get(id=data.get('id'))
        mat_view_name = f'ready_2_launch_detail_{ready_2_launch_detail.id}_mview'
        try:
            Mat_view.objects.get(relname=mat_view_name)
        except Mat_view.DoesNotExist:
            create_tmp_mat_view(f'''SELECT
                                           t."isFolder",
                                           t."STMP_1_id",
                                           t."STMP_2_id",
                                           t.deliting,
                                           t.document__file_document,
                                           t.document_id,
                                           t.editing,
                                           t.id,
                                           t.lastmodified,
                                           t.parent_id,
                                           t.props,
                                           t.qty_operations,
                                           t.refs_id,
                                           t.refs_props,
                                           t.relevant,
                                           t.section,
                                           t.version,
                                           t.where_from
                                    FROM production_ready_2_launch_detail s
                                             CROSS JOIN LATERAL
                                        json_to_recordset(s.item_full_name_obj::json) as t(
                                                                                           "deliting" boolean,
                                                                                           "document__file_document" text,
                                                                                           "document_id" bigint,
                                                                                           "editing" boolean,
                                                                                           "id" bigint,
                                                                                           "isFolder" boolean,
                                                                                           "lastmodified" text,
                                                                                           "parent_id" bigint,
                                                                                           "props" bigint,
                                                                                           "qty_operations" int4,
                                                                                           "refs_id" bigint,
                                                                                           "refs_props" bigint,
                                                                                           "relevant" text,
                                                                                           "section" text,
                                                                                           "STMP_1_id" bigint,
                                                                                           "STMP_2_id" bigint,
                                                                                           "version" int4,
                                                                                           "where_from" text
                                                                                            )
                                        where s.id = {ready_2_launch_detail.id}''', mat_view_name=mat_view_name)
            logger.debug(f'Created MatView: {mat_view_name}')

        data.setdefault('matViewName', mat_view_name)
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
            'check_colvo': IsBitOn(record.props, 6),
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
        ('check_colvo', 'Проверять количество'),  # 64
    ), default=0, db_index=True)

    objects = Ready_2_launchManager()

    def __str__(self):
        return f"ID:{self.id}, code: {self.code}, name: {self.name}, description: {self.description}"

    class Meta:
        verbose_name = 'Готовность к запуску'
