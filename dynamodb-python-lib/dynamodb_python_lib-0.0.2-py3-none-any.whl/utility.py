from dynamodb_python_lib.utilities import annotating_data
from dynamodb_python_lib.utilities import cleaning_data
from dynamodb_python_lib.utilities import scoring_data
from dynamodb_python_lib.utilities import tagging_level_1_ner


class Utility:
    @staticmethod
    def clean(text: str) -> str:
        return cleaning_data.execute(text)

    @staticmethod
    def annotate(text: str) -> str:
        return annotating_data.execute(text)

    @staticmethod
    def score(text: str) -> str:
        return scoring_data.execute(text)

    @staticmethod
    def tag_level_1_ner(text: str, product: str) -> str:
        return tagging_level_1_ner.execute(text, product)
