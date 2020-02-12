import re
import urllib.parse


def limpiar_cuerpo(texto_nota, lower=False):
    """
    Esta función está dedicada a limpiar textos relacionados sobre todo con notas, como el cuerpo, el título, ect.
    :param texto_nota: Texto a limpiar.
    :param lower: Indica si se quieren pasar las mayúsculas a minúsculas o que queden como está.
    :return: Un string con el texto limpio.
    """

    x = texto_nota.strip()
    if lower:
        x = x.lower()
    x = re.sub("&#xe1;", "á", x)
    x = re.sub("&#xe9;", "é", x)
    x = re.sub("&#xed;", "í", x)
    x = re.sub("&#xf3;", "ó", x)
    x = re.sub("&#xfa;", "ú", x)
    x = re.sub('<.*?>', '', x)
    x = re.sub(pattern="&quot;", repl="", string=x)
    x = re.sub("&.*?;", " ", x)
    x = re.sub("\n", "", x)
    return x


def extraer_content_id(url_nota):
    """
    Esta función tiene como objectivo extrar el content_id de una url.
    :param url_nota: Url de la nota a procesar.
    :return: Un string con el content_id.
    """
    content_id_list = re.findall(r"(?:_\d_)(.+)(?:.html)$", url_nota)
    if content_id_list:
        return content_id_list[0]
    else:
        return None


def extraer_seccion(url_nota):
    """
    Esta función tiene como objectivo extrar la sección de una url. Para esto se extrae dentro de la url
    el path padre, es decir el primero de izquierda a derecha.
    :param url_nota: Url de la nota a procesar
    :return: Un string con la sección.
    """
    path = urllib.parse.urlparse(url_nota).path
    return list(filter(None, path.split('/')))[0]
