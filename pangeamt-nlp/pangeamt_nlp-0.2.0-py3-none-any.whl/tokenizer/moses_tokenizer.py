from pangeamt_nlp.tokenizer.tokenizer_base import TokenizerBase
from sacremoses import MosesTokenizer as _MosesTokenizer


class MosesTokenizer(TokenizerBase):
    NAME = "moses"
    LANGS = [""]

    def __init__(self, lang):
        super().__init__(lang)
        self._mtk = _MosesTokenizer(lang)

    def tokenize(self, text):
        return (" ").join(self._mtk.tokenize(text, escape=False))

    def detokenize(self, text):
        pass
