from django.urls import path

from kaf_pas.planing.views import routing

urlpatterns = [

    path('Routing/Fetch/', routing.Routing_Fetch),
    path('Routing/Fetch1/', routing.Operations_FetchView),
    path('Routing/Add', routing.Routing_Add),
    path('Routing/Update', routing.Routing_Update),
    path('Routing/Remove', routing.Routing_Remove),
    path('Routing/Lookup/', routing.Routing_Lookup),
    path('Routing/Info/', routing.Routing_Info),
    path('Routing/Copy', routing.Routing_Copy),
    path('Routing/FetchLevels/', routing.Routing_FetchLevels),
    path('Routing/FetchLocationsLevel/', routing.Routing_FetchLocationsLevel),
    path('Routing/FetchResourcesLevel/', routing.Routing_FetchResourcesLevel),

]
