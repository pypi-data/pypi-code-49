from .text import Text
def text_preprocessing(text):
    """
    :param text (str): raw text you wanna preprocess
    :return: normalize text
    """
    return Text(text).normalize()