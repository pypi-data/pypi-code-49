from django.urls import path

from kaf_pas.planing.views import operation_types

urlpatterns = [

    path('Operation_types/Fetch/', operation_types.Operation_types_Fetch),
    path('Operation_types/Add', operation_types.Operation_types_Add),
    path('Operation_types/Update', operation_types.Operation_types_Update),
    path('Operation_types/Remove', operation_types.Operation_types_Remove),
    path('Operation_types/Lookup/', operation_types.Operation_types_Lookup),
    path('Operation_types/Info/', operation_types.Operation_types_Info),
    path('Operation_types/Copy', operation_types.Operation_types_Copy),

]
