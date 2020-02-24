from django.urls import path

from kaf_pas.production.views import launch_operations_item, operations_item

urlpatterns = [

    path('Launch_operations_item/Fetch/', launch_operations_item.Launch_operations_item_Fetch),
    path('Launch_operations_item/Add', launch_operations_item.Launch_operations_item_Add),
    path('Launch_operations_item/Update', launch_operations_item.Launch_operations_item_Update),
    path('Launch_operations_item/Remove', launch_operations_item.Launch_operations_item_Remove),
    path('Launch_operations_item/Lookup/', launch_operations_item.Launch_operations_item_Lookup),
    path('Launch_operations_item/Info/', launch_operations_item.Launch_operations_item_Info),
    path('Launch_operations_item/Copy', launch_operations_item.Launch_operations_item_Copy),
    path('Launch_operations_item/CopyOpers', launch_operations_item.Launch_operations_item_CopyOpers),

]
