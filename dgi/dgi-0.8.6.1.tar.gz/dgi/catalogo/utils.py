import re

import requests
from datetime import datetime

from bs4 import BeautifulSoup


def recupera_informacoes_da_listagem(url: str) -> dict:
    """Função para mapeamento das características presentes na busca que está sendo realizada

    Args:
        url (str): URL da página de query de imagens do DGI/INPE que deve ser analisada

    Returns:
        dict: Dicionário conténdo as informações da página, dentre elas
            
            elementos: ``int``: Quantidade de elementos encontrados na query de imagens

            paginas: ``int``: Quantidade de páginas para alocar os elementos encontrados
    """

    res = requests.get(url)

    if res.status_code != 200:
        raise RuntimeError("Ops! Erro no link {}".format(url))

    if res.content == b"\xef\xbb\xbf\n\n <h5>Nenhum registro encontrado!</h5>":
        raise RuntimeError("Nenhum registro foi encontrado no link {}".format(url))        
    
    soup = BeautifulSoup(res.content, features="lxml")

    return {
        "elementos": int(soup.findAll('td')[1].find('b').text),
        "paginas": int(soup.findAll('td')[0].text.split()[-1])
    }


def lista_para_data(lista: list) -> datetime:
    """Transforma a lista de tempo coletado do DGI/INPE para Date

    Args:
        lista (list): Lista com as datas coletadas
    
    Returns:
        datetime: Data no formato Y-M-D:H:M:S
    """

    dia = lista[0].split(":")[1]
    hora = lista[1].replace("Hora", "").split("S")[0][1:]

    return datetime.strptime(f"{dia}:{hora}", "%Y-%m-%d:%H:%M:%S")


def formata_lista_de_imagens(soup, pagina, nome_do_local) -> list:
    """Função para formatar os dados de imagens da listagem presente no objeto BeautifulSoup4

    Args:
        soup (bs4.BeautifulSoup): Objeto da página de query de imagens do DGI/INPE
        
        pagina (int): Número da página que foi raspada
        
        nome_do_local (str): Nome do local onde as imagens da página foram coletados

    Returns:
        list: Lista de dicionários, estes que contém as informações das imagens
    """

    lista_de_imagens = []
    imagens_na_pagina = soup.findAll("span", id=re.compile("^imagemblink\d+"))
    quadrantes_das_imagens = soup.findAll("div", id=re.compile("^nuvens\d+"))
    centro_da_imagens = soup.findAll("div", id=re.compile("^centro\d+"))
    coord_superior_imagens = soup.findAll("div", id=re.compile("^superior\d+"))
    coord_inferior_imagens = soup.findAll("div", id=re.compile("^inferior\d+"))
    
    dados_extras_das_imagens = soup.findChildren("td")
    
    for imagem, quadrantes, centro, coord_sup, coord_infer, index in zip(
            imagens_na_pagina, quadrantes_das_imagens, centro_da_imagens, coord_superior_imagens,
                coord_inferior_imagens, range(0, len(imagens_na_pagina))):
        
        i = imagem.find("img")
        
        # Recuperando as coordenadas
        centros = centro.findChildren("td")
        superior = coord_sup.findChildren("td")
        inferior = coord_infer.findChildren("td")

        # Recuperando dados de quadrantes
        qn = quadrantes.findChildren("td")

        informacoes_extras = dados_extras_das_imagens[9 + (90 * index)].text.replace("\t", "").split()
        orbita, ponto = informacoes_extras[2].split("/")
        data = lista_para_data(informacoes_extras[3:5])

        lista_de_imagens.append({
            "nome": i["src"].split("/")[-1].split("_")[1],
            "quicklook_url": "http://www.dgi.inpe.br/" + i["src"],
            "satelite": i["src"].split("/")[2],
            "instrumento": i["src"].split("/")[3],
            "orbita": int(orbita),
            "ponto": int(ponto),
            "data_imagem": data,
            "data_insercao_no_banco": datetime.now(),
            "quantidade_nuvens": {
                "quadrante_1": int(qn[4].text),
                "quadrante_2": int(qn[8].text),
                "quadrante_3": int(qn[13].text),
                "quadrante_4": int(qn[17].text)
            },
            "pagina": pagina,
            "centro_da_cena": {
                "type": "Point",
                "coordinates": [
                    float(centros[7].text), 
                    float(centros[4].text)
                ]
            },
            "poligono_da_cena": {
                "type": "Polygon",
                "coordinates": [[ [
                    float(superior[13].text), # Superior esquerdo
                    float(superior[6].text)
                    ], [
                    float(superior[16].text), # Superior direito
                    float(superior[9].text)
                ], [
                    float(inferior[16].text), # Inferior direito
                    float(inferior[9].text)
                ], [
                    float(inferior[13].text), # Inferior esquerdo
                    float(inferior[6].text)
                ], [
                    float(superior[13].text), # Superior esquerdo (Para fechar o poligono)
                    float(superior[6].text)
                ]]]
            },
            "local": nome_do_local
        })

    return lista_de_imagens
