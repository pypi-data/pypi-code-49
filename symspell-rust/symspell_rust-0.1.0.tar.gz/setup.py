# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['symspell_rust']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'symspell-rust',
    'version': '0.1.0',
    'description': 'Fast and Accurate SpellChecker',
    'long_description': '# symspell_rust\nRust python bindings for symspell\n\n## Quick examples using Python:\n\n```python\n\n>>> from symspell_rust import SymspellPy\n\n>>> sym_spell = SymspellPy(max_distance=2, prefix_length=7, count_threshold=1)\n\n>>> if not sym_spell.load_dictionary("./data/frequency_dictionary_en_82_765.txt",0,1," "):\n      print("File Not Found")\n\n>>> suggestions = sym_spell.lookup_compound("whereis th elove hehad dated forImuch of thepast who couqdn\'tread in sixtgrade and ins pired him",2)\n\n>>> for cand in suggestions:\n      print(f"Term->{cand.term} \\n Distance->{cand.distance} \\n Count->{cand.count}")\n\n>>> segment_obj = sym_spell.word_segmentation("whereisthelove",2)\n\n>>> print(f"String->{segment_obj.segmented_string} \\n Distance->{segment_obj.distance_sum} \\n Prob_Log_Sum->{segment_obj.prob_log_sum}")\n```',
    'author': 'zoho-labs',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': '',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
