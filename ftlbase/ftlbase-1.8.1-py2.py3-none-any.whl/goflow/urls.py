from django.urls import path, include, re_path

from goflow.apptools.views import *
from goflow.workflow.views import process_dot, cron

urlpatterns = [
    # path('.*/logout/$', logout),
    # path('.*/accounts/login/$', login, {'template_name': 'goflow/login.html'}),
    path('apptools/', include('goflow.apptools.urls')),
    # path('graph/', include('goflow.graphics.urls')),
]

urlpatterns += [
    # path('$', index),
    re_path(r'^process/dot/(?P<id>.*)$', process_dot, name='process_dot'),
    path('cron/', cron, name='cron'),
]

urlpatterns += [
    re_path(r'^default_app/(?P<id>.*)/$', default_app, name='default_app'),
    #     path('start/(?P<app_label>.*)/(?P<model_name>.*)/$', start_application),
    #     path('start_proto/(?P<process_name>.*)/$', start_application,
    #         {'form_class': DefaultAppStartForm,
    #          'redirect': '../../',
    #          'template': 'goflow/start_proto.html'}),
]

# urlpatterns += [
#     path('otherswork/$', otherswork),
#     path('otherswork/instancehistory/$', instancehistory),
#     path('myrequests/$', myrequests),
#     path('myrequests/instancehistory/$', instancehistory),
#     path('mywork/$', mywork),
#     path('mywork/activate/(?P<id>.*)/$', activate),
#     path('mywork/complete/(?P<id>.*)/$', complete),
# ]
