#!/usr/bin/env python3

import pickle

from matrix import ESAMatrix
from preprocessor import Preprocessor


def main():
	for corpus in ["strategic-intelligence", \
		    	"debatepedia",\
                	"wikipedia" \
                	]:
		corpus_path = "../../../../resources/corpora/" + corpus + ".csv"
		matrix_path = "../../../../resources/esa-w2v/" + corpus + ".mat"
		p = Preprocessor()
		preprocessed = p.preprocess(corpus_path, lemma = True)
		concepts = tuple(preprocessed.keys())
		bows = tuple([preprocessed[bow] for bow in preprocessed])
		terms = tuple(set([word for bow in bows for word in bow]))
		print(len(concepts))
		print(len(bows))
		print(len(terms))

		mat = ESAMatrix(terms, concepts, bows)
		pickle.dump(mat, open(matrix_path, "wb"))


if __name__ == "__main__":
	main()
