from django import template
register = template.Library()

@register.filter(name='contenido')
def contenido(registro,campos):
    registros = list()
    for campo in campos:
        registros.append(getattr(registro,campo['nombre']))

    return registros

