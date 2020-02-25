from django import forms
from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericForeignKey
from django.utils.translation import ugettext as _

from .models import Question, Answer
from gfk_models.gfk_helpers.functions.text_processors import TextProcessors


class QuestionForm(forms.ModelForm):
    text_allowed_tags = ['img', 'div', 'p', 'h2', 'h3', 'h4']
    text_allowed_attrs = ['alt', 'rel', 'href']

    class Meta:
        model = Question
        fields = ['title', 'text', 'target_content_type', 'target_id', 'author']

    def clean_text(self):
        text = self.cleaned_data['text']
        text = TextProcessors.text_sanitize(text)
        text = TextProcessors.text_linkify(text)
        return text

    def clean(self):
        clean = super(QuestionForm, self).clean()
        # print('clean', clean)
        return clean

    def is_valid(self):
        is_valid = super(QuestionForm, self).is_valid()
        # print('is_valid', is_valid)
        return is_valid

    def save(self, commit=True):
        return super(QuestionForm, self).save(commit)


class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['text', 'author', 'question']

    def clean_text(self):
        text = self.cleaned_data['text']
        text = TextProcessors.text_sanitize(text)
        text = TextProcessors.text_linkify(text)
        return text