import logging
import requests


class Listener():
    """
    Classe que define o Listener que recebe os comandos da Konker
    """

    def __init__(self, usuarioKonker, senhaKonker, url_konker_sub, logger):
        """
        Função construtora da classe Listener
        """
        self.__logger = logger
        self._logger = logging.getLogger(__name__)
        self.usuarioKonker = usuarioKonker
        self.senhaKonker = senhaKonker
        self.url_konker_sub = url_konker_sub
        self._logger.info("carregando listener")

    def tem_comando(self, tarefas_para_executar):
        """
        Função que valida se tem comando no dispositivo e autentica o usuario na Konker
        """
        self._logger.info('Comando tem_comando inicializado')

        url = f'{self.url_konker_sub}{self.usuarioKonker}/cmd'
        headers = {'content-type': 'application/json', 'Accept': 'application/json'}
        auth = (self.usuarioKonker, self.senhaKonker)
        try:
            comando = requests.get(url, headers=headers, auth=auth).json()
        except Exception:
            pass
        else:
            if comando:
                if 'maestro' in comando[0]['meta']['incoming']['deviceId'] and \
                        comando[0]['meta']['outgoing']['channel'] == 'cmd' and \
                        comando[0]['data']['type'] == 'execution':
                    tarefa_dict = {
                        'acao': comando[0]['data']['action'],
                        'id': comando[0]['data']['id'],
                        'registra_execucao': True,
                        'tipo_execucao': comando[0]['data'].get('tipo_execucao', 'sequencial')
                    }
                    self.__logger.registrarCiencia(tarefa_dict['acao'], tarefa_dict['id'])
                    tarefas_para_executar.put(tarefa_dict)

        self._logger.info("Comando tem_comando finalizado")
        return comando
