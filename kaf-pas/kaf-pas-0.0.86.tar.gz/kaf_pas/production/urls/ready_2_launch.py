from django.urls import path

from kaf_pas.production.views import ready_2_launch

urlpatterns = [

    path('Ready_2_launch/Fetch/', ready_2_launch.Ready_2_launch_Fetch),
    path('Ready_2_launch/Add', ready_2_launch.Ready_2_launch_Add),
    path('Ready_2_launch/Update', ready_2_launch.Ready_2_launch_Update),
    path('Ready_2_launch/Remove', ready_2_launch.Ready_2_launch_Remove),
    path('Ready_2_launch/Lookup/', ready_2_launch.Ready_2_launch_Lookup),
    path('Ready_2_launch/Info/', ready_2_launch.Ready_2_launch_Info),
    path('Ready_2_launch/Copy', ready_2_launch.Ready_2_launch_Copy),

]
