from django.urls import path

from kaf_pas.kd.views import lotsman_documents_hierarcy_refs

urlpatterns = [

    path('Lotsman_documents_hierarcy_refs/Fetch/', lotsman_documents_hierarcy_refs.Lotsman_documents_hierarcy_refs_Fetch),
    path('Lotsman_documents_hierarcy_refs/Add', lotsman_documents_hierarcy_refs.Lotsman_documents_hierarcy_refs_Add),
    path('Lotsman_documents_hierarcy_refs/Update', lotsman_documents_hierarcy_refs.Lotsman_documents_hierarcy_refs_Update),
    path('Lotsman_documents_hierarcy_refs/Remove', lotsman_documents_hierarcy_refs.Lotsman_documents_hierarcy_refs_Remove),
    path('Lotsman_documents_hierarcy_refs/Lookup/', lotsman_documents_hierarcy_refs.Lotsman_documents_hierarcy_refs_Lookup),
    path('Lotsman_documents_hierarcy_refs/Info/', lotsman_documents_hierarcy_refs.Lotsman_documents_hierarcy_refs_Info),
    path('Lotsman_documents_hierarcy_refs/Copy', lotsman_documents_hierarcy_refs.Lotsman_documents_hierarcy_refs_Copy),

]
