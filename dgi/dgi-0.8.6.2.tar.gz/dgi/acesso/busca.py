import pandas as pd

from dgi.info import DB_PROPS
from dgi.banco import GeradorDeConexoesMongo
from dgi.acesso.utils import remove_imagens_duplicadas


class BuscaDeImagemNoCatalogo:
    """Catalogo de imagens do LabISA (Banco de dados populado com os registros das imagens do DGI)
    
        Args:
            db_props (dict): Dicionário de configurações do acesso ao banco, possui as seguintes chaves:
            
                host: ``str``: Endereço de IP do banco de dados

                porta: ``int``: Porta do banco de dados

                usuario: ``str``: Usuário para utilizar o banco (Opcional)

                senha: ``str``: Senha para utilizar o banco (Opcional)
    """

    def __init__(self, db_props = DB_PROPS):
        self.__db_props = db_props

    def busca_personalizada_de_imagens(self, op: dict) -> list:
        """Método para busca de imagens utilizando comandos do MongoDB

        Args:
            op (dict): Dicionário contendo os parâmetros de busca do MongoDB

        Returns:
            list: Lista com as imagens encontradas na busca personalizada
        """

        colecao = GeradorDeConexoesMongo.recupera_conexao(self.__db_props).dgi_dumps.catalogo
        return list(colecao.find(op, {"_id": 0}))

    def busca_image_por_quantidade_de_nuvem(self, q1: int, q2: int, q3: int, q4: int) -> list:
        """Método para busca de imagens levando em consideração a quantidade de nuvem em cada quadrante

        Args:
            q1 (int): Porcentagem de nuvem limite no quadrante 1
            
            q2 (int): Porcentagem de nuvem limite no quadrante 2
            
            q3 (int): Porcentagem de nuvem limite no quadrante 3
            
            q4 (int): Porcentagem de nuvem limite no quadrante 4

        Returns:
            list: Lista com todas as imagens encontradas no filtro de nuvem
        """

        colecao = GeradorDeConexoesMongo.recupera_conexao(self.__db_props).dgi_dumps.catalogo
        return list(colecao.find({
            "quantidade_nuvens.quadrante_1": {
                "$lt": q1
            },
            "quantidade_nuvens.quadrante_2": {
                "$lt": q2
            },
            "quantidade_nuvens.quadrante_3": {
                "$lt": q3
            },
            "quantidade_nuvens.quadrante_4": {
                "$lt": q4
            },
        }, {"_id": 0}))

    def busca_imagens_por_instrumento(self, instrumento: str) -> list:
        """Método para busca de imagens através dos instrumentos de registro

        Args:
            instrumento (str): Instrumento que registrou a imagem buscada

        Returns:
            list: Lista com todas as imagens do instrumento
        """

        colecao = GeradorDeConexoesMongo.recupera_conexao(self.__db_props).dgi_dumps.catalogo
        return list(colecao.find({
            "instrumento": instrumento
        }, {"_id": 0}))

    def busca_imagens_por_orbita_ponto(self, orbita: int, ponto: int) -> list:
        """Método para busca de imagens através da orbita-ponto

        Args:
            orbita (int): Valor da orbita da imagem
            
            ponto (int): Valor do ponto da imagem

        Returns:
            list: Lista com todas as imagens encontradas com a orbita ponto definida
        """
        
        colecao = GeradorDeConexoesMongo.recupera_conexao(self.__db_props).dgi_dumps.catalogo
        return list(colecao.find({
            "orbita": orbita,
            "ponto": ponto
        }, {"_id": 0}))

    def busca_imagens_por_instrumento_data_quantidade_de_nuvem(self, instrumento: str, data_inicial: str, 
                                                                data_final: str, quantidade_de_nuvem: dict) -> list:
        """Método para busca de imagens através de range de data, orbita-ponto e instrumento

        Args:
            instrumento (str): Instrumento que registrou a imagem buscada
            
            data_inicial (str): Data inicial da busca (DD-MM-AAAA)
            
            data_final (str): Data final da busca (DD-MM-AAAA)
            
            quantidade_de_nuvem (dict): Dicionário contendo a porcentagem de nuvem de cada quadrante da imagem. As chaves deste dicionário são:
                
                q1: ``int``: Porcentagem de nuvem no primeiro quadrante
                
                q2: ``int``: Porcentagem de nuvem no segundo quadrante
                
                q3: ``int``: Porcentagem de nuvem no terceiro quadrante
                
                q4: ``int``: Porcentagem de nuvem no quarto quadrante

        Returns:
            list: Lista com todas as encontradas na orbita-ponto e instrumento definido
        """

        from dgi.acesso.utils import string_para_data

        data_inicial = string_para_data(data_inicial)
        data_final = string_para_data(data_final)

        colecao = GeradorDeConexoesMongo.recupera_conexao(self.__db_props).dgi_dumps.catalogo 
        return list(colecao.find({
            "instrumento": instrumento,
            "data_imagem": {
                "$gte": data_inicial,
                "$lte": data_final
            }, "quantidade_nuvens.quadrante_1": {
                "$lt": quantidade_de_nuvem["q1"]
            },
            "quantidade_nuvens.quadrante_2": {
                "$lt": quantidade_de_nuvem["q2"]
            },
            "quantidade_nuvens.quadrante_3": {
                "$lt": quantidade_de_nuvem["q3"]
            },
            "quantidade_nuvens.quadrante_4": {
                "$lt": quantidade_de_nuvem["q4"]
            }
        }, {"_id": 0}))

    def busca_imagens_por_data_orbita_ponto_e_instrumento(self, orbita: int, ponto: int, 
                                                            data_inicial: str, data_final: str, instrumento: str) -> list:
        
        """Método para busca de imagens através de range de data, orbita-ponto e instrumento

        Args:
            data_inicial (str): Data inicial da busca (DD-MM-AAAA)
            
            data_final (str): Data final da busca (DD-MM-AAAA)
            
            orbita (int): Valor da orbita da imagem
            
            ponto (int): Valor do ponto da imagem
            
            instrumento (str): Instrumento que registrou a imagem buscada

        Returns:
            list: Lista com todas as encontradas
        """

        from dgi.acesso.utils import string_para_data

        data_inicial = string_para_data(data_inicial)
        data_final = string_para_data(data_final)

        colecao = GeradorDeConexoesMongo.recupera_conexao(self.__db_props).dgi_dumps.catalogo 
        return list(colecao.find({
            "orbita": orbita,
            "ponto": ponto,
            "instrumento": instrumento,
            "data_imagem": {
                "$gte": data_inicial,
                "$lte": data_final
            }
        }, {"_id": 0}))

    def busca_imagens_por_orbita_ponto_e_instrumento(self, orbita: int, ponto: int, instrumento: str) -> list:
        """Método para busca de imagens através de orbita-ponto e instrumento

        Args:
            orbita (int): Valor da orbita da imagem
            
            ponto (int): Valor do ponto da imagem
            
            instrumento (str): Instrumento que registrou a imagem buscada

        Returns:
            list: Lista com todas as encontradas na orbita-ponto e instrumento definido
        """

        colecao = GeradorDeConexoesMongo.recupera_conexao(self.__db_props).dgi_dumps.catalogo 
        return list(colecao.find({
            "orbita": orbita,
            "ponto": ponto,
            "instrumento": instrumento
        }, {"_id": 0}))

    def busca_imagens_por_data_e_instrumento(self, data_inicial: str, data_final: str, instrumento: str) -> list:
        """Método para busca de imagens através de range de datas e instrumentos

        Args:
            data_inicial (str): Data inicial da busca (DD-MM-AAAA)
            
            data_final (str): Data final da busca (DD-MM-AAAA)
            
            instrumento (str): Instrumento que registrou a imagem buscada

        Returns:
            list: Lista com todas as imagens encontradas para o intervalo de datas e pelo instrumento
        """

        from dgi.acesso.utils import string_para_data

        data_inicial = string_para_data(data_inicial)
        data_final = string_para_data(data_final)

        colecao = GeradorDeConexoesMongo.recupera_conexao(self.__db_props).dgi_dumps.catalogo 
        return list(colecao.find({
            "data_imagem": {
                "$gte": data_inicial,
                "$lte": data_final
            },
            "instrumento": instrumento
        }, {"_id": 0}))

    def busca_imagens_por_data(self, data_inicial: str, data_final: str) -> list:
        """Método para busca de imagens utilizando um range de datas
        
        Args:
            data_inicial (str): Data inicial da busca (DD-MM-AAAA)
            
            data_final (str): Data final da busca (DD-MM-AAAA)
        
        Returns:
            list: Lista com todas as imagens encontradas para o intervalo de datas inseridos
        """

        from dgi.acesso.utils import string_para_data

        data_inicial = string_para_data(data_inicial)
        data_final = string_para_data(data_final)

        colecao = GeradorDeConexoesMongo.recupera_conexao(self.__db_props).dgi_dumps.catalogo
        return list(colecao.find({
            "data_imagem": {
                "$gte": data_inicial,
                "$lte": data_final
            }
        }, {"_id": 0}))

    def busca_imagens_por_intersec_ponto(self, lat: float, long: float) -> list:
        """Método para busca de imagens através da referência geográfica

        Args:
            lat (float): Latitude do ponto que está sendo buscado
            
            long (float): Longitude do ponto que está sendo buscado

        Returns:
            list: Lista com todas as imagens que fazer intersecção com o ponto inserido
        """

        colecao = GeradorDeConexoesMongo.recupera_conexao(self.__db_props).dgi_dumps.catalogo
        return list(colecao.find({
            "poligono_da_cena": {
                "$geoIntersects": {
                    "$geometry": {
                        "type": "Point",
                        "coordinates": [
                            long, lat
                        ]
                    }
                }
            }
        }, {"_id": 0}))

    def busca_imagens_dentro_do_shape(self, shape: list) -> list:
        """Método para busca de imagens através de uma lista de pontos


        Args:
            shape (list): Lista com as coordenadas do poligono que está sendo pesquisado

        Returns:
            list: Conjunto com todas as imagens em que seu ponto central faz intersecção com os elementos do 
            poligono inserido pelo usuário
        """

        colecao = GeradorDeConexoesMongo.recupera_conexao(self.__db_props).dgi_dumps.catalogo
        return list(colecao.find({
            "centro_da_cena": {
                "$geoWithin": {
                    "$geometry": {
                        "type": "Polygon",
                        "coordinates": shape
                    }
                }
            }
        }, {"_id": 0}))


class BuscaImagensJaBaixadas:
    """Classe que possibilita a busca de imagens já baixadas na máquina

    Args:
        db_props (dict): Dicionário contendo as informações para conexão com o banco de dados, contendo as seguintes chaves
            
            host: ``str``: Endereço de IP do banco de dados

            porta: ``int``: Porta do banco de dados

            usuario: ``str``: Usuário para utilizar o banco (Opcional)

            senha: ``str``: Senha para utilizar o banco (Opcional)
    """

    def __init__(self, db_props=DB_PROPS):
        self.__db_props = db_props

    def __busca_generica(self, parametros_da_busca: dict) -> list:
        """Método de busca genérica

        Args:
            parametros_da_busca (dict): Parâmetros a serem aplicados na busca no banco de imagen salvas

        Returns:
            list: Lista contendo o resultado da busca
        """

        colecao = GeradorDeConexoesMongo.recupera_conexao(self.__db_props).dgi_dumps.imagens_adquiridas
        return list(colecao.find(parametros_da_busca, {"_id": 0}))

    def recupera_todas_as_imagens_baixadas(self) -> pd.DataFrame:
        """Método recupera todas as imagens já baixadas na máquina

        Returns:
            pd.DataFrame: DataFrame com a relação de imagens e os locais onde foram originalmente salvas
        """

        return pd.DataFrame(self.__busca_generica({}))

    def recupera_todas_as_imagens_baixadas_por_instrumento(self, instrumento) -> pd.DataFrame:
        """Método para recuperar todas as imagens baixadas filtrada por instrumento
        
        Args:
            instrumento (str): Nome do instrumento
        
        Returns:
            pd.DataFrame: DataFrame com a relação de imagens e os locais onde foram originalmente salvas
        """

        return pd.DataFrame(self.__busca_generica({"instrumento": instrumento}))
