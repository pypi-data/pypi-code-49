from django.urls import path

from kaf_pas.planing.views import operation_value

urlpatterns = [

    path('Operation_value/Fetch/', operation_value.Operation_value_Fetch),
    path('Operation_value/Add', operation_value.Operation_value_Add),
    path('Operation_value/Update', operation_value.Operation_value_Update),
    path('Operation_value/Remove', operation_value.Operation_value_Remove),
    path('Operation_value/Lookup/', operation_value.Operation_value_Lookup),
    path('Operation_value/Info/', operation_value.Operation_value_Info),
    path('Operation_value/Copy', operation_value.Operation_value_Copy),

]
