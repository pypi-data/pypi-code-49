#!/usr/bin/env python3

import sys
import argparse
from argument_esa_model.esa import ESA


def create_argparser():
    parser = argparse.ArgumentParser()
    parser.add_argument("--similarity", required = True)
    parser.add_argument("--matrix-path", required = True)
    parser.add_argument("--model-path", required = True)
    parser.add_argument("--model-vocab", required = True)
    parser.add_argument("--text", required = True)
    return parser

def model_topic(path_matrix,path_model,path_vocab,similarity,text):
    e = ESA(matrix_path = path_matrix, model_path = path_model, vocab_path = path_vocab, similarity = similarity)
    result = e.process(text, False)
    return result

def main():
    parser = create_argparser()
    args = parser.parse_args()

    similarity = vars(args)["similarity"]
    path_matrix = vars(args)["matrix_path"]
    path_model = vars(args)["model_path"]
    path_vocab = vars(args)["model_vocab"]
    text = vars(args)["text"]
    result = model_topic(path_matrix,path_model,path_vocab,similarity,text)
    print(result)

if __name__ == "__main__":
    main()