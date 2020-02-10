from django.urls import path

from kaf_pas.kd.views import document_attributes_STMP_120

urlpatterns = [

    path('Document_attributes_STMP_120/Fetch/', document_attributes_STMP_120.Document_attributes_STMP_120_Fetch),
    path('Document_attributes_STMP_120/Add', document_attributes_STMP_120.Document_attributes_STMP_120_Add),
    path('Document_attributes_STMP_120/Update', document_attributes_STMP_120.Document_attributes_STMP_120_Update),
    path('Document_attributes_STMP_120/Remove', document_attributes_STMP_120.Document_attributes_STMP_120_Remove),
    path('Document_attributes_STMP_120/Lookup/', document_attributes_STMP_120.Document_attributes_STMP_120_Lookup),
    path('Document_attributes_STMP_120/Info/', document_attributes_STMP_120.Document_attributes_STMP_120_Info),
    path('Document_attributes_STMP_120/Copy', document_attributes_STMP_120.Document_attributes_STMP_120_Copy),

]
