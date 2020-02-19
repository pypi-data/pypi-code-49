from django.urls import path

from isc_common.auth.views import user_permission

urlpatterns = [

    path('User_permission/Fetch/', user_permission.User_permission_Fetch),
    path('User_permission/Add', user_permission.User_permission_Add),
    path('User_permission/Update', user_permission.User_permission_Update),
    path('User_permission/Remove', user_permission.User_permission_Remove),
    path('User_permission/Lookup', user_permission.User_permission_Lookup),

]
