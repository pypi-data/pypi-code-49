# This file is part of the Sigmentation project.
#    https://gitlab.com/sigmentation/sigmentation
#
# Copyright 2020 Zeyd Boukhers <zeyd@boukhers.com>
#                Matthias Lohr <mail@mlohr.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import argparse
import json
import numpy
import os
import sys
import tempfile
from .algorithm import gen_alg
from .optimization import interpolate, get_sub_sequences
from .processing import norma_one_one


def main():
    argument_parser = argparse.ArgumentParser()
    argument_parser.add_argument('file', help='Input file (JSON)', nargs='?')
    argument_parser.add_argument('--population', type=int, default=50)
    argument_parser.add_argument('--min-split', type=int, default=2)
    argument_parser.add_argument('--max-split', type=int, default=12)
    argument_parser.add_argument('--min-length', type=int, default=12)
    argument_parser.add_argument('--conv', type=int, default=30)
    argument_parser.add_argument('--max-iterations', type=int, default=30)
    argument_parser.add_argument('--new-length', type=int, default=100)
    args = argument_parser.parse_args()

    if args.file:
        with open(args.file, 'r') as f:
            input_data = f.read()
    else:
        input_data = sys.stdin.read()

    # call
    sequences = numpy.array(json.loads(input_data))
    sequences = numpy.array([interpolate(sequence, args.new_length) for sequence in sequences])
    sequences_normalized = numpy.array([norma_one_one(sequence) for sequence in sequences])
    start, best = gen_alg(sequences_normalized, args.population, args.min_split, args.max_split, args.min_length,
                          args.conv, args.max_iterations)
    subsequences = get_sub_sequences(sequences, start[best])
    print(subsequences)  # TODO output in JSON


def nparray2json():
    argument_parser = argparse.ArgumentParser()
    argument_parser.add_argument('file', nargs='?', help='File to read from. If not provided, will read from stdin.')
    args = argument_parser.parse_args()

    if args.file:
        print(json.dumps(numpy.load(args.file).tolist()))
    else:
        _, tmp_file_name = tempfile.mkstemp(prefix='sigmentation-')
        with open(tmp_file_name, 'wb') as f:
            f.write(sys.stdin.buffer.read())
        print(json.dumps(numpy.load(tmp_file_name).tolist()))
        os.remove(tmp_file_name)
