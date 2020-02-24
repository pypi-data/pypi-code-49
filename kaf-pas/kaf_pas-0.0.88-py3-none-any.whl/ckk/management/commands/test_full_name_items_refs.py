import logging

from django.core.management import BaseCommand

from kaf_pas.ckk.models.item_operations_view import Item_operations_view, Item_operations_viewManager

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = "Тестирование"

    def handle(self, *args, **options):
        logger.info(self.help)

        # item_ref = Item_refs.objects.get(child_id=3369823, parent_id=3316573)
        # print(item_ref.child.item_name)
        #
        # print(item_ref.full_name)
        # launch_detail = Ready_2_launch_detail.objects.get(id=91938)
        # obj = launch_detail.item_full_name_obj
        # create_tmp_mat_view(sql_str='select * from ckk_item_view', mat_view_name='ckk_item_mview')

        for item in Item_operations_view.objects.raw(
                raw_query=f'select * from tmp_7db03452_23e3_44a5_8132_cff15f555b4b',
                function=Item_operations_viewManager.getRecord):
            print(item)
