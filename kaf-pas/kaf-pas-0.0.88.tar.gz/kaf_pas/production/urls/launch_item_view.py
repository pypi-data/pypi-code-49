from django.urls import path

from kaf_pas.production.views import launch_item_view

urlpatterns = [

    path('Launch_item_view/Fetch/', launch_item_view.Launch_item_view_Fetch),
    path('Launch_item_view/Add', launch_item_view.Launch_item_view_Add),
    path('Launch_item_view/Update', launch_item_view.Launch_item_view_Update),
    path('Launch_item_view/Remove', launch_item_view.Launch_item_view_Remove),
    path('Launch_item_view/Lookup/', launch_item_view.Launch_item_view_Lookup),
    path('Launch_item_view/Info/', launch_item_view.Launch_item_view_Info),
    path('Launch_item_view/Copy', launch_item_view.Launch_item_view_Copy),

]
