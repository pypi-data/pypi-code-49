import logging

from django.core.management import BaseCommand
from django.db import transaction, connection

from kaf_pas.ckk.models.item import Item
from kaf_pas.ckk.models.item_refs import Item_refs
from tqdm import tqdm

from kaf_pas.ckk.models.item_refs_hierarcy import Item_refs_hierarcy

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = "Заполнение поля section_num"

    def dublicate_childs(self, parent_id, syntetic_parent_id):
        for item_refs in Item_refs.objects.filter(parent_id=parent_id):
            res = Item_refs_hierarcy.objects.create(
                id=item_refs.child.id,
                parent_id=syntetic_parent_id,
                item_refs=item_refs
            )
            logger.debug(res)

            # if Item_refs.objects.filter(parent=item_refs.child).count() > 0:
            #     raise Exception(f'item_refs.child have parents')

    def handle(self, *args, **options):
        logger.info(self.help)
        with transaction.atomic():
            with connection.cursor() as cursor:
                Item_refs_hierarcy.objects.all().delete()
                cursor.execute('''select child_id,
                                         count(*)
                                   from ckk_item_refs 
                                    group by child_id
                                    having count(*) > 1''')
                rows_dbls = cursor.fetchall()

                cursor.execute('''select child_id,
                                           count(*)
                                   from ckk_item_refs 
                                    group by child_id
                                    having count(*) = 1''')
                rows_ones = cursor.fetchall()

                self.pbar = tqdm(total=len(rows_dbls) + len(rows_ones))

                print('row_dbls')

                for row_dbls in rows_dbls:
                    child_id, _ = row_dbls

                    cursor.execute('''select id, parent_id
                                       from ckk_item_refs 
                                        where child_id = %s''', [child_id])

                    child_rows = cursor.fetchall()
                    step = 1
                    for child_row in child_rows:
                        item_refs_id, parent_id = child_row

                        if step == 1:
                            res = Item_refs_hierarcy.objects.create(
                                id=child_id,
                                parent_id=parent_id,
                                item_refs_id=item_refs_id
                            )
                            logger.debug(res)
                            step += 1
                        else:
                            cursor.execute(f"select nextval('ckk_item_id_seq')")
                            syntetic_child_id, = cursor.fetchone()

                            res = Item_refs_hierarcy.objects.create(
                                id=syntetic_child_id,
                                parent_id=parent_id,
                                item_refs_id=item_refs_id
                            )
                            logger.debug(res)

                            # self.dublicate_childs(parent_id=child_id, syntetic_parent_id=syntetic_child_id)

                    if self.pbar:
                        self.pbar.update(1)

                print('rows_ones')
                for row_ones in rows_ones:
                    child_id, _ = row_ones

                    item_refs = Item_refs.objects.get(child_id=child_id)
                    res = Item_refs_hierarcy.objects.create(
                        id=child_id,
                        parent_id=item_refs.parent.id if item_refs.parent else None,
                        item_refs=item_refs
                    )
                    logger.debug(res)

                    if self.pbar:
                        self.pbar.update(1)


                if self.pbar:
                    self.pbar.close()



