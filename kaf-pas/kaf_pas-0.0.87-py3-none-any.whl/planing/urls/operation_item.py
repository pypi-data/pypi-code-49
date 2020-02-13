from django.urls import path

from kaf_pas.planing.views import operation_item

urlpatterns = [

    path('Operation_item/Fetch/', operation_item.Operation_item_Fetch),
    path('Operation_item/Add', operation_item.Operation_item_Add),
    path('Operation_item/Update', operation_item.Operation_item_Update),
    path('Operation_item/Remove', operation_item.Operation_item_Remove),
    path('Operation_item/Lookup/', operation_item.Operation_item_Lookup),
    path('Operation_item/Info/', operation_item.Operation_item_Info),
    path('Operation_item/Copy', operation_item.Operation_item_Copy),

]
