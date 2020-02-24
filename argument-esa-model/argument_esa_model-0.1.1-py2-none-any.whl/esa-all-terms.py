#!/usr/bin/env python3

import sys
import argparse
import pandas as pd
from esa import ESA


def create_argparser():
    parser = argparse.ArgumentParser()
    parser.add_argument("--similarity", required = True)
    parser.add_argument("--matrix-path", required = True)
    parser.add_argument("--model-path", required = True)
    parser.add_argument("--model-vocab", required = True)
    parser.add_argument("--text", required = True)
    return parser

def main():
    parser = create_argparser()
    args = parser.parse_args()

    similarity = vars(args)["similarity"]
    matrix_path = vars(args)["matrix_path"]
    model_path = vars(args)["model_path"]
    vocab_path = vars(args)["model_vocab"]
    text = vars(args)["text"]
    e = ESA(matrix_path = matrix_path, model_path = model_path, vocab_path = vocab_path, similarity = similarity)
    result = e.process(text, False)
    print(result)


if __name__ == "__main__":
    main()