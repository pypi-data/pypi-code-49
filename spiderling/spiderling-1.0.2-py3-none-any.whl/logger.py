import json
import logging
import requests


class Logger():
    """
    Classe Logger que define os loggers da Konker
    """
    def __init__(self, dispositivoKonker, usuarioKonker, senhaKonker, url_konker_pub):
        """
        Função construtora da classe Logger
        """
        self._logger = logging.getLogger(__name__)
        self.dispositivoKonker = dispositivoKonker
        self.usuarioKonker = usuarioKonker
        self.senhaKonker = senhaKonker
        self.url_konker_pub = url_konker_pub

    def post_konker(self, canal, msg):
        """
        Função que realiza o post para a plataforma da konker
        """
        self._logger.info("Comando post_konker inicializado")

        url = f'{self.url_konker_pub}{self.usuarioKonker}/{canal}'
        headers = {'content-type': 'application/json', 'Accept': 'application/json'}
        auth = (self.usuarioKonker, self.senhaKonker)

        try:
            requests.post(url, headers=headers, auth=auth, data=json.dumps(msg))
        except Exception:
            self._logger.error(f'erro postando na konker msg: {msg} no canal: {canal}', exc_info=1)

        self._logger.info("Comando post_konker finalizado")

    def registrarHealth(self, sistema):
        """
        Função que realiza o registro do log do Health
        """
        self._logger.info("Comando registraHealth inicializado")

        # ## GERAL
        msg = {
            "id": self.dispositivoKonker,
            "health": 1,
            "host": {
                "name": sistema.hostname,
                "ip": sistema.ip,
                "memory": {
                    "perc": sistema.memoria_perc,
                    "mb": sistema.memoria_usada
                },
                "cpu": sistema.cpu,
                "swap": {
                    "perc": sistema.swap_perc,
                    "mb": sistema.swap_usada
                },
                "disks": sistema.disco
            }
        }

        self.post_konker('health', msg)

        self._logger.info("Comando registraHealth finalizado")

    def registrarExecucao(self, nome_operacao, id, duracao, mensagem, erro, codigo_erro):
        """
        Função que realiza o registro da execução da operação
        """
        self._logger.info("Comando registraExecucao inicializado")

        # ## GERAL
        if not erro:
            msg = {"action": nome_operacao, "id": id, "status": 'sucess', "message": mensagem, "duration": duracao, }
        else:
            msg = {"action": nome_operacao, "id": id, "status": 'failure', "message": str(f'error : {str(codigo_erro)} - {mensagem}')}

        self.post_konker('log', msg)

        self._logger.info("Comando registraExecucao finalizado")

    def registrarCiencia(self, nome_operacao, id):
        """
        Função que registra a confirmação de recebimento do comando
        """
        self._logger.info("Comando registraCiencia inicializado")

        msg = {'type': 'ack', "action": nome_operacao, "id": id}

        self.post_konker('ack', msg)

        self._logger.info("Comando registraCiencia finalizado")

    def registrar_report(self, id, msg_report):
        """
        Função que registra a mensagem de report
        """
        self._logger.info("Comando registraReport inicializado")

        msg = {'type': 'report', 'id': id, 'msg': msg_report}

        self.post_konker('report', msg)

        self._logger.info("Comando registraReport finalizado")

    def registrar_execucao_modelo(self, acao, operacao, dataExecucao, periodo, duracao, mensagem, mape, acuracia, erro, codigo_erro):
        self._logger.info("Comando registrar_execucao_modelo inicializado")

        if not erro:
            msg = {
                "action": acao,
                "operacao": operacao,
                "status": 'sucess',
                "message": mensagem,
                "dt_execucao": str(dataExecucao.isoformat()),
                "periodo": periodo,
                "duration": duracao,
                "mape": mape,
                "precisao": acuracia
            }
        else:
            msg = {
                "action": acao,
                "operacao": operacao,
                "status": 'failure',
                "message": f'error: {str(codigo_erro)} - {mensagem}',
            }

        self.post_konker('log', msg)

        self._logger.info("Comando registrar_execucao_modelo finalizado")
