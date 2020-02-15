import datetime


def string_para_data(string: str, reverso=True, sep="/") -> datetime.datetime:
    """Função para transformação de string em data

    Args:
        string (str): String no formato DD{sep}MM{sep}AAAA
        
        reverso (bool): Indica se a string inserida deve ser invertida
        
        sep (str): Indica o separador entre cada elemento das datas

    Returns:
        datetime: String traduzida para datetime
    """

    lista = list(map(int, string.split(sep)[::-1]))
    if not reverso:
        lista = list(map(int, string.split(sep)))
    return datetime.datetime(*lista)


def divide_lista(lista: list, n: int) -> list:
    """Função para dividir uma lista em N elementos

    Args:
        lista (list): Lista que deverá ser dividida
        
        n (int): Quantidade de partes que devem ser gerada da lista inserida

    Returns:
        list: Lista contendo as listas divididas
    """

    u = 0.0
    m = len(lista) / float(n)
    saida = []
    
    while u < len(lista):
        saida.append(lista[int(u): int(u + m)])
        u += m

    return saida


def cria_documento_download(link) -> dict:
    """Função para gerar um JSON no formato que deve ser inserido nos registros de
    download do banco de dados

    Args:
        link (str): Link de onde as informações devem ser extraídas

    Returns:remove_imagens_duplicadas
        dict: Dicionário com as seguintes chaves
            satelite: ``str``: Nome do satélite que carrega o instrumento que capturou a imagem
            
            instrumento: ``str``: Nome do instrumento que capturou a imagem
            
            data: ``str``: Data da captura da imagem
            
            orbita: ``str``: Orbita da imagem
            
            ponto: ``str``: Ponto da imagem
    """

    # ToDo: Remover e tentar generalizar a função (E. g. Chain of responsibility)
    if "CBERS_4" not in link:
        raise RuntimeError("Este sensor ainda não é suportado por esta ferramenta! Trabalhamos apenas com CBERS-4")

    link_dividido = link.split("_")

    if "scenario" in link or "png" in link:
        path = link_dividido[-2]
        row = link_dividido[-1].split(".")[0]
        
    else:
        path = link_dividido[-4]
        row = link_dividido[-3]    

    satelite = link_dividido[0]
    instrumento = link_dividido[2]    
    data = f"{link_dividido[3][0:4]}_{link_dividido[3][4:6]}_{link_dividido[3][6:]}" 

    return {
        "satelite": satelite,
        "instrumento": instrumento,
        "data": data,
        "orbita": int(path),
        "ponto": int(row)
    }


def remove_imagens_duplicadas(lista_de_imagens: list) -> set:
    """Função para removação de imagens duplicadas em um conjunto de imagens
    
    Aplica-se um filtro na busca de nomes duplicados, caso haja, estes são removidos

    Args:
        lista_de_imagens (list): Lista de imagens que serão filtradas

    Returns:
        set: Conjunto de imagens filtradas
    """

    return set(map(lambda x: x["nome"], lista_de_imagens))
