from loguru import logger

import requests
from bs4 import BeautifulSoup

from pymongo import MongoClient
from pymongo.errors import BulkWriteError

from time import sleep
from datetime import datetime

from dgi.utils import define_ambiente_de_processamento
from dgi.info import DB_PROPS
from dgi.urls import URL_BUSCA, URL_BUSCA_RETANGULO
from dgi.catalogo.utils import formata_lista_de_imagens, recupera_informacoes_da_listagem

from dgi.decoradores import adiciona_log
from dgi.excecoes import ErroAoAcessarLink, DefinicaoInvalida
from dgi.banco import GeradorDeConexoesMongo

NUVEM_PROPS = {"q1": "", "q2": "", "q3": "", "q4": ""}


class CatalogoDGI:
    """Catálogo de imagens do DGI

    Args:
        db_props (:obt: `dict`, optional): Dicionário de configurações do acesso ao banco, possui as seguintes chaves:
            host: ``str``: Endereço de IP do banco de dados

            porta: ``int``: Porta do banco de dados

            usuario: ``str``: Usuário para utilizar o banco (Opcional)

            senha: ``str``: Senha para utilizar o banco (Opcional)
    """

    def __init__(self, db_props = DB_PROPS):
        self.__db_props = db_props
        self.__ambiente_de_execucao = define_ambiente_de_processamento()

    def __lthread(self, nworker, url, inicio, passo, limite, nome_do_local=""):
        """Método criado para a execução paralela da busca de imagens
        """

        colecao = GeradorDeConexoesMongo.recupera_conexao(self.__db_props).dgi_dumps.catalogo
        while True:
            if inicio > limite:
                break

            res = requests.get(url.replace("*", str(inicio)))
            soup = BeautifulSoup(res.content, features="lxml")

            try:
                # Salva os resultados da página atual
                colecao.insert_many(formata_lista_de_imagens(soup, inicio, nome_do_local), ordered=False)
            except BulkWriteError as bwe:
                logger.error(bwe)

            logger.info(f"Página {inicio} recuperada com sucesso")
            inicio += passo

    @adiciona_log("/tmp/listagem_dgi_regiao_{}.log")
    def lista_imagens_dgi_regiao(self, satelite, instrumento, data, localizacoes, nuvem_props=NUVEM_PROPS) -> dict:
        """Método para listar os dados do DGI INPE levando em consideração um retângulo de referência

        Args:
            satelite (str): Nome do satelite
            instrumento (str): Nome do instrumento
            data (dict): Dicionário de datas, que contém as seguintes chaves
                inicial: ``str``: Data no formato DD-MM-AAAA

                final: ``str``: Data no formato DD-MM-AAAA
            localizacoes (dict): Dicionário de localizações, que contém as seguintes chaves
                norte: ``str``: Ponto do canto norte-leste

                sul: ``str``: Ponto do canto sul-oeste

                leste: ``str``: Ponto do canto norte-leste

                oeste: ``str``: Ponto do canto sul-oeste
            nuvem_props (dict): Dicionário com as propriedades de núvem em cada quadrante das imagens, este que contém as seguintes chaves
                q1: ``str``: Porcentagem de núvem possível no quadrante 1

                q2: ``str``: Porcentagem de núvem possível no quadrante 2

                q3: ``str``: Porcentagem de núvem possível no quadrante 3

                q4: ``str``: Porcentagem de núvem possível no quadrante 4   

        Returns:
            dict: Dicionário contendo as informações gerais do processo 
        """

        try:
            url_inicial = URL_BUSCA_RETANGULO.format(
                "1", satelite, instrumento, data["inicial"], data["final"],
                nuvem_props["q1"], nuvem_props["q2"], nuvem_props["q3"], nuvem_props["q4"],
                localizacoes["norte"], localizacoes["sul"], localizacoes["leste"], localizacoes["oeste"]
            )
            logger.info(f"Buscando dados em: {url_inicial}")

            propriedades_da_pagina = recupera_informacoes_da_listagem(url_inicial)
        except RuntimeError as error:
            logger.error(f"Erro ao tentar recuperar as informações do link {url_inicial}")
            raise ErroAoAcessarLink(str(error))
    
        # Definindo a quantidade de processos de acordo com a quantidade de páginas
        if propriedades_da_pagina["paginas"] == 1:
            workers = 1
        elif propriedades_da_pagina["paginas"] < 5:
            workers = 2
        elif propriedades_da_pagina["paginas"] >= 5:
            workers = 5

        URL_BASE = URL_BUSCA_RETANGULO.format(
                "*", satelite, instrumento, data["inicial"], data["final"],
                nuvem_props["q1"], nuvem_props["q2"], nuvem_props["q3"], nuvem_props["q4"],
                localizacoes["norte"], localizacoes["sul"], localizacoes["leste"], localizacoes["oeste"]
            )

        for i in range(1, workers + 1):
            p = self.__ambiente_de_execucao(target=self.__lthread, 
                                    args=(i, URL_BASE, i, workers, propriedades_da_pagina["paginas"], ))
            p.start()
        p.join()

        logger.info("O processo de listagem foi finalizado!")
        return {
            "propriedades_da_busca": {
                **propriedades_da_pagina
            },
            "datas_pesquisadas": {
                "inicio": data["inicial"],
                "fim": data["final"]
            }
        }

    @adiciona_log("/tmp/listagem_dgi_ponto_{}.log")
    def lista_imagens_dgi_ponto(self, satelite, instrumento, data, 
                                    localizacoes, nome_padrao="", nomes_dos_locais=[], nuvem_props=NUVEM_PROPS) -> dict:
        """Método para listar os dados do DGI INPE levando em consideração um ponto de referência

        Args:
            satelite (str): Nome do satelite
            
            instrumento (str): Nome do instrumento
            
            data (dict): Dicionário de datas, que contém as seguintes chaves
                inicial: ``str``: Data no formato DD-MM-AAAA

                final: ``str``: Data no formato DD-MM-AAAA

            localizacoes (dict): Dicionário de localizações, que contém as seguintes chaves
                lat: ``str``: Latitude da localização pesquisada

                long: ``str``: Longitude da localização pesquisada

            nome_padrao (str): Template com o padrão de nomenclatura que deve ser utilizado na geração automática de nomes
                Neste caso, caso seja inserido a string `PONTO_{}`, todos os pontos terão nome PONTO_1...PONTO_N

            nome_dos_locais (list): Nome dos locais que estão sendo buscados (localizações)
            nuvem_props (dict): Dicionário com as propriedades de núvem em cada quadrante das imagens, este que contém as seguintes chaves
                q1: ``str``: Porcentagem de núvem possível no quadrante 1

                q2: ``str``: Porcentagem de núvem possível no quadrante 2

                q3: ``str``: Porcentagem de núvem possível no quadrante 3

                q4: ``str``: Porcentagem de núvem possível no quadrante 4    

        Returns:
            dict: Dicionário contendo as informações gerais do processo 
        """

        if len(nomes_dos_locais) != len(localizacoes):
            if nome_padrao != "":
                nomes_dos_locais = [nome_padrao.format(str(i)) for i in range(0, localizacoes)]
                assert len(nomes_dos_locais) == len(localizacoes)
            else:
                raise DefinicaoInvalida("Seu input deve conter o nome de cada ponto inserido, ou uma template para a criação automática de nomes para os pontos")

        logger.info("Iniciando trabalhos com até 3 workers")
        for local, localizacao in zip(nomes_dos_locais, localizacoes): 
            logger.info(f"Iniciando busca de {local}")
            
            # Realizando busca inicial (Aquisição de informações gerais)
            url_inicial = URL_BUSCA.format(1, satelite, instrumento, data["inicial"], data["final"], 
                                            nuvem_props["q1"], nuvem_props["q2"], nuvem_props["q3"], nuvem_props["q4"],
                                            localizacao["lat"], localizacao["long"])

            try:
                propriedades_da_pagina = recupera_informacoes_da_listagem(url_inicial)
            except RuntimeError:
                logger.error(f"Erro ao tentar recuperar as informações do link {url_inicial}"); sleep(10)
                continue
            
            # Iniciando os processos de busca para o local atual
            URL_BASE = URL_BUSCA.format("*", satelite, instrumento, data["inicial"], data["final"], 
                                            nuvem_props["q1"], nuvem_props["q2"], nuvem_props["q3"], nuvem_props["q4"],
                                            localizacao["lat"], localizacao["long"]) 

            # Definindo a quantidade de processos de acordo com a quantidade de páginas
            if propriedades_da_pagina["paginas"] == 1:
                workers = 1
            elif propriedades_da_pagina["paginas"] == 2:
                workers = 2
            else:
                workers = 3

            for i in range(1, workers + 1):
                p = self.__ambiente_de_execucao(target=self.__lthread, args=(i, URL_BASE, i, workers, propriedades_da_pagina["paginas"], local, ))
                p.start()
            logger.info(f" Esperando a busca pelos dados de {local} acabarem")
            p.join()

            logger.info(f"Busca de {local} finalizada\n")
        
        return {
            "propriedades_da_busca": {
                **propriedades_da_pagina
            },
            "datas_pesquisadas": {
                "inicio": data["inicial"],
                "fim": data["final"]
            }
        }

    def recupera_data_ultima_insercao(self) -> datetime:
        """Recupera a data da última inserção feita no banco de dados

        Returns:
            datetime: Data da última inserção no banco de dados
        """

        from pymongo import DESCENDING
        colecao = GeradorDeConexoesMongo.recupera_conexao(self.__db_props).dgi_dumps.catalogo
        ultima_pesquisa = list(colecao.find().sort('$natural', DESCENDING).limit(1))

        if len(ultima_pesquisa) > 0:
            return ultima_pesquisa[0]["data_insercao_no_banco"]
        return []
