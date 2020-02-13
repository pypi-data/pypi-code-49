from django.urls import path

from kaf_pas.kd.views import lotsman_document_attr_cross

urlpatterns = [

    path('Lotsman_document_attr_cross/Fetch/', lotsman_document_attr_cross.Lotsman_document_attr_cross_Fetch),
    path('Lotsman_document_attr_cross/Add', lotsman_document_attr_cross.Lotsman_document_attr_cross_Add),
    path('Lotsman_document_attr_cross/Update', lotsman_document_attr_cross.Lotsman_document_attr_cross_Update),
    path('Lotsman_document_attr_cross/Remove', lotsman_document_attr_cross.Lotsman_document_attr_cross_Remove),
    path('Lotsman_document_attr_cross/Lookup/', lotsman_document_attr_cross.Lotsman_document_attr_cross_Lookup),
    path('Lotsman_document_attr_cross/Info/', lotsman_document_attr_cross.Lotsman_document_attr_cross_Info),
    path('Lotsman_document_attr_cross/Copy', lotsman_document_attr_cross.Lotsman_document_attr_cross_Copy),

]
