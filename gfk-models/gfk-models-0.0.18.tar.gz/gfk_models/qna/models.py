from django.contrib.auth.models import User
from django.urls import reverse
from django.db import models

from gfk_models.gfk_base.models import GFKModel
from gfk_models.gfk_base.models import ContentType
from gfk_models.like.mixins import LikesMixin
from gfk_models.gfk_helpers.functions.common import CommonHelpers
import datetime
from hitcount.models import HitCountMixin


class Question(LikesMixin, HitCountMixin, GFKModel):
    ITEMS_PER_PAGE = 30

    target_content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, null=True, blank=True)
    target_id = models.PositiveIntegerField(null=True, blank=True)

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, unique=True, null=True, blank=True)
    slug = models.CharField(max_length=200, unique=True, null=True, blank=True)
    text = models.TextField()

    has_answer = models.BooleanField(default=False)

    last_update = models.DateTimeField(auto_now=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'
        ordering = ['-created_at']

    def __str__(self):
        return self.title

    def get_slug(self):
        if self.slug is None or self.slug == '':
            self.slug = CommonHelpers.get_slug(self.title)
            self.save()

        return self.slug

    def get_absolute_url(self):
        url = reverse('qna:question_single', kwargs={
            'q_id': self.id,
            'q_slug': self.get_slug(),
        })
        return url

    def get_edit_url(self):
        return reverse('qna:question_edit', args=[self.id])

    def toggle_accepted_answer(self, answer_id, user):
        if user.id != self.author.id:
            return False

        # print(answer_id, user, self.author)

        try:
            answer = Answer.objects.get(question=self.id, id=answer_id)

            Answer.objects.filter(question=self.id).exclude(id=answer.id).update(accepted=False)

            answer.accepted = not answer.accepted
            answer.save()

            self.has_answer = answer.accepted
            self.save()

            return answer.accepted
        except Exception as ex:
            # print(ex)
            return False

    @classmethod
    def get_popular_today(cls):
        yesterday = datetime.date.today() - datetime.timedelta(days=1)
        objs = cls.objects.filter(created_at__gt=yesterday)\
                        .order_by('-likes_stats__sum')[:10]

        if not objs:
            objs = cls.objects.filter().order_by('-likes_stats__sum')[:10]

        return objs


class Answer(LikesMixin, models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    accepted = models.BooleanField(default=False)

    last_update = models.DateField(auto_now=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def get_absolute_url(self):
        url = self.question.get_absolute_url()
        return "%s#a%s" % (url, self.id)

    def get_edit_url(self):
        return reverse('qna:answer_edit', kwargs={'a_id':self.id})

    class Meta:
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'
        unique_together = ('author', 'question')
        ordering = ['-accepted', '-last_update']

    def __str__(self):
        return "Ответ - %s" % str(self.author)

