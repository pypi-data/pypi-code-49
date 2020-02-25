from .models import Question
from .forms import QuestionForm

from django.contrib.contenttypes.fields import GenericRelation
from gfk_models.gfk_base.mixins import GFKItemsManager, GFKBaseMixin
from django.core.exceptions import ObjectDoesNotExist


class QuestionItemsManager(GFKItemsManager):
    item_model = Question
    item_form = QuestionForm
    create_or_update_fields = ['author']


class QuestionsMixin(GFKBaseMixin):
    questions = GenericRelation(Question,
                            related_query_name='target',
                            object_id_field='target_id',
                            content_type_field='target_content_type')

    def questions_manager(self):
        return QuestionItemsManager(self)

    class Meta:
        abstract = True
