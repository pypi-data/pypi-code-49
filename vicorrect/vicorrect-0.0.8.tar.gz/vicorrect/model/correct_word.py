from vicorrect.helper.telex import Telex
from vicorrect.datastructures.sentence import Sentence
from collections import Counter
from sklearn.metrics.pairwise import cosine_distances
import numpy as np
import time

class CorrectWord:

    def __init__(self, vocabPath=None):
        self.vocabPath = vocabPath
        self.vectorGenerate()
        self.searchInit()

    def predict(self, word, size=1):
        nWord = Sentence(word).remove_accents()
        if word != nWord: return [(
            word, nWord, word, 0
        )]
        words = Telex(word).invert()
        scores = []
        for word in words:
            results = self.retrieval(word)
            scores.extend(self.ranking(word, results))
        scores = sorted(scores, key=lambda x: -x[3])
        return scores[:size]

    def score(self, query, word, ngrams=(2, 3)):
        score = 0
        for n in ngrams:
            if (n > len(query)) or (n > len(word)): break
            queryItems = [query[i : i + n] for i in range(len(query) - n + 1)]
            wordItems = [word[i : i + n] for i in range(len(word) - n + 1)]
            currentScore = len(set(queryItems).intersection(set(wordItems))) / max(len(wordItems), len(queryItems))
            score += currentScore * n
        return score

    def ranking(self, query, results):
        scores = []
        for aWord, nWord, rWord in results:
            score = self.score(query, nWord) # + self.score(query, rWord)
            scores.append((aWord, nWord, rWord, score))
        scores = sorted(scores, key=lambda x: -x[3])
        return scores

    def retrieval(self, word, nRetrieval=30):
        v = self.convertToVector(Counter(list(word)))
        xq = np.array([v])
        ranked_list = [(score[0], i) for i, score in enumerate(cosine_distances(self.Vectors, xq))]
        ranked_list = sorted(ranked_list)[:10]
        scores = [ranked_list[0][0]]
        indices = []
        for item in ranked_list:
            if item[0] == scores[-1]:
                scores.append(item[0])
                indices.append(item[1])
        results = []
        for index in indices:
            results.append((
                self.aWords[index], 
                Sentence(self.aWords[index]).remove_accents(),
                self.Words[index]))
        return results

    def searchInit(self):
        self.dimension = 26

    def vectorGenerate(self):
        text = open(self.vocabPath).read()
        words = text.splitlines()
        startTime = time.time()
        items = [(word, Telex(word).invert()) for word in words]
        self.aWords, self.Words, self.Vectors = [], [], []
        for item in items:
            word, item = item
            for i in item:
                counterItem = Counter(list(i))
                vector = self.convertToVector(counterItem)
                self.aWords.append(word)
                self.Words.append(i)
                self.Vectors.append(vector)
        self.Vectors = np.array(self.Vectors)

    def convertToVector(self, counter):
        vector = [0] * 26
        for key, val in counter.items():
            index = ord(key) - ord('a')
            if (index >=0) and (index < 26): vector[index] = val
        return np.array(vector).astype("float32")


# if __name__ == "__main__":
#     words = CorrectWord("/home/hanhlv/am-ngu.txt").predict("bongr", 2)
#     print(words)

# from lib.algorithms.telex import Telex

# self.vocabPath = "./data/vocab/Viet74K.txt"
# VOCAB_OUT = "./data/vocab/vocab.txt"
# VLOWER = u'àáâãèéêìíòóôõùúýăđĩũơưạảấầẩẫậắằẳẵặẹẻẽếềểễệỉịọỏốồổỗộớờởỡợụủứừửữựỳỵỷỹ'

# class Main:

#     def __init__(self):
#         text = open(self.vocabPath).read()
#         words = [w.lower() for w in text.splitlines()]
#         distinctWords = set()
#         for word in words: distinctWords.update(word.split())
#         distinctWords = [w for w in distinctWords if self.check(w)]
#         distinctWords.sort()
#         text = "\n".join(distinctWords)
#         f = open(VOCAB_OUT, "w")
#         f.write(text)
#         f.close()
#         # listInverts = Telex("được").invert()
#         # print(listInverts)
    
#     def check(self, word):
#         if not word.isalpha(): return False
#         # for c in word:
#         #     if c in VLOWER: return True
#         # return False
#         return True

# if __name__ == "__main__":
#     Main()

