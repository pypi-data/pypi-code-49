import logging
from datetime import datetime

from django.conf import settings
from django.db import transaction, connection
from django.db.models import TextField, DateTimeField
from django.forms import model_to_dict

import kaf_pas
from isc_common import StackElementNotExist, delAttr
from isc_common.auth.models.user import User
from isc_common.bit import TurnBitOn
from isc_common.common import blinkString
from isc_common.common.mat_views import create_tmp_mat_view, drop_mat_view
from isc_common.datetime import DateToStr
from isc_common.fields.related import ForeignKeyProtect
from isc_common.http.DSRequest import DSRequest
from isc_common.models.audit import AuditManager, AuditModel, AuditQuerySet
from isc_common.progress import managed_progress, ProgressDroped
from kaf_pas.planing.models.operation_types import Operation_types
from kaf_pas.planing.models.status_operation_types import Status_operation_types
from kaf_pas.production.models import progress_deleted
from kaf_pas.production.models.launch_operation_material import Launch_operations_material
from kaf_pas.production.models.launch_operation_resources import Launch_operation_resources
from kaf_pas.production.models.launch_operations_item import Launch_operations_item

logger = logging.getLogger(__name__)


class OperationsQuerySet(AuditQuerySet):
    pass

    def get_facets(self, request):
        request = DSRequest(request=request)
        res = []
        return res


class Route_item():

    def __init__(self, item_id, first_operation, last_operation):
        self.item_id = item_id
        self.first_operation = first_operation
        self.last_operation = last_operation

    def __str__(self):
        return f'item_id: {self.item_id}, first_operation: [{self.first_operation}], last_operation: [{self.last_operation}]'


class OperationPlanItem:
    id = None
    item = None
    resource = None
    production_operation = None
    value = None

    def __init__(self, *args, **kwargs):
        from kaf_pas.ckk.models.item import Item
        from kaf_pas.production.models.resource import Resource
        from kaf_pas.planing.models.operation_value import Operation_value
        from kaf_pas.planing.models.levels import Levels

        if len(kwargs) == 0:
            raise Exception(f'{self.__class__.__name__} kwargs is empty')

        for k, v in kwargs.items():
            setattr(self, k, v() if callable(v) else v)

        if isinstance(self.item, int):
            self.item = Item.objects.get(id=self.item)

        if isinstance(self.resource, int):
            self.resource = Resource.objects.get(id=self.resource)

        if isinstance(self.production_operation, int):
            self.production_operation = kaf_pas.production.models.operations.Operations.objects.get(id=self.production_operation)

        if isinstance(self.value, int):
            self.value = Operation_value.objects.get(id=self.value)

        if isinstance(self.operation_level, int):
            self.operation_level = Levels.objects.get(id=self.operation_level)


class OperationsManager(AuditManager):

    @staticmethod
    def delete_recursive(operation, soft_delete=False, user=None):
        with transaction.atomic():
            from kaf_pas.planing.models.operation_refs import Operation_refs

            count = Operation_refs.objects.get_descendants_count(id=operation.id)
            if count > 0:
                with managed_progress(
                        id=operation.id,
                        qty=Operation_refs.objects.get_descendants_count(id=operation.id),
                        user=user,
                        message='Удаление связанных операций операций',
                        title='Выполнено'
                ) as progress:
                    for item in Operation_refs.objects.get_descendants(id=operation.id, order_by_clause='order by level desc'):
                        if not soft_delete:
                            Operation_refs.objects.filter(id=item.id).delete()
                        else:
                            Operation_refs.objects.filter(id=item.child_id).soft_delete()

                        progress.step()

            if not soft_delete:
                Operations.objects.filter(id=operation.id).delete()
            else:
                Operations.objects.filter(id=operation.id).soft_delete()

    def updateFromRequest(self, request, removed=None, function=None):
        from kaf_pas.planing.models.operation_item import Operation_item
        from kaf_pas.planing.models.operation_value import Operation_value
        from kaf_pas.planing.models.operation_color import Operation_color

        if not isinstance(request, DSRequest):
            request = DSRequest(request=request)
        data = request.get_data()
        _data = data.copy()
        delAttr(_data, 'creator_id')
        _data.setdefault('creator_id', request.user_id)

        item_id = _data.get('item_id')
        edizm_id = _data.get('edizm_id')
        value = _data.get('value')
        color_id = _data.get('color_id')
        operation_id = _data.get('id')

        delAttr(_data, 'id')
        delAttr(_data, 'creator__short_name')

        delAttr(_data, 'opertype__full_name')
        delAttr(_data, 'isFolder')

        delAttr(_data, 'status__code')
        delAttr(_data, 'status__name')

        delAttr(_data, 'location__code')
        delAttr(_data, 'location__name')
        delAttr(_data, 'location__full_name')

        delAttr(_data, 'item__STMP_1_id')
        delAttr(_data, 'item__STMP_1__value_str')

        delAttr(_data, 'item__STMP_2_id')
        delAttr(_data, 'item__STMP_2__value_str')

        delAttr(_data, 'edizm__code')
        delAttr(_data, 'edizm__name')

        if item_id:
            Operation_item.objects.update_or_create(operation_id=operation_id, defaults=dict(item_id=item_id))
        else:
            Operation_item.objects.filter(operation_id=operation_id).delete()

        if edizm_id and value:
            Operation_value.objects.update_or_create(operation_id=operation_id, defaults=dict(edizm_id=edizm_id, value=value))
        else:
            Operation_value.objects.filter(operation_id=operation_id).delete()

        if color_id:
            Operation_color.objects.update_or_create(operation_id=operation_id, defaults=dict(color_id=color_id))
        else:
            Operation_color.objects.filter(operation_id=operation_id).delete()

        with transaction.atomic():
            super().update_or_create(id=operation_id, defaults=_data)
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
                    for operation in super().filter(id=id):
                        OperationsManager.delete_recursive(operation=operation, user=request.user)
                        operation.delete()
                        res += 1
        return res

    @staticmethod
    def make_routing(data):
        from isc_common import Stack
        from kaf_pas.ckk.models.ed_izm import Ed_izm
        from kaf_pas.planing.models.levels import Levels
        from kaf_pas.planing.models.operation_item import Operation_item
        from kaf_pas.planing.models.operation_launches import Operation_launches
        from kaf_pas.planing.models.operation_level import Operation_level
        from kaf_pas.planing.models.operation_material import Operation_material
        from kaf_pas.planing.models.operation_operation import Operation_operation
        from kaf_pas.planing.models.operation_refs import Operation_refs
        from kaf_pas.planing.models.operation_resources import Operation_resources
        from kaf_pas.planing.models.operation_standard_prod import Operation_standard_prod
        from kaf_pas.planing.models.operation_value import Operation_value
        from kaf_pas.production.models.launches import Launches

        # logger.debug(f'data: {data}')

        launch_id = data.get('id')
        launch = Launches.objects.get(id=launch_id)
        user = data.get('user')
        if not isinstance(user, User):
            raise Exception(f'user must be User instance.')
        edizm = Ed_izm.objects.get(code='шт')

        step_res = 0

        if launch.status.code == 'route_made':
            raise Exception(f'Маршрутизация уже выполнена.')

        sql_str = f'''with a as (
                                    with recursive r as (
                                        select *,
                                               1 as level
                                        from production_launch_item_refs
                                        where parent_id is null
                                           and launch_id = {launch_id}
                                           and is_bit_on(props::int,0) = true
                                        union all
                                        select production_launch_item_refs.*,
                                               r.level + 1 as level
                                        from production_launch_item_refs
                                                 join r
                                                      on
                                                          production_launch_item_refs.parent_id = r.child_id
                                        where is_bit_on(r.props::int,0) = true
                                        and is_bit_on(production_launch_item_refs.props::int,0) = true
                                    )
                                
                                    select r1.id,
                                           r1.parent_id,
                                           r1.child_id,
                                           r1.launch_id,
                                           r1.qty,
                                           r1.level,
                                           r1.item_full_name,
                                           r1.item_full_name_obj                 
                                    from (select distinct r.id,
                                                          r.parent_id,
                                                          r.child_id,
                                                          r.launch_id,
                                                          r.item_full_name,
                                                          r.item_full_name_obj,
                                                          r.qty,
                                                          (
                                                              select plil.section
                                                              from production_launch_item_line plil
                                                              where plil.child_id = r.child_id
                                                                and plil.parent_id = r.parent_id
                                                                and plil.launch_id = r.launch_id) section,
                                                          level
                                          from r
                                                   join ckk_item ci on ci.id = r.child_id
                                          where r.launch_id = {launch_id}
                                          order by level desc) r1
                                    where lower(r1.section) != 'документация'
                                       or r1.parent_id is null
                                )
                                
                                
                                select a.id,
                                       a.parent_id,
                                       a.child_id,
                                       a.launch_id,
                                       a.qty,
                                       a.level,
                                       a.item_full_name,
                                       a.item_full_name_obj
                                from a'''

        mat_view_name = create_tmp_mat_view(sql_str=sql_str, indexes=['parent_id', 'child_id'])
        with connection.cursor() as cursor:
            cursor.execute(f'select count(*) from {mat_view_name}')
            count, = cursor.fetchone()

        with managed_progress(
                id=f'launch_{launch.id}_{user.id}',
                qty=count * 2,
                user=user,
                message=f'<h3>Расчет маршрутизации внутри товарных позиций, Запуск № {launch.code} от {DateToStr(launch.date)}</h3>',
                title='Выполнено',
                props=TurnBitOn(0, 0)
        ) as progress:
            progress.except_func = lambda progress: drop_mat_view(mat_view_name)

            with transaction.atomic():
                for launch in Launches.objects.filter(id=launch.id).select_for_update():
                    with connection.cursor() as cursor:
                        cursor.execute(f'select max(level), min(level) from {mat_view_name}')
                        rows = cursor.fetchone()
                        min_level, max_level = rows

                        cursor.execute(f'select * from {mat_view_name} order by level desc')
                        rows = cursor.fetchall()

                        routed_items = Stack()

                        for row in rows:
                            def make_oparetions(row, mode='child'):
                                id, parent_id, child_id, launch_id, qty, level, item_full_name, item_full_name_obj = row

                                # Более низкий уровень в иерархии товарной позиции соответствует более высокому в маршрутизации, т.к. необходимо изготавливать ранньше
                                level = max_level - (level - min_level)
                                logger.debug(f'level: {level}')

                                if mode == 'child':
                                    cursor.execute(f'select * from {mat_view_name} where qty is null and child_id = %s', [child_id])
                                    null_rows = cursor.fetchall()
                                    if len(null_rows) > 0:
                                        nulls_array = []
                                        for null_row in null_rows:
                                            id, parent_id, child_id, launch_id, qty, level, item_full_name, item_full_name_obj = null_row
                                            nulls_str = f'<b>ID: {id}: {item_full_name}</b>'
                                            nulls_array.append(nulls_str)
                                        nulls_str = f'''{blinkString(text='Не указано количество : ', color='red')}<br><div>{'<br>'.join(nulls_array)}</div>'''
                                        raise Exception(nulls_str)

                                    cursor.execute(f'select sum(qty) from {mat_view_name} where child_id = %s', [child_id])
                                    qty, = cursor.fetchone()
                                    logger.debug(f'qty: {qty}')

                                elif mode == 'parent':
                                    if parent_id != None:
                                        child_id = parent_id

                                if len(routed_items.find(lambda child_item: child_item.item_id == child_id)) == 0:
                                    income_operation = None
                                    first_operation = None

                                    # Выполняем маршрутизацию внутри товарной позиции согласно порядку выплонения оперций из production
                                    cnt1 = Launch_operations_item.objects.filter(item_id=child_id, launch_id=launch_id).count()
                                    if cnt1 > 0:
                                        for launch_operations_item in Launch_operations_item.objects.filter(item_id=child_id, launch_id=launch_id).order_by('num'):

                                            outcome_operation = Operations.objects.create(
                                                date=datetime.now(),
                                                opertype=settings.OPERS_TYPES_STACK.ROUTING_TASK,
                                                status=settings.OPERS_TYPES_STACK.ROUTING_TASK_STATUSES.get('new'),
                                                creator=user
                                            )
                                            logger.debug(f'Created outcome_operation :  {outcome_operation}')

                                            operation_launches = Operation_launches.objects.create(operation=outcome_operation, launch=launch)
                                            logger.debug(f'Created operation_launches :  {operation_launches}')

                                            operation_item = Operation_item.objects.create(
                                                operation=outcome_operation,
                                                item=launch_operations_item.item,
                                                item_full_name=item_full_name,
                                                item_full_name_obj=item_full_name_obj
                                            )
                                            logger.debug(f'Created operation_item :  {operation_item}')

                                            operation_operation = Operation_operation.objects.create(
                                                operation=outcome_operation,
                                                production_operation=launch_operations_item.operation,
                                                num=launch_operations_item.num,
                                                qty=launch_operations_item.qty,
                                                ed_izm=launch_operations_item.ed_izm,
                                            )
                                            logger.debug(f'Created operation_operation :  {operation_operation}')

                                            _level, created = Levels.objects.get_or_create(
                                                code=str(level),
                                                defaults=dict(
                                                    name=str(level),
                                                    editing=False,
                                                    deliting=False
                                                ))
                                            if created:
                                                logger.debug(f'Created level :  {_level}')

                                            operation_level = Operation_level.objects.create(operation=outcome_operation, level=_level)
                                            logger.debug(f'Created operation_level :  {operation_level}')

                                            if qty != None:
                                                operation_value = Operation_value.objects.create(operation=outcome_operation, value=qty, edizm=edizm)
                                                logger.debug(f'Created operation_value :  {operation_value}')

                                            for launch_operation_material in Launch_operations_material.objects.filter(launch_operationitem=launch_operations_item):
                                                if launch_operation_material.material_askon != None:
                                                    operation_material = Operation_material.objects.create(operation=outcome_operation, material=launch_operation_material.material_askon)
                                                    logger.debug(f'Created operation_material :  {operation_material}')

                                                if launch_operation_material.material != None:
                                                    operation_standard_prod = Operation_standard_prod.objects.get_or_create(operation=outcome_operation, material=launch_operation_material.material)
                                                    logger.debug(f'Created operation_standard_prod :  {operation_standard_prod}')

                                            def exception_not_resource():
                                                from isc_common.common import blinkString
                                                raise Exception(f'''<b>Для : {item_full_name}</b>  {blinkString(text='не задан ресурс.  Запустите анализатор готовности к запуску.', blink=False, color='red', bold=True)}''')

                                            if Launch_operation_resources.objects.filter(launch_operationitem=launch_operations_item) == 0:
                                                exception_not_resource()

                                            for launch_operation_resources in Launch_operation_resources.objects.filter(launch_operationitem=launch_operations_item):
                                                operation_resources = Operation_resources.objects.create(operation=outcome_operation, resource=launch_operation_resources.resource)
                                                logger.debug(f'Created operation_resources :  {operation_resources}')

                                            if income_operation == None:
                                                first_operation = outcome_operation

                                            operation_refs = Operation_refs.objects.create(
                                                parent=income_operation,
                                                parent_real=income_operation,
                                                child=outcome_operation,
                                                props=Operation_refs.props.inner_routing
                                            )
                                            logger.debug(f'Created operation_refs :  {operation_refs}')

                                            income_operation = outcome_operation
                                            cnt1 -= 1
                                            if cnt1 == 0:
                                                routed_items.push(Route_item(item_id=child_id, first_operation=first_operation, last_operation=outcome_operation), logger=logger)
                                    else:
                                        def exception_not_operations():
                                            from isc_common.common import blinkString
                                            raise Exception(f'''<b>Для : {item_full_name}</b>  {blinkString(text='не задано ни одной операции. Запустите анализатор готовности к запуску.', blink=False, color='red', bold=True)}''')

                                        exception_not_operations()
                                # else:
                                #     raise Exception(f'child_id exisys yet !!!!')

                            make_oparetions(row=row)

                            step_res = progress.step()
                            if step_res != 0:
                                break

                        if step_res == 0:
                            # Выполняем маршрутизацию между товарными позициями соединяя последнюю оперцию предыдущей товарной позиции с первой операциеей следующей
                            # товарной позиции
                            progress.setContentsLabel(f'<h3>Расчет маршрутизации между товарными позициями, Запуск № {launch.code} от {DateToStr(launch.date)}</h3>')

                            for row in rows:
                                id, parent_id, child_id, launch_id, qty, level, item_full_name, item_full_name_obj = row
                                try:
                                    if parent_id == None:
                                        parent_id = child_id
                                    parent_item = routed_items.find_one(lambda item: item.item_id == parent_id)
                                except StackElementNotExist:
                                    logger.warning(f'parent_id: {parent_id} !!!!!!!!!!!!!!!!!!Товарная позиция не обнаружена среди товарных позиций, прошедших внутреннюю маршрутизацию !!!!!!!!!!!!!!!!')
                                    # Если товарная позиция не обнаружена среди товарных позиций, прошедших внутреннюю маршрутизацию

                                    make_oparetions(row=row, mode='parent')
                                    parent_item = routed_items.find_one(lambda item: item.item_id == parent_id)

                                cursor.execute(f'''select child_id from {mat_view_name} where parent_id = %s''', [parent_id])
                                parents_rows = cursor.fetchall()
                                for parents_row in parents_rows:
                                    _child_id, = parents_row
                                    _child = routed_items.find_one(lambda item: item.item_id == _child_id)

                                    operation_refs, created = Operation_refs.objects.get_or_create(
                                        parent=_child.last_operation,
                                        parent_real=_child.last_operation,
                                        child=parent_item.first_operation,
                                        defaults=dict(
                                            props=Operation_refs.props.outer_routing
                                        )
                                    )
                                    logger.debug(f'Created operation_refs :  {operation_refs}')

                                    deleted, _ = Operation_refs.objects.filter(parent__isnull=True, child=parent_item.last_operation).delete()
                                step_res = progress.step()
                                if step_res != 0:
                                    break

                        if step_res == 0:
                            launch.status = settings.PROD_OPERS_STACK.ROUTMADE
                            launch.save()

                            settings.EVENT_STACK.EVENTS_PRODUCTION_MAKE_ROUTING.send_message(f'<h3>Выполнен Расчет маршрутизации: Запуск № {launch.code} от {DateToStr(launch.date)}</h3><p/>')

                            progress.sendMessage(type='refresh_launches_grid')

            drop_mat_view(mat_view_name)

            if step_res != 0:
                raise ProgressDroped(progress_deleted)

    @staticmethod
    def clean_routing(data):
        from kaf_pas.production.models.launches import Launches
        from kaf_pas.planing.models.operation_launches import Operation_launches

        launch_id = data.get('id')
        launch = Launches.objects.get(id=launch_id)

        if launch.status.code == 'formirovanie':
            raise Exception(f'Маршрутизация уже удалена.')

        # logger.debug(f'data: {data}')

        launch_id = data.get('id')
        launch = Launches.objects.get(id=launch_id)

        user = data.get('user')
        query = Operation_launches.objects.filter(launch=launch, operation__opertype__in=[
            settings.OPERS_TYPES_STACK.ROUTING_TASK,
        ])
        step_res = 0

        with managed_progress(
                id=launch.id,
                qty=query.count(),
                user=user,
                message=f'<h3>Удаление маршрутизации: Запуск № {launch.code} от {DateToStr(launch.date)}</h3>',
                title='Выполнено',
                props=TurnBitOn(0, 0)
        ) as progress:
            with transaction.atomic():
                for launch in Launches.objects.filter(id=launch.id).select_for_update():
                    launch.status = launch.status = settings.PROD_OPERS_STACK.FORMIROVANIE
                    launch.save()

                    cnt = 0
                    for operation_launches in query:
                        OperationsManager.delete_recursive(operation=operation_launches.operation, user=user)
                        step_res = progress.step()
                        cnt += 1
                        if step_res != 0:
                            raise ProgressDroped(progress_deleted)

                    if step_res == 0:
                        if cnt > 0:
                            settings.EVENT_STACK.EVENTS_PRODUCTION_DELETE_ROUTING.send_message(f'<h3>Выполнено Удаление маршрутизации: Запуск № {launch.code} от {DateToStr(launch.date)}</h3><p/>')
                        progress.sendMessage(type='refresh_launches_grid')

                if step_res != 0:
                    raise ProgressDroped(progress_deleted)

        return model_to_dict(launch)

    @staticmethod
    def get_locations_users_query(resource, production_operation, item_full_name):
        from kaf_pas.ckk.models.locations_users import Locations_users

        locations_users_query = Locations_users.objects.filter(location=resource.location, parent__isnull=True)
        if locations_users_query.count() == 0:
            raise Exception(f'Не обнаружен ответственный исполнитель для : {resource.location.full_name}, \nоперация: {production_operation.full_name}\n {item_full_name}')

        return locations_users_query

    @staticmethod
    def get_resource_workshop(resource):
        from kaf_pas.ckk.models.locations import Locations
        from kaf_pas.production.models.resource import Resource

        for location in Locations.objects_tree.get_parents(id=resource.location.id, child_id='id', include_self=False):
            if location.props.isWorkshop == True:
                try:
                    resource = Resource.objects.get(location=location)
                    return resource
                except Resource.DoesNotExist:
                    resource = Resource.objects.create(
                        location=location,
                        props=Resource.props.isWorkshop,
                        code=location.code,
                        editing=False,
                        deliting=False,
                    )
                    return resource

        if resource == None:
            raise Exception(f'Не обнаружен цех, с признаком "Уровень цеха" для : {resource.name}')
        return resource

    @staticmethod
    def make_production_order(data):
        from kaf_pas.planing.models.operation_executor import Operation_executor
        from kaf_pas.planing.models.operation_item import Operation_item
        from kaf_pas.planing.models.operation_launches import Operation_launches
        from kaf_pas.planing.models.operation_level import Operation_level
        from kaf_pas.planing.models.operation_operation import Operation_operation
        from kaf_pas.planing.models.operation_refs import Operation_refs
        from kaf_pas.planing.models.operation_resources import Operation_resources
        from kaf_pas.planing.models.operation_value import Operation_value
        from kaf_pas.planing.models.operations_view import Operations_view
        from kaf_pas.production.models.launches import Launches
        from kaf_pas.production.models.launches import Launches
        from kaf_pas.production.models.resource import Resource

        user = data.get('user')
        if isinstance(user, int):
            user = User.objects.get(id=user)

        launch = data.get('id')
        if isinstance(launch, int):
            launch = Launches.objects.get(id=launch)

        if launch.status.code == 'in_production':
            raise Exception(f'Формирование заданий на производство уже выполнено.')

        item_query = Operations_view.objects.filter(
            launch=launch,
            production_operation__isnull=False,
            opertype=settings.OPERS_TYPES_STACK.ROUTING_TASK
        ).values('item', 'item_full_name', 'operation_level').distinct()
        qty = item_query.count()
        logger.debug(f'Calculated qty : {qty}')

        new_status_order_prod = settings.OPERS_TYPES_STACK.PRODUCTION_TASK_STATUSES.get('new')
        new_status_det_order_prod = settings.OPERS_TYPES_STACK.PRODUCTION_DETAIL_TASK_STATUSES.get('new')

        with managed_progress(
                id=f'order_by_prod_launch_{launch.id}_{user.id}',
                qty=item_query.count(),
                user=user,
                message=f'<h3>Расчет заданий на производство, Запуск № {launch.code} от {DateToStr(launch.date)}</h3>',
                title='Выполнено',
                props=TurnBitOn(0, 0)
        ) as progress:
            with transaction.atomic():
                for launch in Launches.objects.filter(id=launch.id).select_for_update():
                    for route_oparation_item in item_query:
                        route_oparation_item = OperationPlanItem(**route_oparation_item)

                        # Головная операция заказа
                        main_oper_production_order = Operations.objects.create(
                            date=datetime.now(),
                            opertype=settings.OPERS_TYPES_STACK.PRODUCTION_TASK,
                            status=new_status_order_prod,
                            creator=user,
                            editing=False,
                            deliting=False
                        )
                        logger.debug(f'Created operation :  {main_oper_production_order}')

                        operation_launches = Operation_launches.objects.create(operation=main_oper_production_order, launch=launch)
                        logger.debug(f'Created operation_launches :  {operation_launches}')

                        operation_item = Operation_item.objects.create(
                            operation=main_oper_production_order,
                            item=route_oparation_item.item,
                            item_full_name=route_oparation_item.item_full_name
                        )
                        logger.debug(f'Created operation_item :  {operation_item}')

                        operation_refs = Operation_refs.objects.create(
                            parent_real_id=route_oparation_item.id,
                            child=main_oper_production_order,
                            props=Operation_refs.props.product_order_routing
                        )
                        logger.debug(f'Created operation_refs :  {operation_refs}')

                        route_items_operations_query = Operations_view.objects.filter(
                            launch=launch,
                            item=route_oparation_item.item,
                            production_operation__isnull=False,
                            opertype=settings.OPERS_TYPES_STACK.ROUTING_TASK).values(
                            'id',
                            'resource',
                            'production_operation',
                            'value',
                            'operation_level',
                            'production_operation_num',
                            'production_operation_qty',
                            'production_operation_edizm',
                            'item_full_name',
                        ).order_by('production_operation_num').distinct()

                        qty = route_items_operations_query.count()
                        logger.debug(f'Calculated qty : {qty}')
                        top_resource = None

                        for route_items_operations in route_items_operations_query:
                            route_items_operations = OperationPlanItem(**route_items_operations)

                            # Пытаемся распознать операцию комплектации
                            production_operation = kaf_pas.production.models.operations.Operations.objects.get(id=route_items_operations.production_operation.id)
                            if production_operation.props.assemly == True:
                                raise Exception(f'Meeting production_operation :  {production_operation} is made_common_form operation')

                            # Операция детализации заказа
                            detail_oper_production_order = Operations.objects.create(
                                date=datetime.now(),
                                opertype=settings.OPERS_TYPES_STACK.PRODUCTION_DETAIL_TASK,
                                status=new_status_det_order_prod,
                                creator=user,
                                editing=False,
                                deliting=False
                            )
                            logger.debug(f'Created order_prod_item_det_operation :  {detail_oper_production_order}')

                            operation_launches = Operation_launches.objects.create(operation=detail_oper_production_order, launch=launch)
                            logger.debug(f'Created operation_launches :  {operation_launches}')

                            operation_item = Operation_item.objects.create(
                                operation=detail_oper_production_order,
                                item=route_oparation_item.item,
                                item_full_name=route_oparation_item.item_full_name
                            )
                            logger.debug(f'Created operation_item :  {operation_item}')

                            operation_level = Operation_level.objects.create(
                                operation=detail_oper_production_order,
                                level=route_items_operations.operation_level,
                            )
                            logger.debug(f'Created operation_level :  {operation_level}')

                            resource = Resource.objects.get(id=route_items_operations.resource.id)
                            if top_resource == None:
                                top_resource = OperationsManager.get_resource_workshop(resource)
                                operation_resources = Operation_resources.objects.create(
                                    operation=main_oper_production_order,
                                    resource=top_resource
                                )
                                logger.debug(f'Created operation_resources :  {operation_resources}')

                                operation_value = Operation_value.objects.create(
                                    operation=main_oper_production_order,
                                    value=route_items_operations.value.value,
                                    edizm=route_items_operations.value.edizm
                                )
                                logger.debug(f'Created operation_value :  {operation_value}')

                                operation_level = Operation_level.objects.create(
                                    operation=main_oper_production_order,
                                    level=route_items_operations.operation_level,
                                )
                                logger.debug(f'Created operation_level :  {operation_level}')

                            locations_users_query = OperationsManager.get_locations_users_query(
                                resource=top_resource,
                                production_operation=production_operation,
                                item_full_name=route_items_operations.item_full_name
                            )
                            for locations_users in locations_users_query:
                                operation_executor = Operation_executor.objects.create(operation=detail_oper_production_order, executor=locations_users.user)
                                logger.debug(f'Created operation_executor :  {operation_executor}')

                            operation_resources = Operation_resources.objects.create(
                                operation=detail_oper_production_order,
                                resource=resource
                            )
                            logger.debug(f'Created operation_resources :  {operation_resources}')

                            operation_operation = Operation_operation.objects.create(
                                operation=detail_oper_production_order,
                                production_operation=route_items_operations.production_operation,
                                num=route_items_operations.production_operation_num,
                                qty=route_items_operations.production_operation_qty,
                                ed_izm_id=route_items_operations.production_operation_edizm,
                            )
                            logger.debug(f'Created operation_operation :  {operation_operation}')

                            operation_value = Operation_value.objects.create(
                                operation=detail_oper_production_order,
                                value=route_items_operations.value.value,
                                edizm=route_items_operations.value.edizm
                            )
                            logger.debug(f'Created operation_value :  {operation_value}')

                            # Привязка к оперции тов позиции из маршрутизации
                            operation_refs = Operation_refs.objects.create(
                                parent_id=route_items_operations.id,
                                parent_real_id=route_items_operations.id,
                                child=detail_oper_production_order,
                                props=Operation_refs.props.product_order_routing
                            )
                            logger.debug(f'Created operation_refs :  {operation_refs}')

                            # Привязка к головной операции заказа на производство
                            operation_refs = Operation_refs.objects.create(
                                parent=main_oper_production_order,
                                child=detail_oper_production_order,
                                props=Operation_refs.props.product_order_routing
                            )
                            logger.debug(f'Created operation_refs :  {operation_refs}')

                        step_res = progress.step()
                        if step_res != 0:
                            raise ProgressDroped(progress_deleted)

                launch.status = settings.PROD_OPERS_STACK.IN_PRODUCTION
                launch.save()
            progress.sendMessage(type='refresh_launches_grid')

    @staticmethod
    def delete_production_order(data):
        from kaf_pas.production.models.launches import Launches
        from kaf_pas.planing.models.operation_refs import Operation_refs

        user = data.get('user')
        if isinstance(user, int):
            user = User.objects.get(id=user)

        launch = data.get('id')
        if isinstance(launch, int):
            launch = Launches.objects.get(id=launch)

        if launch.status.code == 'route_made':
            raise Exception(f'Удалений заданий на производство уже выполнено.')

        opertypes = (settings.OPERS_TYPES_STACK.PRODUCTION_TASK.id, settings.OPERS_TYPES_STACK.PRODUCTION_DETAIL_TASK.id)
        with connection.cursor() as cursor:
            cursor.execute('''WITH RECURSIVE r AS (
                                                SELECT *, 1 AS level
                                                FROM planing_operations_view
                                                WHERE opertype_id in %s
                                                AND launch_id=%s
                                                AND is_bit_on(props::integer, 2) = true

                                                union all

                                                SELECT planing_operations_view.*, r.level + 1 AS level
                                                FROM planing_operations_view
                                                         JOIN r
                                                              ON planing_operations_view.parent_id = r.id
                                                WHERE planing_operations_view.launch_id=%s
                                                AND r.launch_id=%s              
                                                AND is_bit_on(r.props::integer, 2) = true
                                                AND is_bit_on(planing_operations_view.props::integer, 2) = true
                                                )
                                                              

                                            select distinct a.*
                                            from (
                                                     select distinct id, level
                                                     from r
                                                     where opertype_id in %s
                                                 ) as a
                                            order by a.level desc''', [opertypes, launch.id, launch.id, launch.id, opertypes])
            rows = cursor.fetchall()

            qty = len(rows)
            logger.debug(f'Calculated qty : {qty}')
            with managed_progress(
                    id=f'delete_order_by_prod_launch_{launch.id}_{user.id}',
                    qty=qty,
                    user=user,
                    message=f'<h3>Удаление заданий на производство, Запуск № {launch.code} от {DateToStr(launch.date)}</h3>',
                    title='Выполнено',
                    props=TurnBitOn(0, 0)
            ) as progress:
                with transaction.atomic():
                    for launch in Launches.objects.filter(id=launch.id).select_for_update():
                        for row in rows:
                            operation_id, _ = row
                            Operation_refs.objects.filter(child_id=operation_id).delete()
                            Operations.objects.filter(id=operation_id).delete()
                            if progress.step() != 0:
                                raise ProgressDroped(progress_deleted)

                    launch.status = settings.PROD_OPERS_STACK.ROUTMADE
                    launch.save()
                progress.sendMessage(type='refresh_launches_grid')

    @staticmethod
    def getRecord(record):
        res = {
            'id': record.id,
            'opertype_id': record.opertype.id,
            'opertype__full_name': record.opertype.full_name,
            'status_id': record.status.id if record.status else None,
            'status__code': record.status.code if record.status else None,
            'status__name': record.status.name if record.status else None,
        }
        return res

    def get_queryset(self):
        return OperationsQuerySet(self.model, using=self._db)


class Operations(AuditModel):
    date = DateTimeField()
    creator = ForeignKeyProtect(User)
    opertype = ForeignKeyProtect(Operation_types)
    status = ForeignKeyProtect(Status_operation_types)
    description = TextField(null=True, blank=True)

    objects = OperationsManager()

    def __str__(self):
        return f"ID:{self.id}, opertype: [{self.opertype}], status: [{self.status}]"

    def __repr__(self):
        return self.__str__()

    class Meta:
        verbose_name = 'Опреации системные'
