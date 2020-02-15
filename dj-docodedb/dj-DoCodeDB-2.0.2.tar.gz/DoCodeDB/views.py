from django.shortcuts import render
from django.apps import apps

import docode_managebd.procesos_bd as proc_bd
#from Sistema.vistas import procesos_bd as proc_bd

# Create your views here.

# Vista/Funcion para implementar la edicion de registros por medio de un modal
def modaleditar(request):
    id = request.POST.get('id')
    origen = request.POST.get('origen')
    appname = request.POST.get('appname')
    info = origen.split(' ')[0]
    modelo = apps.get_model(appname, info) # Se utliza la aplicacion "Sistema"

    return proc_bd.modal_editar(id,modelo)
      