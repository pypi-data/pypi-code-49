from django.urls import path

from kaf_pas.production.views import resource_users

urlpatterns = [

    path('Resource_users/Fetch/', resource_users.Resource_users_Fetch),
    path('Resource_users/Add', resource_users.Resource_users_Add),
    path('Resource_users/Update', resource_users.Resource_users_Update),
    path('Resource_users/Remove', resource_users.Resource_users_Remove),
    path('Resource_users/Lookup/', resource_users.Resource_users_Lookup),
    path('Resource_users/Info/', resource_users.Resource_users_Info),
    path('Resource_users/Copy', resource_users.Resource_users_Copy),

]
