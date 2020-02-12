import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import re

#set(stopwords.words('english'))
class BasicFeatureSelector:

    def __init__(self, frequency = 0, minimum_words=2, language="english"):
        """ BasicFeatureSelector generic class to select features/words
            for text classification scripts

        Args:
            frequency (float): the minimum frequency of a word in the
            document over total word count that a word
            should have to be selected as a potential feauture
            min_weight(float): minimum weight that a word should
            have to be selected as a feauture
        Attributes:
            words(list): List of cleaned words extracted from text and
            cleaned from stop words
            frequency_ratio(int): Minimum frequency ratio of a word count/
            total word count which will be used to select
            features
            minimum_word_count(int): Minimum number of words in
            features list
            selected_features(list): the list of selected word based
            on the frequency ratio parameter


            """
        set(stopwords.words(language))
        self.words = []
        self.selected_features = []
        self.frequency_ratio = frequency
        #self.word_dictionary = {}
        #self.wordfreq = {}
        self.minimum_word_count = minimum_words

    def read_file(self, file_name):
        """ Function to read data from a text file and
            uses an nltj sentecnce tokenizer to turn the
            text into a list of sentences.
            See: https://stackoverflow.com/questions/37605710/
            tokenize-a-paragraph-into-sentence-and-then-into-words-in-nltk

        Args:
                The filename (string)

        Returns:
                text (String) the text read from the file
        """
        with open(file_name) as file:
                text = ""
                line = file.readline()
                while line:
                        text += line
                        line = file.readline()
        return text
