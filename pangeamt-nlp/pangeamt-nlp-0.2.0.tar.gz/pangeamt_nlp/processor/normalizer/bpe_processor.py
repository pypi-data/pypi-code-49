from pangeamt_nlp.processor.base.normalizer_base import NormalizerBase
from pangeamt_nlp.seg import Seg
from pangeamt_nlp.types import File
from typing import List, Set, Sequence
from re import sub as _sub
import codecs as _codecs
from subword_nmt.apply_bpe import BPE as _BPE
from subword_nmt.apply_bpe import read_vocabulary as _rv


class BPEProcessor(NormalizerBase):
    NAME = "bpe"

    DESCRIPTION_TRAINING = """
        Splits unknown words with @@ as a mark: superman -> super@@ man
    """
    DESCRIPTION_DECODING = """
        Splits unknown words on source and joins them on target
    """

    def __init__(
        self,
        src_lang: str,
        tgt_lang: str,
        bpe_codes: File,
        bpe_vocab: File = None,
        bpe_threshold: int = 50,
        bpe_glossaries: Sequence[str] = None,
    ) -> None:

        super().__init__(src_lang, tgt_lang)

        if bpe_glossaries:
            _glossaries = [self._parse_glossary(i) for i in bpe_glossaries]
        else:
            _glossaries = []

        if bpe_vocab:
            _vocab = _parse_vocab(bpe_vocab)
            self._bpe = _BPE(
                _codecs.open(bpe_codes, encoding="utf-8"),
                vocab=_vocab,
                glossaries=_glossaries,
            )
        else:
            self._bpe = _BPE(_codecs.open(bpe_codes, encoding="utf-8"))

    def _parse_glossary(self, str: str) -> str:
        return str.encode("utf-8").decode("utf-8")

    def _parse_vocab(self, path: File) -> Set:
        return _rv(_codecs.open(path, encoding="utf-8"), bpe_threshold)

    def process_train(self, seg: Seg) -> None:
        seg.src = self._bpe.process_line(seg.src)
        seg.tgt = self._bpe.process_line(seg.tgt)

    def process_src_decoding(self, seg: Seg) -> None:
        seg.src = self._bpe.process_line(seg.src)

    def process_tgt_decoding(self, seg: Seg) -> None:
        seg.tgt = _sub("(@@ )|(@@ ?$)", "", seg.tgt)
