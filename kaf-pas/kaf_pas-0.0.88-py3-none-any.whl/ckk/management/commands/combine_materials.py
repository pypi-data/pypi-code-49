import logging

from django.core.management import BaseCommand
from django.db import connection, transaction
from tqdm import tqdm

from kaf_pas.ckk.models.combineItems import CombineItems
from kaf_pas.ckk.models.item import Item
from kaf_pas.ckk.models.materials import Materials

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = "Удаление дубликатов товарных позиций"

    def handle(self, *args, **options):
        with transaction.atomic():
            with connection.cursor() as cursor:
                cursor.execute(f'''select count(*), gost,location_id, materials_type_id, nomenklatura_model_id
                                    from ckk_materials
                                    group by gost,location_id, materials_type_id, nomenklatura_model_id
                                    having count(*) > 1
                                           ''')
                rows = cursor.fetchall()
                pbar = tqdm(total=len(rows))
                for row in rows:
                    count, gost,location_id, materials_type_id, nomenklatura_model_id = row

                    first_step = True
                    _material = None

                    for material in Materials.objects.filter(location_id=location_id, gost=gost, materials_type_id= materials_type_id, nomenklatura_model_id= nomenklatura_model_id):
                        if not first_step:
                            material.delete()
                        else:
                            _material = material
                            first_step = False
                    pbar.update()
                pbar.close()
