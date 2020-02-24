from django.urls import path

from kaf_pas.accounting.views import tmp_buffer_off

urlpatterns = [

    path('TmpBuffers_off/Fetch/', tmp_buffer_off.Tmp_buffer_off_Fetch),
    path('TmpBuffers_off/Add', tmp_buffer_off.Tmp_buffer_off_Add),
    path('TmpBuffers_off/Update', tmp_buffer_off.Tmp_buffer_off_Update),
    path('TmpBuffers_off/Remove', tmp_buffer_off.Tmp_buffer_off_Remove),
    path('TmpBuffers_off/Lookup/', tmp_buffer_off.Tmp_buffer_off_Lookup),
    path('TmpBuffers_off/Info/', tmp_buffer_off.Tmp_buffer_off_Info),
    path('TmpBuffers_off/Copy', tmp_buffer_off.Tmp_buffer_off_Copy),

]
