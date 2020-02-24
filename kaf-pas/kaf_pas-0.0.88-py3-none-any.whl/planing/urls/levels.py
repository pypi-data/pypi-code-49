from django.urls import path

from kaf_pas.planing.views import levels

urlpatterns = [

    path('Levels/Fetch/', levels.Levels_Fetch),
    path('Levels/Add', levels.Levels_Add),
    path('Levels/Update', levels.Levels_Update),
    path('Levels/Remove', levels.Levels_Remove),
    path('Levels/Lookup/', levels.Levels_Lookup),
    path('Levels/Info/', levels.Levels_Info),
    path('Levels/Copy', levels.Levels_Copy),

]
