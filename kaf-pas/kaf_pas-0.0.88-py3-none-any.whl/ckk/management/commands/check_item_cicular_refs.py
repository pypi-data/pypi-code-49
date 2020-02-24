import logging
from typing import List, Tuple

from django.core.management import BaseCommand
from django.db import transaction

from isc_common.progress import ProgressDroped
from kaf_pas.ckk.models.item import Item
from kaf_pas.ckk.models.item_refs import Item_refs
from kaf_pas.kd.models.lotsman_documents_hierarcy import Lotsman_documents_hierarcy
from kaf_pas.kd.models.lotsman_documents_hierarcy_refs import Lotsman_documents_hierarcy_refs
from kaf_pas.production.models import progress_deleted

logger = logging.getLogger(__name__)


def check_level(
        parent_array: List[Tuple[int, int, str]] = list(),
        item: Item or Lotsman_documents_hierarcy_refs = None,
        level: int = 0,
        table: str = '',
        cycle_ref: List = [],
        full_path: str = '',
        progress=None) -> List:
    res = 0

    if level > 50:
        raise Exception(f'Too big level {level}')

    # progress.setContentsLabel(f'in to level: {level}\n{item.id}\n')
    logger.debug(f'in to level: {level}\n{item.id}\n')

    if table == 'Item_refs':
        query = Item_refs.objects.filter(parent_id=item.id)

    elif table == 'Lotsman_documents_hierarcy_refs':
        query = Lotsman_documents_hierarcy_refs.objects.filter(parent_id=item.id)

    full_path = f'{full_path} / {item.item_name.rstrip()}'

    for item_refs in query:
        cycled = [item for item in parent_array if item[0] == item_refs.child.id and item[1] == item_refs.parent.id]

        if len(cycled) > 0:
            s = f'''<pre>\nlevel:{level}\nID PARENT: {item_refs.parent.id if item_refs.parent else 'None'} ({item_refs.parent.item_name})\nID CHILD: {item_refs.child.id} ({item_refs.child.item_name})</pre>'''
            logger.debug(s)
            cycle_ref.append(s)
            s = f'''<pre>Full path Parent:  {cycled[0][2]}</pre>'''
            cycle_ref.append(s)
            s = f'''<pre>Full path Child: {full_path}</pre>'''
            cycle_ref.append(s)
            # item_refs.delete()
        else:
            parent_array.append((item_refs.parent.id, item_refs.child.id, full_path))
            check_level(
                parent_array=parent_array,
                item=item_refs.child,
                level=level + 1,
                table=table,
                cycle_ref=cycle_ref, progress=progress,
                full_path=full_path
            )
        if progress:
            res = progress.step()

        if res != 0:
            raise ProgressDroped(progress_deleted)
        logger.debug(f'out to level: {level}\n')
    return cycle_ref


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

        cycle_ref = []

        parent_array = list()
        with transaction.atomic():
            if table == 'Item_refs':
                cycle_ref = check_level(parent_array=parent_array, item=Item.objects.get(id=item_id), level=1, table=table)
            elif table == 'Lotsman_documents_hierarcy_refs':
                cycle_ref = check_level(parent_array=parent_array, item=Lotsman_documents_hierarcy.objects.get(id=item_id), level=1, table=table)

        for item in cycle_ref:
            print(item)
