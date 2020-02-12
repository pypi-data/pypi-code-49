import language_check
from gingerit.gingerit import GingerIt
from textblob import TextBlob


def count_word_changed(original_text: str, update_text: str) -> float:
    original_text = original_text.split(" ")
    update_text = update_text.split(" ")

    original_len = len(original_text)
    update_len = len(update_text)

    changed_count = 0
    if original_len == update_len:
        for i in range(original_len):
            if original_text[i] != update_text[i]:
                changed_count += 1
    else:
        return 0

    return 1 - (changed_count / original_len)


def correct_grammar(input_text: str) -> str:
    tool = language_check.LanguageTool("en-US")
    matches = tool.check(input_text)
    return language_check.correct(input_text, matches)


def execute(text: str) -> float:
    error_rate_threshold = 0
    quality_score = 0

    try:
        updated_text = correct_grammar(text)
        quality_score = count_word_changed(text, updated_text)

        if quality_score <= error_rate_threshold:
            updated_text = TextBlob(text).correct().string
            quality_score = count_word_changed(text, updated_text)

            if quality_score <= error_rate_threshold:
                updated_text = GingerIt().parse(text)["result"]
                quality_score = count_word_changed(text, updated_text)

    except:
        print("Text cannot be checked - {}".format(text))

    return quality_score
