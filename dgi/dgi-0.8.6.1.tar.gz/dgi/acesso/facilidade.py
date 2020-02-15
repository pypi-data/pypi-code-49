from loguru import logger

import os
import pathlib
from time import sleep
from datetime import datetime

import requests
import urllib
import urllib.request
from http import cookiejar
from bs4 import BeautifulSoup

import pandas as pd

from pymongo import MongoClient

from multiprocessing import Process

from dgi.utils import define_ambiente_de_processamento
from dgi.info import DB_PROPS
from dgi.urls import URL_CARINHO, URL_CONFIRMA_PEDIDO, URL_FECHA_PEDIDO, URL_LOGIN
from dgi.acesso.utils import divide_lista, cria_documento_download, string_para_data

from dgi.decoradores import adiciona_log
from dgi.banco import GeradorDeConexoesMongo
from dgi.acesso.utils import remove_imagens_duplicadas
from dgi.excecoes import ErroAoAcessarLink, LimiteDoPedidoExcedido


class FacilitaDGI:
    """Classe que facilita a interação com o catálogo DGI/INPE
    
    Args:
        usuario (str): Nome de usuário no catálogo da DGI/INPE
        senha (str): Senha de usuário no catálogo da DGI/INPE
        db_props (dict): Dicionário contendo as informações para conexão com o banco de dados, contendo as seguintes chaves
            
            host: ``str``: Endereço de IP do banco de dados

            porta: ``int``: Porta do banco de dados

            usuario: ``str``: Usuário para utilizar o banco (Opcional)

            senha: ``str``: Senha para utilizar o banco (Opcional)
    """

    def __init__(self, usuario, senha, db_props=DB_PROPS):
        self.__usuario = usuario
        self.__senha = senha
        self.__db_props = db_props
        self.__ambiente_de_execucao = define_ambiente_de_processamento()

    @adiciona_log("/tmp/pedidos_{}.log")
    def realiza_pedido(self, lista_de_imagens) -> dict:
        """Função para fazer pedidos automatizados no catálogo DGI/INPE

        Esta função recebe a lista de dicionários com os parâmetros das imagens (Presentes no catalogo do LabISA) e remove os elementos duplicados, então realiza o pedido

        Args:
            lista_de_image (list): Lista com as imagens que devem estar nos pedidos
        
        Returns:
            dict: Dicionário contendo as informações do pedido realizado. Neste dicionário há a quantidade de imagens no pedido e as imagens propriamente dito. 
        """

        informacoes_do_pedido = {
            "quantidade_de_imagens_no_pedido": 0,
            "imagens_no_pedido": set()
        }

        informacoes_do_pedido["imagens_no_pedido"] = remove_imagens_duplicadas(lista_de_imagens)
        informacoes_do_pedido["quantidade_de_imagens_no_pedido"] = len(informacoes_do_pedido["imagens_no_pedido"])

        if informacoes_do_pedido["quantidade_de_imagens_no_pedido"] > 200:
            raise LimiteDoPedidoExcedido("Seu pedido deve ter no máximo 200 itens")

        logger.info("Iniciando processo de aquisição de imagens")
        cj = cookiejar.CookieJar()
        opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))

        logger.info("Fazendo login"); sleep(1)
        login_data = urllib.parse.urlencode({
            'name' : self.__usuario, 
            'pwd' : self.__senha, 
            'enviar': 'Realizar acesso', 
            'submitted': 1
        })

        # Ao criar uma conexão com opener, os cookies da página serão salvos
        opener.open(URL_LOGIN, login_data.encode())

        logger.info("Recuperando sessão..."); sleep(1)
        cookies = opener.handlers[-2]
        # Recuperando apenas o PHPSESSID
        sess_id = str(cookies.cookiejar).split("PHPSESSID")[1].split()[0].split("=")[1]

        logger.info("Adicionando imagem(s) ao carrinho"); sleep(1)
        for imagem in informacoes_do_pedido["imagens_no_pedido"]:
            try:
                opener.open(URL_CARINHO.format(imagem))            
                logger.info("{}: Adicionada com sucesso!".format(imagem))
            except:
                logger.error("Erro ao adicionar: {}".format(imagem))
        logger.info("Confirmando pedido"); sleep(1)

        # Envia pedido de confirmação do pedido
        opener.open(URL_CONFIRMA_PEDIDO.format(self.__usuario, sess_id))

        logger.info("Fechando pedido"); sleep(2)
        # Após o pedido confirmado, fecha ele para receber as imagens
        try:
            opener.open(URL_FECHA_PEDIDO.format(sess_id, self.__usuario, str(len(lista_de_imagens))))
        except Exception as e:
            logger.error(str(e))
            raise ErroAoAcessarLink("Erro ao tentar fechar o pedido")
        logger.success("Pedido finalizado! Verifique seu email")

        return informacoes_do_pedido

    @adiciona_log("/tmp/downloads_{}.log")
    def baixa_imagens_de_link_do_pedido(self, link_de_pedido, diretorio_de_saida, nprocessos=5) -> pd.DataFrame:
        """Função para realizar o download através de um link de pedido

        Args:
            link_de_pedido (str): Link do local onde as imagens do pedido foram disponibilizadas
            diretorio_de_saida (str): Diretório onde os dados deverão ser salvos
            nprocessos (int): Número de processos de requisição executados ao mesmo tempo

        Returns:
            pd.DataFrame: DataFrame contendo a relação de todas as imagens já baixadas neste computador
        """

        def baixa_lista_de_links(links: list, diretorio_de_saida: str) -> None:
            """Função para download dos dados

            Args:
                links (list): Lista com os links que serão baixados
                diretorio_de_saida (str): Caminho completo para o diretório onde a imagem será salva

            Returns:
                None
            """
            colecao = GeradorDeConexoesMongo.recupera_conexao(self.__db_props).dgi_dumps.imagens_adquiridas

            for link in links:
                divide_em = -1
                complemento = ""
                if "scenario" in link:
                    divide_em = -2
                    complemento = "scenario"

                doc_db = cria_documento_download(link.split("/")[divide_em])            
                # Caso haja arquivos do scenario, o complemento irá criar o diretório a ser utilizado
                diretorio_da_imagem = os.path.join(diretorio_de_saida, "{}/{}/{}/{}_{}".format(*doc_db.values()),
                                                                                                            complemento)
                # Criando o diretório da imagem
                pathlib.Path(diretorio_da_imagem).mkdir(parents=True, exist_ok=True)

                path = os.path.join(diretorio_da_imagem, link.split("/")[-1])
                logger.info("Processando arquivo: {}".format(link))
                urllib.request.urlretrieve(link, path) 

                if "scenario" not in diretorio_da_imagem and len(list(colecao.find({"local": diretorio_da_imagem}))) == 0:
                    doc_db["local"] = diretorio_da_imagem
                    doc_db["data_insercao_no_banco"] = datetime.now()
                    doc_db["data"] = string_para_data(doc_db["data"], reverso=False, sep="_")
                    
                    colecao.insert_one(doc_db)

        if link_de_pedido[-1] != '/':
            link_de_pedido += '/'

        res = requests.get(link_de_pedido)
        soup = BeautifulSoup(res.content, features="lxml")

        links_validos = []

        logger.info("Verificando os links que podem ser baixados")
        # Criando lista de links validos
        for link in soup.find_all("a")[1:]:
            if "scenario" in link["href"]:
                # Caso em que o link representa um diretório
                r = requests.get(link_de_pedido + str(link["href"]))
                s = BeautifulSoup(r.content, features="lxml").findAll("a")

                for i in s[1:]:
                    links_validos.append(link_de_pedido + str(link["href"]) + i["href"])
            else:
                links_validos.append(link_de_pedido + str(link["href"]))
        links_divididos = divide_lista(links_validos, nprocessos)

        logger.info("Iniciando os downloads")
        for i in range(0, nprocessos):
            p = self.__ambiente_de_execucao(target=baixa_lista_de_links, args=(links_divididos[i], diretorio_de_saida,))
            p.start()
        p.join()
        logger.success("As imagens foram salvas com sucesso!")

        # Recuperando as imagens já baixadas, salvas no banco
        colecao = GeradorDeConexoesMongo.recupera_conexao(self.__db_props).dgi_dumps.imagens_adquiridas
        return pd.DataFrame(list(colecao.find({}, {"_id": 0})))
