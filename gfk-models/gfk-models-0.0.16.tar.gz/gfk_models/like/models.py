from django.db import models
from gfk_models.vote.models import VoteAbstract, VoteStatsAbstract


class Like(VoteAbstract):
    class Meta:
        unique_together = ['target_content_type', 'target_id', 'author']


class LikeStats(VoteStatsAbstract):
    model = Like
    positive = models.IntegerField(default=0)
    negative = models.IntegerField(default=0)

    recount_attr_list = ['count', 'sum', 'positive', 'negative']

    def recount_positive(self):
        return self.get_recount_queryset().filter(rating=+1).count()

    def recount_negative(self):
        return self.get_recount_queryset().filter(rating=-1).count()


LikeStats.setup_relation(Like)
