from django.urls import path

from kaf_pas.planing.views import operation_refs

urlpatterns = [

    path('Operation_refs/Fetch/', operation_refs.Operation_refs_Fetch),
    path('Operation_refs/Add', operation_refs.Operation_refs_Add),
    path('Operation_refs/Update', operation_refs.Operation_refs_Update),
    path('Operation_refs/Remove', operation_refs.Operation_refs_Remove),
    path('Operation_refs/Lookup/', operation_refs.Operation_refs_Lookup),
    path('Operation_refs/Info/', operation_refs.Operation_refs_Info),
    path('Operation_refs/Copy', operation_refs.Operation_refs_Copy),

]
