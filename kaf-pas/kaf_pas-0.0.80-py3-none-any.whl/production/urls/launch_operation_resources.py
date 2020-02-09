from django.urls import path

from kaf_pas.production.views import launch_operation_resources

urlpatterns = [

    path('Launch_operation_resources/Fetch/', launch_operation_resources.Launch_operation_resources_Fetch),
    path('Launch_operation_resources/Add', launch_operation_resources.Launch_operation_resources_Add),
    path('Launch_operation_resources/Update', launch_operation_resources.Launch_operation_resources_Update),
    path('Launch_operation_resources/Remove', launch_operation_resources.Launch_operation_resources_Remove),
    path('Launch_operation_resources/Lookup/', launch_operation_resources.Launch_operation_resources_Lookup),
    path('Launch_operation_resources/Info/', launch_operation_resources.Launch_operation_resources_Info),
    path('Launch_operation_resources/Copy', launch_operation_resources.Launch_operation_resources_Copy),

]
