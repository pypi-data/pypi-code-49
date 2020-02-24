from django.urls import path

from kaf_pas.production.views import operation_def_resources

urlpatterns = [

    path('Operation_def_resources/Fetch/', operation_def_resources.Operation_def_resources_Fetch),
    path('Operation_def_resources/Add', operation_def_resources.Operation_def_resources_Add),
    path('Operation_def_resources/Update', operation_def_resources.Operation_def_resources_Update),
    path('Operation_def_resources/AllUpdate', operation_def_resources.Operation_def_resources_AllUpdate),
    path('Operation_def_resources/Remove', operation_def_resources.Operation_def_resources_Remove),
    path('Operation_def_resources/Lookup/', operation_def_resources.Operation_def_resources_Lookup),
    path('Operation_def_resources/Info/', operation_def_resources.Operation_def_resources_Info),
    path('Operation_def_resources/Copy', operation_def_resources.Operation_def_resources_Copy),

]
