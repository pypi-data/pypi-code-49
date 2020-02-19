# -*- coding: utf-8 -*-

from django.urls import path, include, re_path

from . import utils as common_utils, form as common_forms, views as common_views

# from . import form

urlpatterns = [
    # path('base_url.js$', common_views.base_url_js, name='common-base-url-js'),

    path('login/', common_views.loginX, name='loginX'),
    path('logout/', common_views.logoutX, name='logoutX'),

    # Version Compare
    path('version/compare/', common_views.versionViewCompare, name='version_compare'),
    path('version/compare/<int:pk>/', common_views.versionViewCompare, name='versionViewCompare'),

    # Workflow
    path('workflow/action/', common_views.common_workflow,
        {'goto': 'workflow_pending', 'dictionary': {'acao': common_utils.ACAO_WORKFLOW_TO_APPROVE, 'disableMe': True}},
        name="workflow_action_home"),
    path('workflow/action/<int:id>/', common_views.common_workflow,
        {'goto': 'workflow_pending', 'dictionary': {'acao': common_utils.ACAO_WORKFLOW_TO_APPROVE, 'disableMe': True}},
        name="workflow_action"),
    # path('workflow/ratify/<int:id>/', common_views.common_workflow,
    #     {'goto': 'workflow_pending',
    #      'dictionary': {'acao': common_forms.ACAO_WORKFLOW_RATIFY, 'disableMe': True}}, name="workflow_to_ratify"),
    path('workflow/workflow_execute/<int:id>/', common_views.common_workflow_execute,
        {'goto': 'workflow_pending', 'dictionary': {'disableMe': True}},
        name="workflow_execute_std"),

    path('workflow/flag/news/', common_views.common_workflow_flag_news, name='workflow_flag_news'),
    path('workflow/flag/myworks/', common_views.common_workflow_flag_myworks, name='workflow_flag_myworks'),

    path('workflow/news/', common_views.common_workflow_table_process, {'news': True, 'add': False},
        name='workflow_news'),
    path('workflow/myworks/', common_views.common_workflow_table_process, {'my_work': True, 'add': False},
        name='workflow_myworks'),
    path('workflow/pending/', common_views.common_workflow_table_process, {'pending': True, 'add': False},
        name='workflow_pending'),
    path('workflow/all/', common_views.common_workflow_table_process, {'add': False}, name='workflow_all'),

    path('workflow/graph/<int:pk>/', common_views.common_workflow_graph, name='workflow_graph'),
    re_path(r'^workflow/process_graph/(?P<title>.+)/$', common_views.common_process_graph, name='workflow_process_graph'),
    path('workflow/history/<int:pk>/', common_views.common_history_workitems_table,
        {'goto': 'workflow_pending', 'model': common_forms.ProcessWorkItemTable},
        name="workflow_history"),

    path('table/', include('table.urls')),
]

# if settings.DEBUG:
#     import debug_toolbar
#
#     urlpatterns = [
#                       path('__debug__/', include(debug_toolbar.urls)),
#                   ] + urlpatterns
