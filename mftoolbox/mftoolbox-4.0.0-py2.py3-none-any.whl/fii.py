from bs4 import BeautifulSoup
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import sys
sys.path.append('C:\\Users\\coliveira\\OneDrive\\Coding\\Python\\MFToolbox\\mftoolbox')
import funcs
import datetime
#from multiprocessing import Pool, cpu_count
import requests
from tqdm import tqdm
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from cotacoes2 import cotacao, ultimo_pregao

test_partial = 0

caps = DesiredCapabilities().CHROME
# caps["pageLoadStrategy"] = "normal"  #  complete
caps["pageLoadStrategy"] = "eager"  #  interactive
# caps["pageLoadStrategy"] = "none"

STR_HEADER = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) '
                                    'AppleWebKit/537.36 (KHTML, like Gecko) '
                                    'Chrome/39.0.2171.95 Safari/537.36',
                      'Cache-Control': 'no-cache'}

codigos_tipo_mandato = {}
codigos_tipo_gestao = {}
codigos_tipo_investidor = {}
codigos_tipo_prazo = {}
codigos_tipo_segmento = {}
codigos_tipo_fundo = {}
codigos_tipo_anbima = {}
codigos_administradores = {}
dados_administradores = []

primario_tipo_mandato = {}
primario_tipo_gestao = {}
primario_tipo_investidor = {}
primario_tipo_prazo = {}
primario_tipo_segmento = {}
primario_tipo_fundo = {}
primario_tipo_anbima = {}
primario_administradores = {}

def parse_parent_content(_content, _exclude):

    _text = ''

    for i in _content:
        _temp = ''
        if i == '\n':
            continue
        elif i is None:
            continue
        elif i.find(_exclude) != -1:
            continue
        #elif i.find('<span class="value">') is not None:
        if _exclude == 'NOTAS:':
            pass
        if i.string is not None:
            _temp = i.string
            if _text.find(_temp) == -1:
                _text = _text + _temp + ' '

    return _text

def preferencial(_valor1, _valor2, **kwargs):
    """
    Compara os dois valores e define o preferencial baseado em critérios definidos por lógica ou por argumentos.

    :param _valor1: primeiro valor
    :param _valor2: segundo valor
    :param kwargs:
        - codigo = True or False
        - ordem = 1 ou 2
    :return: o valor preferencial segundo a lógica
    """

    if type(_valor1) is str:
        _valor1 = _valor1.replace('N/A', '').replace('-', '')
    if type(_valor2) is str:
        _valor2 = _valor2.replace('N/A', '').replace('-', '')
    if _valor1 is None:
        _valor1 = ''
    if _valor2 is None:
        _valor2 = ''

    if _valor1 == _valor2:
        return _valor1

    código = kwargs.get('código', False)
    ordem = kwargs.get('ordem', 0)

    if ordem !=0 and not código:
        if ordem == 1:
            return _valor1
        else:
            return _valor2

    if type(_valor1) is str:
        if _valor1 == '':
            return _valor2
    if type(_valor2) is str:
        if _valor2 == '':
            return _valor1

    if código:
        if _valor1 <= 1:
            return _valor2
        else:
            return _valor1
    else:
            return _valor1

def initializer():
#    global instance_name
    instance_name = 'mp_fii'

def generate_urls(_array, _lista_fiis):
    for codigo_ativo in _lista_fiis:
        _array.append('https://fiis.com.br/' + codigo_ativo)

def scrape(url):
    rqt_site = requests.get(url, headers=STR_HEADER)
    html_soup = BeautifulSoup(rqt_site.text, 'lxml')
    prs_data_detalhes_fiis = html_soup.find_all('td')
    print(url)
    # print(url.replace('http://www.fundamentus.com.br/detalhes.php?papel=',''),len(prs_data_detalhes_ativos))

class ativo():

    def __init__(self):
        ativo.codigo_administrador = 0
        ativo.administrador = '' #ok
        ativo.administrador_cnpj = '' #ok
        ativo.administrador_fone = '' #ok
        ativo.administrador_email = '' #ok
        ativo.administrador_site = '' #ok
        ativo.cnpj = '' #ok
        ativo.codigo = '' #ok
        ativo.preco_sobre_vpa = 0 #ok
        ativo.cotas_emitidas = 0
        ativo.data_base = ''
        ativo.data_base_str = ''
        ativo.data_constituicao = ''
        ativo.data_pagamento = ''
        ativo.data_pagamento_str = ''
        ativo.data_registro_cvm = ''
        ativo.dy = 0
        ativo.dy_acum_12m = 0
        ativo.dy_acum_3m = 0
        ativo.dy_acum_6m = 0
        ativo.dy_ano = 0
        ativo.dy_med_12m = 0
        ativo.dy_med_3m = 0
        ativo.dy_med_6m = 0
        ativo.dy_patrimonial = 0
        ativo.faltou_funds_explorer = True
        ativo.faltou_lupa_fiis = True
        ativo.liquidez_diaria = 0
        ativo.cod_tipo_mandato = 1
        #ativo.mandato_txt = ''
        ativo.max_52_semanas = 0
        ativo.min_52_semanas = 0
        ativo.nome = ''
        ativo.nome_pregao = ''
        ativo.notas = ''
        ativo.numero_cotas = 0
        ativo.numero_cotistas = 0
        ativo.numero_estados = 0
        ativo.numero_negocios_mes = 0
        ativo.participacao_ifix = 0
        ativo.patrimonio = 0
        ativo.patrimonio_inicial = 0
        ativo.patrimonio_txt = ''
        ativo.cod_tipo_prazo = 1
        ativo.cod_tipo_investidor = 1
        ativo.quantidade_ativos = 0
        ativo.razao_social = ''
        ativo.rendimento_medio_12m_brl = 0
        ativo.rendimento_medio_12m_perc = 0
        ativo.rentabilidade_acum = 0
        ativo.rentabilidade_patrimonio_acum = 0
        ativo.rentabilidade_patrimonio_periodo = 0
        ativo.rentabilidade_periodo = 0
        ativo.cod_tipo_segmento = 1
        ativo.seguidores_fiis_com_br = 0
        ativo.taxa_administracao = ''
        ativo.taxa_consultoria = ''
        ativo.taxa_gerenciamento = ''
        ativo.taxa_gestao = ''
        ativo.taxa_performance = ''
        ativo.taxas = ''
        ativo.ticker = ''
        ativo.cod_tipo_fundo = 1
        ativo.cod_tipo_segmento2 = 1
        ativo.cod_tipo_anbima = 1
        ativo.cod_tipo_gestao = 1
        ativo.ultima_valorizacao = 0
        ativo.ultimo_preco = 0
        ativo.data_ultimo_preco = 0
        ativo.ultimo_rendimento_brl = 0
        ativo.ultimo_rendimento_perc = 0
        ativo.vacancia_financeira = 0
        ativo.vacancia_fisica = 0
        ativo.valor_inicial_cota = 0
        ativo.valor_patrimonial = 0
        ativo.variacao_12_meses = 0
        ativo.variacao_mes = 0
        ativo.variacao_patrimonial = 0
        ativo.variacao_preco = 0
        ativo.execucao_curta = False
        ativo.filtro_liquidez_minima = False
        ativo.filtro_numero_minimo_ativos = False
        ativo.filtro_dy_acumulado_12_minimo = False
        ativo.filtro_prazo = False
        ativo.filtro_desenvolvimento = False
        ativo.filtro_vacancia_maxima = False
        ativo.filtro_ultimo_dividendo_zero = False
        ativo.filtro_p_sobre_vpa_minimo = False
        ativo.filtro_p_sobre_vpa_maximo = False
        ativo.filtro_variacao_preco_positiva = False
        ativo.filtro_variacao_patrimonial_positiva = False
        ativo.filtro_investidor_qualificado = False
        ativo.filtro_dias_sem_pregao = False
        ativo.filtro = False
        ativo.dias_sem_pregao = 0

class provento(object):

    def __init__(self):
        provento._ticker = ''
        provento.data_base_txt = ''
        provento.data_pgto_txt = ''
        provento.cotacao_base = 0
        provento.valor_provento = 0

    @property
    def ticker(self):
        return self._ticker

    @ticker.setter
    def ticker(self, value):
        self._ticker = value.upper().strip()

    @property
    def data_base(self):
        try:
            __teste = datetime.datetime.strptime(self.data_base_txt, "%d/%m/%Y")
        except:
            __teste = ''
        return __teste

    @property
    def data_base_ano(self):
        try:
            __teste = self.data_base.year
        except:
            __teste = ''
        return __teste

    @property
    def data_base_mes(self):
        try:
            __teste = self.data_base.month
        except:
            __teste = ''
        return __teste

    @property
    def data_base_dia(self):
        try:
            __teste = self.data_base.day
        except:
            __teste = ''
        return __teste

    @property
    def data_pgto(self):
        try:
            __teste = datetime.datetime.strptime(self.data_pgto_txt, "%d/%m/%Y")
        except:
            __teste = ''
        return __teste

    @property
    def data_pgto_ano(self):
        try:
            __teste = self.data_pgto.year
        except:
            __teste = ''
        return __teste

    @property
    def data_pgto_mes(self):
        try:
            __teste = self.data_pgto.month
        except:
            __teste = ''
        return __teste

    @property
    def data_pgto_dia(self):
        try:
            __teste = self.data_pgto.day
        except:
            __teste = ''
        return __teste

    @property
    def dy(self):
        return self.valor_provento / self.cotacao_base
    @property
    def ticker_e_data(self):
        try:
            __teste = self.ticker + datetime.datetime.strftime(self.data_base, "%d%m%Y")
        except:
            __teste = ''
        return __teste

class mes_ptb(object):

    def __init__(self):
        self._mes_ptb = ''
        self.__dic_meses = {
            'JANEIRO': '01',
            'FEVEREIRO': '02',
            'MARÇO': '03',
            'ABRIL': '04',
            'MAIO': '05',
            'JUNHO': '06',
            'JULHO': '07',
            'AGOSTO': '08',
            'SETEMBRO': '09',
            'OUTUBRO': '10',
            'NOVEMBRO': '11',
            'DEZEMBRO': '12'}

    @property
    def mes_ptb(self):
        return self._mes_ptb

    @mes_ptb.setter
    def mes_ptb(self, value):
        self._mes_ptb = value.upper().strip()

    @property
    def mes_num(self):
        try:
            return int(self.__dic_meses[self.mes_ptb])
        except:
            return 0

    @property
    def mes_num_str(self):
        try:
            return self.__dic_meses[self.mes_ptb]
        except:
            return 0

class fii:
    """
    Carrega os dados relevenates dos FIIs
    24/11/19: inicio
    """
    def __init__(self, _lst_fiis, _lst_proventos, _registros, _dict_preferencial):

        dic_meses = {
            'JANEIRO': '01',
            'FEVEREIRO': '02',
            'MARÇO': '03',
            'ABRIL': '04',
            'MAIO': '05',
            'JUNHO': '06',
            'JULHO': '07',
            'AGOSTO': '08',
            'SETEMBRO': '09',
            'OUTUBRO': '10',
            'NOVEMBRO': '11',
            'DEZEMBRO': '12'}

        lst_tempos = []
        lst_tempos.append(('URL', 'OPEN BROWSER', 'GET PAGE', 'LOAD HTML', 'SOUP'))
        url = "https://fiis.com.br/lupa-de-fiis/"
        # Chrome opened in silent mode -------------
        options = webdriver.ChromeOptions()
        #prefs = {"profile.managed_default_content_settings.images": 2}
        #options.add_experimental_option("prefs", prefs)
        chrome_prefs = {}

        # chrome_prefs["profile.default_content_settings.images"] = 2
        #chrome_prefs["profile.managed_default_content_settings.images"] = 2
        chrome_prefs = {'profile.managed_default_content_settings.images': 2}
        '''
        chrome_prefs["profile.default_content_settings"] = {"images": 2}
        chrome_prefs["profile.managed_default_content_settings"] = {"images": 2}
        '''

        options.add_argument("headless")
        # options.experimental_options["prefs"] = chrome_prefs
        options.add_experimental_option("prefs", chrome_prefs)
        # ------------------------------------------
        '''
        try:
            browser = webdriver.Chrome(chrome_options=options,  service_args=['--silent'])
        except Exception as e:
            browser = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options,service_args=['--silent'])
        '''
        lap = datetime.datetime.now()
        browser = webdriver.Chrome(chrome_options=options, service_args=['--silent'], desired_capabilities=caps)
        lap1 = datetime.datetime.now()-lap
        #browser = webdriver.PhantomJS()
        lap = datetime.datetime.now()
        browser.get(url)
        lap2 = datetime.datetime.now()-lap
        time.sleep(3)
        lap = datetime.datetime.now()
        html = browser.page_source
        lap3 = datetime.datetime.now() - lap

        soup = BeautifulSoup(html, "lxml")


        lst_fiis_interno = []
        for id, table in enumerate(soup.find_all("table")):
            if id == 1:

                lap = datetime.datetime.now()
                soup = BeautifulSoup(str(table.contents), "lxml")
                lap4 = datetime.datetime.now() - lap

                lst_tempos.append((url, lap1.total_seconds(), lap2.total_seconds(), lap3.total_seconds(), lap4.total_seconds()))
                estrutura = [[]]
                dic_estrutura = {}
                for td in soup.find_all('td'):
                    # print(td.__str__())
                    estrutura.append(td.string)
                int_contador_itens = 1
                pbar = tqdm(total=len(estrutura)+1, unit=' elmentos')
                while int_contador_itens < len(estrutura):
                    # tem que criar uma nova instância da variável a cada passada
                    # de outro modo, quando faz o append na lista, ao invés de copiar os dados, copia apenas a
                    # referência da variável. quando muda a variável, todos os membros da lista são alterados também,
                    # já que todos os elementos da lista contém referência à variável e não uma cópia dos dados de
                    # cada passada
                    _ativo = ativo()
                    _ativo.ticker = estrutura[int_contador_itens + 0].strip()  # primeira fonte
                    pbar.set_description('Carregando https://fiis.com.br/lupa-de-fiis - ' + _ativo.ticker)
                    dic_estrutura[_ativo.ticker] = len(dic_estrutura)
                    _ativo.codigo = ''.join(i for i in _ativo.ticker if not i.isdigit())
                    if estrutura[int_contador_itens + 1].upper().find('GERAL') >= 0:
                        _ativo.cod_tipo_investidor = codigos_tipo_investidor['GERAL']
                    elif estrutura[int_contador_itens + 1].upper().find('QUALIFICADO') >= 0:
                        _ativo.cod_tipo_investidor = codigos_tipo_investidor['QUALIFICADO']
                    else:
                        _ativo.cod_tipo_investidor = codigos_tipo_investidor['N/A']
                    str_tipo = funcs.clean_text(estrutura[int_contador_itens + 2])
                    if str_tipo.upper().find('HÍBRIDO ') >= 0:
                        str_tipo = str_tipo.upper().replace('HÍBRIDO ', 'HÍBRIDO: ').replace('(','').replace(')','')
                    if str_tipo.upper().find('INDEFINIDO') >= 0:
                        str_tipo = 'INDEFINIDO: INDEFINIDO'
                    # str_tipo_fundo = str_tipo[:str_tipo.find(':')].upper().replace('N/A', 'INDEFINIDO').replace(' (TIJOLO/PAPEL)', '')

                    str_tipo_fundo = str_tipo[:str_tipo.find(':')].upper()

                    try:
                        _ativo.cod_tipo_fundo = codigos_tipo_fundo[str_tipo_fundo]
                    except:
                        codigos_tipo_fundo[str_tipo_fundo] = len(codigos_tipo_fundo)
                        _ativo.cod_tipo_fundo = codigos_tipo_fundo[str_tipo_fundo]
                        #print(str_tipo.upper())
                    str_segmento = str_tipo[(str_tipo.find(':')+2):].upper()
                    try:
                        _ativo.cod_tipo_segmento = codigos_tipo_segmento[str_segmento]
                    except:
                        codigos_tipo_segmento[str_segmento] = len(codigos_tipo_segmento)
                        _ativo.cod_tipo_segmento = codigos_tipo_segmento[str_segmento]
                        #print(str_tipo.upper())
                    #str_nome_administrador = funcs.clean_text(estrutura[int_contador_itens + 3])
                    #try:
                    #    _ativo.codigo_administrador = codigos_administradores[str_nome_administrador]
                    #except:
                    #    codigos_administradores[str_nome_administrador] = len(codigos_administradores)
                    #    _ativo.codigo_administrador = codigos_administradores[str_nome_administrador]

                    #_ativo.administrador = funcs.clean_text(estrutura[int_contador_itens + 3])  # primeira fonte
                    _ativo.ultimo_rendimento_brl = funcs.num_ptb2us(estrutura[int_contador_itens + 4])
                    _ativo.ultimo_rendimento_perc = funcs.num_ptb2us(estrutura[int_contador_itens + 5])
                    _ativo.data_pagamento_str = funcs.clean_text(estrutura[int_contador_itens + 6])
                    try:
                        _ativo.data_pagamento = datetime.datetime.strptime(_ativo.data_pagamento_str,'%d/%m/%y')
                    except ValueError:
                        _ativo.data_pagamento = None
                    _ativo.data_base_str = funcs.clean_text(estrutura[int_contador_itens + 7])
                    try:
                        _ativo.data_base = datetime.datetime.strptime(_ativo.data_base_str,'%d/%m/%y')
                    except ValueError:
                        _ativo.data_base = None
                    _ativo.rendimento_medio_12m_brl = funcs.num_ptb2us(estrutura[int_contador_itens + 8])
                    _ativo.rendimento_medio_12m_perc = funcs.num_ptb2us(estrutura[int_contador_itens + 9])
                    _ativo.valor_patrimonial = funcs.num_ptb2us(estrutura[int_contador_itens + 10])
                    _ativo.preco_sobre_vpa = funcs.num_ptb2us(estrutura[int_contador_itens + 11])
                    _ativo.numero_negocios_mes = funcs.num_ptb2us(estrutura[int_contador_itens + 12])
                    _ativo.participacao_ifix = funcs.num_ptb2us(estrutura[int_contador_itens + 13])/100
                    _ativo.numero_cotistas = funcs.num_ptb2us(estrutura[int_contador_itens + 14])
                    _ativo.patrimonio = funcs.num_ptb2us(estrutura[int_contador_itens + 15])

                    int_contador_itens = int_contador_itens + 16
                    #print(int_contador_itens)
                    lst_fiis_interno.append(_ativo)
                    del _ativo
                    pbar.update(16)
                pbar.update(pbar.total - pbar.n)
                pbar.close()

        # browser.close()
        # browser.quit() # teste

        url = "https://www.fundsexplorer.com.br/ranking"
        # Chrome opened in silent mode -------------
        #options = webdriver.ChromeOptions()
        #prefs = {"profile.managed_default_content_settings.images": 2}
        #options.add_experimental_option("prefs", prefs)
        #options.add_argument("headless")
        # ------------------------------------------
        # browser = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)
        lap = datetime.datetime.now()
        # browser = webdriver.Chrome(chrome_options=options, service_args=['--silent'], desired_capabilities=caps) # teste
        lap1 = datetime.datetime.now() - lap
        lap = datetime.datetime.now()
        #browser = webdriver.PhantomJS()
        browser.get(url)
        lap2 = datetime.datetime.now() - lap
        lap = datetime.datetime.now()
        time.sleep(3)
        html = browser.page_source
        lap3 = datetime.datetime.now() - lap

        soup = BeautifulSoup(html, "lxml")

        for id, table in enumerate(soup.find_all("table")):
            if id == 0:
                lap = datetime.datetime.now()
                soup = BeautifulSoup(str(table.contents), "lxml")
                lap4 = datetime.datetime.now() - lap
                lst_tempos.append((url, lap1.total_seconds(), lap2.total_seconds(), lap3.total_seconds(), lap4.total_seconds()))
                estrutura = [[]]
                try:
                    dic_estrutura
                except NameError:
                    dic_estrutura = {}
                for td in soup.find_all('td'):
                    # print(td.__str__())
                    estrutura.append(td.string)
                int_contador_itens = 1
                pbar = tqdm(total=len(estrutura) + 1, unit=' elementos')
                while int_contador_itens < len(estrutura):
                    try:
                        int_pointer = dic_estrutura.get(estrutura[int_contador_itens + 0].strip())
                        #print(estrutura[int_contador_itens + 0].strip())
                        if estrutura[int_contador_itens + 0].strip() == 'ARRI11':
                            #print(estrutura[int_contador_itens + 0].strip())
                            pass
                        pbar.set_description('Carregando https://www.fundsexplorer.com.br/ranking - ' + estrutura[int_contador_itens + 0].strip())
                        try:
                            lst_fiis_interno[int_pointer].cod_tipo_segmento2 = codigos_tipo_segmento[funcs.clean_text(estrutura[int_contador_itens + 1]).upper()] # primeira fonte
                        except:
                            lst_fiis_interno[int_pointer].cod_tipo_segmento2 = codigos_tipo_segmento['INDEFINIDO'] # primeira fonte
                        lst_fiis_interno[int_pointer].ultimo_preco = funcs.num_ptb2us(estrutura[int_contador_itens + 2]) # primeira fonte
                        lst_fiis_interno[int_pointer].liquidez_diaria = funcs.num_ptb2us(estrutura[int_contador_itens + 3]) # primeira fonte
                        lst_fiis_interno[int_pointer].dy_acum_3m = funcs.num_ptb2us(estrutura[int_contador_itens + 6])  # primeira fonte
                        lst_fiis_interno[int_pointer].dy_acum_6m = funcs.num_ptb2us(estrutura[int_contador_itens + 7]) # primeira fonte
                        lst_fiis_interno[int_pointer].dy_acum_12m = funcs.num_ptb2us(estrutura[int_contador_itens + 8]) # primeira fonte
                        lst_fiis_interno[int_pointer].dy_med_3m = funcs.num_ptb2us(estrutura[int_contador_itens + 9]) # primeira fonte
                        lst_fiis_interno[int_pointer].dy_med_6m = funcs.num_ptb2us(estrutura[int_contador_itens + 10]) # primeira fonte
                        lst_fiis_interno[int_pointer].dy_med_12m =funcs.num_ptb2us( estrutura[int_contador_itens + 11]) # primeira fonte
                        lst_fiis_interno[int_pointer].dy_ano = funcs.num_ptb2us(estrutura[int_contador_itens + 12]) # primeira fonte
                        lst_fiis_interno[int_pointer].variacao_preco = funcs.num_ptb2us(estrutura[int_contador_itens + 13]) # primeira fonte
                        lst_fiis_interno[int_pointer].rentabilidade_periodo = funcs.num_ptb2us(estrutura[int_contador_itens + 14]) # primeira fonte
                        lst_fiis_interno[int_pointer].rentabilidade_acum = funcs.num_ptb2us(estrutura[int_contador_itens + 15]) # primeira fonte
                        lst_fiis_interno[int_pointer].dy_patrimonial = funcs.num_ptb2us(estrutura[int_contador_itens + 19]) # primeira fonte
                        lst_fiis_interno[int_pointer].variacao_patrimonial = funcs.num_ptb2us(estrutura[int_contador_itens + 20]) # primeira fonte
                        lst_fiis_interno[int_pointer].rentabilidade_patrimonio_periodo = funcs.num_ptb2us(estrutura[int_contador_itens + 21]) # primeira fonte
                        lst_fiis_interno[int_pointer].rentabilidade_patrimonio_acum = funcs.num_ptb2us(estrutura[int_contador_itens + 22]) # primeira fonte
                        try:
                            lst_fiis_interno[int_pointer].vacancia_fisica = funcs.num_ptb2us(estrutura[int_contador_itens + 23]) # primeira fonte
                        except:
                            pass
                        try:
                            lst_fiis_interno[int_pointer].vacancia_financeira = funcs.num_ptb2us(estrutura[int_contador_itens + 24]) # primeira fonte
                        except:
                            pass
                        lst_fiis_interno[int_pointer].quantidade_ativos = funcs.num_ptb2us(estrutura[int_contador_itens + 25].strip()) # primeira fonte
                        lst_fiis_interno[int_pointer].faltou_funds_explorer = False
                    except:
                        _ativo = ativo()
                        _ativo.ticker = estrutura[int_contador_itens + 0].strip()
                        if _ativo.ticker == 'ANCR11B':
                            pass
                        pbar.set_description('Carregando https://www.fundsexplorer.com.br/ranking - ' + _ativo.ticker)
                        _ativo.codigo = ''.join(i for i in _ativo.ticker if not i.isdigit())
                        dic_estrutura[_ativo.ticker] = len(dic_estrutura)
                        _ativo.faltou_faltou_lupa_fiis = True
                        _ativo.cod_tipo_segmento2 = codigos_tipo_segmento[funcs.clean_text(estrutura[int_contador_itens + 1]).upper()]
                        _ativo.ultimo_preco = funcs.num_ptb2us([int_contador_itens + 2])
                        _ativo.liquidez_diaria = funcs.num_ptb2us(estrutura[int_contador_itens + 3])
                        _ativo.ultimo_rendimento_brl = funcs.num_ptb2us(estrutura[int_contador_itens + 4])
                        _ativo.ultimo_rendimento_perc = funcs.num_ptb2us(estrutura[int_contador_itens + 5])
                        _ativo.dy_acum_3m = funcs.num_ptb2us(estrutura[int_contador_itens + 6])
                        _ativo.dy_acum_6m = funcs.num_ptb2us(estrutura[int_contador_itens + 7])
                        _ativo.dy_acum_12m = funcs.num_ptb2us(estrutura[int_contador_itens + 8])
                        _ativo.dy_med_3m = funcs.num_ptb2us(estrutura[int_contador_itens + 9])
                        _ativo.dy_med_6m = funcs.num_ptb2us(estrutura[int_contador_itens + 10])
                        _ativo.dy_med_12m = funcs.num_ptb2us(estrutura[int_contador_itens + 11])
                        _ativo.dy_ano = funcs.num_ptb2us(estrutura[int_contador_itens + 12])
                        _ativo.variacao_preco = funcs.num_ptb2us(estrutura[int_contador_itens + 13])
                        _ativo.rentabilidade_periodo = funcs.num_ptb2us(estrutura[int_contador_itens + 14])
                        _ativo.rentabilidade_acum = funcs.num_ptb2us(estrutura[int_contador_itens + 15])
                        _ativo.patrimonio = funcs.num_ptb2us(estrutura[int_contador_itens + 16])
                        _ativo.valor_patrimonial = funcs.num_ptb2us(estrutura[int_contador_itens + 17])
                        _ativo.preco_sobre_vpa = funcs.num_ptb2us(estrutura[int_contador_itens + 18])
                        _ativo.dy_patrimonial = funcs.num_ptb2us(estrutura[int_contador_itens + 19])
                        _ativo.variacao_patrimonial = funcs.num_ptb2us(estrutura[int_contador_itens + 20])
                        _ativo.rentabilidade_patrimonio_periodo = funcs.num_ptb2us(estrutura[int_contador_itens + 21])
                        _ativo.rentabilidade_patrimonio_acum = funcs.num_ptb2us(estrutura[int_contador_itens + 22])
                        try:
                            _ativo.vacancia_fisica = funcs.num_ptb2us(estrutura[int_contador_itens + 23])
                        except:
                            pass
                        try:
                            _ativo.vacancia_financeira = funcs.num_ptb2us(estrutura[int_contador_itens + 24])
                        except:
                            pass
                        _ativo.quantidade_ativos = funcs.num_ptb2us(estrutura[int_contador_itens + 25])
                        lst_fiis_interno.append(_ativo)

                    int_contador_itens = int_contador_itens + 26
                    pbar.update(26)
                pbar.update(pbar.total - pbar.n)
                pbar.close()

        # browser.close()
        # browser.quit() # teste
        try:
            _registros = _registros.upper()
        except:
            pass
        if _registros is None or _registros == 'ALL':
            _registros = len(dic_estrutura)
        elif type(_registros) is not int:
            dic_estrutura = {_registros: dic_estrutura[_registros]}
            _registros = 1

        if test_partial <= 1:
            start = datetime.datetime.now()
            lap = datetime.datetime.now()
            pbar = tqdm(total=_registros, unit='ativo')

            #for ticker in take(_registros, dic_estrutura.keys()):
            for ticker in {k: dic_estrutura[k] for k in list(dic_estrutura)[:_registros]}:
                url = 'https://fiis.com.br/' + ticker
                pbar.set_description(url)
                #url = 'file:///C:/Users/coliveira/OneDrive/Coding/Python/FII/ANCR11B%20-%20Ancar%20IC%20-%20Fundo%20de%20Investimento%20Imobili%C3%A1rio.html'

                ''' 
                options = webdriver.ChromeOptions()
                options.add_argument("headless")
                # ------------------------------------------
                try:
                    browser = webdriver.Chrome(chrome_options=options, service_args=['--silent'])
                except Exception as e:
                    browser = webdriver.Chrome(ChromeDriverManager().install(), options=options, service_args=['--silent'])
    
                browser.get(url)
                time.sleep(3)
                html = browser.page_source
                '''
                lap = datetime.datetime.now()
                # browser = webdriver.Chrome(chrome_options=options, service_args=['--silent'], desired_capabilities=caps) # teste
                lap1 = datetime.datetime.now() - lap
                lap = datetime.datetime.now()
                # browser = webdriver.PhantomJS()
                browser.get(url)
                lap2 = datetime.datetime.now() - lap
                lap = datetime.datetime.now()
                # time.sleep(3)
                html = browser.page_source
                lap3 = datetime.datetime.now() - lap
                lap = datetime.datetime.now()
                soup = BeautifulSoup(html, "lxml")
                lap4 = datetime.datetime.now() - lap
                lst_tempos.append((url, lap1.total_seconds(), lap2.total_seconds(), lap3.total_seconds(), lap4.total_seconds()))

                estrutura = [[]]
                dic_estrutura_dinamica = {}
                count_dic = 0
                for td in soup.find_all('span'):
                    # print(td.__str__())
                    try:
                        _temp = parse_parent_content(td.parent.contents, td.string)
                    except Exception as e:
                        print(e)
                    str_text_to_append = ''
                    if _temp == '':
                        str_text_to_append = td.string
                    else:
                        str_text_to_append = funcs.clean_text(_temp)
                    str_text_to_append = ('' if str_text_to_append is None else str_text_to_append)  # se for None, coloca ''
                    estrutura.append(str_text_to_append)
                    dic_estrutura_dinamica[str_text_to_append.upper()] = count_dic
                    count_dic += 1
                    # print(td.string, 'len parent contents = ', len(td.parent.contents), 'parent contents= ', td.parent.contents)

                int_contador_itens = 1
                #while int_contador_itens < len(estrutura):
                #int_pointer = dic_estrutura.get(estrutura[int_contador_itens + 5].strip())
                int_pointer = dic_estrutura.get(ticker)


                lst_fiis_interno[int_pointer].seguidores_fiis_com_br = funcs.num_ptb2us(estrutura[dic_estrutura_dinamica['SEGUIR']+2]) # primeira fonte
                lst_fiis_interno[int_pointer].nome = funcs.clean_text(estrutura[dic_estrutura_dinamica['SEGUIR']+4]) # primeira fonte
                administrador_nome = preferencial(lst_fiis_interno[int_pointer].administrador, funcs.clean_text(estrutura[dic_estrutura_dinamica['ADMINISTRADOR']+2])).upper()
                administrador_cnpj = funcs.formata_cnpj(funcs.clean_text(estrutura[dic_estrutura_dinamica['ADMINISTRADOR'] + 3]))
                administrador_fone = funcs.formata_fone(funcs.clean_text(estrutura[dic_estrutura_dinamica['TELEFONE']+2]))
                administrador_email = funcs.formata_email(funcs.clean_text(estrutura[dic_estrutura_dinamica['EMAIL']+2])).upper()
                administrador_site = funcs.formata_url(funcs.clean_text(estrutura[dic_estrutura_dinamica['SITE']+2])).upper()
                try:
                    lst_fiis_interno[int_pointer].codigo_administrador = codigos_administradores[administrador_cnpj]
                except:
                    codigos_administradores[administrador_cnpj] = len(codigos_administradores)
                    dados_administradores.append([administrador_nome, administrador_cnpj, administrador_fone, administrador_email, administrador_site])
                    lst_fiis_interno[int_pointer].codigo_administrador = codigos_administradores[administrador_cnpj]

                lst_fiis_interno[int_pointer].administrador = administrador_nome

                #lst_fiis_interno[int_pointer].administrador = preferencial(lst_fiis_interno[int_pointer].administrador, funcs.clean_text(estrutura[dic_estrutura_dinamica['ADMINISTRADOR']+2]))
                #lst_fiis_interno[int_pointer].administrador_cnpj = funcs.formata_cnpj(funcs.clean_text(estrutura[dic_estrutura_dinamica['ADMINISTRADOR']+3]))
                #lst_fiis_interno[int_pointer].administrador_fone  = funcs.formata_fone(funcs.clean_text(estrutura[dic_estrutura_dinamica['TELEFONE']+2]))
                #lst_fiis_interno[int_pointer].administrador_email  = funcs.formata_email(funcs.clean_text(estrutura[dic_estrutura_dinamica['EMAIL']+2]))
                #lst_fiis_interno[int_pointer].administrador_site  = funcs.formata_url(funcs.clean_text(estrutura[dic_estrutura_dinamica['SITE']+2]))
                lst_fiis_interno[int_pointer].nome_pregao  = funcs.clean_text(estrutura[dic_estrutura_dinamica['NOME NO PREGÃO']+2]) # primeira fonte
                str_tipo = funcs.clean_text(estrutura[dic_estrutura_dinamica['TIPO DO FII']+2])
                if str_tipo.upper().find('HÍBRIDO') >= 0:
                    str_tipo = str_tipo.upper().replace('HÍBRIDO ', 'HÍBRIDO: ')
                if str_tipo.upper().find('INDEFINIDO') >= 0:
                    str_tipo = 'INDEFINIDO: INDETERMINADO'
                #str_tipo_fundo = str_tipo[:str_tipo.find(':')].upper().replace('N/A', 'INDEFINIDO').replace(' (TIJOLO/PAPEL)', '')
                str_tipo_fundo = str_tipo[:str_tipo.find(':')].upper()
                try:
                    lst_fiis_interno[int_pointer].cod_tipo_fundo = preferencial(lst_fiis_interno[int_pointer].cod_tipo_fundo , codigos_tipo_fundo[str_tipo_fundo], ordem = _dict_preferencial['TIPO DE FUNDO'])
                except:
                    codigos_tipo_fundo[str_tipo_fundo] = len(codigos_tipo_fundo)
                    lst_fiis_interno[int_pointer].cod_tipo_fundo = preferencial(lst_fiis_interno[int_pointer].cod_tipo_fundo, codigos_tipo_fundo[str_tipo_fundo], ordem = _dict_preferencial['TIPO DE FUNDO'])
                str_segmento = str_tipo[(str_tipo.find(':') + 2):].upper()
                try:
                    lst_fiis_interno[int_pointer].cod_tipo_segmento = preferencial(lst_fiis_interno[int_pointer].cod_tipo_segmento, codigos_tipo_segmento[str_segmento], código = True, ordem = _dict_preferencial["TIPO DE SEGMENTO"])
                except:
                    codigos_tipo_segmento[str_segmento] = len(codigos_tipo_segmento)
                    lst_fiis_interno[int_pointer].cod_tipo_segmento = preferencial(lst_fiis_interno[int_pointer].cod_tipo_segmento, codigos_tipo_segmento[str_segmento], código = True, ordem = _dict_preferencial["TIPO DE SEGMENTO"])
                str_tipo_anbima = funcs.clean_text(estrutura[dic_estrutura_dinamica['TIPO ANBIMA']+2]).upper().replace('VALORE ', 'VALORES ')
                if str_tipo_anbima.strip() == '':
                    str_tipo_anbima = 'INDEFINIDO'
                try:
                    lst_fiis_interno[int_pointer].cod_tipo_anbima  = codigos_tipo_anbima[str_tipo_anbima]
                except:
                    codigos_tipo_anbima[str_tipo_anbima] = len(codigos_tipo_anbima)
                    lst_fiis_interno[int_pointer].cod_tipo_anbima = codigos_tipo_anbima[str_tipo_anbima]
                    #print(funcs.clean_text(estrutura[dic_estrutura_dinamica['TIPO ANBIMA']+2]).upper())
                str_tipo_anbima = funcs.find_keys_by_val(codigos_tipo_anbima, lst_fiis_interno[int_pointer].cod_tipo_anbima)
                if str_tipo_anbima.find('ATIVA') >= 0:
                    lst_fiis_interno[int_pointer].cod_tipo_gestao = codigos_tipo_gestao['ATIVA']
                elif str_tipo_anbima.find('PASSIVA') >= 0:
                    lst_fiis_interno[int_pointer].cod_tipo_gestao = codigos_tipo_gestao['PASSIVA']
                else:
                    lst_fiis_interno[int_pointer].cod_tipo_gestao = codigos_tipo_gestao['N/A']
                lst_fiis_interno[int_pointer].data_registro_cvm  = funcs.clean_text(estrutura[dic_estrutura_dinamica['REGISTRO CVM']+2])
                lst_fiis_interno[int_pointer].numero_cotas  = funcs.num_ptb2us(estrutura[dic_estrutura_dinamica['NÚMERO DE COTAS']+2])
                lst_fiis_interno[int_pointer].numero_cotistas  = preferencial(lst_fiis_interno[int_pointer].numero_cotistas,funcs.num_ptb2us(estrutura[dic_estrutura_dinamica['NÚMERO DE COTISTAS']+2]))
                lst_fiis_interno[int_pointer].cnpj  = funcs.formata_cnpj(funcs.clean_text(estrutura[dic_estrutura_dinamica['CNPJ']+2]))
                lst_fiis_interno[int_pointer].notas  = funcs.clean_text(estrutura[int_contador_itens + 31])
                lst_fiis_interno[int_pointer].taxas = funcs.clean_text(estrutura[dic_estrutura_dinamica['CNPJ']+5])
                lst_fiis_interno[int_pointer].dy = funcs.num_ptb2us(estrutura[dic_estrutura_dinamica['DIVIDEND YIELD']])
                lst_fiis_interno[int_pointer].ultimo_rendimento_brl  = preferencial(lst_fiis_interno[int_pointer].ultimo_rendimento_brl,funcs.num_ptb2us(estrutura[dic_estrutura_dinamica['ÚLTIMO RENDIMENTO']]))
                lst_fiis_interno[int_pointer].patrimonio_txt  = funcs.clean_text(estrutura[dic_estrutura_dinamica['PATRIMÔNIO LÍQUIDO']])
                lst_fiis_interno[int_pointer].valor_patrimonial  = preferencial(lst_fiis_interno[int_pointer].valor_patrimonial,funcs.num_ptb2us(estrutura[dic_estrutura_dinamica['VALOR PATRIMONIAL POR COTA']]))
                lst_fiis_interno[int_pointer].ultimo_preco  = preferencial(lst_fiis_interno[int_pointer].ultimo_preco, funcs.num_ptb2us(estrutura[dic_estrutura_dinamica['MÍN. 52 SEMANAS']-4]))
                lst_fiis_interno[int_pointer].ultima_valorizacao  = funcs.num_ptb2us(estrutura[dic_estrutura_dinamica['MÍN. 52 SEMANAS']-3])

                lst_fiis_interno[int_pointer].min_52_semanas  = funcs.num_ptb2us(estrutura[dic_estrutura_dinamica['MÍN. 52 SEMANAS']])
                lst_fiis_interno[int_pointer].max_52_semanas  = funcs.num_ptb2us(estrutura[dic_estrutura_dinamica['MÁX. 52 SEMANAS']])
                lst_fiis_interno[int_pointer].variacao_12_meses  = funcs.num_ptb2us(estrutura[dic_estrutura_dinamica['VALORIZAÇÃO (12 MESES)']-1]) / 100
                lst_fiis_interno[int_pointer].execucao_curta = True

                # print('Ativo: %s, Lap: %s, Total: %s' % (lst_fiis_interno[int_pointer].ticker, str(datetime.datetime.now()-lap), str(datetime.datetime.now()-start)))
                # browser.close()
                # browser.quit() # teste
                lap = datetime.datetime.now()
                pbar.update(1)
            pbar.close()

        if test_partial <=2:
            start = datetime.datetime.now()
            lap = datetime.datetime.now()
            pbar = tqdm(total=_registros, unit='ativo')
            #for ticker in take(_registros, dic_estrutura.keys()):
            for ticker in {k: dic_estrutura[k] for k in list(dic_estrutura)[:_registros]}:
                url = 'https://www.fundsexplorer.com.br/funds/' + ticker
                pbar.set_description(url)
                # url = 'file:///C:/Users/coliveira/OneDrive/Coding/Python/FII/ANCR11B%20-%20Ancar%20IC%20-%20Fundo%20de%20Investimento%20Imobili%C3%A1rio.html'

                ''' 
                options = webdriver.ChromeOptions()
                options.add_argument("headless")
                # ------------------------------------------
                try:
                    browser = webdriver.Chrome(chrome_options=options, service_args=['--silent'])
                except Exception as e:
                    browser = webdriver.Chrome(ChromeDriverManager().install(), options=options, service_args=['--silent'])
    
                browser.get(url)
                time.sleep(3)
                html = browser.page_source
                '''
                lap = datetime.datetime.now()
                # browser = webdriver.Chrome(chrome_options=options, service_args=['--silent'], desired_capabilities=caps) # teste
                lap1 = datetime.datetime.now() - lap
                lap = datetime.datetime.now()
                # browser = webdriver.PhantomJS()
                browser.get(url)
                lap2 = datetime.datetime.now() - lap
                lap = datetime.datetime.now()
                # time.sleep(3)
                html = browser.page_source
                lap3 = datetime.datetime.now() - lap
                lap = datetime.datetime.now()
                soup = BeautifulSoup(html, "lxml")
                lap4 = datetime.datetime.now() - lap
                lst_tempos.append((url, lap1.total_seconds(), lap2.total_seconds(), lap3.total_seconds(), lap4.total_seconds()))

                estrutura = [[]]
                # as páginas de detalhes do FundsExplorer não tem a mesma estrutura
                # foi necessário criar um dicionario com a estrutura de cada página para poder achar a posição dos
                # campos para cada uma
                dic_estrutura_dinamica = {}
                count_dic = 0
                for td in soup.find_all('span'):
                    # print(td.__str__())
                    try:
                        _temp = parse_parent_content(td.parent.contents, td.string)
                    except TypeError:
                        pass
                    str_text_to_append = ''
                    if _temp == '':
                        str_text_to_append = td.string
                    else:
                        str_text_to_append = funcs.clean_text(_temp)
                    str_text_to_append = ('' if str_text_to_append is None else str_text_to_append)  # se for None, coloca ''
                    estrutura.append(str_text_to_append)
                    dic_estrutura_dinamica[str_text_to_append.upper()] = count_dic
                    count_dic += 1
                    # print(td.string, 'len parent contents = ', len(td.parent.contents), 'parent contents= ', td.parent.contents)

                int_contador_itens = 1
                # while int_contador_itens < len(estrutura):
                # int_pointer = dic_estrutura.get(estrutura[int_contador_itens + 5].strip())
                int_pointer = dic_estrutura.get(ticker)
                #if ticker == 'CTXT11':
                #    print(ticker)
                if len(estrutura) == 1:
                    lst_fiis_interno[int_pointer].execucao_curta = True
                    continue
                if estrutura[1] != 'Ops! Algo está errado...':
                    lst_fiis_interno[int_pointer].ultimo_preco = preferencial(funcs.num_ptb2us(estrutura[dic_estrutura_dinamica['EBOOK GRATUITO']+7]), lst_fiis_interno[int_pointer].ultimo_preco)
                    lst_fiis_interno[int_pointer].ultima_valorizacao = preferencial(funcs.num_ptb2us(estrutura[dic_estrutura_dinamica['EBOOK GRATUITO']+8]), lst_fiis_interno[int_pointer].ultima_valorizacao)
                    lst_fiis_interno[int_pointer].liquidez_diaria = preferencial(funcs.num_ptb2us(estrutura[dic_estrutura_dinamica['LIQUIDEZ DIÁRIA']+2]), lst_fiis_interno[int_pointer].liquidez_diaria)
                    lst_fiis_interno[int_pointer].ultimo_rendimento_brl = preferencial(funcs.num_ptb2us(estrutura[dic_estrutura_dinamica['ÚLTIMO RENDIMENTO']+2]), lst_fiis_interno[int_pointer].ultimo_rendimento_brl)
                    lst_fiis_interno[int_pointer].dy = preferencial(funcs.num_ptb2us(estrutura[dic_estrutura_dinamica['DIVIDEND YIELD']+2]), lst_fiis_interno[int_pointer].dy)
                    lst_fiis_interno[int_pointer].patrimonio_txt = preferencial(funcs.clean_text(estrutura[dic_estrutura_dinamica['PATRIMÔNIO LÍQUIDO']+2]), lst_fiis_interno[int_pointer].patrimonio_txt)
                    lst_fiis_interno[int_pointer].valor_patrimonial = preferencial(funcs.num_ptb2us(estrutura[dic_estrutura_dinamica['VALOR PATRIMONIAL']+2]), lst_fiis_interno[int_pointer].valor_patrimonial)
                    lst_fiis_interno[int_pointer].variacao_mes = funcs.num_ptb2us(estrutura[dic_estrutura_dinamica['RENTAB. NO MÊS']+2])
                    lst_fiis_interno[int_pointer].preco_sobre_vpa = preferencial(funcs.num_ptb2us(estrutura[dic_estrutura_dinamica['P/VP']+2]), lst_fiis_interno[int_pointer].preco_sobre_vpa)

                    lst_fiis_interno[int_pointer].razao_social = funcs.clean_text(estrutura[dic_estrutura_dinamica['RAZÃO SOCIAL']+2])

                    str_data_constituicao = funcs.clean_text(estrutura[dic_estrutura_dinamica['DATA DA CONSTITUIÇÃO DO FUNDO']+2]).upper()
                    try:
                        str_mes_data_constituicao = str_data_constituicao[str_data_constituicao.find(' DE ')+4:str_data_constituicao.rfind(' DE ')]
                        str_data_constituicao = str_data_constituicao.replace(' DE ' + str_mes_data_constituicao + ' DE ', '/' + dic_meses[str_mes_data_constituicao]+'/')
                    except:
                        str_data_constituicao = ''
                    lst_fiis_interno[int_pointer].data_constituicao = str_data_constituicao
                    lst_fiis_interno[int_pointer].cotas_emitidas = funcs.num_ptb2us(estrutura[dic_estrutura_dinamica['COTAS EMITIDAS']+2])
                    lst_fiis_interno[int_pointer].patrimonio_inicial = funcs.num_ptb2us(estrutura[dic_estrutura_dinamica['PATRIMÔNIO INICIAL']+2])
                    lst_fiis_interno[int_pointer].valor_inicial_cota = funcs.num_ptb2us(estrutura[dic_estrutura_dinamica['VALOR INICIAL DA COTA']+2])
                    if estrutura[dic_estrutura_dinamica['TIPO DE GESTÃO']+2].upper().find('ATIVA') >= 0:
                        lst_fiis_interno[int_pointer].cod_tipo_gestao = preferencial(codigos_tipo_gestao['ATIVA'], lst_fiis_interno[int_pointer].cod_tipo_gestao, código=True)
                    elif estrutura[dic_estrutura_dinamica['TIPO DE GESTÃO']+2].upper().find('PASSIVA') >= 0:
                        lst_fiis_interno[int_pointer].cod_tipo_gestao = preferencial(codigos_tipo_gestao['PASSIVA'], lst_fiis_interno[int_pointer].cod_tipo_gestao, código=True)
                    else:
                        lst_fiis_interno[int_pointer].cod_tipo_gestao = preferencial('N/A', lst_fiis_interno[int_pointer].cod_tipo_gestao, código=True)
                    lst_fiis_interno[int_pointer].taxa_performance = funcs.clean_text(estrutura[dic_estrutura_dinamica['TAXA DE PERFORMANCE']+2])
                    lst_fiis_interno[int_pointer].taxa_gestao = funcs.clean_text(estrutura[dic_estrutura_dinamica['TAXA DE GESTÃO']+2])
                    lst_fiis_interno[int_pointer].cnpj = funcs.formata_cnpj(preferencial(funcs.clean_text(estrutura[dic_estrutura_dinamica['CNPJ']+2]), lst_fiis_interno[int_pointer].cnpj))
                    if estrutura[dic_estrutura_dinamica['PÚBLICO-ALVO']+2].upper().find('GERAL') >= 0:
                        lst_fiis_interno[int_pointer].cod_tipo_investidor = preferencial(codigos_tipo_investidor['GERAL'], lst_fiis_interno[int_pointer].cod_tipo_investidor, código=True)
                    elif estrutura[dic_estrutura_dinamica['PÚBLICO-ALVO']+2].upper().find('QUALIFICADO') >= 0:
                        lst_fiis_interno[int_pointer].cod_tipo_investidor = preferencial(codigos_tipo_investidor['QUALIFICADO'], lst_fiis_interno[int_pointer].cod_tipo_investidor, código=True)
                    else:
                        lst_fiis_interno[int_pointer].cod_tipo_investidor = preferencial(codigos_tipo_investidor['N/A'], lst_fiis_interno[int_pointer].cod_tipo_investidor, código=True)
                    str_mandato = funcs.clean_text(estrutura[dic_estrutura_dinamica['MANDATO']+2]).upper()
                    if str_mandato == 'N/A':
                        str_tipo_anbima = funcs.find_keys_by_val(codigos_tipo_anbima, lst_fiis_interno[int_pointer].cod_tipo_anbima)
                        if str_tipo_anbima.find('DESENVOLVIMENTO PARA RENDA') >= 0:
                            str_mandato = 'DESENVOLVIMENTO PARA RENDA'
                        elif str_tipo_anbima.find('DESENVOLVIMENTO PARA VENDA') >= 0:
                            str_mandato = 'DESENVOLVIMENTO PARA VENDA'
                        elif str_tipo_anbima.find('RENDA') >= 0:
                            str_mandato = 'RENDA'
                        elif str_tipo_anbima.find('TÍTULOS E VALORES MOBILIÁRIOS') >= 0:
                            str_mandato = 'TÍTULOS E VALORES MOBILIÁRIOS'
                        elif str_tipo_anbima.find('HÍBRIDO') >= 0:
                            str_mandato = 'HÍBRIDO'
                    try:
                        lst_fiis_interno[int_pointer].cod_tipo_mandato = codigos_tipo_mandato[str_mandato]
                    except KeyError:
                        codigos_tipo_mandato[str_mandato] = len(codigos_tipo_mandato)
                        lst_fiis_interno[int_pointer].cod_tipo_mandato = codigos_tipo_mandato[str_mandato]
                        #lst_fiis_interno[int_pointer].mandato_txt = str_mandato
                    str_segmento = funcs.clean_text(estrutura[dic_estrutura_dinamica['SEGMENTO']+2]).upper()
                    try:
                        lst_fiis_interno[int_pointer].cod_tipo_segmento = preferencial(lst_fiis_interno[int_pointer].cod_tipo_segmento, codigos_tipo_segmento[str_segmento], código = True, codigo = True, ordem = _dict_preferencial["TIPO DE SEGMENTO"])
                    except:
                        codigos_tipo_segmento[str_segmento] = len(codigos_tipo_segmento)
                        lst_fiis_interno[int_pointer].cod_tipo_segmento = preferencial(lst_fiis_interno[int_pointer].cod_tipo_segmento, codigos_tipo_segmento[str_segmento], código = True, codigo = True, ordem = _dict_preferencial["TIPO DE SEGMENTO"])
                    if estrutura[dic_estrutura_dinamica['PRAZO DE DURAÇÃO']+2].upper().find('INDETERMINADO') >= 0:
                        lst_fiis_interno[int_pointer].cod_tipo_prazo = codigos_tipo_prazo['INDETERMINADO']
                    elif estrutura[dic_estrutura_dinamica['PRAZO DE DURAÇÃO'] + 2].upper().find('DETERMINADO') >= 0:
                        lst_fiis_interno[int_pointer].cod_tipo_prazo = codigos_tipo_prazo['DETERMINADO']
                    else:
                        lst_fiis_interno[int_pointer].cod_tipo_prazo = codigos_tipo_prazo['N/A']
                    lst_fiis_interno[int_pointer].taxa_administracao = funcs.clean_text(estrutura[dic_estrutura_dinamica['TAXA DE ADMINISTRAÇÃO']+2])
                    lst_fiis_interno[int_pointer].taxa_gerenciamento = funcs.clean_text(estrutura[dic_estrutura_dinamica['TAXA DE GERENCIAMENTO']+2])
                    lst_fiis_interno[int_pointer].taxa_consultoria = funcs.clean_text(estrutura[dic_estrutura_dinamica['TAXA DE CONSULTORIA']+2])
                    try:
                        lst_fiis_interno[int_pointer].quantidade_ativos = preferencial(funcs.num_ptb2us(estrutura[dic_estrutura_dinamica['ÁREA BRUTA LOCÁVEL POR ESTADO'] + 2].replace(' ativo', '').replace('s', '')), lst_fiis_interno[int_pointer].quantidade_ativos)
                    except:
                        pass
                    try:
                        lst_fiis_interno[int_pointer].numero_estados = funcs.num_ptb2us(estrutura[dic_estrutura_dinamica['ÁREA BRUTA LOCÁVEL POR ESTADO']+2+1].replace(' estado','').replace('s',''))
                    except:
                        pass
                    lst_fiis_interno[int_pointer].execucao_curta = True
                '''  
                print('2 passada, Ativo: %s, Lap: %s, Total: %s' % (
                lst_fiis_interno[int_pointer].ticker, str(datetime.datetime.now() - lap), str(datetime.datetime.now() - start)))
                '''
                # browser.close()
                # browser.quit() # teste
                lap = datetime.datetime.now()
                pbar.update(1)
            pbar.close()

        browser.close()
        browser.quit() # teste

        '''
        all_urls = list()

        generate_urls(all_urls, dic_estrutura.keys())

        #start_time = datetime.now()
        # for url in tqdm(all_urls):
        #    scrape(url)
        # print('In Line: '+str((datetime.now()-start_time)))
        # exit()

        cpus = cpu_count()
        # pbar = tqdm(all_urls)
        #if __name__ == '__main__':
        global instance_name
        if instance_name == 'fii':
            # print('Starting parallel processing')
            p = Pool(cpus,initializer=initializer())
            try:
                p.map(scrape, tqdm(all_urls, desc='Processamento paralelo', leave=True))
            except Exception as e:
                print(e)
            p.terminate()
            p.join()
            #print('Tempo total: ' + str((datetime.now() - start_time)))

        '''

        #for line in lst_tempos:
        #    print(line)
        _ultimo_pregao_ibov = ultimo_pregao('ibov')[0]
        pbar = tqdm(total=len(lst_fiis_interno) + 1, unit=' ativos')
        for item in lst_fiis_interno:
            if item.execucao_curta == True:
                pbar.set_description('Carregando dias sem pregao - ' + item.ticker)
                try:
                    _ultimo_pregao_ativo = ultimo_pregao(item.ticker)[0]
                    item.dias_sem_pregao = (_ultimo_pregao_ibov - _ultimo_pregao_ativo).days
                except:
                    item.dias_sem_pregao = 9999
                _lst_fiis.append(item)
                pbar.update(1)

        #_lst_fiis.append(lst_fiis_interno)
