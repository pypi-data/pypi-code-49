# -*- coding: utf-8 -*-
from tqdm import tqdm
import numpy as np
import os
import six
import pickle
import gzip
from collections import defaultdict


class Vocab(object):
    """
    Defines a vocabulary object that will be used to numericalize a field.
    """
    def __init__(self,
                 counter,
                 max_size=None,
                 min_freq=1,
                 init_token=None,
                 eos_token=None,
                 pad_token='<pad>',
                 unk_token='<unk>',
                 nb_extra_specials=10,
                 vectors=None,
                 specials_first=True):
        """
        Create a Vocab object from a collections.Counter.
        Arguments:
            counter: collections.Counter object holding the frequencies of
                each value found in the data.
            max_size: The maximum size of the vocabulary, or None for no
                maximum. Default: None.
            min_freq: The minimum frequency needed to include a token in the
                vocabulary. Values less than 1 will be set to 1. Default: 1.
            vectors: One of either the available pretrained vectors
                or custom pretrained vectors (see Vocab.load_vectors);
                or a list of aforementioned vectors
            specials_first: Whether to add special tokens into the vocabulary
                at first. If it is False, they are added into the vocabulary
                at last. Default: True.
        """
        self.unk_token = unk_token
        self.freqs = counter
        counter = counter.copy()
        min_freq = max(min_freq, 1)

        specials = [
            tok for tok in [init_token, eos_token, pad_token, unk_token]
            if tok is not None
        ]
        for i in range(nb_extra_specials):
            specials.append("<SPEC_{}>".format(i))

        self.itos = []
        self.unk_index = None
        if specials_first:
            self.itos = list(specials)
            max_size = None if max_size is None else max_size + len(specials)

        for tok in specials:
            del counter[tok]

        # sort by frequency, then alphabetically
        words_and_frequencies = sorted(counter.items(), key=lambda tup: tup[0])
        words_and_frequencies.sort(key=lambda tup: tup[1], reverse=True)

        for word, freq in words_and_frequencies:
            if freq < min_freq or len(self.itos) == max_size:
                break
            self.itos.append(word)

        if unk_token in specials:
            unk_index = specials.index(unk_token)  # position in list
            # account for ordering of specials, set variable
            self.unk_index = unk_index if specials_first else len(
                self.itos) + unk_index
            self.stoi = defaultdict(self.__default_unk_index)
        else:
            self.stoi = defaultdict()

        if not specials_first:
            self.itos.extend(list(specials))

        # stoi is simply a reverse dict for itos
        self.stoi.update({tok: i for i, tok in enumerate(self.itos)})

        self.vectors = None
        if vectors is not None:
            self.load_vectors(vectors)

    def __default_unk_index(self):
        return self.unk_index

    def extend(self, v, sort=False):
        words = sorted(v.itos) if sort else v.itos
        for w in words:
            if w not in self.stoi:
                self.itos.append(w)
                self.stoi[w] = len(self.itos) - 1

    def load_vectors(self, vectors):
        """
        Arguments:
            vectors: one of or a list containing instantiations
                of Vectors classes.
            Remaining keyword arguments: Passed to the constructor
                of Vectors classes.
        """
        if not isinstance(vectors, list):
            vectors = [vectors]

        tot_dim = sum(v.dim for v in vectors)

        self.vectors = np.zeros((len(self), tot_dim))
        for i, token in enumerate(self.itos):
            start_dim = 0
            for v in vectors:
                end_dim = start_dim + v.dim
                self.vectors[i][start_dim:end_dim] = v[token.strip()]
                start_dim = end_dim
            assert (start_dim == tot_dim)

    def __unk_init(self, x):
        return np.random.uniform(-0.05, 0.05, x.shape)

    def set_vectors(self, stoi, vectors, dim, unk_init=None):
        """
        Set the vectors for the Vocab instance from a collection of Tensors.
        Arguments:
            stoi: A dictionary of string to the index of the associated vector
                in the `vectors` input argument.
            vectors: An indexed iterable (or other structure supporting
                __getitem__) that given an input index, returns a FloatTensor
                representing the vector for the token associated with the
                index. For example, vector[stoi["string"]] should return the
                vector for "string".
            dim: The dimensionality of the vectors.
            unk_init (callback): by default, initialize out-of-vocabulary word
                vectors to zero vectors; can be any function that takes in a
                Tensor and returns a Tensor of the same size.
                Default: lambda x: np.random.uniform(-0.05, 0.05, x.shape)
        """
        if unk_init is None:
            unk_init = self.__unk_init
        self.vectors = np.zeros((len(self), dim))
        for i, token in enumerate(self.itos):
            wv_index = stoi.get(token, None)
            if wv_index is not None:
                self.vectors[i] = vectors[wv_index]
            else:
                self.vectors[i] = unk_init(self.vectors[i])

    def __getitem__(self, token):
        return self.stoi.get(token, self.stoi.get(self.unk_token))

    def __getstate__(self):
        # avoid picking defaultdict
        attrs = dict(self.__dict__)
        # cast to regular dict
        attrs['stoi'] = dict(self.stoi)
        return attrs

    def __setstate__(self, state):
        if state.get("unk_index", None) is None:
            stoi = defaultdict()
        else:
            stoi = defaultdict(self.__default_unk_index)
        stoi.update(state['stoi'])
        state['stoi'] = stoi
        self.__dict__.update(state)

    def __eq__(self, other):
        if not isinstance(other, Vocab):
            return False
        if self.freqs != other.freqs:
            return False
        if self.stoi != other.stoi:
            return False
        if self.itos != other.itos:
            return False
        if (self.vectors != other.vectors).any():
            return False
        return True

    def __len__(self):
        return len(self.itos)


class Vectors(object):
    def __init__(self,
                 file_path,
                 cache=None,
                 prefix=None,
                 unk_init=None,
                 max_vectors=None):
        """
        Arguments:
           file_path: file that contains the vectors
           cache: directory for cached vectors
           prefix: prefix while caching vectors
           unk_init (callback): by default, initialize out-of-vocabulary
               word vectors with a random array of uniform distribution;
               can be any function that takes in a Tensor and
               returns a Tensor of the same size
           max_vectors (int): this can be used to limit the number of
               pre-trained vectors loaded.
               Most pre-trained vector sets are sorted
               in the descending order of word frequency.
               Thus, in situations where the entire set doesn't fit in memory,
               or is not needed for another reason, passing `max_vectors`
               can limit the size of the loaded set.
        """
        cache = '.vector_cache' if cache is None else cache
        self.itos = None
        self.stoi = None
        self.vectors = None
        self.dim = None
        self.unk_init = self.__unk_init if unk_init is None else unk_init
        self.cache(file_path, cache, prefix=prefix, max_vectors=max_vectors)

    def cache(self, file_path, cache, prefix=None, max_vectors=None):
        if os.path.isfile(file_path):
            path = file_path
            if max_vectors:
                file_suffix = '_{}.pkl'.format(max_vectors)
            else:
                file_suffix = '.pkl'
            vec_name = os.path.basename(file_path)
            if prefix:
                vec_name = prefix + vec_name
            path_pt = os.path.join(cache, vec_name) + file_suffix
        else:
            vec_name = file_path
            if prefix:
                vec_name = prefix + vec_name
            path = os.path.join(cache, vec_name)
            if max_vectors:
                file_suffix = '_{}.pkl'.format(max_vectors)
            else:
                file_suffix = '.pkl'
            path_pt = path + file_suffix

        if not os.path.isfile(path_pt):
            if not os.path.isfile(path):
                raise RuntimeError('no vectors found at {}'.format(path))

            print("Loading vectors from {}".format(path))
            ext = os.path.splitext(path)[1][1:]
            if ext == 'gz':
                open_file = gzip.open
            else:
                open_file = open

            vectors_loaded = 0
            with open_file(path, 'rb') as f:
                num_lines, dim = self.__infer_shape(f)
                if not max_vectors or max_vectors > num_lines:
                    max_vectors = num_lines

                itos, vectors, dim = [], np.zeros((max_vectors, dim)), None

                for line in tqdm(f, total=max_vectors):
                    # Explicitly splitting on " " is important, so we don't
                    # get rid of Unicode non-breaking spaces in the vectors.
                    entries = line.rstrip().split(b" ")

                    word, entries = entries[0], entries[1:]
                    if dim is None and len(entries) > 1:
                        dim = len(entries)
                    elif len(entries) == 1:
                        print("Skipping token {} with 1-dimensional "
                              "vector {}; likely a header".format(
                                  word, entries))
                        continue
                    elif dim != len(entries):
                        raise RuntimeError(
                            "Vector for token {} has {} dimensions, but "
                            "previously read vectors have {} dimensions. "
                            "All vectors must have the same number of "
                            "dimensions.".format(word, len(entries), dim))

                    try:
                        if isinstance(word, six.binary_type):
                            word = word.decode('utf-8')
                    except UnicodeDecodeError:
                        print("Skipping non-UTF8 token {}".format(repr(word)))
                        continue

                    vectors[vectors_loaded] = np.asarray(
                        [float(x) for x in entries])
                    vectors_loaded += 1
                    itos.append(word)

                    if vectors_loaded == max_vectors:
                        break

            self.itos = itos
            self.stoi = {word: i for i, word in enumerate(itos)}
            self.vectors = np.asarray(vectors).reshape(-1, dim)
            self.dim = dim
            print('Saving vectors to {}'.format(path_pt))
            if not os.path.exists(cache):
                os.makedirs(cache)
            with open(path_pt, 'wb') as fwb:
                pickle.dump((self.itos, self.stoi, self.vectors, self.dim),
                            fwb)
        else:
            print('Loading vectors from {}'.format(path_pt))
            with open(path_pt, 'rb') as frb:
                self.itos, self.stoi, self.vectors, self.dim = pickle.load(frb)

    def __unk_init(self, x):
        return np.random.uniform(-0.05, 0.05, x.shape)

    def __infer_shape(self, f):
        num_lines, vector_dim = 0, None
        for line in f:
            if vector_dim is None:
                row = line.rstrip().split(b" ")
                vector = row[1:]
                # Assuming word, [vector] format
                if len(vector) > 2:
                    # The header present in some (w2v) formats contains
                    # two elements.
                    vector_dim = len(vector)
                    num_lines += 1  # First element read
            else:
                num_lines += 1
        f.seek(0)
        return num_lines, vector_dim

    def get_vecs_by_tokens(self, tokens, lower_case_backup=False):
        """Look up embedding vectors of tokens.
        Arguments:
            tokens: a token or a list of tokens. if `tokens` is a string,
                returns a 1-D tensor of shape `self.dim`; if `tokens` is a
                list of strings, returns a 2-D tensor of shape=(len(tokens),
                self.dim).
            lower_case_backup : Whether to look up the token in the lower case.
                If False, each token in the original case will be looked up;
                if True, each token in the original case will be looked up
                first, if not found in the keys of the property `stoi`, the
                token in the lower case will be looked up. Default: False.
        Examples:
            >>> examples = ['chip', 'baby', 'Beautiful']
            >>> vec = text.vocab.GloVe(name='6B', dim=50)
            >>> ret = vec.get_vecs_by_tokens(tokens, lower_case_backup=True)
        """
        to_reduce = False

        if not isinstance(tokens, list):
            tokens = [tokens]
            to_reduce = True

        if not lower_case_backup:
            indices = [self[token] for token in tokens]
        else:
            indices = [
                self[token] if token in self.stoi else self[token.lower()]
                for token in tokens
            ]

        vecs = np.asarray(indices)
        return vecs[0] if to_reduce else vecs

    def __len__(self):
        return len(self.vectors)

    def __getitem__(self, token):
        if token in self.stoi:
            return self.vectors[self.stoi[token]]
        else:
            return self.unk_init(np.zeros((self.dim, )))

    def __eq__(self, other):
        if not isinstance(other, Vectors):
            return False
        if self.stoi != other.stoi:
            return False
        if self.itos != other.itos:
            return False
        if self.dim != other.dim:
            return False
        if (self.vectors != other.vectors).any():
            return False
        return True
