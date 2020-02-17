# Procesos basicos para las operaciones con base de datos
from django.http import HttpResponse
import json, re

# Diccionario para almacenar los mensajes de respuesta
respuesta = {
    'Error' : "-1",
    'mensaje' : "",
    'constraint' : "",
    'registro' : None
}

# Metodo para obtener el registro de campos del modelo dado
def obtener_campos(modelo):
    
    fields_ = list()

    for field in modelo._meta.fields:
        relacion = field.related_model
        choices = field.choices
        if relacion != None:
            modelo_base = relacion.objects.all()
            field_base = {}
            field_base = {
                'nombre' : field.name,
                'foreign' : True,
                'qdata' : modelo_base,
                'tipo' : field.get_internal_type()
            }
            fields_.append(field_base)
        elif len(choices) > 0:
            field_base = {}
            field_base = {
                'nombre' : field.name,
                'foreign' : False,
                'qdata' : choices,
                'tipo' : "choices" 
            }
            fields_.append(field_base)
        else:
            field_base = {}
            field_base = {
                'nombre' : field.name,
                'foreign' : False,
                'qdata' : None,
                'tipo' : field.get_internal_type() 
            }
            fields_.append(field_base)
    
    return fields_


def verificar_formulario(request,modelo):
    idForm = request.POST["idForm"]
    global respuesta
        
    # Nueva 
    if idForm == "nuevo":
        respuesta['mensaje'] = alta_registro(request,modelo)
        
    # Se valida el origen antes de eliminar
    # Eliminar
    if idForm == "eliminar":
        respuesta['mensaje'] = eliminar_registro(request,modelo)
        
    # Editar
    if idForm == "editar":
        editar_registro(request,modelo)
        respuesta['mensaje'] = 3
    
    return respuesta


# Metodo para dar de alta un registro de un modelo dado, con iformacion del request(POST)
def alta_registro(request,modelo):
    
    #global Error
    global respuesta
    objeto = modelo()
    validar = True
    notas = False # Validacion solo para cotizaciones Coamin (Notas)

    valido = False
    for field in modelo._meta.fields:
        try:
            if valido:
                # Se verifica si existe alguna relacion en el campo
                relacion = field.related_model
                if relacion != None:
                    if request.POST[field.name] != "":
                        # Se busca el campo relacion con el "id", y se asigan el modelo al "objeto#
                        campo_modelo = relacion.objects.filter(id=request.POST[field.name]).first()
                        setattr(objeto, field.name, campo_modelo)
                else:
                    if field.get_internal_type() == "BooleanField":
                        try:
                            if request.POST[field.name] == "on":
                                objeto.__dict__[field.name] = True
                            else:
                                objeto.__dict__[field.name] = False
                        except Exception as e:
                            objeto.__dict__[field.name] = False
                    elif field.get_internal_type() == "DateField":
                        if request.POST[field.name] != "":
                            objeto.__dict__[field.name] = request.POST[field.name]
                        else:
                            objeto.__dict__[field.name] = None
                    elif field.get_internal_type() == "FileField":
                        try:
                            objeto.__dict__[field.name] = request.FILES[field.name]
                        except Exception as e:
                            None
                    else:
                        if request.POST[field.name] != "":
                            objeto.__dict__[field.name] = request.POST[field.name]
                        else:
                            validar = False
            else:
                valido = True
        except Exception as e:
            respuesta['Error'] = str(e)
            return 10 # Error en Sistema
    

    if validar:
        try:
            objeto.save()
            respuesta['registro'] = objeto
            return 1 # Registro agregado correctamente
        except Exception as e:
            respuesta['Error'] = str(e)
            return 10 # Error en Sistema
    else:
        return 8 # Campos Vacios


# Metodo para eliminar un registro de un modelo dado, con informacion del request(POST)
def eliminar_registro(request,modelo):    
    idsol = request.POST["idEliminar"]
    objeto = modelo.objects.all().filter(id=idsol).first()
    if objeto != None:
        try:
            objeto.delete()
            return 7 # Registro eliminado correctamente
        except Exception as e:
            return mensaje_constraint(str(e))


# Metodo para editar un registro de un modelo dado, con informacion del request(POST)
def editar_registro(request,modelo):
    
    global respuesta
    idsol = request.POST["idEditar"]
    objeto = modelo.objects.all().filter(id=idsol).first()
    if objeto != None:

        valido = False
        for field in modelo._meta.fields:
            if valido:
                relacion = field.related_model
                if relacion != None:
                    if request.POST[field.name] != "":
                        # Se busca el campo relacion con el "id", y se asigan el modelo al "objeto#
                        datos = str(request.POST[field.name]).split(",")
                        campo_modelo = relacion.objects.filter(id=datos[0]).first()
                        setattr(objeto, field.name, campo_modelo)
                    else:
                        setattr(objeto, field.name, None)
                else:
                    if field.get_internal_type() == "BooleanField":
                        try:
                            if request.POST[field.name] == "on":
                                objeto.__dict__[field.name] = True
                            else:
                                objeto.__dict__[field.name] = False
                        except Exception as e:
                            objeto.__dict__[field.name] = False
                    elif field.get_internal_type() == "FileField":
                        try:
                            objeto.__dict__[field.name] = request.FILES[field.name]
                        except Exception as e:
                            None
                    else:
                        if request.POST[field.name] != "":
                            objeto.__dict__[field.name] = request.POST[field.name]
            else:
                valido = True
        
        respuesta['registro'] = objeto
        objeto.save()


# Metodo para llenar el modal de editar con informacion del modelo dado
def modal_editar(id,modelo):

    response_data = {}
    objeto_editar = modelo.objects.all().filter(id=id).first()

    try:
        valido = False
        for field in modelo._meta.fields:
            if valido:
                # Verificar si el campo tiene relacion (foreignkey)
                relacion = field.related_model
                if relacion != None:
                    # Si tiene relacion unicamente asignar el "id" del modelo relacionado
                    modelo_base = getattr(objeto_editar, field.name)
                    try:
                        response_data[field.name+"_editar"] = modelo_base.id
                    except Exception as e:
                        response_data[field.name+"_editar"] = None
                else:
                    if field.get_internal_type() == "DateField":
                        response_data[field.name+"_editar"] = obtener_fecha(getattr(objeto_editar, field.name))
                    elif field.get_internal_type() == "FileField":
                        file = getattr(objeto_editar, field.name)
                        response_data[field.name+"_editar"] = ""
                    else:
                        #response_data[field.name+"_editar"] = objeto_editar.__dict__[field.name]
                        response_data[field.name+"_editar"] = getattr(objeto_editar, field.name)
            else:
                valido = True

        response_data['valido'] = True # Validacion correcta
    except Exception as e:
        response_data['valido'] = False
        response_data['mensaje']  = "Error: " + str(e)
    
    try:
        return HttpResponse(
                json.dumps(response_data),
                content_type="application/json"
            )
    except Exception as e:
        response_data['mensaje']  = "Error: " + str(e)
        # Validacion fallida
        response_data['valido'] = False
        return HttpResponse(
                json.dumps(response_data),
                content_type="application/json"
            )

def obtener_fecha(fecha):
    if fecha != None:
        fecha_string = fecha.strftime("%Y-%m-%d")
    else:
        fecha_string = None
    return fecha_string


# Mensaje para identificar el constraint ligado al registro especifico
def mensaje_constraint(error):
    if "constraint" in error:
        s = error.split("constraint",1)[1]
        s = s.split("table",1)[1]
        result = re.search('"(.*)"', s)
        result = result.group(1)
        global respuesta
        respuesta['constraint'] = str(result)
        return 5 # El registro no se puede eliminar, esta siendo utilizada en otro modulo
    else:
        return 5

def test():
    return "Prueba completa correctamente"