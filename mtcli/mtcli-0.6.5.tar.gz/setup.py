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
    'version': '0.6.5',
    'description': 'Utilitario de linha de comando para leitura de graficos do MetaTrader 5',
    'long_description': '# mtcli  \n  \nUtilitário de linha de comando para leitura de gráficos do MetaTrader 5.  \n  \n[PyPI](https://pypi.python.org/pypi/mtcli)  \n[Documentação](https://vfranca.github.io/mtcli)  \n  \n------------\n\n## Pré-requisitos  \n\n* [MetaTrader5](https://www.metatrader5.com/pt) - Plataforma de trading.  \n* [GeraCSV.ex5](https://drive.google.com/file/d/1ijglZp05ZI29VzrMKTbKrQFO6CYPznyp/view?usp=sharing) - Expert advisor executando no MetaTrader5.  \n* [Python](https://www.python.org/) - Interpretador de comandos disponível no prompt de comando.  \n\n\n## Instalação\n\n```\n> pip install mtcli\n```\n\n### Arquivo .env  \n  \nCrie um arquivo .env na pasta raiz do Windows com o conteúdo abaixo:  \n  \n```\nDIGITS="2"  \nCSV_PATH=<caminho_dos_arquivos_do_metatrader5>  \n```\n  \n  \n### Arquivos mtcli  \n\nUma pasta compactada está disponível para download contendo os arquivos acima descritos para uso com o mtcli bem como instruções de como usá-los.  \nSegue o link para download: https://drive.google.com/open?id=1olFEKJnnunBI1SDoW7QoMT9p6_yRQyhp  \n  \n  \n## Comandos  \n  \n* [mt bars](chart.md) - Exibe as barras do gráfico.  \n* [mt sma](chart.md) - Exibe a média móvel simples.  \n* [mt ema](chart.md) - Exibe a média móvel exponencial.  \n* [mt atr](chart.md) - Exibe average true range.  \n* [mt fib](chart.md) - Exibe retrações e projeções de fibonacci.  \n\n------------\n  \n  ## Agradecimentos  \n  \nAgradecimentos ao @MaiconBaggio desenvolvedor do PyMQL5 que faz uma comunicação com o MetaTrader5 e fornecedor do robô que faz a geração automática dos arquivos CSV.  \n\n------------\n  \n## Licenciamento  \n\nEste pacote é software livre e está licenciado sob os termos da [MIT](../LICENSE).  \n',
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
