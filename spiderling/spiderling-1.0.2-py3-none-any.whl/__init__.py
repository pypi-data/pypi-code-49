from multiprocessing import Queue
from threading import Thread
import queue
import time
import datetime
import os
from spiderling.listener import Listener
from spiderling.logger import Logger
from spiderling.dispatcher import Dispatcher
from spiderling.sistema import Sistema
import logging
import logging.config
import json
import importlib

FOLDER_LOCATION = os.path.dirname(os.path.abspath(__file__))
FOLDER_LOCATION_LOGS = os.path.join(FOLDER_LOCATION, 'logs')
FOLDER_LOCATION_LOCAL = os.path.join(FOLDER_LOCATION, 'local')


class Spiderling():
    """
    Classe que define o Spiderling
    """
    def __init__(self,
                 dispositivoKonker='',
                 usuarioKonker='',
                 senhaKonker='',
                 lista_acoes=None,
                 intervalo_listening=15,
                 intervalo_health=300,
                 url_konker_pub='http://data.demo.konkerlabs.net:80/pub/',
                 url_konker_sub='http://data.demo.konkerlabs.net:80/sub/',
                 log_settings_path='',
                 settings_file=None):
        """
        Função construtora da Spiderling
        """

        if settings_file:
            settings_file = importlib.import_module(settings_file)

            if 'dispositivoKonker' in settings_file.__dict__ and settings_file.dispositivoKonker != '':
                self.dispositivoKonker = settings_file.dispositivoKonker
            else:
                raise ValueError('dispositivoKonker config variable not set in settings file')

            if 'usuarioKonker' in settings_file.__dict__ and settings_file.usuarioKonker != '':
                self.usuarioKonker = settings_file.usuarioKonker
            else:
                raise ValueError('usuarioKonker config variable not set in settings file')

            if 'senhaKonker' in settings_file.__dict__ and settings_file.senhaKonker != '':
                self.senhaKonker = settings_file.senhaKonker
            else:
                raise ValueError('senhaKonker config variable not set in settings file')

            if 'intervalo_listening' in settings_file.__dict__ and settings_file.intervalo_listening != '':
                self.intervalo_listening = settings_file.intervalo_listening
            else:
                raise ValueError('intervalo_listening config variable not set in settings file')

            if 'intervalo_health' in settings_file.__dict__ and settings_file.intervalo_health != '':
                self.intervalo_health = settings_file.intervalo_health
            else:
                raise ValueError('intervalo_health config variable not set in settings file')

            if 'url_konker_pub' in settings_file.__dict__ and settings_file.url_konker_pub != '':
                self.url_konker_pub = settings_file.url_konker_pub
            else:
                raise ValueError('url_konker_pub config variable not set in settings file')

            if 'url_konker_sub' in settings_file.__dict__ and settings_file.url_konker_sub != '':
                self.url_konker_sub = settings_file.url_konker_sub
            else:
                raise ValueError('url_konker_sub config variable not set in settings file')

            if 'log_settings_path' in settings_file.__dict__ and settings_file.log_settings_path != '':
                self.log_settings_path = settings_file.log_settings_path
            else:
                raise ValueError('log_settings_path config variable not set in settings file')

            if 'lista_acoes' in settings_file.__dict__:
                for acao in settings_file.lista_acoes:
                    if 'nome' not in acao or acao['nome'] == '' and \
                            'tipo_comando' not in acao or acao['tipo_comando'] == '' and \
                            'comando' not in acao or acao['comando'] == '' and \
                            'retorno_padrao' not in acao:
                        raise ValueError('lista_acoes config variable not set properly')
                self.lista_acoes = settings_file.lista_acoes

        else:
            if dispositivoKonker != '':
                self.dispositivoKonker = dispositivoKonker
            else:
                raise ValueError('dispositivoKonker variable cannot be empty')

            if usuarioKonker != '':
                self.usuarioKonker = usuarioKonker
            else:
                raise ValueError('usuarioKonker variable cannot be empty')

            if senhaKonker != '':
                self.senhaKonker = senhaKonker
            else:
                raise ValueError('senhaKonker variable cannot be empty')

            if intervalo_listening != '':
                self.intervalo_listening = intervalo_listening
            else:
                raise ValueError('intervalo_listening variable cannot be empty')

            if intervalo_health != '':
                self.intervalo_health = intervalo_health
            else:
                raise ValueError('intervalo_health variable cannot be empty')

            if url_konker_pub != '':
                self.url_konker_pub = url_konker_pub
            else:
                raise ValueError('url_konker_pub variable cannot be empty')

            if url_konker_sub != '':
                self.url_konker_sub = url_konker_sub
            else:
                raise ValueError('url_konker_sub variable cannot be empty')

            if log_settings_path != '':
                self.log_settings_path = log_settings_path
            else:
                raise ValueError('log_settings_path variable cannot be empty')

            if lista_acoes:
                for acao in lista_acoes:
                    if 'nome' not in acao or acao['nome'] == '' and \
                            'tipo_comando' not in acao or acao['tipo_comando'] == '' and \
                            'comando' not in acao or acao['comando'] == '' and \
                            'retorno_padrao' not in acao:
                        raise ValueError('lista_acoes config variable not set properly')
                self.lista_acoes = lista_acoes

        self.setup_logging(default_path=self.log_settings_path)
        self._logger = logging.getLogger(__name__)

        self.__logger = Logger(self.dispositivoKonker, self.usuarioKonker, self.senhaKonker, self.url_konker_pub)
        self.__listener = Listener(self.usuarioKonker, self.senhaKonker, self.url_konker_sub, self.__logger)
        self.__dispatcher = Dispatcher(self.__logger, self.lista_acoes)

        self.tarefas_para_executar = Queue()
        self.processos_tarefas = []

        self.__data_hora_listening = datetime.datetime.now() - datetime.timedelta(seconds=self.intervalo_listening)
        self.__data_hora_health = datetime.datetime.now() - datetime.timedelta(seconds=self.intervalo_health)

    def setup_logging(self, default_path=os.path.join(FOLDER_LOCATION_LOGS, 'logging.json'), default_level=logging.INFO, env_key='LOG_CFG'):
        """
        Função que executa a configuração de logs do Spiderling
        """
        path = default_path
        value = os.getenv(env_key, None)
        if value:
            path = value
        if os.path.exists(path):
            with open(path, 'rt') as f:
                config = json.load(f)
                for key, handler in config['handlers'].items():
                    if 'filename' in handler:
                        try:
                            os.mkdir('logs')
                        except OSError:
                            pass
                        handler['filename'] = os.path.join('logs', handler['filename'])

            logging.config.dictConfig(config)
        else:
            logging.basicConfig(level=default_level)

    def thread_health(self):
        """
        Função que realiza o disparo da thread de health do dispositivo
        """
        if (datetime.datetime.now() > self.__data_hora_health):
            sistema = Sistema()
            sistema.pegar_health_sistema()
            self.__logger.registrarHealth(sistema)
            self.__data_hora_health = datetime.datetime.now() + datetime.timedelta(seconds=self.intervalo_health)

    def tem_comando(self):
        """
        Função que valida se tem comando de acordo com o ultimo executado
        """
        if (datetime.datetime.now() > self.__data_hora_listening):
            self.__listener.tem_comando(self.tarefas_para_executar)
            self.__data_hora_listening = datetime.datetime.now() + datetime.timedelta(seconds=self.intervalo_listening)

    def executa_tarefas(self):
        """
        Função que valida se existe tarefa de acordo com a fila interna
        """
        def executa_tarefa(tarefa, processos_tarefas):
            self._logger.info(f'Tarefa Encontrada: {tarefa["acao"]}')
            processo_tarefa = Thread(target=self.__dispatcher.executarComando, args=(tarefa['acao'], tarefa['id'], tarefa['registra_execucao']))
            processos_tarefas.append((processo_tarefa, tarefa['acao']))
            processo_tarefa.daemon = True
            processo_tarefa.start()

        try:
            tarefa = self.tarefas_para_executar.get_nowait()
        except queue.Empty:
            pass
        else:
            if tarefa['tipo_execucao'] == 'sequencial':
                for tarefa_processada in self.processos_tarefas:
                    processo, acao = tarefa_processada
                    if processo.is_alive() and tarefa['acao'] == acao:
                        print(f'Ja tem uma tarefa Viva dessa ação: {acao}')
                        self.tarefas_para_executar.put(tarefa)
                        break
                else:
                    executa_tarefa(tarefa, self.processos_tarefas)
            else:
                executa_tarefa(tarefa, self.processos_tarefas)

    def rodar(self):
        """
        Função que realiza o start das funções: thread_health, tem_comando e executa_tarefas
        """
        thread_health = None
        thread_listener = None
        thread_execute = None
        while True:
            # Health
            if not thread_health or not thread_health.is_alive():
                thread_health = Thread(target=self.thread_health)
                thread_health.daemon = True
                thread_health.start()

            # Tem Comando
            if not thread_listener or not thread_listener.is_alive():
                thread_listener = Thread(target=self.tem_comando)
                thread_listener.daemon = True
                thread_listener.start()

            # Executa Tarefas
            if not thread_execute or not thread_execute.is_alive():
                thread_execute = Thread(target=self.executa_tarefas)
                thread_execute.daemon = True
                thread_execute.start()

            time.sleep(1)
