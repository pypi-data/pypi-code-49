from pangeamt_nlp.processor.base.normalizer_base import NormalizerBase
from pangeamt_nlp.seg import Seg
import csv as _csv
import re as _re
import os as _os


class AmericanizerNormalizer(NormalizerBase):
    NAME = "americanizer"

    DESCRIPTION_TRAINING = """
        Apply the americanizer process to the source or the target, checking
        with the src_lang and tgt_lang to decide where to apply it.
    """

    DESCRIPTION_DECODING = """
        Apply the americanizer process to src if src_lang is english, do nothing
        otherwise.
    """

    def __init__(self, src_lang: str, tgt_lang: str) -> None:
        if src_lang is not "en" and tgt_lang is not "en":
            raise ValueError("Americanizer processor requires English")

        super().__init__(src_lang, tgt_lang)
        self._regex = _re.compile(
            r'( |,|;|:|\.|\{|\}|\[|\]|\/|\\|\(|\)|\?|¡|"|\')'
        )
        self._words = {}
        csv_path = _os.path.join(
            _os.path.dirname(_os.path.realpath(__file__)), "americanizer.csv"
        )
        with open(csv_path, newline="") as csvfile:
            spamreader = _csv.reader(csvfile, delimiter=",", quotechar="|")
            for row in spamreader:
                self._words[row[0]] = row[1]

    def normalize(self, txt: str) -> str:
        entry = self._regex.split(txt)
        result = list()

        for item in entry:
            if len(item) < 3:
                result.append(item)
                continue

            if item in self._words:
                result.append(self._words[item])
            else:
                result.append(item)

        return "".join(result)

    def process_train(self, seg: Seg) -> None:
        if self.src_lang == "en":
            seg.src = self.normalize(seg.src)
        else:
            seg.tgt = self.normalize(seg.tgt)

    def process_src_decoding(self, seg: Seg) -> None:
        if self.src_lang == "en":
            seg.src = self.normalize(seg.src)

    def process_tgt_decoding(self, seg: Seg) -> None:
        pass
