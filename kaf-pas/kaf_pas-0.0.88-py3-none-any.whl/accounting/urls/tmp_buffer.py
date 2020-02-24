from django.urls import path

from kaf_pas.accounting.views import tmp_buffer

urlpatterns = [

    path('TmpBuffers/Fetch/', tmp_buffer.Tmp_buffer_Fetch),
    path('TmpBuffers/Add', tmp_buffer.Tmp_buffer_Add),
    path('TmpBuffers/Update', tmp_buffer.Tmp_buffer_Update),
    path('TmpBuffers/Remove', tmp_buffer.Tmp_buffer_Remove),
    path('TmpBuffers/Lookup/', tmp_buffer.Tmp_buffer_Lookup),
    path('TmpBuffers/Info/', tmp_buffer.Tmp_buffer_Info),
    path('TmpBuffers/Copy', tmp_buffer.Tmp_buffer_Copy),

]
