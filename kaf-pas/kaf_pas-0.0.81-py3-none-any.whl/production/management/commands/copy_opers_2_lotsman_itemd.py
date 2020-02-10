import logging

from django.core.management import BaseCommand
from django.db import transaction
from tqdm import tqdm

from kaf_pas.ckk.models.item import Item
from kaf_pas.production.models.operations_item import Operations_item

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = "Тестирование"

    # def add_arguments(self, parser):
    #     parser.add_argument('--demand_id', type=int)
    #     parser.add_argument('--user_id', type=int)

    def handle(self, *args, **options):
        # demand_id = options.get('demand_id')
        # user_id = options.get('user_id')

        no = 0
        with transaction.atomic():
            total = Operations_item.objects.exclude(item__props=Item.props.from_lotsman).count()
            pbar = tqdm(total=total)
            for operations_item in [item for item in Operations_item.objects.exclude(item__props=Item.props.from_lotsman)]:
                if operations_item.item.STMP_1 == None:
                    query = Item.objects.filter(STMP_2__value_str=operations_item.item.STMP_2.value_str, props=Item.props.from_lotsman)
                elif operations_item.item.STMP_2 == None:
                    query = Item.objects.filter(STMP_1__value_str=operations_item.item.STMP_1.value_str, props=Item.props.from_lotsman)
                elif operations_item.item.STMP_1 != None and operations_item.item.STMP_2 != None:
                    query = Item.objects.filter(STMP_1__value_str=operations_item.item.STMP_1.value_str, STMP_2__value_str=operations_item.item.STMP_2.value_str, props=Item.props.from_lotsman)

                for item_lotsman in query:
                    # lotsman_operations_item, created = Operations_item.objects.get_or_create(
                    #     item=item_lotsman,
                    #     operation=operations_item.operation,
                    #     defaults=dict(
                    #         ed_izm=operations_item.ed_izm,
                    #         qty=operations_item.qty,
                    #         num=operations_item.num,
                    #         description=operations_item.description,
                    #     ))
                    #
                    # if created:
                    #     for operation_resources in Operation_resources.objects.filter(operationitem=operations_item):
                    #         Operation_resources.objects.get_or_create(
                    #             operationitem=lotsman_operations_item,
                    #             resource=operation_resources.resource,
                    #             location=operation_resources.location
                    #         )
                    #
                    #     for operation_material in Operation_material.objects.filter(operationitem=operations_item):
                    #         Operation_material.objects.get_or_create(
                    #             operationitem=lotsman_operations_item,
                    #             material=operation_material.material,
                    #             material_askon=operation_material.material_askon,
                    #             ed_izm=operation_material.ed_izm,
                    #             qty=operation_material.qty,
                    #         )
                    no += 1
                pbar.update()
            pbar.close()
        percents = round(no * 100 / total, 2)
        print(f'{no} - {percents}% Done.')
