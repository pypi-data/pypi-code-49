# Manejo de formularios DoCode

import docode_managebd.procesos_bd as proc_bd
#from Sistema.vistas import procesos_bd as proc_bd

def dc_verificarform(request,model,spinner):
      
    _spinner = spinner
    # Proceso para obtener campos del modelo
    fields_ = proc_bd.obtener_campos(model)
    fields_.pop(0)

    # directorio que almacena los mensajes
    respuesta = {}
    respuesta = {
        'Error' : "-1",
        'mensaje' : "",
        'constraint' : "",
        'registro' : None
    }
    #++++++++++ MANEJO FORMULARIOS (FORM) ++++++++++
    if request.method == 'POST':
        try:
            respuesta = proc_bd.verificar_formulario(request,model)
        except Exception as e:
            None
    #++++++++++ MANEJO FORMULARIOS (FORM) ++++++++++

    # Todos los registros del modelo
    registros = model.objects.all()
    object_name = model._meta.object_name
    appname = model._meta.app_label

    if _spinner == "" or _spinner == None:
          _spinner = "Spinner.html"

    sub={
      'appname' : appname,
      'object_name' : object_name,
      'respuesta' : respuesta,
      'registros' : registros,
      'campos' : fields_,
      'spinner_dc' : _spinner
    }

    return sub