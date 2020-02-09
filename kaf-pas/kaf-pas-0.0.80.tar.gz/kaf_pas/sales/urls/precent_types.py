from django.urls import path

from kaf_pas.sales.views import precent_types

urlpatterns = [

    path('Precent_types/Fetch/', precent_types.Precent_types_Fetch),
    path('Precent_types/Add', precent_types.Precent_types_Add),
    path('Precent_types/Update', precent_types.Precent_types_Update),
    path('Precent_types/Remove', precent_types.Precent_types_Remove),
    path('Precent_types/Lookup/', precent_types.Precent_types_Lookup),
    path('Precent_types/Info/', precent_types.Precent_types_Info),
    path('Precent_types/Copy', precent_types.Precent_types_Copy),

]
