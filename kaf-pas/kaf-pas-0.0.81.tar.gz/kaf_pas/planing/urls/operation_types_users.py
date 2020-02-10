from django.urls import path

from kaf_pas.planing.views import operation_types_users

urlpatterns = [

    path('Operation_types_users/Fetch/', operation_types_users.Operation_types_users_Fetch),
    path('Operation_types_users/Add', operation_types_users.Operation_types_users_Add),
    path('Operation_types_users/Update', operation_types_users.Operation_types_users_Update),
    path('Operation_types_users/Remove', operation_types_users.Operation_types_users_Remove),
    path('Operation_types_users/Lookup/', operation_types_users.Operation_types_users_Lookup),
    path('Operation_types_users/Info/', operation_types_users.Operation_types_users_Info),
    path('Operation_types_users/Copy', operation_types_users.Operation_types_users_Copy),

]
