from django.urls import path

from kaf_pas.accounting.views import buffers

urlpatterns = [

    path('Buffers/Fetch/', buffers.Buffers_Fetch),
    path('Buffers/Add', buffers.Buffers_Add),
    path('Buffers/Update', buffers.Buffers_Update),
    path('Buffers/Remove', buffers.Buffers_Remove),
    path('Buffers/Lookup/', buffers.Buffers_Lookup),
    path('Buffers/Info/', buffers.Buffers_Info),
    path('Buffers/Copy', buffers.Buffers_Copy),

]
