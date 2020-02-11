import os

import numpy as np

from snnw.nn.model import Model
from snnw.nn.config import load


def evaluate(model_dir, config_path, image_path, label_path):

    model_config = load(os.path.realpath(config_path))

    test_images = np.load(os.path.realpath(image_path))
    test_labels = np.load(os.path.realpath(label_path))

    test_model = Model(x_input=test_images, y_true=test_labels, model_config=model_config)
    test_model.evaluate(model_dir=model_dir)
