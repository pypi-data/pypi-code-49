# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['nlp_jp_gears']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'nlp-jp-gears',
    'version': '0.1.1',
    'description': '',
    'long_description': '# NLP JP Gears\n\n[![PyPI version](https://badge.fury.io/py/nlp-jp-gears.svg)](https://badge.fury.io/py/nlp-jp-gears)\n![](https://github.com/tokusumi/nlp-jp-gears/workflows/Tests/badge.svg)\n\n\n## Overview\n\n日本語の自然言語処理で頻出の前処理をまとめたものです。pipelineをしいて、複数の処理をまとめることができます。\n\n## API\n\n- pipelineの作成: composer.Composer\n- 全角英数字記号を半角に変換: zenhan.ZenToHanConverter\n- 半角英数字記号を全角に変換: zenhan.HanToZenConverter\n- 括弧とその間のテキストを削除: remover.TextBtwBracketsRemover\n\n## Requirements\n\nPython 3.6+\n\n## Installation\n\n```bash\npip install nlp-jp-gears\n```\n\n## Example\n\n```py\nfrom nlp_jp_gears import Composer\nfrom nlp_jp_gears import (\n    ZenToHanConverter,\n    TextBtwBracketsRemover\n)\n\ntxt_btw_brackets_remover = TextBtwBracketsRemover()\nzenhan_converter = ZenToHanConverter()\n\ncomposer = Composer(txt_btw_brackets_remover, zenhan_converter)\ntext = "Ｐｙｔｈｏｎ（パイソン）で自然言語処理？"\nout = composer(text)\nprint(out)\n```\n\nThen, input text is preprocessed.\n\n```txt\nPythonで自然言語処理?\n```\n\nAnd you can check what is removed and converted, as follows,\n\n```py\nprint(txt_btw_brackets_remover.removes)\nprint(zenhan_converter.converts)\n```\n\n```txt\n<{[(「『（［〈《〔｛«‹\n\n！＂＃＄％＆＇（）＊＋，－．／：；＜＝＞？＠［＼］＾＿｀｛｜｝～０１２３４５６７８９ＡＢＣＤＥＦＧＨＩＪＫＬＭＮＯＰＱＲＳＴＵＶＷＸＹＺａｂｃｄｅｆｇｈｉｊｋｌｍｎｏｐｑｒｓｔｕｖｗｘｙｚ\n```',
    'author': 'Tokusumi',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/tokusumi/nlp-jp-gears',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
