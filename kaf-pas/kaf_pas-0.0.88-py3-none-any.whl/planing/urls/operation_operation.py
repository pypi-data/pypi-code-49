from django.urls import path

from kaf_pas.planing.views import operation_operation

urlpatterns = [

    path('Operation_operation/Fetch/', operation_operation.Operation_operation_Fetch),
    path('Operation_operation/Add', operation_operation.Operation_operation_Add),
    path('Operation_operation/Update', operation_operation.Operation_operation_Update),
    path('Operation_operation/Remove', operation_operation.Operation_operation_Remove),
    path('Operation_operation/Lookup/', operation_operation.Operation_operation_Lookup),
    path('Operation_operation/Info/', operation_operation.Operation_operation_Info),
    path('Operation_operation/Copy', operation_operation.Operation_operation_Copy),

]
