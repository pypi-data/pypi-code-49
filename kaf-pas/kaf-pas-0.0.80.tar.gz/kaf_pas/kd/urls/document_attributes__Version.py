from django.urls import path

from kaf_pas.kd.views import document_attributes__Version

urlpatterns = [

    path('Document_attributes__Version/Fetch/', document_attributes__Version.Document_attributes__Version_Fetch),
    path('Document_attributes__Version/Add', document_attributes__Version.Document_attributes__Version_Add),
    path('Document_attributes__Version/Update', document_attributes__Version.Document_attributes__Version_Update),
    path('Document_attributes__Version/Remove', document_attributes__Version.Document_attributes__Version_Remove),
    path('Document_attributes__Version/Lookup/', document_attributes__Version.Document_attributes__Version_Lookup),
    path('Document_attributes__Version/Info/', document_attributes__Version.Document_attributes__Version_Info),
    path('Document_attributes__Version/Copy', document_attributes__Version.Document_attributes__Version_Copy),

]
