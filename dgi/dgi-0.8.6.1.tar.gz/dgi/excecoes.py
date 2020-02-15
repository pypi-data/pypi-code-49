class ErroAoAcessarLink(RuntimeError):
    """Exceção para indicar problemas relacionados ao acesso aos links do catalogo do DGI
    """

    def __init__(self, mensagem):
        super().__init__(mensagem)


class DefinicaoInvalida(RuntimeError):
    """Exceção para indicar problemas relacionados a inputs inválidos
    """

    def __init__(self, mensagem):
        super().__init__(mensagem)


class LimiteDoPedidoExcedido(RuntimeError):
    """Exceção para indicar problemas relacionados a quantidade de pedidos realizados
    """

    def __init__(self, mensagem):
        super().__init__(mensagem)


class ArquivoDeConfiguracaoNaoEncontrado(FileNotFoundError):
    """Exceção para indicar problemas relacionados a arquivos de configuração
    """

    def __init__(self, mensagem):
        super().__init__(mensagem)


class ArquivoDeConfiguracaoIncorreto(TypeError):
    """Exceção para indicar problemas relacionados a arquivos de configuração
    """

    def __init__(self, mensagem):
        super().__init__(mensagem)


class ErroNaExecucaoDaBuscaNoServico(RuntimeError):
    """Exceção para indicar problemas relacionados busca de dados nos serviços
    """

    def __init__(self, mensagem):
        super().__init__(mensagem)


class ErroDePlataforma(RuntimeError):
    """Exceção para indicar problemas relacionados a erros de plataforma
    """

    def __init__(self, mensagem):
        super().__init__(mensagem)
