from .models import Screenshot

from django.contrib.contenttypes.fields import GenericRelation
from gfk_models.gfk_base.mixins import GFKItemsManager, GFKBaseMixin
from django.core.exceptions import ObjectDoesNotExist


class ScreenshotManager(GFKItemsManager):
    item_model = Screenshot


class ScreenshotMixin(GFKBaseMixin):
    screenshots = GenericRelation(Screenshot,
                            related_query_name='target',
                            object_id_field='target_id',
                            content_type_field='target_content_type')

    def questions_manager(self):
        return ScreenshotManager(self)

    class Meta:
        abstract = True
