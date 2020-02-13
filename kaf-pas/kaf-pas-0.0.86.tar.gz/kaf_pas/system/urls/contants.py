from django.urls import path

from kaf_pas.system.views import contants

urlpatterns = [

    path('Contants/Fetch/', contants.Contants_Fetch),
    path('Contants/Add', contants.Contants_Add),
    path('Contants/Update', contants.Contants_Update),
    path('Contants/RefreshMatView', contants.Contants_RefreshMatView),
    path('Contants/Remove', contants.Contants_Remove),
    path('Contants/fixed_num_in_operations', contants.Contants_fixed_num_in_operations),
    path('Contants/Lookup/', contants.Contants_Lookup),
    path('Contants/Info/', contants.Contants_Info),
    path('Contants/Copy', contants.Contants_Copy),

]
