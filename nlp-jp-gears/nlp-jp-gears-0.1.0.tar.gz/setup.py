# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['nlp_jp_gears']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'nlp-jp-gears',
    'version': '0.1.0',
    'description': '',
    'long_description': '# NLP JP Gears\n\n![](https://github.com/tokusumi/nlp-jp-gears/workflows/Tests/badge.svg)\n\n## Overview\n\n日本語の自然言語処理で頻出の前処理をまとめたものです。pipelineをしいて、複数の処理をまとめることができます。\n\n## API\n\n- pipelineの作成: composer.Composer\n- 全角英数字記号を半角に変換: zenhan.ZenToHanConverter\n- 半角英数字記号を全角に変換: zenhan.HanToZenConverter\n- 括弧とその間のテキストを削除: remover.TextBtwBracketsRemover\n\n## Example\n\n```py\n>>> from nlp_jp_gears import Composer\n>>> from nlp_jp_gears import (\n...     ZenToHanConverter,\n...     TextBtwBracketsRemover\n... )\n>>>\n>>> txt_btw_brackets_remover = TextBtwBracketsRemover()\n>>> print(txt_btw_brackets_remover.removes)\n<{[(「『（［〈《〔｛«‹\n>>>\n>>> zenhan_converter = ZenToHanConverter()\n>>> print(zenhan_converter.converts)\n！＂＃＄％＆＇（）＊＋，－．／：；＜＝＞？＠［＼］＾＿｀｛｜｝～０１２３４５６７８９ＡＢＣＤＥＦＧＨＩＪＫＬＭＮＯＰＱＲＳＴＵＶＷＸＹＺａｂｃｄｅｆｇｈｉｊｋｌｍｎｏｐｑｒｓｔｕｖｗｘｙｚ\n>>>\n>>> composer = Composer(txt_btw_brackets_remover, zenhan_converter)\n>>> text = "Ｐｙｔｈｏｎ（パイソン）で自然言語処理？"\n>>> out = composer(text)\n>>> print(out)\nPythonで自然言語処理?\n```\n',
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
