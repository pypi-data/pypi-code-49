from .models import ReviewStats, Review
from .forms import ReviewForm

from gfk_models.gfk_base.mixins import GFKItemsStatsManager, GFKBaseMixin
from django.contrib.contenttypes.fields import GenericRelation


class ReviewStatsManager(GFKItemsStatsManager):
    stats_model = ReviewStats

    item_model = Review
    item_form = ReviewForm

    create_or_update_fields = ['author']


class ReviewsMixin(GFKBaseMixin):
    reviews = GenericRelation(Review,
                              related_query_name='target',
                              object_id_field='target_id',
                              content_type_field='target_content_type')

    def reviews_manager(self):
        return ReviewStatsManager(self)

    class Meta:
        abstract = True