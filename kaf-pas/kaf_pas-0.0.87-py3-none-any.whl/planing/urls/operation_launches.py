from django.urls import path

from kaf_pas.planing.views import operation_launches

urlpatterns = [

    path('Operation_launches/Fetch/', operation_launches.Operation_launches_Fetch),
    path('Operation_launches/Add', operation_launches.Operation_launches_Add),
    path('Operation_launches/Update', operation_launches.Operation_launches_Update),
    path('Operation_launches/ReCalcRoutes', operation_launches.Operation_launches_ReCalcRoutes),
    path('Operation_launches/CleanRoutes', operation_launches.Operation_launches_CleanRoutes),
    path('Operation_launches/Remove', operation_launches.Operation_launches_Remove),
    path('Operation_launches/Lookup/', operation_launches.Operation_launches_Lookup),
    path('Operation_launches/Info/', operation_launches.Operation_launches_Info),
    path('Operation_launches/Copy', operation_launches.Operation_launches_Copy),

]
