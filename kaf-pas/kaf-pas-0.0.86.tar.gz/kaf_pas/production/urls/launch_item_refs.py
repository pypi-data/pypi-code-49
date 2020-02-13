from django.urls import path

from kaf_pas.production.views import launch_item_refs

urlpatterns = [

    path('Launch_item_refs/Fetch/', launch_item_refs.Launch_item_refs_Fetch),
    path('Launch_item_refs/Add', launch_item_refs.Launch_item_refs_Add),
    path('Launch_item_refs/Update', launch_item_refs.Launch_item_refs_Update),
    path('Launch_item_refs/Remove', launch_item_refs.Launch_item_refs_Remove),
    path('Launch_item_refs/Lookup/', launch_item_refs.Launch_item_refs_Lookup),
    path('Launch_item_refs/Info/', launch_item_refs.Launch_item_refs_Info),
    path('Launch_item_refs/Copy', launch_item_refs.Launch_item_refs_Copy),

]
