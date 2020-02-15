from dgi.info import DB_PROPS
from dgi.catalogo import CatalogoDGI
from dgi.decoradores import adiciona_log
from dgi.excecoes import ErroNaExecucaoDaBuscaNoServico, ErroDePlataforma

from loguru import logger

from time import sleep
from datetime import datetime, timedelta


@adiciona_log("/tmp/servico_de_aquisicao_de_dados.log", temporal=False)
def servico_dgi_windows(db_props = DB_PROPS):
    """Função geral que será aplicada aos serviços dos diferentes sistemas operacionais
    
    Args:
        db_props (dict): Dicionário contendo as informações para conexão com o banco de dados, contendo as seguintes chaves
            
            host: ``str``: Endereço de IP do banco de dados

            porta: ``int``: Porta do banco de dados

            usuario: ``str``: Usuário para utilizar o banco (Opcional)

            senha: ``str``: Senha para utilizar o banco (Opcional)
    
    """

    import platform
    if platform.system() != "Windows":
        raise ErroDePlataforma("Este serviço está disponível apenas para Windows")

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
