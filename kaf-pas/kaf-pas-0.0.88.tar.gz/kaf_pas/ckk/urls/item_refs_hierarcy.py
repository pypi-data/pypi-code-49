from django.urls import path

from kaf_pas.ckk.views import item_refs_hierarcy

urlpatterns = [

    path('Item_refs_hierarcy/Fetch/', item_refs_hierarcy.Item_refs_hierarcy_Fetch),
    path('Item_refs_hierarcy/Add', item_refs_hierarcy.Item_refs_hierarcy_Add),
    path('Item_refs_hierarcy/Update', item_refs_hierarcy.Item_refs_hierarcy_Update),
    path('Item_refs_hierarcy/Remove', item_refs_hierarcy.Item_refs_hierarcy_Remove),
    path('Item_refs_hierarcy/Lookup/', item_refs_hierarcy.Item_refs_hierarcy_Lookup),
    path('Item_refs_hierarcy/Info/', item_refs_hierarcy.Item_refs_hierarcy_Info),
    path('Item_refs_hierarcy/Copy', item_refs_hierarcy.Item_refs_hierarcy_Copy),

]
