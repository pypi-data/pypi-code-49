from django.urls import path

from kaf_pas.kd.views import document_attributes_Name_sortament

urlpatterns = [

    path('Document_attributes_Name_sortament/Fetch/', document_attributes_Name_sortament.Document_attributes_Name_sortament_Fetch),
    path('Document_attributes_Name_sortament/Add', document_attributes_Name_sortament.Document_attributes_Name_sortament_Add),
    path('Document_attributes_Name_sortament/Update', document_attributes_Name_sortament.Document_attributes_Name_sortament_Update),
    path('Document_attributes_Name_sortament/Remove', document_attributes_Name_sortament.Document_attributes_Name_sortament_Remove),
    path('Document_attributes_Name_sortament/Lookup/', document_attributes_Name_sortament.Document_attributes_Name_sortament_Lookup),
    path('Document_attributes_Name_sortament/Info/', document_attributes_Name_sortament.Document_attributes_Name_sortament_Info),
    path('Document_attributes_Name_sortament/Copy', document_attributes_Name_sortament.Document_attributes_Name_sortament_Copy),

]
