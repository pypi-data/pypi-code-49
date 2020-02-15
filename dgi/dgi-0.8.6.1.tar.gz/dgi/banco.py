from abc import ABC, abstractmethod
from pymongo import MongoClient

from dgi.excecoes import DefinicaoInvalida


class GeradorDeConexoes(ABC):
    """Classe abstrata para generalizações de conexão com o banco de dados
    """
    
    @staticmethod
    @abstractmethod
    def recupera_conexao(db_props) -> MongoClient:
        pass


class GeradorDeConexoesMongo(GeradorDeConexoes):
    """Classe para gerar conexões com o MongoDB
    """

    @staticmethod
    def recupera_conexao(db_probs) -> MongoClient:
        """Método para recuperar a conexão com o banco de dados

        Args:
            db_props (dict): Dicionário contendo as informações para conexão com o banco de dados, contendo as seguintes chaves
                
                host: ``str``: Endereço de IP do banco de dados

                porta: ``int``: Porta do banco de dados

                usuario: ``str``: Usuário para utilizar o banco (Opcional)

                senha: ``str``: Senha para utilizar o banco (Opcional)
        Returns:
            MongoClient: Conexão com o banco de dados
        """

        if "usuario" in db_probs:
            if "senha" in db_probs:
                return MongoClient('mongodb://%s:%s@%s:%i' % (db_probs["host"], db_probs["porta"], 
                                                                    db_probs["usuario"], db_probs["senha"]))
            else:
                raise DefinicaoInvalida("Ao inserir o usuário do banco de dados é necessário definir a senha")
        return MongoClient(db_probs["host"], db_probs["porta"])
