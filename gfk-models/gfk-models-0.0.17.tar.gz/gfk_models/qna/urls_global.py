from django.conf.urls import url, include
from . import views, models

urlpatterns = [
    url(r'^questions$', views.QuestionListView.as_view(), name='list'),

    url(r'^question/(?P<q_id>[\d]+)/edit$',
        views.QuestionUpdateView.as_view(), name='question_edit'),

    url(r'^question/(?P<q_id>[\d]+)/answer/add$',
        views.AnswerCreateView.as_view(), name='answer_add'),

    url(r'^answer/(?P<a_id>[\d]+)/edit$',
        views.AnswerUpdateView.as_view(), name='answer_edit'),

    url(r'^question/(?P<q_id>[\d]+)/answer/(?P<a_id>[\d]+)/accept$',
        views.QuestionAcceptAnswerView.as_view(), name='answer_accept'),


    # Последние чтобы слаг не перебивал случайно
    url(r'^question/(?P<q_id>[\d]+)/(?P<q_slug>[\w\-]+)',
        views.QuestionDetailView.as_view(), name='question_single'),

    url(r'^qna/add', views.QuestionCreateView.as_view(), name='add'),
]

