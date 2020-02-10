from django.urls import path

from kaf_pas.planing.views import operation_executor

urlpatterns = [

    path('Operation_executor/Fetch/', operation_executor.Operation_executor_Fetch),
    path('Operation_executor/Add', operation_executor.Operation_executor_Add),
    path('Operation_executor/Update', operation_executor.Operation_executor_Update),
    path('Operation_executor/Remove', operation_executor.Operation_executor_Remove),
    path('Operation_executor/Lookup/', operation_executor.Operation_executor_Lookup),
    path('Operation_executor/Info/', operation_executor.Operation_executor_Info),
    path('Operation_executor/Copy', operation_executor.Operation_executor_Copy),

]
