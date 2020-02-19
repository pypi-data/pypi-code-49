from ttabooster.datasets import cifar10_validation_set
from ttabooster.TTABoost import TTABooster
from tensorflow.keras.models import load_model

from albumentations import (
    Compose, RandomSizedCrop
)

model = load_model('../saved_models/Keras_cifar10_200epc_resnet110v2_for_Kaduri.h5')  # Load any keras model
x_test, y_test = cifar10_validation_set(limit=200)  # Load your validation set

AUGMENTATIONS_TEST = Compose([
    RandomSizedCrop((28, 28), 32, 32, w2h_ratio=1.0, interpolation=1, always_apply=False, p=1.0),
])

booster = TTABooster(model, batch_size=100, augmentations=AUGMENTATIONS_TEST)
booster.benchmark_results(x_test, y_test)
