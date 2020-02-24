import numpy as np
import time
import sklearn.metrics.pairwise as sk
from scipy import sparse
from scipy.sparse.linalg import norm



class Similarity:

    def __init__(self):
        pass

    def cosine_similarity(input_vec, concept_vec):
        start_time = time.time()
        similarity = sk.cosine_similarity(input_vec.transpose().todense(), concept_vec.transpose().todense())[0,0]
        end_time = time.time()
        return (similarity, end_time - start_time, 1)
        

    def maximum_matching_similarity(model, input_vec, concept_vec, input_terms, corpus_terms):
        s = model.similarity
        comparisons = 0
        start_time = time.time()
        t1 = input_terms
        t2 = corpus_terms
        ind2 = concept_vec.indices
        similarity = 0.0
        for i in input_vec.indices:
            max_similarity = 0.0
            index = 0
            for j in ind2:
                comparisons += 1
                current_similarity = s(t1[i], t2[j])                    
                if current_similarity > max_similarity:
                    max_similarity = current_similarity
                    index = j
                if max_similarity >= 1.0:
                    break
                else:
                    continue
            similarity += (input_vec[i] * concept_vec[index])[0, 0] * max_similarity
        similarity /= norm(input_vec) * norm(concept_vec)
        end_time = time.time()
        return (similarity, end_time - start_time, comparisons)


    def average_similarity(model, input_vec, concept_vec, input_terms, corpus_terms):
        raise NotImplementedError