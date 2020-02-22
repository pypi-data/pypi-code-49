import datetime as _datetime
import zeep as _zeep
import xml.etree.ElementTree as _ET

class UltimaCotacaoDolar:

    # Documentação de apoio:
    #
    #   http://catalogo.governoeletronico.gov.br/arquivos/Documentos/WS_SGS_BCB.pdf - descrição do uso do Webservice
    #   http://python-zeep.readthedocs.io/en/master/ - zeep, biblioteca para trabalhar com webservices
    #   http://blog.tiagocrizanto.com/configuracoes-do-webservice-do-banco-central-cotacoes-diversas/

    def __init__(self):
        STR_WSDL='https://www3.bcb.gov.br/sgspub/JSP/sgsgeral/FachadaWSSGS.wsdl'
        # 07/11/19: nome da variável alterado de cliente para zzz.
        # por algum motivo, passou a dar erro depois do upgrade para 3.8.0
        try:
            OBJ_CLIENTE=_zeep.client.Client(wsdl=STR_WSDL)
            XML_RESPONSE = OBJ_CLIENTE.service.getUltimoValorVO(1).ultimoValor  # o 1 é o código da série temporal Dólar
            self.valor = XML_RESPONSE.valor._value_1
            self.data = _datetime.date(XML_RESPONSE.ano, XML_RESPONSE.mes, XML_RESPONSE.dia)
            self.erro = False
            self.erro_txt=''
        except Exception as e:
            self.valor = 0
            self.erro = True
            self.erro_txt = 'Ocorreu um erro: ' + e.args[0]
            dtt_now = _datetime.datetime.now()
            self.data = _datetime.date(dtt_now.year, dtt_now.month, dtt_now.day)

class CotacaoDolarData:

    def __init__(self, arg_data):
        self.data = _datetime.datetime.strptime(arg_data,'%d/%m/%Y')
        STR_WSDL = 'https://www3.bcb.gov.br/sgspub/JSP/sgsgeral/FachadaWSSGS.wsdl'
        try:
            OBJ_CLIENTE = _zeep.client.Client(wsdl=STR_WSDL)
            XML_RESPONSE = OBJ_CLIENTE.service.getValor(1,arg_data)  # o 1 é o código da série temporal Dólar
            self.valor = XML_RESPONSE._value_1
            self.erro = False
            self.erro_txt = ''
        except Exception as e:
            self.valor = 0
            self.erro = True
            self.erro_txt = e.args[0]
            if self.erro_txt.find('Value(s) not found') != -1:
                self.erro_txt = 'Não há cotação para ' + arg_data
            else:
                self.erro_txt = 'Ocorreu um erro: ' + _erro_txt

class CotacaoDolarHistorico:
    #ideias para chegar à solução vieram de vários sites:
    #https://python-zeep.readthedocs.io/en/master/datastructures.html
    #https://stackoverflow.com/questions/1130819/how-to-create-arraytype-for-wsdl-in-python-using-suds
    #depois fiquei testando no prompt até conseguir montar um objeto que funcionasse
    def __init__(self, arg_data_inicio, arg_data_fim):
        self.data_inicio = _datetime.datetime.strptime(arg_data_inicio, '%d/%m/%Y')
        self.data_fim = _datetime.datetime.strptime(arg_data_fim, '%d/%m/%Y')
        STR_WSDL = 'https://www3.bcb.gov.br/sgspub/JSP/sgsgeral/FachadaWSSGS.wsdl'
        try:
            OBJ_CLIENTE=_zeep.client.Client(wsdl=STR_WSDL)
            OBJ_FACTORY = OBJ_CLIENTE.type_factory('ns0')
            OBJ_ARRAYOFFLONG = OBJ_FACTORY.ArrayOfflong([1])
            XML_RESPONSE = OBJ_CLIENTE.service.getValoresSeriesXML(OBJ_ARRAYOFFLONG, arg_data_inicio, arg_data_fim)
            XML_ROOT = _ET.fromstring(XML_RESPONSE._value_1)
            lst_resultado = []
            for xml_element in XML_ROOT[0]:
                lst_resultado.append([xml_element[0].text, xml_element[1].text])
            self.erro = False
            self.erro_txt = ''
            self.cotacoes = lst_resultado
            self.itens = len(lst_resultado)
        except Exception as e:
            self.cotacoes = []
            self.itens = 0
            self.erro = True
            self.erro_txt = e.args[0]
            if self.erro_txt.find('Value(s) not found') != -1:
                self.erro_txt = 'Não há cotação para o período entre ' + arg_data_inicio + ' e ' + arg_data_fim
            else:
                self.erro_txt = 'Ocorreu um erro: ' + _erro_txt