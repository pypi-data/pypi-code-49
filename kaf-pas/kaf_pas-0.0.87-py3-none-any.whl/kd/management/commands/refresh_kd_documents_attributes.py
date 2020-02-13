import logging

from django.core.management import BaseCommand
from django.db import transaction, connection

from isc_common.logger.Logger import Logger

logger = logging.getLogger(__name__)
logger.__class__ = Logger


class Command(BaseCommand):
    help = 'Создание товаоных позиций после импорта из Лоцмана'

    def handle(self, *args, **options):
        try:
            from kaf_pas.kd.models.documents_thumb import Documents_thumbManager
            with transaction.atomic():
                with connection.cursor() as cursor:
                    cursor.execute(f'''SELECT count(*),
                                           attr_type_id,
                                           value_str
                                    FROM kd_document_attributes
                                    where value_str is not null
                                    group by attr_type_id,
                                             value_str
                                    having count(*) > 1''')
                    rows = cursor.fetchall()
                    no = 1
                    for row in rows:
                        count, attr_type_id, value_str = row
                        cursor.execute(f'''select
                                                id
                                            from
                                                kd_document_attributes
                                            where
                                                attr_type_id = %s
                                                and value_str = %s''', [attr_type_id, value_str])
                        rows1 = cursor.fetchall()
                        first_step = True
                        id1 = None
                        id2 = None
                        for row1 in rows1:
                            if not first_step:
                                id2, = row1
                                cursor.execute(f'''update kd_document_attr_cross set attribute_id=%s where attribute_id=%s''', [id1, id2])
                                cursor.execute(f'''update ckk_item set "STMP_1_id"=%s where "STMP_1_id"=%s''', [id1, id2])
                                cursor.execute(f'''update ckk_item set "STMP_2_id"=%s where "STMP_2_id"=%s''', [id1, id2])
                                cursor.execute(f'''update ckk_item_line set "SPC_CLM_COUNT_id"=%s where "SPC_CLM_COUNT_id"=%s''', [id1, id2])
                                cursor.execute(f'''update ckk_item_line set "SPC_CLM_FACTORY_id"=%s where "SPC_CLM_FACTORY_id"=%s''', [id1, id2])
                                cursor.execute(f'''update ckk_item_line set "SPC_CLM_FORMAT_id"=%s where "SPC_CLM_FORMAT_id"=%s''', [id1, id2])
                                cursor.execute(f'''update ckk_item_line set "SPC_CLM_KOD_id"=%s where "SPC_CLM_KOD_id"=%s''', [id1, id2])
                                cursor.execute(f'''update ckk_item_line set "SPC_CLM_MASSA_id"=%s where "SPC_CLM_MASSA_id"=%s''', [id1, id2])
                                cursor.execute(f'''update ckk_item_line set "SPC_CLM_MATERIAL_id"=%s where "SPC_CLM_MATERIAL_id"=%s''', [id1, id2])
                                cursor.execute(f'''update ckk_item_line set "SPC_CLM_NOTE_id"=%s where "SPC_CLM_NOTE_id"=%s''', [id1, id2])
                                cursor.execute(f'''update ckk_item_line set "SPC_CLM_POS_id"=%s where "SPC_CLM_POS_id"=%s''', [id1, id2])
                                cursor.execute(f'''update ckk_item_line set "SPC_CLM_USER_id"=%s where "SPC_CLM_USER_id"=%s''', [id1, id2])
                                cursor.execute(f'''update ckk_item_line set "SPC_CLM_ZONE_id"=%s where "SPC_CLM_ZONE_id"=%s''', [id1, id2])
                                cursor.execute(f'''update ckk_item_line set "SPC_CLM_NAME_id"=%s where "SPC_CLM_NAME_id"=%s''', [id1, id2])
                                cursor.execute(f'''update ckk_item_line set "SPC_CLM_MARK_id"=%s where "SPC_CLM_MARK_id"=%s''', [id1, id2])
                                cursor.execute(f'''update ckk_item_line set "Документ_на_материал_id"=%s where "Документ_на_материал_id"=%s''', [id1, id2])
                                cursor.execute(f'''update kd_lotsman_document_attr_cross set attribute_id=%s where attribute_id=%s''', [id1, id2])
                                cursor.execute(f'''delete from kd_document_attributes where id =%s''', [id2])
                                print(f'Deleted: #{no} {id2}')
                                no += 1
                            else:
                                id1, = row1
                                first_step = False
        except Exception as ex:
            raise ex
