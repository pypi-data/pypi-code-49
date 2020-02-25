from django.conf.urls import url, include
from . import views, models


urlpatterns = [
    # url(r'^list', views.list, name='list'),
    url(r'^questions', views.QuestionListView.as_view(), name='list'),

    url(r'^qna/(?P<q_id>[\d]+)-(?P<q_slug>[\w\-]+)$',
        views.QuestionDetailView.as_view(), name='single'),
    #
    # url(r'^qna/(?P<q_id>[\d]+)-(?P<q_slug>[\w\-]+)/(?P<answer_id>[\d]+)$',
    #     views.QuestionAcceptAnswerView.as_view(), name='accept_answer'),
    # like dislike urls for question
    # url(r'^qna/(?P<q_id>[\d]+)-(?P<q_slug>[\w\-]+)/',
    #     include('gfk.like.urls'),
    #     {
    #         'target_model': models.Question,
    #         'target_request_attr': 'q_id',
    #         'target_retrieve_attr': 'id'
    #     }),
    url(r'^qna/add', views.QuestionCreateView.as_view(), name='add'),
]