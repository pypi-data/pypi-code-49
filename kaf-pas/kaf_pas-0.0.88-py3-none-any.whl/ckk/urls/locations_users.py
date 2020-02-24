from django.urls import path

from kaf_pas.ckk.views import locations_users

urlpatterns = [

    path('Locations_users/Fetch/', locations_users.Locations_users_Fetch),
    path('Locations_users/Add', locations_users.Locations_users_Add),
    path('Locations_users/Update', locations_users.Locations_users_Update),
    path('Locations_users/CopyUsers', locations_users.Locations_users_CopyUsers),
    path('Locations_users/Remove', locations_users.Locations_users_Remove),
    path('Locations_users/Lookup/', locations_users.Locations_users_Lookup),
    path('Locations_users/Info/', locations_users.Locations_users_Info),
    path('Locations_users/Copy', locations_users.Locations_users_Copy),

]
