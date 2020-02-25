from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.shortcuts import redirect
from django.http.response import JsonResponse
from django.forms import ValidationError
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic

from gfk_models.gfk_base.views import GFKListView, GFKDetailView, GFKCreateView, GFKUpdateView
from gfk_models.gfk_helpers.functions.common import CommonHelpers
from .forms import QuestionForm, AnswerForm
from .models import Question, Answer
from hitcount.views import HitCountDetailView


class QuestionCreateView(LoginRequiredMixin, GFKCreateView):
    model = Question
    form_class = QuestionForm
    template_name = "qna/add.html"

    def __init__(self, *args, **kwargs):
        # self.login_url = reverse('auth:sign_in')
        return super().__init__(*args, **kwargs)

    @method_decorator(login_required)
    def post(self, request, *args, **kwargs):

        post_dict = request.POST.copy()
        post_dict.update({'author': CommonHelpers.get_user__by_request(request).id})
        request.POST = post_dict

        return super(QuestionCreateView, self).post(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['submit_button_text'] = "Задать вопрос"
        return data


class QuestionUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Question
    form_class = QuestionForm
    pk_url_kwarg = 'q_id'

    def __init__(self, *args, **kwargs):
        # self.login_url = reverse('auth:sign_in')
        return super().__init__(*args, **kwargs)

    template_name = "qna/add.html"

    def dispatch(self, request, *args, **kwargs):

        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):

        post_dict = request.POST.copy()
        post_dict.update({'author': CommonHelpers.get_user__by_request(request).id})
        request.POST = post_dict

        return super(QuestionUpdateView, self).post(request, *args, **kwargs)

    def get_object(self, queryset=None):
        object = super().get_object(queryset)

        if object.author.id != self.request.user.id:
            raise ValidationError('Редактировать можно только свои вопросы и ответы.')

        return object

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['submit_button_text'] = "Сохранить вопрос"
        return data


class QuestionListView(GFKListView):
    model = Question
    paginate_by = 10
    paginate_orphans = 5

    template_name = "qna/list.html"

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['sidebar_popular'] = Question.get_popular_today()

        return data


class QuestionDetailView(HitCountDetailView, GFKDetailView):
    model = Question
    count_hit = True
    pk_url_kwarg = 'q_id'

    template_name = "qna/single.html"

    def get_target(self):
        return

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['target'] = data['object'].get_target()
        data['sidebar_popular'] = Question.get_popular_today()

        return data

    def get(self, request, *args, **kwargs):
        question = Question.objects.get(id=kwargs['q_id'])

        if question.get_slug() != kwargs['q_slug']:
            return redirect(question.get_absolute_url())
        else:
            return super().get(request, *args, **kwargs)


class QuestionAcceptAnswerView(LoginRequiredMixin, generic.DetailView):
    model = Question
    pk_url_kwarg = 'q_id'

    def __init__(self, *args, **kwargs):
        # self.login_url = reverse('auth:sign_in')
        return super().__init__(*args, **kwargs)

    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        question = Question.objects.get(id=kwargs['q_id'])
        result = question.toggle_accepted_answer(kwargs['a_id'], request.user)

        return JsonResponse({
            'checked': result
        })


class AnswerCreateView(LoginRequiredMixin, generic.CreateView):
    model = Answer
    form_class = AnswerForm

    template_name = "qna/answer_add.html"

    def __init__(self, *args, **kwargs):
        # self.login_url = reverse('auth:sign_in')
        return super().__init__(*args, **kwargs)

    def post(self, request, *args, **kwargs):
        post_dict = request.POST.copy()
        post_dict.update({'author': CommonHelpers.get_user__by_request(request).id})
        request.POST = post_dict

        return super().post(request, *args, **kwargs)


class AnswerUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Answer
    pk_url_kwarg = 'a_id'
    form_class = AnswerForm

    template_name = "qna/answer_add.html"

    def __init__(self, *args, **kwargs):
        # self.login_url = reverse('auth:sign_in')
        return super().__init__(*args, **kwargs)

    def post(self, request, *args, **kwargs):
        post_dict = request.POST.copy()
        post_dict.update({'author': CommonHelpers.get_user__by_request(request).id})
        request.POST = post_dict

        return super().post(request, *args, **kwargs)

    def get_object(self, queryset=None):
        object = super().get_object(queryset)

        if object.author.id != self.request.user.id:
            raise ValidationError('Редактировать можно только свои вопросы и ответы.')

        return object
