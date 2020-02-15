def adiciona_log(arquivo_de_log, temporal=True, rotacao="600 MB"):
    """Decorador para adicionar instância de log em funções decoradas

    Parameters:
        arquivo_de_log (str): Caminho absoluto do arquivo onde o log será salvo
        
        temporal (bool): Indica se para cada execução da função um arquivo de log com a data deve ser criada. Caso seja temporal
        o nome do `arquivo_de_log` deverá ser um template (E.g. /tmp/log_{}.log)
        
        rotacao (str): Tamanho máximo do arquivo de log

    Returns:
        function: wrapper
   """

    def fnc_adiciona_log(fnc):
        def wrapper(*args):
            from loguru import logger
            if temporal:
                from datetime import datetime
                logger.add(arquivo_de_log.format(datetime.now().strftime("%d_%m_%y_%H%M%S")))
            else:
                logger.add(arquivo_de_log, rotation=rotacao)            
            return fnc(*args)
        return wrapper
    return fnc_adiciona_log
