from pangeamt_nlp.tokenizer.tokenizer_base import TokenizerBase
from MeCab import Tagger as _Tagger


class MecabTokenizer(TokenizerBase):
    NAME = "mecab"
    LANGS = ["ja"]

    def __init__(self, lang):
        super().__init__(lang)
        self._tok = _Tagger("-Owakati")

    def tokenize(self, text):
        return self._tok.parse(text)

    def detokenize(self, text):
        pass
