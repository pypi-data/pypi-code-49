# -*- coding: utf-8 -*-
import torch
import random
import re
from torch._six import container_abcs


class Dataset(torch.utils.data.Dataset):
    def __init__(self, datastorage, key=None, reverse=False):
        self.datastorage = datastorage
        self.fields = datastorage.fields
        if key is not None:
            self.datastorage.sort(key=key, reverse=reverse)

    def __getitem__(self, i):
        return self.datastorage.get_array(i)

    def __len__(self):
        return len(self.datastorage)


class BucketSampler(torch.utils.data.Sampler):
    def __init__(self,
                 sorted_dataset,
                 batch_size=1,
                 shuffle=False,
                 drop_last=False):
        self.dataset = sorted_dataset
        self.batch_size = batch_size
        self.shuffle = shuffle
        self.drop_last = drop_last
        self.all_batches = []
        batch = []
        for idx in range(len(self.dataset)):
            batch.append(idx)
            if len(batch) == self.batch_size:
                self.all_batches.append(batch)
                batch = []
        if len(batch) > 0 and not self.drop_last:
            self.all_batches.append(batch)

    def __iter__(self):
        if self.shuffle:
            random.shuffle(self.all_batches)
        for batch in self.all_batches:
            yield batch

    def __len__(self):
        if self.drop_last:
            return len(self.dataset) // self.batch_size
        else:
            return (len(self.dataset) + self.batch_size - 1) // self.batch_size


class BucketCollate(object):
    def __init__(self, dataset):
        self.fields = dataset.fields

    def __align(self, batch):
        for idx, (name, field) in enumerate(self.fields.items()):
            if field.sequential:
                pad_idx = field.vocab.stoi[field.pad_token]
                max_len = 0
                if field.include_lengths:
                    max_len = max(batch[idx][1]).item()
                    batch[idx][0] = batch[idx][0][:, :max_len]
                else:
                    max_len = max(torch.sum(batch[idx] != pad_idx,
                                            dim=1)).item()
                    batch[idx] = batch[idx][:, :max_len]

    def __call__(self, batch, field=None):
        np_str_obj_array_pattern = re.compile(r'[SaUO]')
        default_collate_err_msg_format = (
            "default_collate: batch must contain tensors, numpy arrays, "
            "numbers, dicts or lists; found {}")

        elem = batch[0]
        elem_type = type(elem)
        if isinstance(elem, torch.Tensor):
            out = None
            if torch.utils.data.get_worker_info() is not None:
                # If we're in a background process, concatenate directly into a
                # shared memory tensor to avoid an extra copy
                numel = sum([x.numel() for x in batch])
                storage = elem.storage()._new_shared(numel)
                out = elem.new(storage)
            return torch.stack(batch, 0, out=out)
        elif elem_type.__module__ == 'numpy' and elem_type.__name__ != 'str_' \
                and elem_type.__name__ != 'string_':
            elem = batch[0]
            if elem_type.__name__ == 'ndarray':
                # array of string classes and object
                if np_str_obj_array_pattern.search(elem.dtype.str) is not None:
                    raise TypeError(
                        default_collate_err_msg_format.format(elem.dtype))

                return self.__call__([torch.as_tensor(b) for b in batch])
            elif elem.shape == ():  # scalars
                return torch.as_tensor(batch)
        elif isinstance(elem, tuple):  # namedtuple
            transposed = zip(*batch)
            return [self.__call__(samples) for samples in transposed]
        elif isinstance(elem, container_abcs.Sequence):
            transposed = zip(*batch)
            ret = [self.__call__(samples) for samples in transposed]
            self.__align(ret)
            return ret

        raise TypeError(default_collate_err_msg_format.format(elem_type))
