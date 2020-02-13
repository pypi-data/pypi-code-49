from django.urls import path

from kaf_pas.input.views import users_ex

urlpatterns = [

    path('Users_ex/Fetch/', users_ex.Users_ex_Fetch),
    path('Users_ex/Add', users_ex.Users_ex_Add),
    path('Users_ex/Update', users_ex.Users_ex_Update),
    path('Users_ex/Remove', users_ex.Users_ex_Remove),
    path('Users_ex/Lookup/', users_ex.Users_ex_Lookup),
    path('Users_ex/Info/', users_ex.Users_ex_Info),
    path('Users_ex/Copy', users_ex.Users_ex_Copy),

]
