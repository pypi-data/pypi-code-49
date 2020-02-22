# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['ja_sentence_segmenter',
 'ja_sentence_segmenter.common',
 'ja_sentence_segmenter.concatenate',
 'ja_sentence_segmenter.normalize',
 'ja_sentence_segmenter.split']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'ja-sentence-segmenter',
    'version': '0.0.2',
    'description': 'sentence segmenter for japanese text',
    'long_description': '# ja_sentence_segmenter\n日本語のテキストに対して、ルールベースによる文区切り（sentence segmentation）を行います。\n\n## Getting Started\n\n### Prerequisites\n* Python 3.6+\n\n### Installing\n`pip install ja_sentence_segmenter`\n\n### Usage\n```Python\nimport functools\n\nfrom ja_sentence_segmenter.common.pipeline import make_pipeline\nfrom ja_sentence_segmenter.concatenate.simple_concatenator import concatenate_matching\nfrom ja_sentence_segmenter.normalize.neologd_normalizer import normalize\nfrom ja_sentence_segmenter.split.simple_splitter import split_newline, split_punctuation\n\nsplit_punc2 = functools.partial(split_punctuation, punctuations=r"。!?")\nconcat_tail_no = functools.partial(concatenate_matching, former_matching_rule=r"^(?P<result>.+)(の)$", remove_former_matched=False)\nsegmenter = make_pipeline(normalize, split_newline, concat_tail_no, split_punc2)\n\n# Golden Rule: Simple period to end sentence #001 (from https://github.com/diasks2/pragmatic_segmenter/blob/master/spec/pragmatic_segmenter/languages/japanese_spec.rb#L6)\ntext1 = "これはペンです。それはマーカーです。"\nprint(list(segmenter(text1)))\n```\n\n```\n> ["これはペンです。", "それはマーカーです。"]\n```\n\n## Versioning\nWe use SemVer for versioning. For the versions available, see the tags on this repository.\n\n## Contributing\nTODO\n\n## License\nMIT\n\n## Acknowledgments\n\n### テキストの正規化処理\nテキスト正規化のコードは、[mecab-ipadic-NEologd](https://github.com/neologd/mecab-ipadic-neologd)の以下のWIKIを参考に一部修正を加えています。\n\nサンプルコードの提供者であるhideaki-t氏とoverlast氏に感謝します。\n\nhttps://github.com/neologd/mecab-ipadic-neologd/wiki/Regexp.ja#python-written-by-hideaki-t--overlast\n\n### 文区切り（sentence segmentation）のルール\n文区切りのルールとして、[Pragmatic Segmenter](https://github.com/diasks2/pragmatic_segmenter)の日本語ルールを参考にしました。\n\nhttps://github.com/diasks2/pragmatic_segmenter#golden-rules-japanese\n\nまた、以下のテストコード中で用いられているテストデータを、本PJのテストコードで利用しました。\n\nhttps://github.com/diasks2/pragmatic_segmenter/blob/master/spec/pragmatic_segmenter/languages/japanese_spec.rb\n\n作者のKevin S. Dias氏と[コントリビュータの方々](https://github.com/diasks2/pragmatic_segmenter/graphs/contributors)に感謝します。\n\nThanks to Kevin S. Dias and [contributors](https://github.com/diasks2/pragmatic_segmenter/graphs/contributors).\n',
    'author': 'wwwcojp',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/wwwcojp',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
