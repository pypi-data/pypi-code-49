from collections import defaultdict
import warnings
import random

import numpy as np

from dbispipeline.base import Loader
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import ParameterGrid


class MultiLoaderGenerator(Loader):
    """ this class dynamically constructs a multiloader by selecting a loader
    along with a set of parameters to be used by it.

    Args:
        loader_class: the class of the dataloader to be instantiated. Do not
            pass an instance.
        parameters: if passed a list, this generator will return one dataloader
            instance for each entry in the list, and each entry in the list is
            passed to the constructor of the loader.
            If passed a dict, a grid of all combinations is generated and
            passed to the loader.
    """

    def __init__(self, loader_class, parameters):
        self.loaders = []
        if isinstance(parameters, dict):
            for sample in ParameterGrid(parameters):
                # this produces only dicts
                self.loaders.append(loader_class(**sample))
        else:
            for sample in parameters:
                if isinstance(sample, dict):
                    self.loaders.append(loader_class(**sample))
                else:
                    self.loaders.append(loader_class(*sample))

    def load(self):
        for loader in self.loaders:
            yield loader.load()

    @property
    def configuration(self):
        for i, loader in enumerate(self.loaders):
            config = loader.configuration
            config['run_number'] = i
            config['class'] = loader.__class__.__name__
            yield config

    @property
    def run_count(self):
        return len(self.loaders)


class LimitingLoader(Loader):

    """Limits the amount of targets and samples per target for any loader."""

    def __init__(
            self,
            max_targets,
            max_documents_per_target,
            loader_class,
            strategy='first',
            random_seed=None,
            encode_labels=False,
            *args,
            **kwargs):

        valid_strategies = ['first', 'random']
        if strategy not in valid_strategies:
            raise ValueError(f'the strategy {strategy} is not valid. Please '
                             f'choose from {valid_strategies}')
        if max_targets is not None and max_targets < 2:
            raise ValueError(f'max_targets must be 2 or greater')
        if (max_documents_per_target is not None
                and max_documents_per_target < 1):
            raise ValueError('max_document_per_target must be 1 or greater')

        self.max_targets = max_targets
        self.max_documents_per_target = max_documents_per_target
        self.loader_class = loader_class
        self.loader = loader_class(*args, **kwargs)
        self.strategy = strategy
        self.random_seed = random_seed
        self.encode_labels = encode_labels

        if self.random_seed is not None:
            random.seed(self.random_seed)

    @property
    def run_count(self):
        return self.loader.run_count

    def load(self):
        pairs = []
        if hasattr(self.loader, 'load_validate'):
            pairs.append(self.loader.load_validate())
        if hasattr(self.loader, 'load_test'):
            pairs.append(self.loader.load_test())
            pairs.append(self.loader.load_train())
        else:
            pairs.append(self.loader.load())

        # first, restructure (x, y) pairs to {y: [x0, x1, ...]} dict
        # for each of the train, test, validate pairs
        dicts = []
        for pair in pairs:
            entry = defaultdict(list)
            for data, label in zip(pair[0], pair[1]):
                if isinstance(label, np.ndarray) or isinstance(label, list):
                    label = str(label)
                entry[label].append(data)
            dicts.append(entry)

        training_targets = set(dicts[-1].keys())
        selected_targets = self._sample(training_targets, self.max_targets)

        if self.encode_labels:
            label_encoder = LabelEncoder()
            label_encoder.fit(selected_targets)

        result = []
        for bunch in dicts:
            bunch_result = [[], []]
            for key in selected_targets:
                values = self._sample(
                    bunch[key],
                    self.max_documents_per_target)
                for value in values:
                    bunch_result[0].append(value)
                    bunch_result[1].append(key)
            if self.encode_labels:
                bunch_result[1] = label_encoder.transform(bunch_result[1])
            result.append(bunch_result)
        if len(result) == 1:
            return result[0]
        return result

    def _sample(self, values, sample_limit):
        if sample_limit is None:
            return list(values)

        if sample_limit >= len(values):
            warnings.warn(
                f'sample_limit ({sample_limit}) >= targets '
                f'({len(values)})')
            return list(values)

        if self.strategy == 'first':
            return list(values)[:sample_limit]

        if self.strategy == 'random':
            return random.sample(values, sample_limit)

    @property
    def configuration(self):
        wrapped_configuration = self.loader.configuration
        wrapped_configuration.update({
            'max_targets': self.max_targets,
            'max_documents_per_target': self.max_documents_per_target,
            'loader_class': self.loader_class.__name__,
            'strategy': self.strategy,
            'random_seed': self.random_seed,
            'encode_labels': self.encode_labels,
        })
        return wrapped_configuration
