from django.urls import path

from kaf_pas.planing.views import operations

urlpatterns = [

    path('Operations_plan/Fetch/', operations.Operations_Fetch),
    path('Operations_plan/Add', operations.Operations_Add),
    path('Operations_plan/Update', operations.Operations_Update),
    path('Operations_plan/Remove', operations.Operations_Remove),
    path('Operations_plan/Lookup/', operations.Operations_Lookup),
    path('Operations_plan/Info/', operations.Operations_Info),
    path('Operations_plan/Copy', operations.Operations_Copy),

]
