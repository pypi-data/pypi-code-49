from django.urls import path

from kaf_pas.planing.views import operation_level

urlpatterns = [

    path('Operation_level/Fetch/', operation_level.Operation_level_Fetch),
    path('Operation_level/Add', operation_level.Operation_level_Add),
    path('Operation_level/Update', operation_level.Operation_level_Update),
    path('Operation_level/Remove', operation_level.Operation_level_Remove),
    path('Operation_level/Lookup/', operation_level.Operation_level_Lookup),
    path('Operation_level/Info/', operation_level.Operation_level_Info),
    path('Operation_level/Copy', operation_level.Operation_level_Copy),

]
