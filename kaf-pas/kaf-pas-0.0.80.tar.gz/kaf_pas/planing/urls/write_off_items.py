from django.urls import path

from kaf_pas.planing.views import write_off_items

urlpatterns = [

    path('Write_off_items/Fetch/', write_off_items.Write_off_items_Fetch),
    path('Write_off_items/Add', write_off_items.Write_off_items_Add),
    path('Write_off_items/Update', write_off_items.Write_off_items_Update),
    path('Write_off_items/Remove', write_off_items.Write_off_items_Remove),
    path('Write_off_items/Lookup/', write_off_items.Write_off_items_Lookup),
    path('Write_off_items/Info/', write_off_items.Write_off_items_Info),
    path('Write_off_items/Copy', write_off_items.Write_off_items_Copy),

]
