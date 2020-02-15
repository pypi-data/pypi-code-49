from django.core.mail import send_mail
from DoCodeDB.models import Tsendgrid
from django.template import loader
from django.conf import settings


# Metodo para enviar correo info = contexto a enviar al template
def enviar_correo(origen,correo_enviar,cc,info,template):

    if settings.ENVIAR_CORREO :
        try:
            api_key = Tsendgrid.objects.all().first()
            settings.SENDGRID_API_KEY = api_key.key

            # PROCESOS PARA AGREGAR IMAGENES AL CORREO PERSONALIZADO
            # header_img = ""
            # footer_img = ""

            # imagenes = correoImagene.objects.all()

            # for img in imagenes:
            #     if img.tipo == "header":
            #         header_img = img.get_img()
            #     if img.tipo == "footer":
            #         footer_img = img.get_img()
            
            context = {}

            context.update(info)
            
            html_message = loader.render_to_string(
                template,
                context
            )
            
            send_mail(
                'Registro',
                "Body",
                origen,
                [correo_enviar],
                fail_silently=False,
                html_message = html_message,
            )
            # Enviar correo con copia
            if cc != None:
                send_mail('Formulario de Contacto','',origen,cc,fail_silently=False,html_message = html_message)
            return True

        except Exception as e:
            #_logs.nuevo_log(str(e))
            return False

    else:
        #_logs.nuevo_log("No se envio correo: ENVIAR_CORREO = False")
        return False