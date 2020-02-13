from typing import List


def filter_docs_by_size(text: str, lt: int = 0) -> str:
    return "" if len(text) < lt else text


def filter_words_by_pos_tag(text: str, model, allowed_postags: List[str] = None) -> str:
    return " ".join(
        [
            token.text
            for token in model(text)
            if (allowed_postags is None or token.pos_ in allowed_postags)
        ]
    )


def filter_words_by_size(text: str, lt: int = 0, gt: int = 999) -> str:
    return " ".join([word for word in text.split() if len(str(word)) in range(lt, gt)])
