from django.urls import path

from kaf_pas.production.views import launch_item_line

urlpatterns = [

    path('Launch_item_line/Fetch/', launch_item_line.Launch_item_line_Fetch),
    path('Launch_item_line/Add', launch_item_line.Launch_item_line_Add),
    path('Launch_item_line/Update', launch_item_line.Launch_item_line_Update),
    path('Launch_item_line/Remove', launch_item_line.Launch_item_line_Remove),
    path('Launch_item_line/Lookup/', launch_item_line.Launch_item_line_Lookup),
    path('Launch_item_line/Info/', launch_item_line.Launch_item_line_Info),
    path('Launch_item_line/Copy', launch_item_line.Launch_item_line_Copy),

]
