from django.urls import path

from kaf_pas.planing.views import posting_items

urlpatterns = [

    path('Posting_items/Fetch/', posting_items.Posting_items_Fetch),
    path('Posting_items/Add', posting_items.Posting_items_Add),
    path('Posting_items/Update', posting_items.Posting_items_Update),
    path('Posting_items/Remove', posting_items.Posting_items_Remove),
    path('Posting_items/Lookup/', posting_items.Posting_items_Lookup),
    path('Posting_items/Info/', posting_items.Posting_items_Info),
    path('Posting_items/Copy', posting_items.Posting_items_Copy),

]
