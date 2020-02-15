from loguru import logger
from daemonize import Daemonize

from time import sleep
from datetime import datetime, timedelta

from dgi.info import DB_PROPS
from dgi.catalogo import CatalogoDGI
from dgi.decoradores import adiciona_log
from dgi.excecoes import ErroNaExecucaoDaBuscaNoServico, ErroDePlataforma

PID = "/tmp/dgid.pid"


@adiciona_log("/tmp/servico_de_aquisicao_de_dados.log", temporal=False)
def _fnc_busca_dados(db_props = DB_PROPS) -> None:
    """Função para a busca de dados
    
    Args:
        db_props (dict): Dicionário contendo as informações para conexão com o banco de dados, contendo as seguintes chaves
            
            host: ``str``: Endereço de IP do banco de dados

            porta: ``int``: Porta do banco de dados

            usuario: ``str``: Usuário para utilizar o banco (Opcional)

            senha: ``str``: Senha para utilizar o banco (Opcional)
    
    Returns:
        None
    """
    
    logger.info("Serviço de busca de imagens inicializado")
    
    catalogo = CatalogoDGI(db_props)
    data_da_ultima_atualizacao = catalogo.recupera_data_ultima_insercao()

    data_de_busca = {"inicial": "01/01/2014", "final": datetime.today().strftime("%d/%m/%Y")}
    localizacoes = {
            "norte": "11.04024846",
            "sul": "-36.49917303", 
            "leste": "-30.77297895",
            "oeste": "-74.80618208"
    }
    
    if data_da_ultima_atualizacao == []:
        logger.info(f"Iniciando processo de listagem de 2014 até {data_de_busca['final']}")
    else:
        logger.info(f"O processo de atualização, continuará da seguinte data: {data_da_ultima_atualizacao}")
        data_de_busca["inicial"] = data_da_ultima_atualizacao.strftime("%d/%m/%Y")
        
    try:
        if data_de_busca["inicial"] != data_de_busca["final"]:
            catalogo.lista_imagens_dgi_regiao("CB4", "", data_de_busca, localizacoes)
    except RuntimeError as e:
        logger.trace(e)
        
        raise ErroNaExecucaoDaBuscaNoServico(f"Problemas ocorreram durante a busca de dados no serviço: {str(e)}")

    logger.info("Iniciando processo de busca diária dos dados")
    while True:
        try:
            # Recuperando a data de hoje
            data_atual = datetime.today()
            inicial = (data_atual - timedelta(days=3)).strftime("%d/%m/%y")
            final = data_atual.strftime("%d/%m/%y")

            data_de_busca = {"inicial": inicial, "final": final}
            
            logger.info("Listagem começou a ser realizada")
            catalogo.lista_imagens_dgi_regiao("CB4", "", data_de_busca, localizacoes)
            
            logger.info("Processo finalizado! Aguardando 3 dias para a atualização")
            sleep((3 * 24) * 60 * 60)
        except Exception as e:
            logger.trace(e)
            
            raise ErroNaExecucaoDaBuscaNoServico(f"Problemas ocorreram durante a busca de dados no serviço: {str(e)}")


def servico_dgi_linux(db_props = DB_PROPS) -> None:
    """Função para iniciar o serviço de busca de imagens no Linux
    
    Args:
        db_props (dict): Dicionário contendo as informações para conexão com o banco de dados, contendo as seguintes chaves
            
            host: ``str``: Endereço de IP do banco de dados

            porta: ``int``: Porta do banco de dados

            usuario: ``str``: Usuário para utilizar o banco (Opcional)

            senha: ``str``: Senha para utilizar o banco (Opcional)
    
    Returns:
        None
    """

    import platform

    if platform.system() != "Linux":
        raise ErroDePlataforma("Este serviço está disponível apenas para Linux")

    def funcao_do_servico():
        """Função do serviço DGI para Linux
        """
        try:
            _fnc_busca_dados(db_props)
        except Exception as e:
            raise ErroNaExecucaoDaBuscaNoServico(str(e))
    Daemonize(app="dgid", pid=PID, action=funcao_do_servico).start()
