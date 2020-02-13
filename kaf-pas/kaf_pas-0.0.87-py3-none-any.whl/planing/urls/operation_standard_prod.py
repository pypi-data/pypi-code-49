from django.urls import path

from kaf_pas.planing.views import operation_standard_prod

urlpatterns = [

    path('Operation_standard_prod/Fetch/', operation_standard_prod.Operation_standard_prod_Fetch),
    path('Operation_standard_prod/Add', operation_standard_prod.Operation_standard_prod_Add),
    path('Operation_standard_prod/Update', operation_standard_prod.Operation_standard_prod_Update),
    path('Operation_standard_prod/Remove', operation_standard_prod.Operation_standard_prod_Remove),
    path('Operation_standard_prod/Lookup/', operation_standard_prod.Operation_standard_prod_Lookup),
    path('Operation_standard_prod/Info/', operation_standard_prod.Operation_standard_prod_Info),
    path('Operation_standard_prod/Copy', operation_standard_prod.Operation_standard_prod_Copy),

]
