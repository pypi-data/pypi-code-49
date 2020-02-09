import logging
from typing import List, Tuple

from django.core.management import BaseCommand
from django.db import transaction

from kaf_pas.ckk.models.item import Item
from kaf_pas.ckk.models.item_refs import Item_refs
from kaf_pas.kd.models.lotsman_documents_hierarcy import Lotsman_documents_hierarcy
from kaf_pas.kd.models.lotsman_documents_hierarcy_refs import Lotsman_documents_hierarcy_refs

logger = logging.getLogger(__name__)


def check_level(parent_array: List[Tuple[int, int]], item: Item or Lotsman_documents_hierarcy_refs, level: int, table: str) -> None:
    if level > 25:
        raise Exception(f'Too big level {level}')

    logger.debug(f'in to level: {level}\n')
    logger.debug(f'{item.id}\n')

    if table == 'Item_refs':
        query = Item_refs.objects.filter(parent_id=item.id)

    elif table == 'Lotsman_documents_hierarcy_refs':
        query = Lotsman_documents_hierarcy_refs.objects.filter(parent_id=item.id)

    for item_refs in query:
        if (item_refs.child.id, item_refs.parent.id) in parent_array:
            logger.debug(f'Item: {item_refs} have a cicular reference will deleted.')
            # item_refs.delete()
        else:
            parent_array.append((item_refs.parent.id, item_refs.child.id))
            check_level(parent_array=parent_array, item=item_refs.child, level=level + 1, table=table)
        logger.debug(f'out to level: {level}\n')


class Command(BaseCommand):
    help = "Нахождение циклических ссылок"

    def add_arguments(self, parser):
        parser.add_argument('--table', type=str)
        parser.add_argument('--item_id', type=int)

    def handle(self, *args, **options):
        table = options.get('table')
        item_id = options.get('item_id')

        print(f'table: {table}')
        print(f'item_id: {item_id}')

        parent_array = list()
        with transaction.atomic():
            if table == 'Item_refs':
                check_level(parent_array=parent_array, item=Item.objects.get(id=item_id), level=1, table=table)
            elif table == 'Lotsman_documents_hierarcy_refs':
                check_level(parent_array=parent_array, item=Lotsman_documents_hierarcy.objects.get(id=item_id), level=1, table=table)
