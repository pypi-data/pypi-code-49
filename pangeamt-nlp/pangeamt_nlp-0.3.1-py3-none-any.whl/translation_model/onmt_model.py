import os
import argparse
from pangeamt_nlp.translation_model.translation_model_base import (
    TranslationModelBase,
)
from onmt.bin.train import train as onmt_train
from onmt.bin.train import _get_parser


class ONMT_model(TranslationModelBase):
    NAME = "onmt"
    INITIALIZED = False

    DEFAULT = (
        "-layers 6 -rnn_size 512 -word_vec_size 512 -transformer_ff 2048 -heads "
        "8 -encoder_type transformer -decoder_type transformer -position_encoding "
        "-train_steps 500000 -max_generator_batches 2 -dropout 0.1 -batch_size 4096 "
        "-batch_type tokens -normalization tokens -accum_count 2 -optim adam "
        "-adam_beta2 0.998 -decay_method noam -warmup_steps 8000 -learning_rate 2 "
        "-max_grad_norm 0 -param_init 0 -param_init_glorot -label_smoothing 0.1 "
        "-valid_steps 10000 -save_checkpoint_steps 10000 -keep_checkpoint 10 "
        "-early_stopping 8"
    )

    def __init__(self):
        super().__init__()

    @staticmethod
    def train(
        data_path: str, model_path: str, *args, gpu: str = None, **kwargs
    ):

        prepend_args = (
            f"-data {data_path}/data -save_model {model_path}/model "
        )
        if gpu:
            apend_args = f"-gpu_ranks {gpu} -log_file {data_path}/log.txt"
        else:
            apend_args = f"-log_file {data_path}/log.txt"

        args = (
            prepend_args + (" ").join(list(args)) + " " + apend_args
        ).split(" ")

        parser = _get_parser()

        opt = parser.parse_args(list(args))
        onmt_train(opt)
