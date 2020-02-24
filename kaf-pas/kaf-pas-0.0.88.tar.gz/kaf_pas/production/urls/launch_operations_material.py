from django.urls import path

from kaf_pas.production.views import launch_operations_material

urlpatterns = [

    path('Launch_operations_material/Fetch/', launch_operations_material.Launch_operations_material_Fetch),
    path('Launch_operations_material/Add', launch_operations_material.Launch_operations_material_Add),
    path('Launch_operations_material/Update', launch_operations_material.Launch_operations_material_Update),
    path('Launch_operations_material/Remove', launch_operations_material.Launch_operations_material_Remove),
    path('Launch_operations_material/Lookup/', launch_operations_material.Launch_operations_material_Lookup),
    path('Launch_operations_material/Info/', launch_operations_material.Launch_operations_material_Info),
    path('Launch_operations_material/Copy', launch_operations_material.Launch_operations_material_Copy),

]
