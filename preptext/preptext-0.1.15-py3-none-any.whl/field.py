# -*- coding: utf-8 -*-
import six
from collections import Counter, OrderedDict
from itertools import chain
import numpy as np
from copy import deepcopy

from .vocab import Vocab
from .datastorage import DataStorage


class Field(object):
    """
    Defines a datatype together with instructions for converting to Tensor.

    Field class models common text processing datatypes that can be represented
    by tensors.  It holds a Vocab object that defines the set of possible
    values for elements of the field and their corresponding numerical
    representations.
    The Field object also holds other parameters relating to how a datatype
    should be numericalized, such as a tokenization method and the kind of
    Tensor that should be produced.

    If a Field is shared between two columns in a dataset (e.g., question and
    answer in a QA dataset), then they will have a shared vocabulary.

    Attributes:
        sequential: Whether the datatype represents sequential data. If False,
            no tokenization is applied. Default: True.
        use_vocab: Whether to use a Vocab object. If False, the data in this
            field should already be numerical. Default: True.
        init_token: A token that will be prepended to every example using this
            field, or None for no initial token. Default: None.
        eos_token: A token that will be appended to every example using this
            field, or None for no end-of-sentence token. Default: None.
        fix_length: A fixed length that all examples
            using this field will be padded to
            or None for max sequence lengths. Default: None.
        dtype: Data type that represents a batch of examples
            of this kind of data. Default: int.
        preprocessing: The Pipeline that will be applied to examples
            using this field after tokenizing but before numericalizing. Many
            Datasets replace this attribute with a custom preprocessor.
            Default: None.
        postprocessing: A Pipeline that will be applied to examples using
            this field after numericalizing but before the numbers are turned
            into a Tensor. The pipeline function takes the batch as a list, and
            the field's Vocab.
            Default: None.
        lower: Whether to lowercase the text in this field. Default: False.
        include_lengths: Whether to return a tuple of a padded minibatch and
            a list containing the lengths of each examples, or just a padded
            minibatch. Default: False.
        pad_token: The string token used as padding. Default: "<pad>".
        unk_token: The string token used to represent OOV words.
            Default: "<unk>".
        pad_first: Do the padding of the sequence at the beginning.
            Default: False.
        truncate_first: Do the truncating of the sequence at the beginning.
            Default: False
        stop_words: Tokens to discard during the preprocessing step.
            Default: None
    """
    def __init__(self,
                 sequential=True,
                 use_vocab=True,
                 init_token=None,
                 eos_token=None,
                 fix_length=None,
                 dtype=int,
                 preprocessing=None,
                 postprocessing=None,
                 lower=False,
                 include_lengths=False,
                 pad_token="<pad>",
                 unk_token="<unk>",
                 pad_first=False,
                 truncate_first=False,
                 stop_words=None):
        self.sequential = sequential
        self.use_vocab = use_vocab
        self.init_token = init_token
        self.eos_token = eos_token
        if fix_length:
            assert isinstance(fix_length, int), "fix_length must be int"
        self.fix_length = fix_length
        self.dtype = dtype
        self.preprocessing = preprocessing
        self.postprocessing = postprocessing
        self.lower = lower
        self.include_lengths = include_lengths
        self.pad_token = pad_token if self.sequential else None
        self.unk_token = unk_token
        self.pad_first = pad_first
        self.truncate_first = truncate_first
        try:
            self.stop_words = set(
                stop_words) if stop_words is not None else None
        except TypeError:
            raise ValueError("Stop words must be convertible to a set")
        if self.sequential:
            self.__max_len = 0
        else:
            self.__max_len = None
        self.vocab = None

    def preprocess(self, data):
        if self.sequential and isinstance(data, six.text_type):
            data = data.rstrip('\n').split()
        if self.lower:
            data = [d.lowercase() for d in data]
        if self.sequential and self.use_vocab and self.stop_words is not None:
            data = [d for d in data if d not in self.stop_words]
        if self.init_token:
            data.insert(0, self.init_token)
        if self.eos_token:
            data.append(self.eos_token)
        if self.preprocessing is not None:
            data = self.preprocessing(data)
        if self.sequential:
            len_data = len(data) + (self.init_token,
                                    self.eos_token).count(None) - 2
            self.__max_len = max(self.__max_len, len_data)
        return data

    def process(self, x):
        padded = self.pad(x)
        array = self.numericalize(padded)
        return array

    def pad(self, inp_x):
        x = deepcopy(inp_x)
        if not self.sequential:
            return x
        if self.fix_length:
            max_len = self.fix_length + (self.init_token,
                                         self.eos_token).count(None) - 2
        else:
            max_len = self.__max_len

        if x[0] == self.init_token:
            x.pop(0)
        if x[-1] == self.eos_token:
            x.pop(-1)

        if self.pad_first:
            padded = [self.pad_token] * max(0, max_len - len(x)) \
                + ([] if self.init_token is None else [self.init_token]) \
                + list(x[-max_len:] if self.truncate_first else x[:max_len]) \
                + ([] if self.eos_token is None else [self.eos_token])
        else:
            padded = ([] if self.init_token is None else [self.init_token]) \
                + list(x[-max_len:] if self.truncate_first else x[:max_len]) \
                + ([] if self.eos_token is None else [self.eos_token]) \
                + [self.pad_token] * max(0, max_len - len(x))

        length = len(padded) - max(0, max_len - len(x))

        if self.include_lengths:
            return (padded, length)
        return padded

    def numericalize(self, arr):
        if isinstance(arr, tuple):
            arr, length = arr
            length = np.asarray(length)

        if self.use_vocab:
            if self.sequential:
                arr = [self.vocab.stoi[x] for x in arr]
            else:
                arr = self.vocab.stoi[arr]

            if self.postprocessing is not None:
                arr = self.postprocessing(arr)
        else:
            if not self.sequential:
                arr = [
                    self.dtype(x) if not isinstance(x, self.dtype) else x
                    for x in arr
                ]
            if self.postprocessing is not None:
                arr = self.postprocessing(arr)
        var = np.asarray(arr)
        if self.include_lengths:
            return var, length
        return var

    def build_vocab(self, *args, **kwargs):
        """Construct the Vocab object for this field from one or more datasets.
        Arguments:
            *args: Dataset objects or other iterable data
                sources from which to construct the Vocab object that
                represents the set of possible values for this field. If
                a Dataset object is provided, all columns corresponding
                to this field are used; individual columns can also be
                provided directly.
            **kwargs:
                max_size: The maximum size of the vocabulary, or None for no
                    maximum. Default: None.
                min_freq: The minimum frequency needed to include a token in
                    the vocabulary. Values less than 1 will be set to 1.
                    Default: 1.
                nb_extra_specials: number of extra special tokens.
                vectors: One of either the available pretrained vectors
                    or custom pretrained vectors (see Vocab.load_vectors);
                    or a list of aforementioned vectors
                specials_first: Whether to add special tokens into the
                    vocabulary at first. If it is False, they are added into
                    the vocabulary at last. Default: True.
        """
        counter = Counter()
        sources = []
        for arg in args:
            if isinstance(arg, DataStorage):
                sources += [
                    getattr(arg, name) for name, field in arg.fields.items()
                    if field is self
                ]
            else:
                sources.append(arg)
        for data in sources:
            for x in data:
                if not self.sequential:
                    x = [x]
                try:
                    counter.update(x)
                except TypeError:
                    counter.update(chain.from_iterable(x))
        self.vocab = Vocab(counter,
                           init_token=self.init_token,
                           eos_token=self.eos_token,
                           pad_token=self.pad_token,
                           unk_token=self.unk_token,
                           **kwargs)

    def __eq__(self, other):
        if not isinstance(other, Field):
            return False
        return self.__dict__ == other.__dict__

    def __getstate__(self):
        attrs = dict(self.__dict__)
        return attrs

    def __setstate__(self, state):
        self.__dict__.update(state)


class Fields(object):
    """
    a collection of fields
    """
    def __init__(self):
        self.__fields = OrderedDict()

    def add_field(self,
                  name,
                  sequential=True,
                  use_vocab=True,
                  init_token=None,
                  eos_token=None,
                  fix_length=None,
                  dtype=int,
                  preprocessing=None,
                  postprocessing=None,
                  lower=False,
                  include_lengths=False,
                  pad_token="<pad>",
                  unk_token="<unk>",
                  pad_first=False,
                  truncate_first=False,
                  stop_words=None):
        """
        Attributes:
            name: Name of the field.
            sequential: Whether the datatype represents sequential data.
                If False, no tokenization is applied. Default: True.
            use_vocab: Whether to use a Vocab object. If False, the data
                in this field should already be numerical. Default: True.
            init_token: A token that will be prepended to every example
                using this field, or None for no initial token. Default: None.
            eos_token: A token that will be appended to every example using
                this field, or None for no end-of-sentence token.
                Default: None.
            fix_length: A fixed length that all examples
                using this field will be padded to
                or None for max sequence lengths.
                Default: None.
            dtype: Data type that represents a batch of examples
                of this kind of data. Default: int.
            preprocessing: The Pipeline that will be applied to examples
                using this field after tokenizing but before numericalizing.
                Many datasets replace this attribute with a custom
                preprocessor. Default: None.
            postprocessing: A Pipeline that will be applied to examples using
                this field after numericalizing but before the numbers are
                turned into a Tensor. The pipeline function takes the batch
                as a list, and the field's Vocab. Default: None.
            lower: Whether to lowercase the text in this field. Default: False.
            include_lengths: Whether to return a tuple of a padded minibatch
                and a list containing the lengths of each examples, or just a
                padded minibatch. Default: False.
            pad_token: The string token used as padding. Default: "<pad>".
            unk_token: The string token used to represent OOV words.
                Default: "<unk>".
            pad_first: Do the padding of the sequence at the beginning.
                Default: False.
            truncate_first: Do the truncating of the sequence at the beginning.
                Default: False
            stop_words: Tokens to discard during the preprocessing step.
                Default: None
        """
        args = [
            sequential, use_vocab, init_token, eos_token, fix_length, dtype,
            preprocessing, postprocessing, lower, include_lengths, pad_token,
            unk_token, pad_first, truncate_first, stop_words
        ]
        self.__fields[name] = Field(*args)

    def del_field(self, name):
        if name in self.__fields:
            self.__fields.pop(name)

    def items(self):
        return list(self.__fields.items())

    def keys(self):
        return list(self.__fields.keys())

    def values(self):
        return list(self.__fields.values())

    def __str__(self):
        return str(self.__fields)

    def __repr__(self):
        return repr(self.__fields)

    def __len__(self):
        return len(self.__fields)

    def __getitem__(self, key):
        return self.__fields[key]

    def __iter__(self):
        return iter(self.keys())

    def __getattr__(self, attr):
        return self.__fields[attr]

    def __getstate__(self):
        attrs = dict(self.__dict__)
        return attrs

    def __setstate__(self, state):
        self.__dict__.update(state)

    def __eq__(self, other):
        if not isinstance(other, Fields):
            return False
        return self.__dict__ == other.__dict__
