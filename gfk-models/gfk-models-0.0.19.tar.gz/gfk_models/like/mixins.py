from .models import LikeStats, Like
from gfk_models.gfk_base.mixins import GFKItemsStatsManager, GFKBaseMixin
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.contenttypes.fields import GenericRelation


class LikeStatsManager(GFKItemsStatsManager):
    stats_model = LikeStats
    item_model = Like


class LikesMixin(GFKBaseMixin):
    likes = GenericRelation(Like,
                            # related_query_name='target',
                            object_id_field='target_id',
                            content_type_field='target_content_type')

    likes_stats = GenericRelation(LikeStats,
                            # related_query_name='target',
                            object_id_field='target_id',
                            content_type_field='target_content_type')

    def likes_manager(self):
        return LikeStatsManager(self)

    def __add_rating(self, user, value):
        # print('__add_rating', self, user, value)
        try:
            likes = self.likes_manager().stats()
            like = Like.objects.get(_target=self, author=user)
            likes.sum += -like.rating + value
            like.rating = value

        except ObjectDoesNotExist:
            like = Like(target=self, rating=value, author=user)
            likes.sum += value
            likes.count += 1

        like.save()
        # If there is no Exceptions then it's ok
        return likes

    def like(self, user):
        return self.__add_rating(user, +1)

    def dislike(self, user):
        return self.__add_rating(user, -1)

    class Meta:
        abstract = True