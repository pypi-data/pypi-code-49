from django.urls import path

from kaf_pas.production.views import ready_2_launch_detail

urlpatterns = [

    path('Ready_2_launch_detail/Fetch/', ready_2_launch_detail.Ready_2_launch_detail_Fetch),
    path('Ready_2_launch_detail/Add', ready_2_launch_detail.Ready_2_launch_detail_Add),
    path('Ready_2_launch_detail/Update', ready_2_launch_detail.Ready_2_launch_detail_Update),
    path('Ready_2_launch_detail/Remove', ready_2_launch_detail.Ready_2_launch_detail_Remove),
    path('Ready_2_launch_detail/Lookup/', ready_2_launch_detail.Ready_2_launch_detail_Lookup),
    path('Ready_2_launch_detail/Info/', ready_2_launch_detail.Ready_2_launch_detail_Info),
    path('Ready_2_launch_detail/Copy', ready_2_launch_detail.Ready_2_launch_detail_Copy),

]
