from django.urls import path

from kaf_pas.kd.views import lotsman_documents_hierarcy_files

urlpatterns = [

    path('Lotsman_documents_hierarcy_files/Fetch/', lotsman_documents_hierarcy_files.Lotsman_documents_hierarcy_files_Fetch),
    path('Lotsman_documents_hierarcy_files/Add', lotsman_documents_hierarcy_files.Lotsman_documents_hierarcy_files_Add),
    path('Lotsman_documents_hierarcy_files/Update', lotsman_documents_hierarcy_files.Lotsman_documents_hierarcy_files_Update),
    path('Lotsman_documents_hierarcy_files/Remove', lotsman_documents_hierarcy_files.Lotsman_documents_hierarcy_files_Remove),
    path('Lotsman_documents_hierarcy_files/Lookup/', lotsman_documents_hierarcy_files.Lotsman_documents_hierarcy_files_Lookup),
    path('Lotsman_documents_hierarcy_files/Info/', lotsman_documents_hierarcy_files.Lotsman_documents_hierarcy_files_Info),
    path('Lotsman_documents_hierarcy_files/Copy', lotsman_documents_hierarcy_files.Lotsman_documents_hierarcy_files_Copy),

]
