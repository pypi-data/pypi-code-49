import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import re

set(stopwords.words('english'))
class FeatureSelector:

    def __init__(self, frequency=0.3,lang="english"):
        """ FeatureSelector class to select features/words
            for text classification scripts

        Args:
            frequency (float): the minimum frequency of a word in the
            document over total word count that a word
            should have to be selected as a potential feauture
            min_weight(float): minimum weight that a word should
            have to be selected as a feauture
        Attributes:
            file(str): the name of the file with the text
            whose feautures or relevant words will be selected
            for text classification algorithms
            frequency(int): Minimum frequency ratio of a word count/
            total word count wich will be used to select
            features
            min_weight(float): minimum weight that a word should
            have to be selected as a feature

            words(list): A list of words
            word_dictionary (dictionary) : a dictionary or words
            selected_features(list): the list of selected word based
            on the frequency ratio parameter


            """
        self.words = []
        self.frequency_ratio = frequency
        self.word_dictionary = {}
        self.wordfreq = {}

        self.selected_features = []



        set(stopwords.words(lang))
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



    def frequency_dictionary(self):
        """ Function that creates the frequency dictionary with
            the count of occurances of each word
            The word will be the keys and the values would be the
            count of occurances of the word in the string

        Args:
            The list of Senteces

        Returns:


        """
        self.wordfreq = {}
        for word in self.words:
            if word not in self.wordfreq.keys():
                self.wordfreq[word] = 1
            else:
                self.wordfreq[word] += 1

        self.word_dictionary =  self.wordfreq








    def feature_selection(self, frequency):
        """ Function that makes the feature selection
            by filtering out words with low frequency

        Args:
            frequency(float) : The frequency ratio of a word.
            We will multiply this number by total words to select
            the top n words with highest frequency

        Returns:
            a list of words which have been selected as features
        """
        import heapq
        self.frequency_ratio = frequency
        frequency_number = int(round(frequency * len(self.words)))
        self.selected_features = heapq.nlargest(frequency_number,
                                       self.wordfreq, key=self.wordfreq.get)

        return self.selected_features

    def prepare_word_array(self, text):


        list_of_tokens = word_tokenize(text)
        list_of_tokens_no_stop_words = []

        for token in list_of_tokens:
            if token not in stopwords.words():
                list_of_tokens_no_stop_words.append(token)

        self.words = list_of_tokens_no_stop_words
        cleaned_text = " ".join(self.words).join("\n\n")
        list_of_cleaned_sentences = nltk.sent_tokenize(cleaned_text)

        for i in range(len(list_of_cleaned_sentences)):
            list_of_cleaned_sentences [i] = list_of_cleaned_sentences [i].lower()
            list_of_cleaned_sentences [i] = re.sub(r'\W',' ',list_of_cleaned_sentences [i])
            list_of_cleaned_sentences [i] = re.sub(r'\s+',' ',list_of_cleaned_sentences [i])
        cleaned_words = " ".join(list_of_cleaned_sentences).join("\n\n")
        list_of_cleaned_words = word_tokenize(cleaned_words)

        list_of_cleaned_tokens = []
        for token in list_of_cleaned_words:
            list_of_cleaned_tokens.append(token)
        self.words = list_of_cleaned_tokens

















    print("hi there")
