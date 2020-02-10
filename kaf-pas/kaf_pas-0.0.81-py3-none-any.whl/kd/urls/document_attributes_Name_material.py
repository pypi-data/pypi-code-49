from django.urls import path

from kaf_pas.kd.views import document_attributes_Name_material

urlpatterns = [

    path('Document_attributes_Name_material/Fetch/', document_attributes_Name_material.Document_attributes_Name_material_Fetch),
    path('Document_attributes_Name_material/Add', document_attributes_Name_material.Document_attributes_Name_material_Add),
    path('Document_attributes_Name_material/Update', document_attributes_Name_material.Document_attributes_Name_material_Update),
    path('Document_attributes_Name_material/Remove', document_attributes_Name_material.Document_attributes_Name_material_Remove),
    path('Document_attributes_Name_material/Lookup/', document_attributes_Name_material.Document_attributes_Name_material_Lookup),
    path('Document_attributes_Name_material/Info/', document_attributes_Name_material.Document_attributes_Name_material_Info),
    path('Document_attributes_Name_material/Copy', document_attributes_Name_material.Document_attributes_Name_material_Copy),

]
