from django.urls import path

from kaf_pas.planing.views import operation_color

urlpatterns = [

    path('Operation_color/Fetch/', operation_color.Operation_color_Fetch),
    path('Operation_color/Add', operation_color.Operation_color_Add),
    path('Operation_color/Update', operation_color.Operation_color_Update),
    path('Operation_color/Remove', operation_color.Operation_color_Remove),
    path('Operation_color/Lookup/', operation_color.Operation_color_Lookup),
    path('Operation_color/Info/', operation_color.Operation_color_Info),
    path('Operation_color/Copy', operation_color.Operation_color_Copy),

]
