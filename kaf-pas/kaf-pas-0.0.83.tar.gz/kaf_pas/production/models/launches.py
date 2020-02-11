import datetime
import logging

from bitfield import BitField
from django.conf import settings
from django.db import transaction
from django.db.models import DateTimeField, PositiveIntegerField, F

from isc_common import setAttr
from isc_common.datetime import DateToStr
from isc_common.fields.related import ForeignKeyProtect
from isc_common.http.DSRequest import DSRequest
from isc_common.models.base_ref import BaseRefHierarcy, BaseRefManager, BaseRefQuerySet
from isc_common.number import StrToNumber, DelProps
from isc_common.ws.progressStack import ProgressStack
from kaf_pas.production.models import SPC_CLM_COUNT_ATTR
from kaf_pas.production.models.status_launch import Status_launch
from kaf_pas.sales.models.demand import Demand
from kaf_pas.sales.models.demand_view import Demand_view

logger = logging.getLogger(__name__)


class LaunchesQuerySet(BaseRefQuerySet):
    def delete(self):
        return super().delete()

    def create(self, **kwargs):
        return super().create(**kwargs)

    def filter(self, *args, **kwargs):
        return super().filter(*args, **kwargs)


class LaunchesManager(BaseRefManager):

    @staticmethod
    def get_count(item_line, qty):
        from kaf_pas.kd.models.document_attributes import Document_attributes

        _str = item_line.SPC_CLM_COUNT.value_str if item_line.SPC_CLM_COUNT else None
        if _str != None:
            if _str.find(',') != -1:
                try:
                    str1 = _str.replace(',', '.')
                    count = StrToNumber(str1)

                    SPC_CLM_COUNT, created = Document_attributes.objects.get_or_create(attr_type=SPC_CLM_COUNT_ATTR, value_str=_str)
                    if created == False:
                        SPC_CLM_COUNT.value_int = count
                        SPC_CLM_COUNT.value_str = str1
                        SPC_CLM_COUNT.save()

                    if qty > 1:
                        count *= qty
                        SPC_CLM_COUNT, created = Document_attributes.objects.get_or_create(attr_type=SPC_CLM_COUNT_ATTR, value_str=str(count))
                        if created != True:
                            SPC_CLM_COUNT.value_int = count
                            SPC_CLM_COUNT.save()

                    return SPC_CLM_COUNT
                except ValueError:
                    SPC_CLM_COUNT, created = Document_attributes.objects.get_or_create(attr_type=SPC_CLM_COUNT_ATTR, value_str='1')
                    if created == True:
                        SPC_CLM_COUNT.value_int = 1
                        SPC_CLM_COUNT.save()

            else:
                try:
                    count = StrToNumber(_str)
                    if qty > 1:
                        count *= qty
                        SPC_CLM_COUNT, created = Document_attributes.objects.get_or_create(attr_type=SPC_CLM_COUNT_ATTR, value_str=str(count))
                        if created == True:
                            SPC_CLM_COUNT.value_int = count
                            SPC_CLM_COUNT.save()
                        return SPC_CLM_COUNT
                    else:
                        return item_line.SPC_CLM_COUNT
                except ValueError:
                    SPC_CLM_COUNT, created = Document_attributes.objects.get_or_create(attr_type=SPC_CLM_COUNT_ATTR, value_str='1')
                    if created == True:
                        SPC_CLM_COUNT.value_int = 1
                        SPC_CLM_COUNT.save()

        else:
            return item_line.SPC_CLM_COUNT

    @staticmethod
    def make_launch(data):
        # logger.debug(f'data: {data}')

        from isc_common.auth.models.user import User
        from kaf_pas.ckk.models.item_line import Item_line
        from kaf_pas.ckk.models.item_refs import Item_refs
        from kaf_pas.ckk.models.locations import Locations
        from kaf_pas.production.models.launch_item_line import Launch_item_line
        from kaf_pas.production.models.launch_item_refs import Launch_item_refs
        from kaf_pas.production.models.launch_operation_material import Launch_operations_material
        from kaf_pas.production.models.launch_operation_resources import Launch_operation_resources
        from kaf_pas.production.models.launch_operations_item import Launch_operations_item
        from kaf_pas.production.models.operation_material import Operation_material
        from kaf_pas.production.models.operation_resources import Operation_resources
        from kaf_pas.production.models.operations_item import Operations_item

        demand_id = data.get('demand_id')
        qty = data.get('qty')

        description = data.get('description')
        date = data.get('date')
        date = datetime.datetime.strptime(date, '%Y-%m-%d')
        user = User.objects.get(id=data.get('user_id'))
        status = settings.PROD_OPERS_STACK.FORMIROVANIE

        with transaction.atomic():
            for demand in Demand.objects.select_for_update().filter(id=demand_id):
                cnt = Launches.objects.filter(demand=demand).count() + 1
                code = f'{demand.code}/{cnt}'
                tail_qty = Demand_view.objects.get(id=demand_id).tail_qty
                if tail_qty < qty:
                    raise Exception(f'Затребованное количестово для запуска ({qty}), превышает возможное к запуску ({tail_qty})')

                launch = Launches.objects.create(
                    code=code,
                    date=date,
                    demand_id=demand_id,
                    description=description,
                    qty=qty,
                    status=status
                )

                progress = ProgressStack(
                    host=settings.WS_HOST,
                    port=settings.WS_PORT,
                    channel=f'common_{user.username}',
                )

                id_progress = f'launch_{launch.id}_{user.id}'
                demand_str = f'<h3>Формирование запуска: Заказ № {demand.code} от {DateToStr(demand.date)}</h3>'

                cntAll = Item_refs.objects.get_descendants_count(id=demand.precent_item.item.id, where_clause='where is_bit_on(props::integer, 0) = true')
                # logger.debug(f'cntAll: {cntAll}')
                progress.show(
                    title=f'<b>Обработано товарных позиций</b>',
                    label_contents=demand_str,
                    cntAll=cntAll,
                    id=id_progress
                )

                cnt = 0
                Item_refs.objects.filter(child=F('parent')).delete()
                try:

                    for item_ref in Item_refs.objects.get_descendants(id=demand.precent_item.item.id, where_clause='where is_bit_on(props::integer, 0) = true'):

                        launch_item_refs, _ = Launch_item_refs.objects.get_or_create(
                            child=item_ref.child,
                            parent=item_ref.parent if item_ref.level != 1 else None,
                            launch=launch,
                            defaults=dict(item_refs=item_ref)
                        )

                        for item_line in Item_line.objects.filter(parent=item_ref.parent, child=item_ref.child):
                            # logger.debug(item_ref)

                            Launch_item_line.objects.get_or_create(
                                child=item_line.child,
                                parent=item_line.parent,
                                item_line=item_line,
                                launch=launch,

                                SPC_CLM_FORMAT=item_line.SPC_CLM_FORMAT,
                                SPC_CLM_ZONE=item_line.SPC_CLM_ZONE,
                                SPC_CLM_POS=item_line.SPC_CLM_POS,
                                SPC_CLM_MARK=item_line.SPC_CLM_MARK,
                                SPC_CLM_NAME=item_line.SPC_CLM_NAME,
                                SPC_CLM_COUNT=LaunchesManager.get_count(item_line, qty),
                                SPC_CLM_NOTE=item_line.SPC_CLM_NOTE,
                                SPC_CLM_MASSA=item_line.SPC_CLM_MASSA,
                                SPC_CLM_MATERIAL=item_line.SPC_CLM_MATERIAL,
                                SPC_CLM_USER=item_line.SPC_CLM_USER,
                                SPC_CLM_KOD=item_line.SPC_CLM_KOD,
                                SPC_CLM_FACTORY=item_line.SPC_CLM_FACTORY,
                                section=item_line.section,
                                section_num=item_line.section_num,
                                subsection=item_line.subsection,
                            )

                            # logger.debug(item_line)

                        def rec_operations_data(item):
                            cnt = Operations_item.objects.filter(item=item).count()
                            if cnt == 0:
                                launch_operations_item, _ = Launch_operations_item.objects.get_or_create(
                                    item=item,
                                    launch=launch,
                                    num=0,
                                    operation=settings.OPERS_STACK.NOOP,
                                )

                                Launch_operation_resources.objects.get_or_create(
                                    launch_operationitem=launch_operations_item,
                                    location=Locations.objects.get(code='000'),
                                )
                            else:
                                for operations_item in Operations_item.objects.filter(item=item):
                                    launch_operations_item, _ = Launch_operations_item.objects.get_or_create(
                                        item=operations_item.item,
                                        launch=launch,
                                        num=operations_item.num,
                                        operation=operations_item.operation,
                                        defaults=dict(
                                            description=operations_item.description,
                                            ed_izm=operations_item.ed_izm,
                                            operationitem=operations_item,
                                            qty=operations_item.qty,
                                        )
                                    )
                                    for operation_material in Operation_material.objects.filter(operationitem=operations_item):
                                        Launch_operations_material.objects.get_or_create(
                                            launch_operationitem=launch_operations_item,
                                            material=operation_material.material,
                                            material_askon=operation_material.material_askon,
                                            defaults=dict(
                                                edizm=operation_material.edizm,
                                                qty=operation_material.qty,
                                                operation_material=operation_material,
                                            )
                                        )
                                    for operation_resources in Operation_resources.objects.filter(operationitem=operations_item):
                                        Launch_operation_resources.objects.get_or_create(
                                            launch_operationitem=launch_operations_item,
                                            resource=operation_resources.resource,
                                            location=operation_resources.location,
                                            defaults=dict(
                                                operation_resources=operation_resources,
                                                batch_size=operation_resources.batch_size,
                                            )
                                        )

                        if item_ref.parent:
                            rec_operations_data(item_ref.parent)
                        rec_operations_data(item_ref.child)

                        progress.setCntDone(cnt, id_progress)
                        cnt += 1

                    progress.close(id=id_progress)
                    settings.EVENT_STACK.EVENTS_PRODUCTION_MAKE_LAUNCH.send_message(f'Выполнено формирование запуска  <h3>{launch.code} от {launch.date}</h3><p/>')
                except Exception as ex:
                    progress.close(id=id_progress)
                    raise ex
        return data

    # @staticmethod
    # def update_launch(data):
    #     logger.debug(f'data: {data}')
    #
    #     from isc_common.auth.models.user import User
    #     from kaf_pas.ckk.models.item_line import Item_line
    #     from kaf_pas.ckk.models.item_refs import Item_refs
    #     from kaf_pas.production.models.launch_item_line import Launch_item_line
    #     from kaf_pas.production.models.launch_item_refs import Launch_item_refs
    #     from kaf_pas.production.models.launch_operations_item import Launch_operations_item
    #     from kaf_pas.production.models.operation_material import Operation_material
    #     from kaf_pas.production.models.operation_resources import Operation_resources
    #     from kaf_pas.production.models.operations_item import Operations_item
    #     from kaf_pas.production.models.launch_operation_material import Launch_operations_material
    #     from kaf_pas.production.models.launch_operation_resources import Launch_operation_resources
    #
    #     id = data.get('id')
    #     demand_id = data.get('demand_id')
    #     qty = data.get('qty')
    #     code = data.get('code')
    #     description = data.get('description')
    #     date = data.get('date')
    #     date = datetime.datetime.strptime(date.replace('T00:00:00.000', ''), '%Y-%m-%d')
    #     user = User.objects.get(id=getAttr(data, 'user_id'))
    #     status, _ = Status_launch.objects.update_or_create(name='Переформирование', editing=False, deliting=False)
    #
    #     def rec_operations_data(item, launch_item_refs, item_message):
    #         for operations_item in Operations_item.objects.filter(item=item):
    #
    #             try:
    #                 launch_operations_item = Launch_operations_item.objects.get(
    #                     description=operations_item.description,
    #                     ed_izm=operations_item.ed_izm,
    #                     item=operations_item.item,
    #                     launch=parent_launch,
    #                     num=operations_item.num,
    #                     operation=operations_item.operation,
    #                     operationitem=operations_item,
    #                 )
    #                 if launch_operations_item.qty != operations_item.qty:
    #                     _launch_operations_item, _ = Launch_operations_item.objects.get_or_create(
    #                         description=operations_item.description,
    #                         ed_izm=operations_item.ed_izm,
    #                         item=operations_item.item,
    #                         launch=launch,
    #                         num=operations_item.num,
    #                         operation=operations_item.operation,
    #                         operationitem=operations_item,
    #                         parent=launch_operations_item,
    #                         qty=launch_operations_item.qty,
    #                     )
    #                     Launch_operations_item.objects.get_or_create(
    #                         description=operations_item.description,
    #                         ed_izm=operations_item.ed_izm,
    #                         item=operations_item.item,
    #                         launch=parent_launch,
    #                         num=operations_item.num,
    #                         operation=operations_item.operation,
    #                         operationitem=operations_item,
    #                         parent=_launch_operations_item,
    #                         qty=operations_item.qty,
    #                     )
    #                     launch_operations_item.props &= ~Launch_operations_item.props.enabled
    #                     item_message.append(f'Для операции {launch_operations_item} изменена длительность.')
    #                     launch_item_refs.props |= Launch_item_refs.props.edited
    #                     launch_item_refs.save()
    #                 else:
    #                     launch_operations_item.props |= Launch_operations_item.props.refreshed
    #                 launch_operations_item.save()
    #
    #                 for operation_material in Operation_material.objects.filter(operationitem=operations_item):
    #                     try:
    #                         launch_operations_material = Launch_operations_material.objects.get(
    #                             operation_material=operation_material,
    #                             launch_operationitem=launch_operations_item,
    #                             material=operation_material.material,
    #                             material_askon=operation_material.material_askon,
    #                             edizm=operation_material.edizm,
    #                             qty=operation_material.qty,
    #                         )
    #
    #                         if launch_operations_material.qty != operation_material.qty:
    #                             _launch_operations_material, _ = Launch_operations_material.objects.get_or_create(
    #                                 operation_material=operation_material,
    #                                 launch_operationitem=launch_operations_item,
    #                                 material=operation_material.material,
    #                                 material_askon=operation_material.material_askon,
    #                                 edizm=operation_material.edizm,
    #                                 qty=launch_operations_material.qty,
    #                                 parent=launch_operations_material,
    #                             )
    #
    #                             Launch_operations_material.objects.get_or_create(
    #                                 operation_material=operation_material,
    #                                 launch_operationitem=launch_operations_item,
    #                                 material=operation_material.material,
    #                                 material_askon=operation_material.material_askon,
    #                                 edizm=operation_material.edizm,
    #                                 qty=launch_operations_material.qty,
    #                                 parent=_launch_operations_material,
    #                             )
    #
    #                             item_message.append(f'Для материала {launch_operations_material} изменено количество.')
    #
    #                             launch_operations_material.props &= ~Launch_operations_material.props.enabled
    #                             launch_item_refs.props |= Launch_item_refs.props.edited
    #                             launch_item_refs.save()
    #                         else:
    #                             launch_operations_material.props |= Launch_operations_material.props.refreshed
    #                         launch_operations_material.save()
    #
    #                     except Launch_operations_material.DoesNotExist:
    #                         Launch_operations_material.objects.get_or_create(
    #                             operation_material=operation_material,
    #                             launch_operationitem=launch_operations_item,
    #                             material=operation_material.material,
    #                             material_askon=operation_material.material_askon,
    #                             edizm=operation_material.edizm,
    #                             qty=operation_material.qty,
    #                         )
    #
    #                 for operation_resources in Operation_resources.objects.filter(operationitem=operations_item):
    #                     try:
    #                         launch_operation_resources = Launch_operation_resources.objects.get(
    #                             operation_resources=operation_resources,
    #                             launch_operationitem=launch_operations_item,
    #                             resource=operation_resources.resource,
    #                             location=operation_resources.location,
    #                         )
    #                         launch_operation_resources.props |= Launch_operation_resources.props.refreshed
    #                         launch_operation_resources.save()
    #                     except Launch_operation_resources.DoesNotExist:
    #                         Launch_operation_resources.objects.get_or_create(
    #                             operation_resources=operation_resources,
    #                             launch_operationitem=launch_operations_item,
    #                             resource=operation_resources.resource,
    #                             location=operation_resources.location,
    #                             batch_size=operation_resources.batch_size,
    #                         )
    #
    #             except Launch_operations_item.DoesNotExist:
    #                 launch_operations_item, created = Launch_operations_item.objects.get_or_create(
    #                     description=operations_item.description,
    #                     ed_izm=operations_item.ed_izm,
    #                     item=operations_item.item,
    #                     launch=launch,
    #                     num=operations_item.num,
    #                     operation=operations_item.operation,
    #                     operationitem=operations_item,
    #                     qty=operations_item.qty,
    #                 )
    #                 item_message.append(f'Добавлена операция {launch_operations_item}.')
    #                 for operation_material in Operation_material.objects.filter(operationitem=operations_item):
    #                     Launch_operations_material.objects.get_or_create(
    #                         operation_material=operation_material,
    #                         launch_operationitem=launch_operations_item,
    #                         material=operation_material.material,
    #                         material_askon=operation_material.material_askon,
    #                         edizm=operation_material.edizm,
    #                         qty=operation_material.qty,
    #                     )
    #                     item_message.append(f'Добавлен материал {operation_material}.')
    #                 for operation_resources in Operation_resources.objects.filter(operationitem=operations_item):
    #                     Launch_operation_resources.objects.get_or_create(
    #                         operation_resources=operation_resources,
    #                         launch_operationitem=launch_operations_item,
    #                         resource=operation_resources.resource,
    #                         location=operation_resources.location,
    #                         batch_size=operation_resources.batch_size,
    #                     )
    #                     item_message.append(f'Добавлен ресурс {operation_resources}.')
    #
    #                 launch_item_refs.props |= Launch_item_refs.props.edited
    #                 launch_item_refs.save()
    #
    #         # logger.debug(f'not_rfreshed_or_edited_qty: {get_not_rfreshed_or_edited_qty()}')
    #         for launch_operations_item in Launch_operations_item.objects. \
    #                 filter(item=item, launch=parent_launch). \
    #                 exclude(props=Launch_operations_item.props.refreshed):
    #             launch_operations_item.props &= ~Launch_operations_item.props.enabled
    #             launch_operations_item.disabled_launch = launch
    #             launch_operations_item.save()
    #
    #     def append_line(item_line, SPC_CLM_COUNT):
    #         launch_item_line, _ = Launch_item_line.objects.get_or_create(
    #             child=item_line.child,
    #             parent=item_line.parent,
    #             item_line=item_line,
    #             launch=launch,
    #
    #             SPC_CLM_FORMAT=item_line.SPC_CLM_FORMAT,
    #             SPC_CLM_ZONE=item_line.SPC_CLM_ZONE,
    #             SPC_CLM_POS=item_line.SPC_CLM_POS,
    #             SPC_CLM_MARK=item_line.SPC_CLM_MARK,
    #             SPC_CLM_NAME=item_line.SPC_CLM_NAME,
    #             SPC_CLM_COUNT=SPC_CLM_COUNT,
    #             SPC_CLM_NOTE=item_line.SPC_CLM_NOTE,
    #             SPC_CLM_MASSA=item_line.SPC_CLM_MASSA,
    #             SPC_CLM_MATERIAL=item_line.SPC_CLM_MATERIAL,
    #             SPC_CLM_USER=item_line.SPC_CLM_USER,
    #             SPC_CLM_KOD=item_line.SPC_CLM_KOD,
    #             SPC_CLM_FACTORY=item_line.SPC_CLM_FACTORY,
    #             section=item_line.section,
    #             section_num=item_line.section_num,
    #             subsection=item_line.subsection,
    #         )
    #
    #         Launch_item_line.objects.get_or_create(
    #             child=item_line.child,
    #             parent=item_line.parent,
    #             added_parent=launch_item_line,
    #             item_line=item_line,
    #             launch=parent_launch,
    #
    #             SPC_CLM_FORMAT=item_line.SPC_CLM_FORMAT,
    #             SPC_CLM_ZONE=item_line.SPC_CLM_ZONE,
    #             SPC_CLM_POS=item_line.SPC_CLM_POS,
    #             SPC_CLM_MARK=item_line.SPC_CLM_MARK,
    #             SPC_CLM_NAME=item_line.SPC_CLM_NAME,
    #             SPC_CLM_COUNT=SPC_CLM_COUNT,
    #             SPC_CLM_NOTE=item_line.SPC_CLM_NOTE,
    #             SPC_CLM_MASSA=item_line.SPC_CLM_MASSA,
    #             SPC_CLM_MATERIAL=item_line.SPC_CLM_MATERIAL,
    #             SPC_CLM_USER=item_line.SPC_CLM_USER,
    #             SPC_CLM_KOD=item_line.SPC_CLM_KOD,
    #             SPC_CLM_FACTORY=item_line.SPC_CLM_FACTORY,
    #             section=item_line.section,
    #             section_num=item_line.section_num,
    #             subsection=item_line.subsection,
    #             editing=False,
    #             deliting=False,
    #         )
    #
    #     with transaction.atomic():
    #         for parent_launch in Launches.objects.select_for_update().filter(id=id):
    #             for demand in Demand.objects.select_for_update().filter(id=demand_id):
    #                 tail_qty = Demand_view.objects.get(id=demand_id).tail_qty + parent_launch.qty
    #                 if tail_qty < qty:
    #                     raise Exception(f'Затребованное количестово для переформирования ({qty}), превышает возможное к запуску ({tail_qty})')
    #
    #                 launch, _ = Launches.objects.get_or_create(
    #                     code=code,
    #                     date=date,
    #                     demand_id=demand_id,
    #                     description=description,
    #                     qty=qty,
    #                     status=status,
    #                     parent=parent_launch,
    #                     editing=False
    #                 )
    #
    #                 progress = ProgressStack(
    #                     host=settings.WS_HOST,
    #                     port=settings.WS_PORT,
    #                     channel=f'common_{user.username}',
    #                 )
    #
    #                 id_progress1 = f'launch_{launch.id}_{user.id}'
    #                 demand_str = f'<h3>Переформирование запуска (этап-I): № {parent_launch.code} от {DateToStr(parent_launch.date)}</h3>'
    #
    #                 cntAll = Item_refs.objects.get_descendants_count(id=demand.precent_item.item.id)
    #                 progress.show(
    #                     title=f'<b>Обработано товарных позиций</b>',
    #                     label_contents=demand_str,
    #                     cntAll=cntAll,
    #                     id=id_progress1
    #                 )
    #
    #                 cnt = 0
    #                 Item_refs.objects.filter(child=F('parent')).delete()
    #
    #                 for item_ref in Item_refs.objects.get_descendants(id=demand.precent_item.item.id):
    #                     item_message = []
    #                     launch_item_refs, created = Launch_item_refs.objects.get_or_create(
    #                         child=item_ref.child,
    #                         parent=item_ref.parent if item_ref.level != 1 else None,
    #                         item_refs=item_ref,
    #                         launch=parent_launch,
    #                         defaults=dict(
    #                             props=Launch_item_refs.props.enabled | Launch_item_refs.props.added,
    #                             added_launch=launch
    #                         )
    #                     )
    #
    #                     if created:
    #                         launch_item_refs, _ = Launch_item_refs.objects.get_or_create(
    #                             child=item_ref.child,
    #                             parent=item_ref.parent if item_ref.level != 1 else None,
    #                             item_refs=item_ref,
    #                             launch=launch,
    #                         )
    #
    #                         item_message.append(f'Товарная позиция: {launch_item_refs.child.item_name} добавлена в спецификациию, как ранее не существовавшая.')
    #
    #                         for item_line in Item_line.objects.filter(parent=launch_item_refs.parent, child=launch_item_refs.child):
    #                             append_line(item_line, LaunchesManager.get_count(item_line, qty))
    #
    #                     else:
    #                         launch_item_refs, _ = Launch_item_refs.objects.get_or_create(
    #                             child=item_ref.child,
    #                             parent=item_ref.parent if item_ref.level != 1 else None,
    #                             item_refs=item_ref,
    #                             launch=launch,
    #                         )
    #
    #                         for item_line in Item_line.objects.filter(parent=launch_item_refs.parent, child=launch_item_refs.child):
    #                             try:
    #                                 launch_item_line = Launch_item_line.objects.get(
    #                                     child=item_line.child,
    #                                     parent=item_line.parent,
    #                                     item_line=item_line,
    #                                     launch=parent_launch,
    #                                 )
    #
    #                                 if item_line.SPC_CLM_FORMAT != launch_item_line.SPC_CLM_FORMAT or \
    #                                         item_line.SPC_CLM_ZONE != launch_item_line.SPC_CLM_ZONE or \
    #                                         item_line.SPC_CLM_POS != launch_item_line.SPC_CLM_POS or \
    #                                         item_line.SPC_CLM_MARK != launch_item_line.SPC_CLM_MARK or \
    #                                         item_line.SPC_CLM_NAME != launch_item_line.SPC_CLM_NAME or \
    #                                         LaunchesManager.get_count(item_line, qty) != launch_item_line.SPC_CLM_COUNT or \
    #                                         item_line.SPC_CLM_NOTE != launch_item_line.SPC_CLM_NOTE or \
    #                                         item_line.SPC_CLM_MASSA != launch_item_line.SPC_CLM_MASSA or \
    #                                         item_line.SPC_CLM_MATERIAL != launch_item_line.SPC_CLM_MATERIAL or \
    #                                         item_line.SPC_CLM_USER != launch_item_line.SPC_CLM_USER or \
    #                                         item_line.SPC_CLM_KOD != launch_item_line.SPC_CLM_KOD or \
    #                                         item_line.SPC_CLM_FACTORY != launch_item_line.SPC_CLM_FACTORY or \
    #                                         item_line.section != launch_item_line.section or \
    #                                         item_line.section_num != launch_item_line.section_num or \
    #                                         item_line.subsection != launch_item_line.subsection:
    #                                     launch_item_line.props &= ~Launch_item_line.props.enabled
    #                                     launch_item_line.save()
    #
    #                                     item_message.append(f'Изменена строка детелизации : {launch_item_line.item_name}.')
    #
    #                                     append_line(item_line, LaunchesManager.get_count(item_line, qty))
    #                                     launch_item_refs.props |= Launch_item_refs.props.edited
    #                                     launch_item_refs.save()
    #                                 else:
    #                                     pass
    #
    #                             except Launch_item_line.DoesNotExist:
    #                                 item_message.append(f'Cтрока детелизации : {item_line.child.item_name} добавлена, как ранее не существовавшая.')
    #                                 append_line(item_line, LaunchesManager.get_count(item_line, qty))
    #
    #                     if item_ref.parent:
    #                         rec_operations_data(item=launch_item_refs.parent, launch_item_refs=launch_item_refs, item_message=item_message)
    #                     rec_operations_data(item=launch_item_refs.child, launch_item_refs=launch_item_refs, item_message=item_message)
    #
    #                     if ~launch_item_refs.props.edited:
    #                         launch_item_refs.delete()
    #
    #                     progress.setCntDone(cnt, id_progress1)
    #                     cnt += 1
    #
    #                 launch_item_refs = Launch_item_refs.objects.filter(launch=launch)
    #                 cntAll = launch_item_refs.count()
    #                 if cntAll == 0:
    #                     msg_str = f'Выполненое Переформирование запуска  <h3>{parent_launch.code} от {parent_launch.date}</h3> изменений не обнаружило.<p/>'
    #                     launch.delete()
    #                 else:
    #                     id_progress2 = f'launch_{launch.id}_{user.id}'
    #                     demand_str = f'<h3>Переформирование запуска (этап-II): № {parent_launch.code} от {DateToStr(parent_launch.date)}</h3>'
    #
    #                     progress.show(
    #                         title=f'<b>Обработано товарных позиций</b>',
    #                         label_contents=demand_str,
    #                         cntAll=cntAll,
    #                         id=id_progress2
    #                     )
    #
    #                     cnt = 0
    #                     for launch_item in launch_item_refs:
    #                         for _launch_item in Launch_item_refs.tree_objects.get_descendants(child_id=launch_item.child.id, parent_id=launch_item.parent.id, where_clause=f' where r.launch_id={launch.id}'):
    #                             print(_launch_item)
    #                         progress.setCntDone(cnt, id_progress2)
    #                         cnt += 1
    #                     progress.close(id=id_progress2)
    #                     msg_str = f'Выполнено Переформирование запуска  <h3>{parent_launch.code} от {parent_launch.date}</h3><p/>'
    #
    #             progress.close(id=id_progress1)
    #             settings.EVENT_STACK.EVENTS_PRODUCTION_RE_MAKE_LAUNCH.send_message(msg_str)
    #
    #     return data

    def createFromRequest(self, request):
        request = DSRequest(request=request)
        data = request.get_data()
        setAttr(data, 'user_id', request.user_id)
        return LaunchesManager.make_launch(data)

    def reCreateFromRequest(self, request):
        request = DSRequest(request=request)
        data = request.get_data()
        setAttr(data, 'user_id', request.user_id)
        return LaunchesManager.update_launch(data)

    def deleteFromRequest(self, request, removed=None, ):
        from kaf_pas.planing.models.operation_launches import Operation_launches
        from kaf_pas.production.models.launch_item_line import Launch_item_line
        from kaf_pas.production.models.launch_item_refs import Launch_item_refs
        from kaf_pas.production.models.launch_operation_material import Launch_operations_material
        from kaf_pas.production.models.launch_operation_resources import Launch_operation_resources
        from kaf_pas.production.models.launch_operations_item import Launch_operations_item

        request = DSRequest(request=request)
        res = 0
        tuple_ids = request.get_tuple_ids()
        progress = ProgressStack(
            host=settings.WS_HOST,
            port=settings.WS_PORT,
            channel=f'common_{request.username}',
        )

        with transaction.atomic():
            for id, mode in tuple_ids:
                if mode == 'hide':
                    super().filter(id=id).soft_delete()
                else:
                    launch = Launches.objects.get(id=id)
                    id_progress = f'launch_{id}_{request.user_id}'
                    demand_str = f'<h3>Удаление запуска: № {launch.code} от {DateToStr(launch.date)}</h3>'

                    cntAll = Launch_operations_item.objects.filter(launch=id).count()
                    cnt = 0
                    # logger.debug(f'cntAll: {cntAll}')
                    progress.show(
                        title=f'<b>Обработано товарных позиций</b>',
                        label_contents=demand_str,
                        cntAll=cntAll,
                        id=id_progress
                    )

                    qty, _ = Launch_item_refs.objects.filter(launch_id=id).delete()
                    qty1, _ = Launch_item_line.objects.filter(launch_id=id).delete()
                    qty += qty1

                    for launch_operations_item in Launch_operations_item.objects.filter(launch=id):
                        qty1, _ = Launch_operations_material.objects.filter(launch_operationitem=launch_operations_item).delete()
                        qty += qty1
                        qty1, _ = Launch_operation_resources.objects.filter(launch_operationitem=launch_operations_item).delete()
                        qty += qty1
                        launch_operations_item.delete()
                        qty += 1
                        progress.setCntDone(cnt, id_progress)
                        cnt += 1

                    for operation_launches in Operation_launches.objects.filter(launch_id=id):
                        operation_launches.operation.delete()
                    qty1, _ = super().filter(id=id).delete()

                    progress.close(id=id_progress)
                    settings.EVENT_STACK.EVENTS_PRODUCTION_DELETE_LAUNCH.send_message(f'Выполнено удаление запуска  <h3>{launch.code} от {launch.date}</h3><p/>')
                res += qty + qty1
        return res

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
            'props': record.props,

            'editing': record.editing,
            'deliting': record.deliting,
        }
        return DelProps(res)

    @staticmethod
    def props():
        return BitField(flags=(
            ('routing_made', 'Маршрутизация выполнена'),  # 1
        ), default=0, db_index=True)

    def get_queryset(self):
        return LaunchesQuerySet(self.model, using=self._db)


class Launches(BaseRefHierarcy):
    date = DateTimeField()
    status = ForeignKeyProtect(Status_launch)
    demand = ForeignKeyProtect(Demand)
    qty = PositiveIntegerField()
    props = LaunchesManager.props()

    objects = LaunchesManager()

    def __str__(self):
        return f"ID:{self.id}, " \
               f"code: {self.code}, " \
               f"name: {self.name}, " \
               f"description: {self.description}, " \
               f"date: {self.date}, " \
               f"status: [{self.status}], " \
               f"demand: [{self.demand}], " \
               f"qty: {self.qty}"

    class Meta:
        verbose_name = 'Запуски'
