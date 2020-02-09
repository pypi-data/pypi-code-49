from django.urls import path

from kaf_pas.planing.views import operation_locations

urlpatterns = [

    path('Operation_locations/Fetch/', operation_locations.Operation_locations_Fetch),
    path('Operation_locations/Add', operation_locations.Operation_locations_Add),
    path('Operation_locations/Update', operation_locations.Operation_locations_Update),
    path('Operation_locations/Remove', operation_locations.Operation_locations_Remove),
    path('Operation_locations/Lookup/', operation_locations.Operation_locations_Lookup),
    path('Operation_locations/Info/', operation_locations.Operation_locations_Info),
    path('Operation_locations/Copy', operation_locations.Operation_locations_Copy),

]
