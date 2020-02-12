import logging
import datetime
import subprocess as sp


class Dispatcher():
    """
    Classe que define o Dispatcher que envia os comandos para a Konker
    """
    def __init__(self, logger, lista_acoes):
        """
        Função construtora da classe Dispatcher
        """
        self.__logger = logger
        self._logger = logging.getLogger(__name__)
        self._logger.info("Carregando dispatcher")
        self.lista_acoes = lista_acoes

    def executarComando(self, nome_acao, id, registra_execucao=True):
        """
        Função que executa e registra a execução na Konker
        """
        for acao in self.lista_acoes:
            if acao['nome'] == nome_acao:
                tipo_retorno_padrao = acao['retorno_padrao']
                sucesso = True
                retorno_stdout = ''
                retorno_stderr = ''
                retorno_code = -999
                mensagem = ''
                duracao = 0  # deverá ser calculado para envio na mensagem de sucesso
                duracao = datetime.datetime.now()

                self._logger.info(f"Comando {acao['nome']} inicializado")

                if acao['tipo_comando'] == 'script':
                    retorno_execucao = sp.run([acao['comando']], capture_output=True, universal_newlines=True)
                    retorno_code = retorno_execucao.returncode
                    retorno_stdout = retorno_execucao.stdout
                    retorno_stderr = retorno_execucao.stderr
                elif acao['tipo_comando'] == 'funcao_python':
                    try:
                        retorno_execucao = acao['comando'](acao['nome'])
                    except TypeError:
                        try:
                            retorno_execucao = acao['comando']()
                        except Exception as exc:
                            retorno_code = -999
                            retorno_stderr = f'Erro ao executar funcao: {acao["nome"]} erro: {exc}'
                            retorno_stdout = f'Erro ao executar funcao: {acao["nome"]} erro: {exc}'
                        else:
                            retorno_code = 0
                            retorno_stderr = ''
                            retorno_stdout = retorno_execucao
                    else:
                        retorno_code = 0
                        retorno_stderr = ''
                        retorno_stdout = retorno_execucao

                self._logger.debug(f'RetornoOut: {retorno_stdout}\nRetornoErr: {retorno_stderr}\nRetornoCode: {retorno_code}')
                self._logger.info(f"Comando {acao['nome']} finalizado")
                try:
                    # registro de logs de execução, ignorar se o próprio serviço enviar estes logs
                    # tratar as mensages de retorno para identificar se houve erro
                    duracao = (datetime.datetime.now() - duracao).total_seconds()
                    if registra_execucao:
                        if retorno_code == 0 and retorno_stderr == '':
                            # registrar log de sucesso
                            status = 'sucesso'
                            if tipo_retorno_padrao:
                                mensagem = f'Comando {nome_acao} finalizado com {status} duracao: {duracao}'
                            else:
                                mensagem = retorno_stdout
                            self.__logger.registrarExecucao(nome_acao, id, duracao, mensagem, False, 0)
                            self._logger.info(f"Ação {nome_acao} executada com sucesso")
                        else:
                            # registrar log de erro
                            status = 'falha'
                            codigo_erro = retorno_code
                            mensagem = f'Comando {nome_acao} finalizado com {status} duracao: {duracao}\nErro: {retorno_stderr}'
                            self.__logger.registrarExecucao(nome_acao, id, duracao, mensagem, True, codigo_erro)
                            sucesso = False
                            self._logger.info(f"Ação {nome_acao} falhou. Erro {str(codigo_erro)} - {mensagem}")
                        self.__logger.registrar_report(id, mensagem)
                    return sucesso
                except Exception as e:
                    self._logger.error(f'Erro: {str(e)}')
                    return False
