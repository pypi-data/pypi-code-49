import logging

from bitfield import BitField
from django.db import transaction, connection
from django.db.models import BigIntegerField, deletion

from isc_common import Stack
from isc_common.common.mat_views import create_tmp_mat_view, drop_mat_view
from isc_common.fields.related import ForeignKeyProtect
from isc_common.http.DSRequest import DSRequest
from isc_common.models.audit import AuditManager, AuditQuerySet, AuditModel
from isc_common.progress import managed_progress
from kaf_pas.ckk.models.attr_type import Attr_type
from kaf_pas.kd.models.documents import Documents, DocumentManager

logger = logging.getLogger(__name__)


class Lotsman_documents_hierarcyQuerySet(AuditQuerySet):
    def delete(self):
        return super().delete()

    def create(self, **kwargs):
        return super().create(**kwargs)

    def filter(self, *args, **kwargs):
        return super().filter(*args, **kwargs)


class Lotsman_documents_hierarcyManager(AuditManager):
    @staticmethod
    def delete(id, user):
        from isc_common.auth.models.user import User
        from kaf_pas.ckk.models.item import Item
        from kaf_pas.ckk.models.item import ItemManager
        from kaf_pas.kd.models.documents_thumb import Documents_thumb
        from kaf_pas.kd.models.documents_thumb10 import Documents_thumb10
        from kaf_pas.kd.models.lotsman_document_attr_cross import Lotsman_document_attr_cross
        from kaf_pas.kd.models.lotsman_documents_hierarcy_files import Lotsman_documents_hierarcy_files

        if not isinstance(user, User):
            raise Exception(f'user  must be a User instance.')

        res = 0

        Documents_thumb.objects.filter(lotsman_document_id=id).delete()
        Documents_thumb10.objects.filter(lotsman_document_id=id).delete()
        Lotsman_document_attr_cross.objects.filter(document_id=id).delete()

        for item in Item.objects.filter(lotsman_document_id=id):
            ItemManager.delete_recursive(item_id=item.id, user=user)

        Lotsman_documents_hierarcy_files.objects.filter(lotsman_document_id=id).delete()
        try:
            res += Lotsman_documents_hierarcy.objects.filter(id=id).delete()[0]
        except deletion.ProtectedError:
            pass
        return res

    @staticmethod
    def delete_file(id, user):
        from isc_common.auth.models.user import User
        from kaf_pas.kd.models.documents_thumb import Documents_thumb
        from kaf_pas.kd.models.documents_thumb10 import Documents_thumb10
        from kaf_pas.kd.models.lotsman_documents_hierarcy_files import Lotsman_documents_hierarcy_files

        if not isinstance(user, User):
            raise Exception(f'user  must be a User instance.')

        res = 0

        res += Documents_thumb.objects.filter(lotsman_document_id=id).delete()[0]
        res += Documents_thumb10.objects.filter(lotsman_document_id=id).delete()[0]

        res += Lotsman_documents_hierarcy_files.objects.filter(lotsman_document_id=id).delete()[0]
        return res

    @staticmethod
    def get_props():
        return BitField(flags=(
            ('relevant', 'Актуальность'),
            ('beenItemed', 'Был внесен в состав изделий'),
        ), default=1, db_index=True)

    @staticmethod
    def make_items(logger, record=None):
        from kaf_pas.ckk.models.item import Item
        from kaf_pas.ckk.models.item_refs import Item_refs
        from kaf_pas.kd.models.document_attributes import Document_attributesManager
        from kaf_pas.kd.models.lotsman_documents_hierarcy_view import Lotsman_documents_hierarcy_view
        from kaf_pas.system.models.contants import Contants

        items_pairs = Stack()

        assmbl_progress = None
        progress = None
        mat_view_name = None
        try:
            imp_frpm_lotsman_label = 'Импорт из Лоцмана'
            top_parent = None

            if record == None:
                record = Lotsman_documents_hierarcy.objects.get(id=1)

            lotsman_documents_hierarcy_parent_id = record.get('parent')
            if lotsman_documents_hierarcy_parent_id != None:
                try:
                    top_parent = Item.objects.get(lotsman_document_id=lotsman_documents_hierarcy_parent_id)
                except Item.DoesNotExist:
                    raise Exception(f'Не существует товарной позиции родителя.')

            if top_parent == None:
                top_parent, created = Item.objects.get_or_create(
                    STMP_1=Document_attributesManager.get_or_create_attribute(
                        attr_codes='STMP_1',
                        value_str=imp_frpm_lotsman_label,
                        logger=logger
                    )[0],
                    props=Item.props.relevant | Item.props.from_lotsman
                )

                Item_refs.objects.get_or_create(
                    child=top_parent
                )

            item_top_level, _ = Contants.objects.update_or_create(
                code='top_level',
                defaults=dict(
                    name='Вершины товарных позиций')
            )
            const4, _ = Contants.objects.update_or_create(
                code='lotsman_top_level',
                defaults=dict(
                    parent=item_top_level,
                    name=imp_frpm_lotsman_label,
                    value=top_parent.id)
            )

            parent_str = 'parent_id IS NULL'

            if lotsman_documents_hierarcy_parent_id != None:
                parent_str = f'''parent_id ={record.get('id')}'''
            props_str = f'props in (1, 3)'

            sql_str = f'''WITH RECURSIVE r AS (
                            SELECT *, 1 AS level
                            FROM kd_lotsman_documents_hierarcy_mview
                            WHERE {parent_str}
                                  and  {props_str}  

                            union all

                            SELECT kd_lotsman_documents_hierarcy_mview.*, r.level + 1 AS level
                            FROM kd_lotsman_documents_hierarcy_mview
                                JOIN r
                            ON kd_lotsman_documents_hierarcy_mview.parent_id = r.id)

                        select * from r where {props_str} order by level'''

            mat_view_name = create_tmp_mat_view(sql_str=sql_str, indexes=['attr_name', 'parent_id'])

            with connection.cursor() as cursor:
                cursor.execute(f'select count(*) from {mat_view_name}')
                cnt, = cursor.fetchone()

            logger.debug(f'''SPC_CLM_NAME: {record.get('SPC_CLM_NAME__value_str')}''')
            logger.debug(f'qty: {cnt}')

            if cnt > 0:
                assmbl_progress = None

                with managed_progress(
                        id=record.get('id'),
                        qty=cnt,
                        user=record.get('user_id'),
                        message=f'''Создание товарных позиций ({record.get('SPC_CLM_NAME__value_str')} {cnt} шт.)''',
                        title='Выполнено'
                ) as progress:

                    first_step = True

                    for lotsman_documents_hierarcy in Lotsman_documents_hierarcy_view.objects.raw(f'select * from {mat_view_name} order by level'):
                        with transaction.atomic():
                            if lotsman_documents_hierarcy.attr_name not in ['Материал']:

                                item, created1 = Lotsman_documents_hierarcyManager.get_item(
                                    lotsman_documents_hierarcy=lotsman_documents_hierarcy,
                                    items_pairs=items_pairs,
                                    logger=logger
                                )

                                parent = None
                                if lotsman_documents_hierarcy.parent_id != None:
                                    _lotsman_documents_hierarcy = None
                                    try:
                                        _lotsman_documents_hierarcy = Lotsman_documents_hierarcy_view.objects.get(id=lotsman_documents_hierarcy.parent_id)
                                    except Lotsman_documents_hierarcy_view.DoesNotExist as ex:
                                        raise ex
                                    except Lotsman_documents_hierarcy_view.MultipleObjectsReturned:
                                        _lotsman_documents_hierarcy = Lotsman_documents_hierarcy_view.objects.filter(id=lotsman_documents_hierarcy.parent_id).distinct('id')[0]

                                    parent, created2 = Lotsman_documents_hierarcyManager.get_item(
                                        lotsman_documents_hierarcy=_lotsman_documents_hierarcy,
                                        items_pairs=items_pairs,
                                        logger=logger
                                    )

                                    created3 = False
                                    if first_step == True:
                                        item_refs, created3 = Item_refs.objects.get_or_create(parent=top_parent, child=parent)
                                        first_step = False

                                if parent != item or parent == None:
                                    item_refs, created2 = Item_refs.objects.get_or_create(parent=parent, child=item)

                                # FOR DEBUG
                                # if created == True or created1 == True or created2 == True or created3 == True:
                                #     pass
                                # END FOR DEBUG

                            Lotsman_documents_hierarcy.objects.update_or_create(
                                id=lotsman_documents_hierarcy.id,
                                defaults=dict(
                                    props=lotsman_documents_hierarcy.props | Lotsman_documents_hierarcy.props.beenItemed
                                ))

                        if progress != None:
                            progress.step()

                with connection.cursor() as cursor:
                    cursor.execute(f'''select count(*) from {mat_view_name} where attr_name=%s''', ['''Сборочная единица'''])
                    assmbl_progress_count, = cursor.fetchone()

                with managed_progress(
                        id=f'''assmbl_{record.get('id')}''',
                        qty=assmbl_progress_count,
                        user=record.get('user_id'),
                        message=f'''Создание сборочных единиц. ({assmbl_progress_count}  шт.)''',
                        title='Выполнено'
                ) as assmbl_progress:

                    logger.debug(f'''Сборочные единицы SPC_CLM_NAME: {record.get('SPC_CLM_NAME__value_str')}''')
                    logger.debug(f'qty: {assmbl_progress_count}')

                    for lotsman_documents_hierarcy in Lotsman_documents_hierarcy_view.objects.raw(f'''select * from {mat_view_name} where attr_name=%s order by level''', ['''Сборочная единица''']):
                        with transaction.atomic():
                            assmbl_progress.setContentsLabel(f'''<h3>Создание сборочной единицы. ({lotsman_documents_hierarcy.SPC_CLM_NAME.value_str if lotsman_documents_hierarcy.SPC_CLM_NAME else ''} : 
                                                                                                  {lotsman_documents_hierarcy.SPC_CLM_MARK.value_str if lotsman_documents_hierarcy.SPC_CLM_MARK else ''})</h3>''')
                            item, _ = Lotsman_documents_hierarcyManager.get_item(
                                lotsman_documents_hierarcy=lotsman_documents_hierarcy,
                                items_pairs=items_pairs,
                                logger=logger)

                            Lotsman_documents_hierarcyManager.make_lines(
                                parent=item,
                                items_pairs=items_pairs,
                                logger=logger,
                                mat_view_name=mat_view_name,
                                user_id=record.get('user_id'),
                                record=record,
                            )

                        if progress != None:
                            progress.step()

                        if assmbl_progress != None:
                            assmbl_progress.step()

                with connection.cursor() as cursor:
                    cursor.execute(f'''select count(*) from {mat_view_name} where attr_name=%s''', ['''Чертеж'''])
                    assmbl_progress_count, = cursor.fetchone()

                with managed_progress(
                        id=f'''assmbl_{record.get('id')}''',
                        qty=assmbl_progress_count,
                        user=record.get('user_id'),
                        message=f'''Привязка чертежей. ({assmbl_progress_count}  шт.)''',
                        title='Выполнено'
                ) as assmbl_progress:

                    logger.debug(f'''Чертежи SPC_CLM_NAME: {record.get('SPC_CLM_NAME__value_str')}''')
                    logger.debug(f'qty: {assmbl_progress_count}')

                    for lotsman_documents_hierarcy in Lotsman_documents_hierarcy_view.objects.raw(f'''select * from {mat_view_name} where attr_name=%s order by level''', ['''Чертеж''']):
                        with transaction.atomic():

                            assmbl_progress.setContentsLabel(f'''<h3>Привязка чертежей. ({lotsman_documents_hierarcy.SPC_CLM_NAME.value_str if lotsman_documents_hierarcy.SPC_CLM_NAME else ''} : 
                                                                                         {lotsman_documents_hierarcy.SPC_CLM_MARK.value_str if lotsman_documents_hierarcy.SPC_CLM_MARK else ''})</h3>''')
                            item, _ = Lotsman_documents_hierarcyManager.get_item(
                                lotsman_documents_hierarcy=lotsman_documents_hierarcy,
                                items_pairs=items_pairs,
                                logger=logger)

                            for item_ref in Item_refs.objects.filter(child=item):
                                if item_ref.parent.lotsman_document.attr_type.code != 'Сборочная единица':
                                    DocumentManager.link_image_to_lotsman_item(
                                        lotsman_document=lotsman_documents_hierarcy,
                                        item=item_ref.parent,
                                        logger=logger
                                    )
                                    item_ref.delete()

                        if assmbl_progress != None:
                            assmbl_progress.step()

                        if progress != None:
                            progress.step()

                with managed_progress(
                        id=f'''assmbl_{record.get('id')}''',
                        qty=assmbl_progress_count,
                        user=record.get('user_id'),
                        message=f'''Перемещение чертежей. ({assmbl_progress_count}  шт.)''',
                        title='Выполнено'
                ) as assmbl_progress:

                    for lotsman_documents_hierarcy in Lotsman_documents_hierarcy_view.objects.raw(f'''select * from {mat_view_name} where attr_name=%s order by level''', ['''Чертеж''']):
                        with transaction.atomic():
                            item, _ = Lotsman_documents_hierarcyManager.get_item(
                                lotsman_documents_hierarcy=lotsman_documents_hierarcy,
                                items_pairs=items_pairs,
                                logger=logger)

                            if Item_refs.objects.filter(child=item).count() == 0 and Item_refs.objects.filter(parent=item).count() == 0:
                                item.delete()

                        if assmbl_progress != None:
                            assmbl_progress.step()

                        if progress != None:
                            progress.step()

                    assmbl_progress.sendInfo('Создание выполнено.')

            drop_mat_view(mat_view_name)
        except Exception as ex:
            drop_mat_view(mat_view_name)
            raise ex

    @staticmethod
    def make_lines(parent, items_pairs, logger, mat_view_name, user_id, record):
        from kaf_pas.ckk.models.item import Item
        from kaf_pas.kd.models.lotsman_documents_hierarcy_view import Lotsman_documents_hierarcy_view
        from kaf_pas.ckk.models.item_line import Item_line
        from kaf_pas.ckk.models.item_line import Item_lineManager

        if not isinstance(parent, Item):
            raise Exception(f'item mut be Item instnce.')

        with connection.cursor() as cursor:
            cursor.execute(f'select count(*) from {mat_view_name} where parent_id=%s', [parent.lotsman_document.id])
            count, = cursor.fetchone()

        logger.debug(f'parent.lotsman_document: {parent.lotsman_document}')
        logger.debug(f'qty: {count}')

        with managed_progress(
                id=f'''lines_{parent.id}''',
                qty=count,
                user=user_id,
                message=f'''Создание строк детализации. ({count} шт.)''',
                title='Выполнено'
        ) as lines_progress:
            for lotsman_documents_hierarcy in Lotsman_documents_hierarcy_view.objects.raw(f'select * from {mat_view_name} where parent_id=%s order by level', [parent.lotsman_document.id]):
                item, _ = Lotsman_documents_hierarcyManager.get_item(
                    lotsman_documents_hierarcy=lotsman_documents_hierarcy,
                    items_pairs=items_pairs,
                    logger=logger
                )

                if lotsman_documents_hierarcy.attr_name != 'Материал':

                    if lotsman_documents_hierarcy.section == None:
                        if lotsman_documents_hierarcy.attr_name in ['Чертеж', 'Спецификация']:
                            lotsman_documents_hierarcy.section = 'Документация'
                        elif lotsman_documents_hierarcy.attr_name in ['Сборочная единица']:
                            lotsman_documents_hierarcy.section = 'Сборочные единицы'
                        elif lotsman_documents_hierarcy.attr_name in ['Деталь']:
                            lotsman_documents_hierarcy.section = 'Детали'

                    if lotsman_documents_hierarcy.section == None:
                        lotsman_documents_hierarcy.section = lotsman_documents_hierarcy.attr_name

                    Документ_на_материал = None
                    Наименование_материала = None
                    Документ_на_сортамент = None
                    Наименование_сортамента = None

                    for lotsman_documents_hierarcy_view in Lotsman_documents_hierarcy_view.objects.filter(parent_id=lotsman_documents_hierarcy.id):
                        if lotsman_documents_hierarcy_view.attr_name in ['Материал']:
                            Документ_на_материал = lotsman_documents_hierarcy_view.Документ_на_материал
                            Наименование_материала = lotsman_documents_hierarcy_view.Наименование_материала
                            Документ_на_сортамент = lotsman_documents_hierarcy_view.Документ_на_сортамент
                            Наименование_сортамента = lotsman_documents_hierarcy_view.Наименование_сортамента
                            break

                    item_line, created = Item_line.objects.update_or_create(
                        parent=parent,
                        child=item,
                        defaults=dict(
                            SPC_CLM_FORMAT=lotsman_documents_hierarcy.SPC_CLM_FORMAT,
                            SPC_CLM_ZONE=lotsman_documents_hierarcy.SPC_CLM_ZONE,
                            SPC_CLM_POS=lotsman_documents_hierarcy.SPC_CLM_POS,
                            SPC_CLM_MARK=lotsman_documents_hierarcy.SPC_CLM_MARK,
                            SPC_CLM_NAME=lotsman_documents_hierarcy.SPC_CLM_NAME,
                            SPC_CLM_COUNT=lotsman_documents_hierarcy.SPC_CLM_COUNT,
                            SPC_CLM_NOTE=lotsman_documents_hierarcy.SPC_CLM_NOTE,
                            SPC_CLM_MASSA=lotsman_documents_hierarcy.SPC_CLM_MASSA,
                            SPC_CLM_MATERIAL=lotsman_documents_hierarcy.SPC_CLM_MATERIAL if lotsman_documents_hierarcy.SPC_CLM_MATERIAL else Наименование_материала,
                            SPC_CLM_USER=lotsman_documents_hierarcy.SPC_CLM_USER,
                            SPC_CLM_KOD=lotsman_documents_hierarcy.SPC_CLM_KOD,
                            SPC_CLM_FACTORY=lotsman_documents_hierarcy.SPC_CLM_FACTORY,
                            Документ_на_материал=Документ_на_материал,
                            Наименование_материала=Наименование_материала,
                            Документ_на_сортамент=Документ_на_сортамент,
                            Наименование_сортамента=Наименование_сортамента,
                            section=lotsman_documents_hierarcy.section,
                            section_num=Item_lineManager.section_num(lotsman_documents_hierarcy.section),
                            subsection=lotsman_documents_hierarcy.subsection,
                        )
                    )

                if lines_progress:
                    lines_progress.step()

    @staticmethod
    def get_item(lotsman_documents_hierarcy, items_pairs, logger):
        from kaf_pas.ckk.models.item import Item
        from kaf_pas.kd.models.lotsman_documents_hierarcy_refs import Lotsman_documents_hierarcy_refs

        items = [item[1] for item in items_pairs.stack if item[0] == lotsman_documents_hierarcy.id]
        if len(items) == 0:
            STMP_1 = lotsman_documents_hierarcy.SPC_CLM_NAME
            STMP_2 = lotsman_documents_hierarcy.SPC_CLM_MARK

            item, created = Item.objects.get_or_create(
                lotsman_document_id=lotsman_documents_hierarcy.id,
                version=lotsman_documents_hierarcy._Version.value_int if lotsman_documents_hierarcy._Version else None,
                lotsman_type_id=lotsman_documents_hierarcy._Type.value_int if lotsman_documents_hierarcy._Type else None,
                defaults=dict(
                    STMP_1=STMP_1,
                    STMP_2=STMP_2,
                    props=Item.props.relevant | Item.props.from_lotsman,
                )
            )

            if lotsman_documents_hierarcy.attr_name in ['Деталь']:
                for lotsman_documents_hierarcy_chert in Lotsman_documents_hierarcy_refs.objects.filter(
                        parent_id=lotsman_documents_hierarcy.id,
                        child__attr_type__code='Чертеж'):
                    DocumentManager.link_image_to_lotsman_item(
                        lotsman_document=lotsman_documents_hierarcy_chert.child,
                        item=item,
                        logger=logger
                    )
            else:
                DocumentManager.link_image_to_lotsman_item(
                    lotsman_document=lotsman_documents_hierarcy,
                    item=item,
                    logger=logger
                )

            items_pairs.push((lotsman_documents_hierarcy.id, item))

            # if logger and created:
            #     logger.logging(f'\nAdded parent: {item}', 'debug')

            return item, created
        elif len(items) == 1:
            return items[0], False
        else:
            raise Exception(f'Неоднозначный выбор.')

    @staticmethod
    def make_mview():
        from kaf_pas.system.models.contants import Contants
        from django.db import connection

        index_sql = []
        fields_sql = []
        sql_array = []

        parent_system_const, _ = Contants.objects.update_or_create(
            code='lotsman_attibutes',
            defaults=dict(name='Атрибуты товарных позиций импортированных из Лоцмана')
        )

        attr_map = {
            'Зона': 'SPC_CLM_ZONE',
            'Код': 'SPC_CLM_KOD',
            'Масса': 'SPC_CLM_MASSA',
            'Материал': 'SPC_CLM_MATERIAL',
            'Наименование': 'SPC_CLM_NAME',
            'Обозначение': 'SPC_CLM_MARK',
            'Позиция': 'SPC_CLM_POS',
            'Пользовательская': 'SPC_CLM_USER',
            'Предприятие - изготовитель': 'SPC_CLM_FACTORY',
            'Примечание': 'SPC_CLM_NOTE',
            'Формат': 'SPC_CLM_FORMAT',
        }

        for name, code in attr_map.items():
            Contants.objects.update_or_create(
                code=code,
                defaults=dict(
                    name=name,
                    parent=parent_system_const
                )
            )

        m_view_name = 'kd_lotsman_documents_hierarcy_mview'
        m_view_recurs_name = 'kd_lotsman_documents_hierarcy_recurs_view'

        sql_array.append(f'DROP VIEW IF EXISTS {m_view_recurs_name} CASCADE')
        sql_array.append(f'DROP MATERIALIZED VIEW IF EXISTS {m_view_name} CASCADE')
        sql_array.append(f'''CREATE MATERIALIZED VIEW {m_view_name} AS SELECT lts.id,
                                                                                   lts.deleted_at,
                                                                                   lts.editing,
                                                                                   lts.deliting,
                                                                                   lts.lastmodified,                                                                                
                                                                                   ltsr.parent_id,
                                                                                   lts.props,
                                                                                   lts.attr_type_id,
                                                                                   lts.document_id,
                                                                                   CASE
                                                                                        WHEN (select count(1) as count
                                                                                              from kd_lotsman_documents_hierarcy_refs hr                                                            	
                                                                                              where hr.parent_id = lts.id) > 0 THEN true
                                                                                        ELSE false
                                                                                   END AS "isFolder",                                                                                 
                                                                                   ltsr.section, 
                                                                                   ltsr.subsection,
                                                                                   att.code attr_code,
                                                                                   att.name attr_name
                                                                                   $COMMA
                                                                                   $FIELDS     
                                                                            FROM kd_lotsman_documents_hierarcy lts
                                                                                    join kd_lotsman_documents_hierarcy_refs ltsr on ltsr.child_id = lts.id
                                                                                    join ckk_attr_type att on att.id = lts.attr_type_id WITH DATA;
                                                                                    --join ckk_attr_type att on att.id = lts.attr_type_id ;
                                                                            $INDEXES''')

        for field in ['id', 'deleted_at', 'editing', 'deliting', 'lastmodified', 'parent_id', 'props', 'attr_type_id', 'document_id', 'isFolder', 'section', 'subsection', 'attr_code', 'attr_name']:
            index_sql.append(f'''CREATE INDEX "ldh_attr_{field}_idx" ON {m_view_name} USING btree ("{field}")''')

        for field in Contants.objects.filter(parent__code='lotsman_attibutes'):
            fields_sql.append(f'''( SELECT kat.id
                                               FROM kd_document_attributes kat
                                                 JOIN kd_lotsman_document_attr_cross dc ON kat.id = dc.attribute_id
                                                 JOIN ckk_attr_type att ON att.id = kat.attr_type_id
                                              WHERE dc.document_id = ltsr.child_id and (dc.parent_document_id = ltsr.parent_id or ltsr.parent_id is null) AND att.code::text = '{field.code}'::text limit 1) AS "{field.code}_id"''')
            index_sql.append(f'''CREATE INDEX "ldh_attr_{field.code}_idx" ON {m_view_name} USING btree ("{field.code}_id")''')

        if len(fields_sql) > 0:
            sql_str = ';\n'.join(sql_array).replace('$FIELDS', ',\n'.join(fields_sql)).replace('$INDEXES', ';\n'.join(index_sql))
            sql_str = sql_str.replace('$COMMA', ',')
        else:
            sql_str = ';\n'.join(sql_array).replace('$FIELDS', '')
            sql_str = sql_str.replace('$COMMA', '')

        with connection.cursor() as cursor:
            logger.debug(f'\n{sql_str}')
            cursor.execute(sql_str)
            logger.debug(f'{m_view_name} recreated')

            sql_array = []
            sql_array.append(f'''CREATE VIEW {m_view_recurs_name} AS select * from (WITH RECURSIVE r AS (
                                    SELECT *, 1 AS level
                                    FROM {m_view_name}
                                    WHERE parent_id IS NULL
                                
                                    union all
                                
                                    SELECT {m_view_name}.*, r.level + 1 AS level
                                    FROM {m_view_name}
                                             JOIN r
                                                  ON {m_view_name}.parent_id = r.id)                                
                                select * from r order by level) as a''')
            sql_str = ';\n'.join(sql_array)
            logger.debug(f'\n{sql_str}')
            cursor.execute(sql_str)
            logger.debug(f'{m_view_recurs_name} recreated')

    @staticmethod
    def getRecord(record):
        res = {
            'id': record.id,
            'parent': record.parent.id if record.parent else None,
            'editing': record.editing,
            'deliting': record.deliting,
        }
        return res

    def makeItemFromRequest(self, request):
        request = DSRequest(request=request)
        data = request.get_data()

        Lotsman_documents_hierarcyManager.make_items(logger=logger, record=data)

        return data

    def get_queryset(self):
        return Lotsman_documents_hierarcyQuerySet(self.model, using=self._db)

    def deleteFromRequest(self, request, removed=None, ):
        request = DSRequest(request=request)
        res = 0
        tuple_ids = request.get_tuple_ids()
        with transaction.atomic():
            for id, mode in tuple_ids:
                if mode == 'hide':
                    super().filter(id=id).soft_delete()
                else:
                    qty, _ = super().filter(id=id).delete()
                res += qty
        return res


class Lotsman_documents_hierarcy(AuditModel):
    id = BigIntegerField(primary_key=True, verbose_name="Идентификатор")
    attr_type = ForeignKeyProtect(Attr_type, verbose_name='Тип документа')
    document = ForeignKeyProtect(Documents)

    props = Lotsman_documents_hierarcyManager.get_props()

    objects = Lotsman_documents_hierarcyManager()

    def __str__(self):
        return f'ID:{self.id}, attr_type: {self.attr_type}, document: {self.document}, props: {self.props}'

    def __repr__(self):
        return self.__str__()

    class Meta:
        verbose_name = 'Иерархия документа из Лоцмана'
