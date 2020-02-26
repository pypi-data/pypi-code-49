import requests
from bs4 import BeautifulSoup
from datetime import datetime
import sys
#sys.path.append('C:\\Users\\coliveira\\OneDrive\\Coding\\Python\\MFToolbox\\')
from mftoolbox import constants

def ultimo_pregao(_ativo):
    """
    Busca no site IBOVX a data do último pregão para um ativo

    :param _ativo: código do ativo
    :return: tuple com a data como datetime, data no formato DD/MM/AAAA e a cotação
    """

    url = 'https://www.ibovx.com.br/historico-papeis-bovespa.aspx?papel=' + _ativo + '&qtdpregoes=1'
    r = requests.get(url, headers=constants.Header.header)
    soup = BeautifulSoup(r.text, 'lxml')
    _tabela = soup.find_all('td')
    try:
        if _tabela[20].text == 'Nº Negócios':
            posicao = 21
        else:
            posicao = 19
        return  (datetime.strptime(_tabela[posicao].text, '%d/%m/%Y'),_tabela[posicao].text)
    except:
        return (None, None)

def cotacao(_ativo, _data):
    """
    Busca no site IBOVX a cotação do ativo na data especificada. Retorna um tuple com data e cotação. Se não houver
    negociação naquela data, retorna a primeira cotação anterior disponível

    :param _ativo: código do ativo
    :param _data: data da cotação

    :return: tuple com a data como datetime, data no formato DD/MM/AAAA e a cotação
    """
    _data = datetime.strptime(_data, '%d/%m/%Y')
    _pregoes = str((datetime.now() - _data).days)
    url = 'https://www.ibovx.com.br/historico-papeis-bovespa.aspx?papel=' + _ativo + '&qtdpregoes=' + _pregoes
    r = requests.get(url, headers=constants.Header.header)
    soup = BeautifulSoup(r.text, 'lxml')
    _tabela = soup.find_all('td')
    i = len(_tabela)
    _cotacao_anterior = []
    if _tabela[20].text == 'Nº Negócios':
        incremento = 9
    else:
        incremento = 7

    try:
        while i >=0:
            _data_pagina = datetime.strptime(_tabela[i-incremento].text, '%d/%m/%Y')
            _cotacao = float(_tabela[i-incremento+3].text.replace('.','').replace(',','.'))
            if _data_pagina == _data:
                return (_data, _data.strftime('%d/%m/%Y'), _cotacao)
            elif _data_pagina > _data:
                return (_cotacao_anterior)
            _cotacao_anterior = (_data_pagina, _data_pagina.strftime('%d/%m/%Y'), _cotacao)
            i -= incremento
    except:
        return (_cotacao_anterior)