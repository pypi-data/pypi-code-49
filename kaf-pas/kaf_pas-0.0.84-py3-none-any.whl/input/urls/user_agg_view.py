from django.urls import path

from kaf_pas.input.views import user_agg_view

urlpatterns = [

    path('User_agg_view/Fetch/', user_agg_view.User_agg_view_Fetch),
    path('User_agg_view/Add', user_agg_view.User_agg_view_Add),
    path('User_agg_view/Update', user_agg_view.User_agg_view_Update),
    path('User_agg_view/Remove', user_agg_view.User_agg_view_Remove),
    path('User_agg_view/Lookup/', user_agg_view.User_agg_view_Lookup),
    path('User_agg_view/Info/', user_agg_view.User_agg_view_Info),
    path('User_agg_view/Copy', user_agg_view.User_agg_view_Copy),

]
