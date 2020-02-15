def define_ambiente_de_processamento():
    """Método para definir o ambiente de execução
    """

    import platform
            
    if platform.system() == "Windows":
        from threading import Thread
        return Thread
    from multiprocessing import Process
    return Process


def carregar_arquivo_de_configuracao_do_banco_de_dados(arquivo_de_configuracao: str) -> dict:
    """Função para carregar arquivo de configuração do banco de dados

    Args:
        arquivo_de_configuracao (str): Caminho completo (Absoluto) até o arquivo de configuração. Veja o formato do arquivo de configuração
            [BANCO_DE_DADOS]
            HOST = "127.0.0.1"
            PORTA = 27017
            USUARIO = "USUARIO_DO_BANCO"
            SENHA = "SENHA_DO_BANCO"
    Returns:
        dict: Dicionário com as informações inseridas
    """

    import os
    import configparser
    from dgi.excecoes import ArquivoDeConfiguracaoNaoEncontrado, ArquivoDeConfiguracaoIncorreto

    if not os.path.isfile(arquivo_de_configuracao):
        raise ArquivoDeConfiguracaoNaoEncontrado("O arquivo de configuração indicado não existe!")

    configuracoes = configparser.ConfigParser()
    with open(arquivo_de_configuracao, 'r') as ac:
        configuracoes.read_file(ac)

    if not "BANCO_DE_DADOS" in configuracoes:
        raise ArquivoDeConfiguracaoIncorreto("O arquivo deve possuir a chave `BANCO_DE_DADOS` com as configurações de acesso ao banco")
    
    configuracoes = dict(configuracoes["BANCO_DE_DADOS"])
    configuracoes["porta"] = int(configuracoes["porta"])
    
    return configuracoes
