# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['mtcli', 'mtcli.indicator']

package_data = \
{'': ['*']}

install_requires = \
['click>=7.0,<8.0', 'pymql5>=1.2.0,<2.0.0', 'python-dotenv>=0.10.3,<0.11.0']

entry_points = \
{'console_scripts': ['atr = mtcli.cli:atr',
                     'bars = mtcli.cli:bars',
                     'buy = mtcli.cli:buy',
                     'cancel = mtcli.cli:cancel',
                     'ema = mtcli.cli:ema',
                     'fib = mtcli.cli:fib',
                     'mt = mtcli.cli:cli',
                     'order = mtcli.cli:orders',
                     'position = mtcli.cli:positions',
                     'sell = mtcli.cli:sell',
                     'sma = mtcli.cli:sma']}

setup_kwargs = {
    'name': 'mtcli',
    'version': '0.6.3',
    'description': 'Utilitario de linha de comando para leitura de graficos do MetaTrader 5',
    'long_description': '# mtcli  \n  \nUtilitário de linha de comando para leitura de gráficos do MetaTrader 5.  \n  \n[PyPI](https://pypi.python.org/pypi/mtcli)  \n[Documentação](https://vfranca.github.io/mtcli)  \n  \n## Pré-requisitos  \n  \n* [MetaTrader 5](https://www.metatrader5.com/) - plataforma de trading.  \n* [GeraCSV.ex5](https://drive.google.com/open?id=1jSSCRJnRg8Ag_sX_ZZAT4YJ2xnncSSAe) - robô executado no MetaTrader 5.  \n  \n## Instalação\n  \n```\npip install mtcli\n```\n  \n  \n### Procedimento no MetaTrader 5  \n  \n1. Faça o download do GeraCSV.ex5.  \n2. Execute o MetaTrader 5 e abra um gráfico.  \n3. Execute o GeraCSV.ex5.  \n4. Selecione a opção "anexar ao gráfico" no menu de contexto do GeraCSV.ex5.  \n  \n  \n### Arquivo .env  \n  \nCrie um arquivo .env na pasta raiz do Windows com o conteúdo abaixo:  \n  \n```\nDIGITS="2"  \nCSV_PATH=<caminho_dos_arquivos_do_metatrader5>  \n```\n  \n  \n### Arquivos mtcli  \n\nUma pasta compactada está disponível para download contendo os arquivos acima descritos necessários para uso com o mtcli bem como instruções de como usá-los.  \nSegue o link para download: https://drive.google.com/open?id=1olFEKJnnunBI1SDoW7QoMT9p6_yRQyhp  \n  \n  \n## Exemplos de Uso  \n  \n```\nPara exibir as últimas 20 barras do diário do winq19:  \nmt bars winq19 -p daily -c 20  \n\nPara exibir o canal das últimas 20 barras do diário do winq19:  \nmt bars winq19 -p daily -v ch -c 20  \n\nPara exibir o preço de fechamento das últimas 20 barras do diário do winq19:  \nmt bars winq19 -p daily -v c -c 20  \n\nPara exibir o preço máximo das últimas 20 barras do diário do winq19:  \nmt bars winq19 -p daily -v h -c 20  \n\nPara exibir o preço mínimo das últimas 20 barras do diário do winq19  \nmt bars winq19 -p daily -v l -c 20\n\nPara exibir o range das últimas 20 barras do diário do winq19:  \nmt bars winq19 -p daily -v r -c 20  \n\nPara exibir o volume das últimas 20 barras do diário do winq19:  \nmt bars winq19 -p daily -v vol -c 20  \n\nPara exibir o ATR(14) do diário do winq19:  \nmt atr winq19 -p daily  \n\nPara exibir o ATR(20) do diário do winq19:  \nmt atr winq19 -p daily -c 20  \n\nPara exibir a média móvel aritmética de 20 períodos do diário do winq19:  \nmt sma winq19 -p daily -c 20  \n\nPara exibir as retrações e extensões de Fibonacci entre 103900 e 102100 na tendência de alta:  \nmt fib 103900 102100 h  \n\nPara exibir as retrações e extensões de Fibonacci entre 103900 e 102100 na tendência de baixa:  \nmt fib 103900 102100 l  \n```\n  \nAgradecimentos ao @MaiconBaggio, que além de outras importantes contribuições, gentilmente forneceu o expert advisor GeraCSV.ex5 do MetaTrader 5.  \n  \nEste pacote é software livre e está licensiado sob os termos da [MIT](../LICENSE).  \n',
    'author': 'Valmir Franca',
    'author_email': 'vfranca3@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/vfranca/mtcli',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
