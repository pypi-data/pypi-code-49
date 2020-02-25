from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.db.models import Avg

from gfk_models.vote.models import VoteStatsAbstract, VoteAbstract


class ReviewStats(VoteStatsAbstract):
    # Average for connected vote objects
    avg = models.FloatField(default=0)

    recount_attr_list = ['count', 'sum', 'avg']

    def recount_avg(self):
        avg = self.get_recount_queryset().aggregate(Avg('rating'))['rating__avg']
        return round(avg, 1)


class Review(VoteAbstract):
    ACCEPTED_VALUES = [1, 2, 3, 4, 5]

    # target_content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    # target_id = models.PositiveIntegerField()
    # target = GenericForeignKey('target_content_type', 'target_id')

    # review_list = models.ForeignKey(ReviewList, blank=True, default=None, null=True)
    # vote_list_attr_name = 'review_list'

    pros = models.TextField(null=True, blank=True)
    cons = models.TextField(null=True, blank=True)
    summary = models.TextField()
    advise = models.BooleanField()

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
        unique_together = ['target_content_type', 'target_id', 'author']

# Register signals to recount
ReviewStats.setup_relation(Review)


# class Review(models.Model):
#     target_content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
#     target_id = models.PositiveIntegerField()
#     target = GenericForeignKey('target_content_type', 'target_id')
#
#     _id = models.CharField(max_length=24, unique=True, null=True, blank=True)
#
#     author = models.ForeignKey(User)
#
#     pros = models.TextField(null=True, blank=True)
#     cons = models.TextField(null=True, blank=True)
#     summary = models.TextField()
#
#     rating = models.IntegerField()
#     advise = models.BooleanField()
#
#     last_update = models.DateField(auto_now=True, null=True)
#
#     class Meta:
#         verbose_name = 'Отзыв'
#         verbose_name_plural = 'Отзывы'
#         unique_together = ('author', 'target_content_type', 'target_id')
#
#     @staticmethod
#     def filter_by_target(target):
#         return Review.objects.filter(target_id=target.id, target_content_type=ContentType.objects.get_for_model(target).id)
#
#     def save(self, *args, **kwargs):
#         super(Review, self).save(*args, **kwargs)
#
#         target = self.target_content_type.model_class().objects.get(id=self.target_id)
#
#         rating = Review.objects\
#                             .filter(target_content_type=self.target_content_type, target_id=self.target_id)\
#                             .aggregate(Avg('rating'))
#         # print(rating)
#         target.rating = round(rating['rating__avg'], 1)
#         target.save()
#
#     def __str__(self):
#         return "%s - %s" % (self.author, str(self.rating))

