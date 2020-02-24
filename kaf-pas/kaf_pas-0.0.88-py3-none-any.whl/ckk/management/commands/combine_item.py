import logging

from django.core.management import BaseCommand
from django.db import connection, transaction
from tqdm import tqdm

from kaf_pas.ckk.models.combineItems import CombineItems
from kaf_pas.ckk.models.item import Item

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = "Удаление дубликатов товарных позиций"

    def handle(self, *args, **options):
        with transaction.atomic():
            with connection.cursor() as cursor:
                cursor.execute(f'''select count(*), "STMP_1_id", "STMP_2_id", version, props, lotsman_document_id
                                    from ckk_item
                                    group by "STMP_1_id", "STMP_2_id", version, props, lotsman_document_id
                                    having count(*) > 1
                                        ''')
                rows = cursor.fetchall()
                pbar = tqdm(total=len(rows))
                for row in rows:
                    count, STMP_1_id, STMP_2_id, version, props, lotsman_document_id = row

                    first_step = True
                    recordTarget = dict()
                    recordsSource = []

                    for item in Item.objects.filter(STMP_1_id=STMP_1_id, STMP_2_id=STMP_2_id, version=version, props=props, lotsman_document_id=lotsman_document_id):
                        if not first_step:
                            recordsSource.append(dict(id=item.id))
                        else:
                            recordTarget.setdefault('id', item.id)
                            first_step = False

                    if len(recordsSource) > 0 and len(recordTarget) > 0:
                        CombineItems.combine(recordsSource=recordsSource, recordTarget=recordTarget)
                    pbar.update()
                pbar.close()
