def get_cep(cep : str):
    cep = ''.join(e for e in cep if e.isnumeric())
    url = f"viacep.com.br/ws/{cep}/json/"
    import requests
    try:
        result = requests.get(url).json()
        return result
    except Exception as e:
        import logging
        logging.debug("Erro ao consultar a API :")
        logging.debug(e)