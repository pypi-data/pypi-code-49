from django.urls import path

from kaf_pas.planing.views import status_operation_types

urlpatterns = [

    path('Status_operation_types/Fetch/', status_operation_types.Status_operation_types_Fetch),
    path('Status_operation_types/Add', status_operation_types.Status_operation_types_Add),
    path('Status_operation_types/Update', status_operation_types.Status_operation_types_Update),
    path('Status_operation_types/Remove', status_operation_types.Status_operation_types_Remove),
    path('Status_operation_types/Lookup/', status_operation_types.Status_operation_types_Lookup),
    path('Status_operation_types/Info/', status_operation_types.Status_operation_types_Info),
    path('Status_operation_types/Copy', status_operation_types.Status_operation_types_Copy),

]
