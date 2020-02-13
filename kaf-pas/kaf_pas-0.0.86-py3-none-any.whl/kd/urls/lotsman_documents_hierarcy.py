from django.urls import path

from kaf_pas.kd.views import lotsman_documents_hierarcy

urlpatterns = [

    path('Lotsman_documents_hierarcy/Fetch/', lotsman_documents_hierarcy.Lotsman_documents_hierarcy_Fetch),
    path('Lotsman_documents_hierarcy/Fetch1/', lotsman_documents_hierarcy.Lotsman_documents_hierarcy_Fetch1),
    path('Lotsman_documents_hierarcy_doc/Fetch/', lotsman_documents_hierarcy.Lotsman_documents_hierarcy_doc_Fetch),
    path('Lotsman_documents_hierarcy/Add', lotsman_documents_hierarcy.Lotsman_documents_hierarcy_Add),
    path('Lotsman_documents_hierarcy/Update', lotsman_documents_hierarcy.Lotsman_documents_hierarcy_Update),
    path('Lotsman_documents_hierarcy/Remove', lotsman_documents_hierarcy.Lotsman_documents_hierarcy_Remove),
    path('Lotsman_documents_hierarcy/Lookup/', lotsman_documents_hierarcy.Lotsman_documents_hierarcy_Lookup),
    path('Lotsman_documents_hierarcy/Info/', lotsman_documents_hierarcy.Lotsman_documents_hierarcy_Info),
    path('Lotsman_documents_hierarcy/Copy', lotsman_documents_hierarcy.Lotsman_documents_hierarcy_Copy),
    path('Lotsman_documents_hierarcy/MakeItem', lotsman_documents_hierarcy.Lotsman_documents_hierarcy_MakeItem),
    path('Lotsman_documents_hierarcy/ReloadDoc', lotsman_documents_hierarcy.Lotsman_documents_hierarcy_ReloadDoc),
    path('Lotsman_documents_hierarcy/RefreshMView', lotsman_documents_hierarcy.Lotsman_documents_hierarcys_RefreshMView),
]
