"""@package deepacstrain.command_line
A DeePaC CLI. Support subcommands, prediction with built-in and custom models, training, evaluation, data preprocessing.

"""
import sklearn # to load libgomp early to solve problems with static TLS on some systems like bioconda mulled-tests
import numpy as np
import tensorflow.compat.v1 as tf
import random as rn
import os
from deepacstrain import __file__
from deepacstrain import __version__

from deepac.command_line import MainRunner


def main():
    """Run DeePaC-strain CLI."""
    seed = 0
    np.random.seed(seed)
    tf.set_random_seed(seed)
    rn.seed(seed)
    tf.disable_v2_behavior()
    modulepath = os.path.dirname(__file__)
    print("DeePaC-strain {}. Using bacterial strain models.".format(__version__))
    builtin_configs = {"rapid": os.path.join(modulepath, "builtin", "config",
                                             "nn-patric-strain-rapid-sensitive-cnn.ini"),
                       "sensitive": os.path.join(modulepath, "builtin", "config",
                                                 "nn-patric-strain-rapid-sensitive-cnn.ini")}
    builtin_weights = {"rapid": os.path.join(modulepath, "builtin", "weights",
                                             "nn-patric-strain-rapid-sensitive-cnn.h5"),
                       "sensitive": os.path.join(modulepath, "builtin", "weights",
                                                 "nn-patric-strain-rapid-sensitive-cnn.h5")}
    runner = MainRunner(builtin_configs, builtin_weights)
    runner.parse()


if __name__ == "__main__":
    main()
