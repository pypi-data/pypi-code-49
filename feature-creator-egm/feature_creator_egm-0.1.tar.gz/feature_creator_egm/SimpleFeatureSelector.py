import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import re
from .Basic_Feature_Creator import BasicFeatureSelector


class SimpleFeatureSelector(BasicFeatureSelector):

    def __init__(self, sample_features=1,  sample_size = 3, lang="english"):
        """ FeatureSelector class to select features/words
            for text classification scripts

        Args:
            frequency (float): the minimum frequency of a word in the
            document over total word count that a word
            should have to be selected as a potential feauture
            min_weight(float): minimum weight that a word should
            have to be selected as a feauture


        Attributes:

            standard_features(int): A standard number of selected features
            given a standard sample size
            sample_size(int): A threshhold sample size
            word_dictionary(dictionary) : The dictionary of words and counts
            freuqency_number = The number that will be used
            to select the top frequency_number words that will be selected



            """
        self.standard_features = sample_features
        self.sample_size = sample_size
        self.word_dictionary = {}
        self.frequency_number = 0
        #self.wordfreq = {}
        #self.wordfreq = {}
        frequency = sample_features/sample_size
        BasicFeatureSelector.__init__(self,frequency,sample_features,lang)







    def frequency_dictionary(self):
        """ Function that creates the frequency dictionary with
            the count of occurances of each word
            The word will be the keys and the values would be the
            count of occurances of the word in the string

        Args:
            The list of Senteces

        Returns:


        """

        for word in self.words:
            if word not in self.word_dictionary.keys():
                self.word_dictionary[word] = 1
            else:
                self.word_dictionary[word] += 1

    def feature_selection(self):
        import heapq
        self.frequency_number = int(round(self.frequency_ratio * len(self.words)))
        self.selected_features = heapq.nlargest(self.frequency_number,self.word_dictionary, key=self.word_dictionary.get)

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
