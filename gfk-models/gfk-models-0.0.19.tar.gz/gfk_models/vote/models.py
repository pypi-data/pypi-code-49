from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import models
from django.db.models import Avg, Sum
from django.utils.translation import ugettext_lazy as _
from django.core.validators import MaxLengthValidator
from gfk_models.gfk_base.models import GFKModel, GFKStats


class VoteStatsAbstract(GFKStats):
    # total sum for connected vote objects
    sum = models.IntegerField(default=0)
    # Model to count stats on
    model = None

    recount_attr_list = ['count', 'sum']

    class Meta:
        abstract = True

    def recount_sum(self):
        return self.get_recount_queryset().aggregate(Sum('rating'))['rating__sum']


class VoteAbstract(GFKModel):
    # vote_list = models.ForeignKey(MyVoteList)
    # * required
    # vote_list_attr_name = 'vote_list'

    ACCEPTED_VALUES = [-1, +1]

    # Vote author
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    author_anonym = models.CharField(max_length=30, default="Аноним", validators=[MaxLengthValidator(30)])

    # Current rating
    rating = models.IntegerField()

    last_update = models.DateField(auto_now=True, null=True)

    is_reviewd = models.BooleanField(default=False)

    def clean_rating(self):
        if self.rating not in self.ACCEPTED_VALUES:
            raise ValidationError(_('Rating field accept only this values: %s') % self.ACCEPTED_VALUES)

    class Meta:
        abstract = True

    def get_author_name(self):
        if self.author is not None:
            return str(self.author)
        else:
            return self.author_anonym
