import os

import numpy as np

from snnw.nn.model import Model
from snnw.nn.config import load


def train(model_dir, config_path, image_path, label_path, steps=60000, learning_rate=5e-4):

    model_config = load(os.path.realpath(config_path))

    train_images = np.load(os.path.realpath(image_path))
    train_labels = np.load(os.path.realpath(label_path))

    train_model = Model(x_input=train_images, y_true=train_labels, model_config=model_config)
    train_model.train(steps=steps, learning_rate=learning_rate, model_dir=model_dir)
