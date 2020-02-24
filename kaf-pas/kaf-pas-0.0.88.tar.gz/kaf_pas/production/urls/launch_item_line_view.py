from django.urls import path

from kaf_pas.production.views import launch_item_line_view

urlpatterns = [

    path('Launch_item_line_view/Fetch/', launch_item_line_view.Launch_item_line_view_Fetch),
    path('Launch_item_line_view/Add', launch_item_line_view.Launch_item_line_view_Add),
    path('Launch_item_line_view/Update', launch_item_line_view.Launch_item_line_view_Update),
    path('Launch_item_line_view/Remove', launch_item_line_view.Launch_item_line_view_Remove),
    path('Launch_item_line_view/Lookup/', launch_item_line_view.Launch_item_line_view_Lookup),
    path('Launch_item_line_view/Info/', launch_item_line_view.Launch_item_line_view_Info),
    path('Launch_item_line_view/Copy', launch_item_line_view.Launch_item_line_view_Copy),

]
